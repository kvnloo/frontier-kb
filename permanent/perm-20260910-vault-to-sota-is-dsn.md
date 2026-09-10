---
id: perm-20260910-vault-to-sota-is-dsn
title: "Vault to SOTA is a DSN cutover, not a product rewrite"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, pi]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [permanent, kb, postgres, migration]
---

# Vault to SOTA is a DSN cutover, not a product rewrite

## Idea (atomic)

Keep the Zettelkasten (id, type, status, wikilinks, git review). Make Postgres the live ledger. Every harness reads and writes `FRONTIER_KB_DSN` (`scripts/kb_store.py put|get|search`). One process `ingest`s the existing markdown, then `export`s accepted rows back to this folder for Obsidian and PRs. Do not replace the store with Cognee, Mem0, Letta, Graphiti, or Supermemory.

## Why it matters for our harnesses

The factory already has 100-agent CAS locally. Production DSN is host 0 over Tailscale. The remaining work is operational: publish that DSN, stop agents from `write()`ing markdown, unique-id new literature/permanents, CAS-retry on `cas_conflict`. MOCs (`atlas/`, `domains/`) are regenerated from `links`, not hand-edited under contention. Retrieval today is FTS; embeddings come later on the same tables.

## Related

- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-kb-hosting-postgres]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]
