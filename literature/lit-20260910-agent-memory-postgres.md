---
id: lit-20260910-agent-memory-postgres
title: "Agent memory SOTA is one Postgres, not a git vault plus SQLite funnel"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://www.cognee.ai/just-postgres", "https://hindsight.vectorize.io/blog/2026/08/11/open-source-agent-memory-systems", "https://github.com/kvnloo/frontier-kb/pull/3", "https://linear.app/0ism/issue/PER-1297"]
harnesses: [omp, hermes, cursor, claude, pi]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [literature, postgres, pgvector, cognee, hindsight, concurrency]
---

# Agent memory SOTA is one Postgres, not a git vault plus SQLite funnel

## Claim (one sentence)

100 harness agents cannot share this vault by writing markdown files; the 2026 self-host pattern is one Postgres (graph + pgvector + sessions), with git kept as the human export.

## Evidence

### What this repo actually shipped (2026-09-09)

Initial commit `991bb8c`: Obsidian-compatible git Zettelkasten + schema CI, inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch). That is the *literature* layer.

PER-1297 / [PR #3](https://github.com/kvnloo/frontier-kb/pull/3) (open): `inbox/<node>/` exclusive writes, frontmatter CI, **SQLite funnel on nodes; promote short schema-valid notes only**. The funnel exists because SQLite WAL is one writer and git is last-write-wins. 100 agents hitting the same files produce merge conflicts, not a knowledge graph.

OMP already has the same bottleneck in-tree: mnemopi/SHMR on SQLite (PER-811).

### 2026 self-host agent memory (do not invent a new product)

| System | Storage | Concurrent R/W | Fit for this vault |
| --- | --- | --- | --- |
| **Cognee 1.0 Just Postgres** ([post](https://www.cognee.ai/just-postgres), updated 2026-09-03) | graph + pgvector + SQL session cache + metadata in **one** Postgres; local still SQLite/LanceDB | single-transaction graph+vector writes; SQL session cleanup | Architecture to copy. Do not vendor Cognee into v0 (runtime/LLM extract pipeline is heavier than a note store). |
| **Hindsight** ([roundup](https://hindsight.vectorize.io/blog/2026/08/11/open-source-agent-memory-systems)) | one container, embedded PostgreSQL, MIT, multi-strategy retrieval | one service | Evidence that "one Postgres" is the boring deploy. Vendor-authored scores (LongMemEval/BEAM) — treat as pattern, not a purchase. |
| Graphiti / Zep | Neo4j or FalkorDB (embedded FalkorDB lite exists) | ingestion concurrency limited by LLM 429s | Extra graph ops. Skip unless we need bi-temporal edges. |
| Mem0 | embedded default; production often external vector DB | conversational `user_id`/`agent_id` | Personalization, not a literature vault. |
| Letta | agent runtime + memory | n/a | Runtime, not a store. |

Cognee's own table: relationships, embeddings, sessions, metadata used to be four systems; 1.0 puts them in Postgres. They report ~10% faster search than split graph+vector from fewer hops, and 6M+ memories/month.

### What 100 agents need

- Append-only **events** (never update a row another agent holds).
- **CAS** on note `revision` (Postgres `UPDATE ... WHERE revision = $n`).
- Node isolation matching `inbox/<node>/`.
- A **single serializer** that exports notes to markdown for Obsidian/PR review.

Git remains the review surface. Postgres is the operational surface.

## Fact vs interpretation

- Fact: this vault is markdown in git. PR #3 names a SQLite funnel. SQLite serializes writers.
- Fact: Cognee 1.0 and Hindsight both collapsed agent memory onto Postgres.
- Interpretation: copy the Postgres unification, do not replace Obsidian, do not take Cognee as a hard dependency in v0.
- HOLD: embeddings are `vector(8)` placeholders until we pick an embed model. Do not pretend ANN is live.

## Links

- Cognee: https://www.cognee.ai/just-postgres
- Hindsight roundup: https://hindsight.vectorize.io/blog/2026/08/11/open-source-agent-memory-systems
- PER-1297: https://linear.app/0ism/issue/PER-1297
- Store: `scripts/kb_store.py` · `store/schema.sql`
- [[literature/lit-20260910-agent-kb-concurrency]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
