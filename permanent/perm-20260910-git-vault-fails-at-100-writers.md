---
id: perm-20260910-git-vault-fails-at-100-writers
title: "A git markdown vault cannot take 100 concurrent writers"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, pi, grok]
domains: [cs, frameworks]
confidence: high
tags: [permanent, git, sqlite, concurrency]
---

# A git markdown vault cannot take 100 concurrent writers

## Idea (atomic)

Obsidian files plus git PRs are a review log, not a database. Unbounded readers can clone. 100 concurrent writers cannot. Unique new notes usually survive; shared MOCs and in-place edits race. Git has no compare-and-swap; merge is the lock; last-write-wins is silent data loss. The SQLite funnel in PER-1297 still serializes writers (`SQLITE_BUSY` under WAL). 100 agents must not `write()` the vault.

## Why it matters for our harnesses

Frontier, OMP, Hermes, Cursor, Grok, and Pi can all *read* the checkout. They write to Postgres (`FRONTIER_KB_DSN`) and a single serializer exports accepted notes (`python scripts/kb_store.py export`). `inbox/<node>/` is an export convention after the store accepts the row, not a hot lock. Mixing 100 harness checkouts into one working tree is how this vault dies.

## Related

- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-agent-kb-concurrency]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
