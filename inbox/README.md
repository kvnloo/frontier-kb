# inbox/

Raw captures and distributed writes from mesh nodes.

## Layout

- `inbox/` — Root-level fleeting captures (CoS, ad hoc)
- `inbox/<node>/` — Per-node incoming notes from distributed writers

## Distributed Writer Nodes

Each node in the mesh writes **only** to its own `inbox/<node>/` subdirectory:

| Node | Writes to | Owner |
|------|-----------|-------|
| `frontier` | `inbox/frontier/` | Frontier agent (Grok Bot `7443a4ff`) |
| `omp` | `inbox/omp/` | OMP harness agent |
| *(others)* | `inbox/<node>/` | Add as nodes join |

## Rules

1. **Node isolation:** Writers append to `inbox/<node>/` only — never cross-write to other node dirs or root dirs (literature, permanent, harnesses, domains, atlas).
2. **PR flow:** Node writes → open PR → `validate-schema.py` CI gate → CoS merge to main.
3. **Schema requirement:** All notes under `inbox/` and `inbox/<node>/` must include frontmatter: `id`, `title`, `type`, `status`, `created`, `updated`.
4. **SQLite funnel:** Nodes should run local SQLite filtering; only promote short, schema-valid notes to PRs.
5. **NO PERSONAL DATA:** Never copy personal, private, or sensitive data into this public vault. All content is public OSS. Personal agentic memory stays in Hermes (`~/.hermes/memories`). This inbox is research capture only.

## Templates

Use `/templates/inbox-note.md` for new inbox entries.

## Processing

Inbox notes are **fleeting** — process to literature/permanent or delete. CoS promotes actionable gaps → Linear HITL.
