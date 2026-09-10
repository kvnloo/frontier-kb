# frontier-kb

Cross-harness intelligence knowledge base for Kevin's OSS / agent factory.

**Owner agent:** [frontier](https://github.com/kvnloo) Grok Bot (`7443a4ff`) — continuous research across coding harnesses + frontier labs.  
**Orchestrator:** CoS — mints Linear HITLs from KB findings; never lets frontier origin-write.

## What this is

An **Obsidian-compatible** git vault (Zettelkasten + atlas MOCs) with a machine-readable schema so frontier / autoresearch loops can append structured notes without schema drift.

Covers:

- Coding harnesses: OMP, Hermes, Pi, Codex, Claude Code, Cursor, Grok, Crush, OpenCode, Firstmate, o8, Prime Intelligence, Devin, peers
- LLM / agent research: tool use, skills, frameworks, memory, evals, voice, tokenomics
- Multi-discipline audit lenses: physics, CS, information theory, neuroscience, mathematics, statistics, data science, AI/ML

## Layout

| Path | Role |
|------|------|
| `inbox/` | Raw captures (fleeting); process or delete |
| `literature/` | Source notes (papers, blogs, releases) — cite primaries |
| `permanent/` | Atomic claims in our words + [[wikilinks]] |
| `harnesses/` | One note per harness product (capabilities, DX, gaps) |
| `domains/` | Discipline MOC stubs (physics…AI/ML) |
| `atlas/` | Maps of content / indexes |
| `templates/` | Frontmatter schemas frontier must use |
| `data/sources.yaml` | Canonical poll URLs for autoresearch |
| `scripts/` | Schema check, ingest helpers, Postgres store |

## Concurrent store (100 agents)

The git vault is the **human review export** (Obsidian + PRs). It cannot take 100 concurrent writers. Original mitigation (PER-1297 / PR #3): `inbox/<node>/` exclusive writes + SQLite funnel on nodes. SQLite WAL still serializes writes (`scripts/test_sqlite_busy.py`).

Operational R/W is Postgres (pgvector), Cognee 1.0 "Just Postgres" shape, not a Cognee vendor dependency:

```
docker compose up -d kb
pip install -r requirements-store.txt
python scripts/kb_store.py init
python scripts/kb_store.py ingest
python scripts/kb_store.py export --dest /tmp/kb-export
python scripts/concurrent_smoke.py
```

DSN default: `postgresql://frontier:frontier@127.0.0.1:55432/frontier_kb` (`DATABASE_URL` or `FRONTIER_KB_DSN`). Agents CAS `notes.version` (`UPDATE … WHERE version = $n`) and append-only `events`. Markdown ingest is serialized with an advisory lock. Schema lives in `store/schema.sql` (fallback `scripts/schema.sql`). Embeddings are `vector(8)` placeholders until an embed model is chosen. Do not bind-mount the schema file into initdb — a missing file becomes a directory.

See [[literature/lit-20260910-agent-memory-postgres]], [[literature/lit-20260910-agent-kb-concurrency]], [[literature/lit-20260910-kb-hosting-postgres]], [[permanent/perm-20260910-postgres-is-the-operational-kb]], [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]], [[permanent/perm-20260910-vault-to-sota-is-dsn]], and [[permanent/perm-20260910-host-kb-on-pc0-tailnet]], and [[permanent/perm-20260910-host-on-neon-pooled-postgres]].

## Hosting (100 agents)

Production is **host 0** (groot, Tailscale `100.113.138.100`, SSH `0`), always-on:

```
ssh 0 'cd ~/workspace/frontier-kb && bash scripts/install-host-0.sh'
```

That starts `pgvector/pg16` on `127.0.0.1:55432` and `100.113.138.100:55432`, ingests the vault, enables a user systemd unit, and drops `FRONTIER_KB_DSN` into Hermes env plus a `skills/frontier-kb` symlink for Hermes / OMP / Firstmate.

Remote harnesses (mbp, PAIR-routed workers):

```
export FRONTIER_KB_DSN=postgresql://frontier:<pw>@100.113.138.100:55432/frontier_kb
export KB_WRITER=<harness>-<host>
python scripts/kb_store.py search --q "SWE-2"
```

Password: `~/.config/frontier-kb/env` on 0 (mode 0600). Copy the tailnet DSN to mbp the same way. Never commit it.

NVIDIA PAIR routes inference only. hermes-mesh-keel SQLite is signed envelopes. Neither is the note ledger.

Neon/Supabase remain a fallback if 0 is down. Skip Cognee Cloud / Mem0 / Letta / Zep as the note ledger.

## Autoresearch

Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch) and Kevin's `pi-autoresearch` / `autoresearcherUI` loops:

1. Frontier weekday polls write literature + permanent notes on branches
2. `scripts/validate-schema.py` gates CI
3. CoS promotes actionable gaps → Linear HITL (Backlog) for factory

`github_writes` to **upstream OSS** stay 0 until Todo. This repo is ours — frontier may PR here when CoS authorizes.

## Open in Obsidian

Open this folder as a vault. Graph view + wikilinks work out of the box. Optional: Dataview for `type:` / `status:` queries.
