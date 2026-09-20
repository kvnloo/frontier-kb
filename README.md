# frontier-kb

Cross-harness intelligence knowledge base for Kevin's OSS / agent factory.

**Owner agent:** [frontier](https://github.com/kvnloo) Grok Bot (`7443a4ff`) — continuous research across coding harnesses + frontier labs.  
**Orchestrator:** CoS — mints Linear HITLs from KB findings; never lets frontier origin-write.

## What this is

An **Obsidian-compatible** git vault (Zettelkasten + atlas MOCs) with a machine-readable schema so frontier / autoresearch loops can append structured notes without schema drift.

This is **cutting-edge research memory only**: harnesses, papers, labs, evals, tokenomics, SOTA. It is not personal agentic memory.

**Personal agentic memory stays private in Hermes** (`~/.hermes/memories`). Do not copy chats, USER.md, MEMORY.md, operator preferences, or private session recall into this vault or its Postgres store. Dash may later *display* this research plane as one UI surface; it is not a write path for personal memory.

Covers:

- Coding harnesses: OMP, Hermes, Pi, Codex, Claude Code, Cursor, Grok, Crush, OpenCode, Firstmate, o8, Prime Intelligence, Devin, fx, peers. Canonical ids in [kvnloo/aodl `harnesses/catalog.json`](https://github.com/kvnloo/aodl/blob/main/harnesses/catalog.json). Firstmate is a distro.
- LLM / agent research: tool use, skills, frameworks, memory, evals, voice, tokenomics
- Multi-discipline audit lenses: physics, CS, information theory, neuroscience, learning-acceleration, mathematics, statistics, data science, AI/ML
- Human learning OS: encode → retrieve → rest → measure → prune (Sung / Huberman / Johnson / Patrick). Frontend: [kvnloo/humanity-vault](https://github.com/kvnloo/humanity-vault)

## Layout

| Path | Role |
|------|------|
| `inbox/` | Raw captures (fleeting); process or delete. See `inbox/README.md` for distributed-writer conventions |
| `inbox/<node>/` | Per-node distributed writes (e.g. `frontier/`, `omp/`) — mesh writers ONLY write to their node dir |
| `literature/` | Source notes (papers, blogs, releases) — cite primaries |
| `permanent/` | Atomic claims in our words + [[wikilinks]] |
| `harnesses/` | One note per harness product (capabilities, DX, gaps) |
| `domains/` | Discipline MOCs (physics…AI/ML, learning-acceleration) |
| `atlas/` | Maps of content / indexes |
| `graphql/` | Brain GraphQL schema (humanity-vault contract) |
| `templates/` | Frontmatter schemas frontier must use |
| `data/sources.yaml` | Canonical poll URLs for autoresearch |
| `scripts/` | Schema check, ingest helpers, Postgres store, synapse loop, GraphQL |
| `apps/humanity-vault/` | Mobile GraphQL learning OS (also published as kvnloo/humanity-vault) |

## Concurrent store (100 agents)

The git vault is the **human review export** (Obsidian + PRs). It cannot take 100 concurrent writers. Original mitigation (PER-1297 / PR #3): `inbox/<node>/` exclusive writes + SQLite funnel on nodes. SQLite WAL still serializes writes (`scripts/test_sqlite_busy.py`).

Operational R/W is Postgres (pgvector), Cognee 1.0 "Just Postgres" shape, not a Cognee vendor dependency:

```
docker compose up -d kb
pip install -r requirements-store.txt
python scripts/kb_store.py init
python scripts/kb_store.py ingest
python scripts/kb_store.py export --dest /tmp/kb-export
python scripts/concurrent_smoke.py
```

Local development may use a loopback Postgres DSN via `DATABASE_URL` or `FRONTIER_KB_DSN`; credentials and non-loopback addresses stay in local configuration. Agents CAS `notes.version` (`UPDATE … WHERE version = $n`) and append-only `events`. Markdown ingest is serialized with an advisory lock. Schema lives in `store/schema.sql` (fallback `scripts/schema.sql`). Embeddings are `vector(8)` placeholders until an embed model is chosen. Do not bind-mount the schema file into initdb — a missing file becomes a directory.

## Humanity's vault (brain loop)

The markdown vault is the review export. The **brain** is synapses + usage:

```
python scripts/kb_store.py init
python scripts/kb_store.py ingest
python scripts/synapse_loop.py seed
python scripts/synapse_loop.py loop          # dry-run decay + prune proposals
python scripts/synapse_loop.py fire --id perm-20260911-encoding-beats-exposure --actor human-kb
python scripts/graphql_server.py              # GraphQL on :8787
```

Notes are neurons. Wikilinks seed synapses. Human retrieve/encode and agent search/get are spikes. Idle edges decay (sleep-homeostasis analog). Below threshold, `status` becomes `pruned` (never DELETE). Frontend: [kvnloo/humanity-vault](https://github.com/kvnloo/humanity-vault).

See [[domains/learning-acceleration]], [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]].

See [[literature/lit-20260910-agent-memory-postgres]], [[literature/lit-20260910-agent-kb-concurrency]], [[literature/lit-20260910-kb-hosting-postgres]], [[permanent/perm-20260910-postgres-is-the-operational-kb]], [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]], [[permanent/perm-20260910-vault-to-sota-is-dsn]], and [[permanent/perm-20260910-host-kb-on-pc0-tailnet]], and [[permanent/perm-20260910-host-on-neon-pooled-postgres]].

## Hosting (100 agents)

The public repository documents the **deployment shape**, not private network coordinates.

A designated always-on host can run the Postgres/pgvector store and expose it to trusted harnesses over a private network. Keep hostnames, tailnet addresses, DSNs, passwords, and machine-specific paths in local configuration or a secret manager; never commit them to this public research vault.

```sh
# on the designated host
bash scripts/install-host-0.sh

# on an authorized client
export FRONTIER_KB_DSN='postgresql://USER:PASSWORD@PRIVATE_HOST:PORT/frontier_kb'
export KB_WRITER='<harness>-<host>'
python scripts/kb_store.py search --q "SWE-2"
```

The deployment script defaults to loopback binding. A private-network bind address must be supplied explicitly through local environment configuration.

NVIDIA PAIR routes inference only. hermes-mesh-keel SQLite is signed envelopes. Neither is the note ledger.

Hosted Postgres services remain fallback options. Memory products such as Mem0, Letta, or Zep are different layers and are not treated as the canonical note ledger.

## Autoresearch & Distributed Writers

Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch) and Kevin's `pi-autoresearch` / `autoresearcherUI` loops:

1. Frontier weekday polls write literature + permanent notes on branches
2. Mesh writers (frontier, OMP, etc.) write **only** to `inbox/<node>/` — never cross-write to other dirs
3. PR flow: node writes → open PR → `scripts/validate-schema.py` CI gate → merge to main
4. CoS promotes actionable gaps → Linear HITL (Backlog) for factory

**Rules for distributed writers:**
- Write to `inbox/<node>/` only (your assigned node subdirectory)
- All notes under `inbox/` require frontmatter: `id`, `title`, `type`, `status`, `created`, `updated`
- Run SQLite funnel on nodes; promote short, schema-valid notes only
- **NEVER copy personal or private data into this public vault** — all content is public OSS

`github_writes` to **upstream OSS** stay 0 until Todo. This repo is ours — frontier may PR here when CoS authorizes.

## Open in Obsidian

Open this folder as a vault. Graph view + wikilinks work out of the box. Optional: Dataview for `type:` / `status:` queries.

## Network

- IR: [kvnloo/aodl](https://github.com/kvnloo/aodl) (HOTL 0.2; no `consciousness` kind)
- FlyForge engine: [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) ([ROADMAP.md](https://github.com/kvnloo/evolution-lab/blob/main/ROADMAP.md); claimable P0 is [issue #2](https://github.com/kvnloo/evolution-lab/issues/2))
- Claim protocol: [kvnloo/verified-oss-loop](https://github.com/kvnloo/verified-oss-loop) (leases on evolution-lab GitHub, not this vault)
- Phone: [kvnloo/dash](https://github.com/kvnloo/dash)
- Hermes governance: [kvnloo/hermes-keel](https://github.com/kvnloo/hermes-keel)
- Human frontend: [kvnloo/humanity-vault](https://github.com/kvnloo/humanity-vault) (GraphQL learning OS)
