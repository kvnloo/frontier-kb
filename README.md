# frontier-kb

Cross-harness intelligence knowledge base for Kevin's OSS / agent factory.

**Owner agent:** [frontier](https://github.com/kvnloo) Grok Bot (`7443a4ff`) — continuous research across coding harnesses + frontier labs.  
**Orchestrator:** CoS — mints Linear HITLs from KB findings; never lets frontier origin-write.

## What this is

An **Obsidian-compatible** git vault (Zettelkasten + atlas MOCs) with a machine-readable schema so frontier / autoresearch loops can append structured notes without schema drift.

Covers:

- Coding harnesses: OMP, Hermes, Pi, Codex, Claude Code, Cursor, Grok, Crush, OpenCode, Firstmate, o8, Prime Intelligence, peers
- LLM / agent research: tool use, skills, frameworks, memory, evals, voice, tokenomics
- Multi-discipline audit lenses: physics, CS, information theory, neuroscience, mathematics, statistics, data science, AI/ML

## Layout

| Path | Role |
|------|------|
| `inbox/` | Raw captures (fleeting); process or delete. See `inbox/README.md` for distributed-writer conventions |
| `inbox/<node>/` | Per-node distributed writes (e.g. `frontier/`, `omp/`) — mesh writers ONLY write to their node dir |
| `literature/` | Source notes (papers, blogs, releases) — cite primaries |
| `permanent/` | Atomic claims in our words + [[wikilinks]] |
| `harnesses/` | One note per harness product (capabilities, DX, gaps) |
| `domains/` | Discipline MOC stubs (physics…AI/ML) |
| `atlas/` | Maps of content / indexes |
| `templates/` | Frontmatter schemas frontier must use |
| `data/sources.yaml` | Canonical poll URLs for autoresearch |
| `scripts/` | Schema check + ingest helpers |

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
