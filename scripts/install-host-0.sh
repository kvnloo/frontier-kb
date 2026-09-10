#!/usr/bin/env bash
# Install frontier-kb store on host 0 (groot). Idempotent. No secrets in git.
set -euo pipefail

REPO_CANDIDATES=(
  "${FRONTIER_KB_ROOT:-}"
  "$HOME/workspace/frontier-kb"
  "/workspace/frontier-kb"
  "/home/kvn/workspace/frontier-kb"
)
ROOT=""
for c in "${REPO_CANDIDATES[@]}"; do
  if [[ -n "$c" && -d "$c/.git" ]]; then ROOT="$c"; break; fi
done
if [[ -z "$ROOT" ]]; then
  ROOT="${HOME}/workspace/frontier-kb"
  mkdir -p "$(dirname "$ROOT")"
  git clone https://github.com/kvnloo/frontier-kb.git "$ROOT"
fi
cd "$ROOT"
git fetch origin
if git show-ref --verify --quiet refs/remotes/origin/kb-swe2-concurrent-store; then
  git checkout kb-swe2-concurrent-store
  git pull --ff-only origin kb-swe2-concurrent-store
else
  git checkout main
  git pull --ff-only origin main
fi

CFG="$HOME/.config/frontier-kb"
mkdir -p "$CFG"
chmod 700 "$CFG"
ENVF="$CFG/env"
if [[ ! -f "$ENVF" ]]; then
  PASS="$(openssl rand -hex 16)"
  umask 077
  cat >"$ENVF" <<EOF
POSTGRES_USER=frontier
POSTGRES_PASSWORD=$PASS
POSTGRES_DB=frontier_kb
FRONTIER_KB_DSN=postgresql://frontier:${PASS}@127.0.0.1:55432/frontier_kb
FRONTIER_KB_DSN_TAILNET=postgresql://frontier:${PASS}@100.113.138.100:55432/frontier_kb
KB_WRITER=host-0
EOF
  chmod 600 "$ENVF"
  echo "wrote $ENVF"
else
  echo "keeping existing $ENVF"
fi
set -a
# shellcheck disable=SC1090
source "$ENVF"
set +a

if ! command -v docker >/dev/null; then
  echo "docker is required on host 0" >&2
  exit 1
fi
docker compose -f docker-compose.yml -f docker-compose.host-0.yml up -d kb
for _ in $(seq 1 40); do
  if docker exec frontier-kb-pg pg_isready -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

PY="$ROOT/.venv/bin/python"
if [[ ! -x "$PY" ]]; then
  python3 -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/pip" install -q -r "$ROOT/requirements-store.txt"
fi
"$PY" "$ROOT/scripts/kb_store.py" init
"$PY" "$ROOT/scripts/kb_store.py" ingest

UNIT_SRC="$ROOT/deploy/frontier-kb.service"
UNIT_DST="$HOME/.config/systemd/user/frontier-kb.service"
if [[ -f "$UNIT_SRC" ]]; then
  mkdir -p "$(dirname "$UNIT_DST")"
  sed "s|/home/kvn/workspace/frontier-kb|$ROOT|g" "$UNIT_SRC" >"$UNIT_DST"
  if command -v systemctl >/dev/null; then
    systemctl --user daemon-reload || true
    systemctl --user enable --now frontier-kb.service || true
  fi
fi

install_skill() {
  local dest="$1"
  mkdir -p "$dest"
  ln -sfn "$ROOT/skills/frontier-kb" "$dest/frontier-kb"
}

install_skill "${HERMES_HOME:-$HOME/.hermes}/skills"
if [[ -d /workspace/hermes-home ]]; then
  install_skill /workspace/hermes-home/skills
fi
install_skill "${HOME}/.omp/skills"
if [[ -n "${FM_HOME:-}" ]]; then
  install_skill "$FM_HOME/skills"
elif [[ -d "$HOME/.firstmate" ]]; then
  install_skill "$HOME/.firstmate/skills"
fi

append_dsn() {
  local f="$1"
  local dsn="${2:-$FRONTIER_KB_DSN}"
  mkdir -p "$(dirname "$f")"
  touch "$f"
  chmod 600 "$f"
  if grep -q '^FRONTIER_KB_DSN=' "$f" 2>/dev/null; then
    return 0
  fi
  printf 'FRONTIER_KB_DSN=%s\n' "$dsn" >>"$f"
}
append_dsn "$HOME/.hermes/.env"
if [[ -d /workspace/hermes-home ]]; then
  append_dsn /workspace/hermes-home/.env
fi

"$PY" "$ROOT/scripts/test_sqlite_busy.py" || true
echo "host-0 store ready. local DSN in $ENVF"
echo "tailnet DSN host=100.113.138.100 port=55432 db=frontier_kb user=frontier"
