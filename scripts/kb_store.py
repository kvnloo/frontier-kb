#!/usr/bin/env python3
"""Postgres CAS store for frontier-kb. Markdown stays the git/Obsidian projection."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_CANDIDATES = (ROOT / "store" / "schema.sql", ROOT / "scripts" / "schema.sql")
NOTE_DIRS = ("literature", "permanent", "harnesses", "domains", "atlas", "inbox")
WIKI_RE = re.compile(r"\[\[([^\]|#]+)")
REQUIRED = {"id", "title", "type", "status", "created", "updated"}
FM_ORDER = (
    "id",
    "title",
    "type",
    "status",
    "created",
    "updated",
    "sources",
    "harnesses",
    "domains",
    "confidence",
    "tags",
)
SMOKE_IDS = {"cas-shared"}
SMOKE_PREFIXES = ("smokeu-", "unique-")
DEFAULT_DSN = "postgresql://frontier:frontier@127.0.0.1:55432/frontier_kb"
ADVISORY_LOCK = 732910


def database_url() -> str:
    return os.environ.get("DATABASE_URL") or os.environ.get("FRONTIER_KB_DSN", DEFAULT_DSN)


def schema_path() -> Path:
    for path in SCHEMA_CANDIDATES:
        if path.is_file():
            return path
    raise FileNotFoundError("missing store/schema.sql (and scripts/schema.sql fallback)")


def connect() -> psycopg.Connection:
    return psycopg.connect(database_url(), row_factory=dict_row)


def apply_schema(conn: psycopg.Connection) -> None:
    conn.execute(schema_path().read_text(encoding="utf-8"))
    conn.commit()


def extract_links(body: str) -> list[tuple[str, str]]:
    out = []
    for raw in WIKI_RE.findall(body):
        target = raw.strip().split("|", 1)[0].strip()
        target = target.rsplit("/", 1)[-1]
        if target:
            out.append((target, "wikilink"))
    return out


def parse_ts(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, parts[2].lstrip("\n")


def _replace_links(cur, note_id: str, links: list[tuple[str, str]]) -> None:
    cur.execute("DELETE FROM links WHERE src = %s", (note_id,))
    for dst, rel in links:
        cur.execute(
            "INSERT INTO links (src, dst, rel) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
            (note_id, dst, rel),
        )


def _log(cur, note_id, op, writer, expected, new_version, ok, detail) -> None:
    cur.execute(
        """
        INSERT INTO events (note_id, op, writer, expected_version, new_version, ok, detail)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (note_id, op, writer, expected, new_version, ok, detail),
    )


def put_cas(
    conn: psycopg.Connection,
    *,
    note_id: str,
    path: str,
    title: str,
    type_: str,
    status: str,
    body: str,
    frontmatter: dict,
    writer: str | None,
    created: datetime,
    expected_version: int | None,
) -> dict:
    with conn.cursor() as cur:
        cur.execute("SELECT id, version FROM notes WHERE id = %s", (note_id,))
        row = cur.fetchone()
        if row is None:
            try:
                cur.execute(
                    """
                    INSERT INTO notes (id, path, title, type, status, body, frontmatter, writer, version, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1, %s, now())
                    RETURNING version
                    """,
                    (note_id, path, title, type_, status, body, Jsonb(frontmatter), writer, created),
                )
            except psycopg.errors.UniqueViolation:
                conn.rollback()
                cur.execute("SELECT version FROM notes WHERE id = %s", (note_id,))
                current = cur.fetchone()
                current_v = current["version"] if current else 1
                _log(cur, note_id, "cas_conflict", writer, expected_version, current_v, False, "insert race")
                conn.commit()
                return {
                    "ok": False,
                    "id": note_id,
                    "error": "cas_conflict",
                    "expected": expected_version,
                    "current": current_v,
                }
            saved = cur.fetchone()
            _log(cur, note_id, "insert", writer, None, saved["version"], True, None)
            _replace_links(cur, note_id, extract_links(body))
            conn.commit()
            return {"ok": True, "id": note_id, "version": saved["version"], "op": "insert"}

        if expected_version is None:
            expected_version = row["version"]
        cur.execute(
            """
            UPDATE notes
               SET path = %s, title = %s, type = %s, status = %s, body = %s,
                   frontmatter = %s, writer = %s, version = version + 1, updated_at = now()
             WHERE id = %s AND version = %s
         RETURNING version
            """,
            (path, title, type_, status, body, Jsonb(frontmatter), writer, note_id, expected_version),
        )
        saved = cur.fetchone()
        if saved is None:
            cur.execute("SELECT version FROM notes WHERE id = %s", (note_id,))
            current = cur.fetchone()
            current_v = current["version"] if current else None
            _log(cur, note_id, "cas_conflict", writer, expected_version, current_v, False, "version mismatch")
            conn.commit()
            return {
                "ok": False,
                "id": note_id,
                "error": "cas_conflict",
                "expected": expected_version,
                "current": current_v,
            }
        _log(cur, note_id, "update", writer, expected_version, saved["version"], True, None)
        _replace_links(cur, note_id, extract_links(body))
        conn.commit()
        return {"ok": True, "id": note_id, "version": saved["version"], "op": "update"}


def ingest(conn: psycopg.Connection, writer: str) -> dict:
    inserted = updated = conflicts = skipped = 0
    with conn.cursor() as cur:
        cur.execute("SELECT pg_advisory_lock(%s)", (ADVISORY_LOCK,))
    try:
        for folder in NOTE_DIRS:
            base = ROOT / folder
            if not base.exists():
                continue
            for path in sorted(base.rglob("*.md")):
                text = path.read_text(encoding="utf-8")
                meta, body = parse_frontmatter(text)
                if REQUIRED - set(meta):
                    skipped += 1
                    continue
                result = put_cas(
                    conn,
                    note_id=meta["id"],
                    path=str(path.relative_to(ROOT)),
                    title=meta["title"] or path.stem,
                    type_=meta["type"],
                    status=meta["status"],
                    body=body,
                    frontmatter=meta,
                    writer=writer,
                    created=parse_ts(meta.get("created")),
                    expected_version=None,
                )
                if not result["ok"]:
                    conflicts += 1
                elif result["op"] == "insert":
                    inserted += 1
                else:
                    updated += 1
    finally:
        with conn.cursor() as cur:
            cur.execute("SELECT pg_advisory_unlock(%s)", (ADVISORY_LOCK,))
        conn.commit()
    return {"ok": True, "inserted": inserted, "updated": updated, "conflicts": conflicts, "skipped": skipped}


def get_note(conn: psycopg.Connection, note_id: str) -> dict | None:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
        row = cur.fetchone()
        if not row:
            return None
        cur.execute("SELECT dst, rel FROM links WHERE src = %s", (note_id,))
        row["links"] = list(cur.fetchall())
        return row


def search_notes(conn: psycopg.Connection, query: str, limit: int) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, title, type, status, version,
                   ts_rank(to_tsvector('english', coalesce(title,'') || ' ' || body),
                           plainto_tsquery('english', %s)) AS rank
              FROM notes
             WHERE to_tsvector('english', coalesce(title,'') || ' ' || body) @@ plainto_tsquery('english', %s)
                OR title ILIKE %s
          ORDER BY rank DESC, updated_at DESC
             LIMIT %s
            """,
            (query, query, f"%{query}%", limit),
        )
        return list(cur.fetchall())


def dump_row(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if hasattr(v, "isoformat"):
            out[k] = v.isoformat()
        elif isinstance(v, (bytes, memoryview)):
            out[k] = list(v)
        else:
            out[k] = v
    return out


def format_yaml_value(value) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(str(item) for item in value) + "]"
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    text = str(value)
    if (text.startswith("[") and text.endswith("]")) or (text.startswith("{") and text.endswith("}")):
        return text
    special = set(":{}[]&*!|>%@`#'\"")
    if (
        text == ""
        or text.strip() != text
        or any(ch in text for ch in special)
        or text.lower() in {"true", "false", "null", "yes", "no"}
    ):
        return json.dumps(text, ensure_ascii=False)
    return text


def render_markdown(frontmatter: dict, body: str) -> str:
    keys = [key for key in FM_ORDER if key in frontmatter]
    keys.extend(key for key in frontmatter if key not in keys)
    lines = ["---"]
    for key in keys:
        lines.append(f"{key}: {format_yaml_value(frontmatter[key])}")
    lines.append("---")
    text = "\n".join(lines) + "\n"
    body = body or ""
    if body:
        text += "\n" + body
        if not body.endswith("\n"):
            text += "\n"
    else:
        text += "\n"
    return text


def projectable(note_id: str, path: str) -> bool:
    if note_id in SMOKE_IDS or note_id.startswith(SMOKE_PREFIXES):
        return False
    rel = Path(path)
    if rel.is_absolute() or ".." in rel.parts:
        return False
    return bool(rel.parts) and rel.parts[0] in NOTE_DIRS


def export(conn: psycopg.Connection, dest_root: Path | None = None) -> dict:
    dest_root = (dest_root or ROOT).resolve()
    written = skipped = unchanged = 0
    with conn.cursor() as cur:
        cur.execute("SELECT pg_advisory_lock(%s)", (ADVISORY_LOCK,))
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, path, title, type, status, body, frontmatter, created_at, updated_at
                  FROM notes
              ORDER BY path
                """
            )
            rows = list(cur.fetchall())
        for row in rows:
            if not projectable(row["id"], row["path"]):
                skipped += 1
                continue
            target = (dest_root / row["path"]).resolve()
            try:
                target.relative_to(dest_root)
            except ValueError:
                skipped += 1
                continue
            meta = dict(row["frontmatter"] or {})
            meta.setdefault("id", row["id"])
            meta.setdefault("title", row["title"])
            meta.setdefault("type", row["type"])
            meta.setdefault("status", row["status"])
            text = render_markdown(meta, row["body"])
            if target.exists() and target.read_text(encoding="utf-8") == text:
                unchanged += 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            tmp = target.with_name(target.name + ".tmp")
            tmp.write_text(text, encoding="utf-8")
            tmp.replace(target)
            written += 1
    finally:
        with conn.cursor() as cur:
            cur.execute("SELECT pg_advisory_unlock(%s)", (ADVISORY_LOCK,))
        conn.commit()
    return {"ok": True, "written": written, "unchanged": unchanged, "skipped": skipped}


def main() -> int:
    parser = argparse.ArgumentParser(description="frontier-kb Postgres store")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    sub.add_parser("ingest")
    export_p = sub.add_parser("export")
    export_p.add_argument("--dest", default=None, help="export root (default: vault root)")
    g = sub.add_parser("get")
    g.add_argument("--id", required=True)
    s = sub.add_parser("search")
    s.add_argument("--q", required=True)
    s.add_argument("--limit", type=int, default=20)
    p = sub.add_parser("put")
    p.add_argument("--id", required=True)
    p.add_argument("--path", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--type", dest="type_", required=True)
    p.add_argument("--status", default="draft")
    p.add_argument("--body", default="")
    p.add_argument("--cas", type=int, default=None)
    p.add_argument("--writer", default=os.environ.get("KB_WRITER", "cli"))
    args = parser.parse_args()
    writer = os.environ.get("KB_WRITER", getattr(args, "writer", "cli"))

    try:
        conn = connect()
    except psycopg.OperationalError as exc:
        print(json.dumps({"ok": False, "error": "connect", "detail": str(exc)}))
        return 2

    try:
        if args.cmd == "init":
            apply_schema(conn)
            print(json.dumps({"ok": True, "op": "init"}))
        elif args.cmd == "ingest":
            apply_schema(conn)
            print(json.dumps(ingest(conn, writer)))
        elif args.cmd == "export":
            apply_schema(conn)
            dest = Path(args.dest).resolve() if args.dest else ROOT
            print(json.dumps(export(conn, dest)))
        elif args.cmd == "get":
            row = get_note(conn, args.id)
            print(json.dumps(dump_row(row) if row else {"ok": False, "error": "not_found"}))
        elif args.cmd == "search":
            print(json.dumps([dump_row(r) for r in search_notes(conn, args.q, args.limit)]))
        elif args.cmd == "put":
            result = put_cas(
                conn,
                note_id=args.id,
                path=args.path,
                title=args.title,
                type_=args.type_,
                status=args.status,
                body=args.body,
                frontmatter={"id": args.id, "title": args.title, "type": args.type_},
                writer=args.writer,
                created=datetime.now(timezone.utc),
                expected_version=args.cas,
            )
            print(json.dumps(result))
            return 0 if result["ok"] else 1
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
