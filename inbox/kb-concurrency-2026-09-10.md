---
id: inbox-kb-concurrency-20260910
title: "KB concurrent R/W: git vault vs Postgres"
type: inbox
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, pi]
tags: [inbox, kb, postgres, concurrency]
---

# KB concurrency wave

User ask 2026-09-10: store SWE-2 properly; does the vault support 100 agents hitting it; move to Postgres or the SOTA store from the original setup.

Original setup (991bb8c + PER-1297 / PR #3): Obsidian git vault, `inbox/<node>/` exclusive writes, SQLite funnel on nodes, promote short notes via PR. That is a *human review* design. It is not a 100-writer operational store.

Processed:

- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-agent-kb-concurrency]]
- [[literature/lit-20260910-kb-hosting-postgres]]
- [[literature/lit-20260910-kb-mesh-pair-keel]]
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]

Store: `docker compose up -d kb`, `python scripts/kb_store.py init|ingest|export`, `python scripts/concurrent_smoke.py`.
Host: **0** (`100.113.138.100:55442`). `scripts/install-host-0.sh`. Neon is fallback. Mesh: PAIR routes inference; keel carries envelopes; agents `put`/`get`/`search`.
