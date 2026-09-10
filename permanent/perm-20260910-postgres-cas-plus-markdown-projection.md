---
id: perm-20260910-postgres-cas-plus-markdown-projection
title: "Postgres CAS is the machine store; markdown stays the projection"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, grok, claude]
domains: [cs, frameworks]
confidence: high
tags: [permanent, kb, postgres]
---

# Postgres CAS is the machine store; markdown stays the projection

## Idea (atomic)

Keep the Zettelkasten schema (id, type, status, frontmatter, body, wikilinks). Put the live rows in Postgres. Writers `INSERT` unique ids or `UPDATE … WHERE version = $expected`. Conflicts return the current row; the agent re-reads. MOCs are regenerated from the `links` table, never hand-edited under contention. `scripts/kb_store.py ingest|export` keeps git/Obsidian/CI in sync as a batch, under an advisory lock. Export writes markdown under `--dest` (default: vault root) and skips smoke rows.

Graphiti/Zep can later ingest exported notes as a retrieval overlay. It is not the note ledger.

## Why it matters for our harnesses

This is the original vault intent (schema-gated notes, git review) plus the PER-299 registry, with actual MVCC. 100 harnesses can write without a PR queue. Humans still open Obsidian.

## Related

- [[literature/lit-20260910-agent-kb-concurrency]]
- [[literature/lit-20260910-agent-memory-postgres]]
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
