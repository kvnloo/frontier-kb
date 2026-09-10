---
id: perm-20260910-host-kb-on-pc0-tailnet
title: "The shared KB runs on host 0 over Tailscale, not Neon"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, firstmate, cursor, grok]
domains: [cs, frameworks]
confidence: high
tags: [permanent, hosting, pc0, tailscale]
---

# The shared KB runs on host 0 over Tailscale, not Neon

## Idea (atomic)

Production ledger is `pgvector/pg16` on **host 0** (`groot`, `100.113.138.100`, SSH alias `0`), 24/7. Bind loopback plus the Tailscale address (`55432`). Harnesses on mbp and PAIR-routed workers set `FRONTIER_KB_DSN` to that tailnet URL. Markdown export stays git. Neon/Supabase are a fallback if 0 is down, not the default.

## Why it matters for our harnesses

Firstmate, Hermes, and OMP already live on this LAN/tailnet. PAIR routes inference; it has no note schema. hermes-mesh-keel SQLite is signed envelopes. Both keep doing their jobs. The KB is one extra DSN + `scripts/kb_store.py`. Do not flip keel `production_enabled` to "wire the KB."

## Related

- [[literature/lit-20260910-kb-hosting-postgres]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]
- `scripts/install-host-0.sh`
