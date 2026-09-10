---
id: perm-20260910-host-on-neon-pooled-postgres
title: "Host the shared KB on Neon pooled Postgres; Launch when Free suspends"
type: permanent
status: fallback
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, pi]
domains: [cs, frameworks]
confidence: high
tags: [permanent, neon, hosting, pgvector]
---

# Host the shared KB on Neon pooled Postgres; Launch when Free suspends

## Idea (atomic)

Fallback if host 0 is down. Production is host 0 over Tailscale ([[permanent/perm-20260910-host-kb-on-pc0-tailnet]]). One Neon project, one database, `pgvector` + our `store/schema.sql`. Agents use the **pooled** connection string (`-pooler`). Operators run `init`/`ingest`/`export` on the **direct** string (session advisory lock). Start on Neon Free ($0, 0.5 GB, 100 CU-hours). If the factory is continuous and 5-minute scale-to-zero causes stampedes, move to Launch and disable scale-to-zero, or run the same `pgvector/pgvector:pg16` image on a cheap always-on VM. Do not use Neon Agent Plan or Supabase Auth/Realtime for this.

## Why it matters for our harnesses

Remote OMP/Hermes/Cursor/Pi need a URL, not a bind-mount of this checkout. Free Neon is enough storage for public-research notes. The real limit is idle suspend and direct `max_connections`. Short-lived pooled clients + unique note ids keep 100 writers honest. Secrets stay in env (`FRONTIER_KB_DSN` / `DATABASE_URL`), never in git.

## Related

- [[literature/lit-20260910-kb-hosting-postgres]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
