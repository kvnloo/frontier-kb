---
id: lit-20260910-kb-hosting-postgres
title: "Host the operational KB on pooled Postgres; Neon Free works until always-on"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://neon.com/docs/introduction/plans", "https://neon.com/docs/connect/connection-pooling", "https://neon.com/docs/introduction/agent-plan", "https://supabase.com/pricing", "https://supabase.com/docs/guides/platform/compute-and-disk", "https://www.cognee.ai/graph-on-postgres", "https://mnemoverse.com/docs/library/ai-memory-solutions-2026-q3"]
harnesses: [omp, hermes, cursor, claude, pi]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [literature, postgres, neon, supabase, hosting, pgvector]
---

# Host the operational KB on pooled Postgres; Neon Free works until always-on

## Claim (one sentence)

The unified store for 100 harnesses is one Postgres (pgvector + CAS), not a memory vendor; host it on **host 0** (always-on PC, Tailscale `100.113.138.100:55442`). Neon pooled Postgres is the fallback if 0 is down. Do not vendor Cognee/Mem0/Letta.

## Evidence

### What we already have

This repo's machine store is `store/schema.sql` + `scripts/kb_store.py` on `pgvector/pgvector:pg16` (`docker compose up -d kb`, port 55432). Agents `put` unique ids or `UPDATE … WHERE version = $n`. Markdown is `ingest`/`export`. That is Cognee 1.0's **shape** (one Postgres for notes + links + events + placeholder embeddings), not a Cognee runtime.

Mnemoverse Q3 2026: Mem0 is a drop-in fact API, Letta is a runtime, Zep/Graphiti is a bi-temporal graph needing Neo4j/FalkorDB, Cognee is an ECL pipeline, Supermemory is a closed engine. None of those replace our literature/permanent/harness schema.

### Hosting options (retrieved 2026-09-10)

| Host | Cost | Storage | Connections | Always-on | Fit |
| --- | --- | --- | --- | --- | --- |
| **Host 0 compose** (groot, Tailscale) | $0 | disk | 200 | yes, 24/7 | **Production.** Loopback + `100.113.138.100:55442`. |
| **Local compose** | $0 | disk | 200 (`max_connections`) | yes, one machine | Dev on mbp. Prefer pointing mbp at 0. |
| **Neon Free** | $0 | 0.5 GB/project | 0.25 CU ≈ 104 `max_connections` (7 reserved); PgBouncer `-pooler` up to 10k *client* conns, transaction mode | Scale-to-zero after 5 min, **cannot disable** | Fine for the current tiny corpus. Cold start is the 100-agent failure mode. 100 CU-hours/project/month; 5 GB egress. |
| **Neon Launch** | pay-as-you-use (~$0.106/CU-hour; 0.25 CU always-on ≈ a few $/mo) | $0.35/GB-month | same pooling; autoscaling to 16 CU | Scale-to-zero can be **disabled** | Production DSN for a continuous factory. |
| **Neon Agent Plan** | Scale enrollment + approval | sponsored free org | fleet API | n/a | For platforms that provision *thousands of DBs for end users*. We need **one** shared KB. Skip. |
| **Supabase Free** | $0 | 500 MB | Nano: 60 direct / 200 pooler | **Paused after 1 week inactivity**; 2 active projects | Worse always-on than Neon. pgvector included. |
| **Supabase Pro** | $25 + compute (Micro ~$10, credits cover one) | 8 GB then $0.125/GB | Micro 60/200 | never pauses | Extra Auth/Realtime we do not need for a note store. |
| **Self-host VM** (Oracle always-free, Hetzner, Fly) | $0–cheap | disk | set `max_connections` + PgBouncer | yes | Same image as compose. You own backups and TLS. |

Neon pooling: agents use the hostname with `-pooler`. Direct (non-pooler) connections for `init` / `ingest` / `export` / `pg_dump`: those take a *session* advisory lock (`pg_advisory_lock`), which PgBouncer transaction mode does not keep across transactions. Agent `put` / `get` / `search` is row-level `UPDATE … WHERE version` and is transaction-safe on the pooler.

### 100 agents vs free-tier limits

100 concurrent **clients** must use the pooler and drop connections after each put/get/search. They must not hold 100 idle direct sessions. Neon Free's 97 application slots plus pooler is enough for bursty writes if agents disconnect. A 24/7 factory that never idles 5 minutes should disable scale-to-zero (Launch) or run compose on a VM.

Storage is not the constraint: 0.5 GB holds far more than this Zettelkasten.

## Fact vs interpretation

- Fact: Neon Free and Supabase Free both give pgvector Postgres at $0. Neon Free suspends after 5 minutes; Supabase Free pauses after 7 days.
- Fact: Neon PgBouncer accepts 10k client connections; actual Postgres backends are still `max_connections` for the compute size.
- Interpretation: Do not buy Cognee Cloud, Zep Flex ($1,250/year), or Mem0 Platform for this vault. Point `FRONTIER_KB_DSN` at one Postgres.
- HOLD: embeddings stay `vector(8)` until we pick a model. ANN is not live on any host.

## Links

- Neon plans: https://neon.com/docs/introduction/plans
- Neon pooling: https://neon.com/docs/connect/connection-pooling
- Supabase pricing: https://supabase.com/pricing
- Cognee Just Postgres: https://www.cognee.ai/graph-on-postgres
- [[literature/lit-20260910-agent-memory-postgres]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]
