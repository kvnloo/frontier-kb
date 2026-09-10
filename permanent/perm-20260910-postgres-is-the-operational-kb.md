---
id: perm-20260910-postgres-is-the-operational-kb
title: "Postgres is the operational KB; git is the export"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, pi]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [permanent, postgres, pgvector, cognee]
---

# Postgres is the operational KB; git is the export

## Idea (atomic)

Operational R/W for this factory is Postgres with pgvector: append-only `events`, CAS on `notes.version`, node rows matching `inbox/<node>/`. A single serializer exports accepted notes to markdown for Obsidian and PRs. That is the Cognee 1.0 "Just Postgres" shape without vendoring Cognee's extract pipeline.

## Why it matters for our harnesses

100 agents connect to `FRONTIER_KB_DSN` (compose maps 55432). They never share a git index. Humans still open this folder in Obsidian. If we later need Cognee ECL or Hindsight retrieval, they sit on the *same* database — we do not add Neo4j.

## Related

- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-agent-kb-concurrency]]
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
- `scripts/kb_store.py`
