---
id: lit-20260910-agent-kb-concurrency
title: "100-agent KBs: git vaults serialize; Graphiti is memory; Postgres CAS is the note store"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://github.com/getzep/graphiti", "https://www.getzep.com/platform/graphiti/", "https://linear.app/0ism/issue/PER-299", "https://linear.app/0ism/issue/PER-1297"]
harnesses: [omp, hermes, claude, cursor, grok]
domains: [cs, frameworks]
confidence: high
tags: [literature, kb, postgres, graphiti, concurrency]
---

# 100-agent KBs: git vaults serialize; Graphiti is memory; Postgres CAS is the note store

## Claim (one sentence)

This vault (Obsidian markdown + git) supports unbounded concurrent *reads* and serializes *writes* through git/PRs; 100 harnesses writing the same files lose updates. 2026 SOTA agent *memory* is Graphiti/Zep (temporal KG on Neo4j/FalkorDB/Kuzu). The SOTA for *this* Zettelkasten is Postgres with CAS + a markdown export, which is what PER-299 called a git-reviewable registry rather than a second wiki.

## Evidence

### Failure mode of this repo today

100 agents `read`/`write` markdown:

- Distinct new files (`inbox/<node>/…`) usually merge. PER-1297 is this convention, still GitHub-serialized.
- Shared MOCs (`atlas/home.md`, `domains/*.md`) last-write-wins or conflict. Two agents appending the same bullet is a dirty worktree, not a transaction.
- Git has no row-level CAS. `git pull --rebase` is human/CI, not 100-writer MVCC.
- GitHub rate limits and PR queues become the lock. That is fine for frontier weekday polls. It is not a hot store.

Linear PER-299 (2026-09-06 federated map): keep content in authoritative sources; add a local registry of Resources/Entities/Relations; Linear is the human projection, not the machine corpus. Exact IDs and metadata first; embeddings only for recall.

Original frontier-kb choice (991bb8c): Obsidian Zettelkasten + schema CI, inspired by karpathy/autoresearch. That is the *human and review* layer. It was never a concurrent database.

### Ranked 2026 systems (agent KB / memory)

| System | What it is | Concurrent writers | Fits this vault? |
| --- | --- | --- | --- |
| **Postgres + CAS** | Notes/links/events, `UPDATE … WHERE version=` | Yes (MVCC) | Yes: same ids/frontmatter, markdown is a projection |
| **Graphiti / Zep** (Apache-2.0, ~30k★) | Temporal context graph from episodes; hybrid vector+FTS+graph | Yes, via FalkorDB/Neo4j; `group_id` multi-tenant | Overlay later. Episodes ≠ literature/permanent notes. Not postgres-native notes |
| mem0 | Memory layer, popularity winner | Yes (service) | Conversation memory, not Zettelkasten schema |
| Letta | MemGPT production | Yes | Agent state, not this schema |
| LightRAG / cognee | GraphRAG | Ingest-heavy | Retrieval, not multi-writer notes |
| Khoj | Personal research assistant (in factory roster) | App, not a 100-writer ledger | Wrong layer |
| SQLite WAL | One writer | No | 100 agents queue; not the ask |

Graphiti backends in 2026: Neo4j, FalkorDB, Kuzu, Neptune — not a drop-in replacement for `literature/` markdown. Zep reports beating mem0 on LongMemEval. That is the memory SOTA, not the note-store SOTA.

## Fact vs interpretation

- Fact: git markdown cannot give 100 agents lossless concurrent writes on shared notes.
- Fact: Graphiti is the 2026 SOTA temporal memory engine; it does not preserve our literature/permanent/harness schema or git review.
- Interpretation: machine store = Postgres notes+links with optimistic concurrency; Obsidian git remains the reviewable projection. Graphiti may ingest exported notes later. Do not migrate Linear into this corpus.

## Links

- Graphiti: https://github.com/getzep/graphiti
- PER-299: https://linear.app/0ism/issue/PER-299
- PER-1297: https://linear.app/0ism/issue/PER-1297
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
