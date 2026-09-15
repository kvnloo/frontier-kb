---
id: notes-opencode-hermes-playbook-mirror
title: OpenCode ← Hermes contribution playbook mirror
type: permanent
status: draft
created: 2026-09-15
updated: 2026-09-15
harnesses: [opencode, hermes]
domains: [ai-ml, frameworks]
confidence: high
tags: [opencode, hermes, playbook, contribution, wave]
---

# OpenCode ← Hermes playbook mirror

How to run the same *quality motion* we use on Hermes Agent against OpenCode — adapted to OpenCode's CONTRIBUTING gates and the factory **openclaw-only** origin-write lock.

## Hermes quality motion (what we mirror)

From [[harnesses/hermes]] + statedb/voice/HTTP lane waves:

1. **Wave/meta consolidation** across a feature cluster (not one-off drive-bys).
2. **Verify-first** on current `dev` / release before claiming.
3. **Tiny mergeable slices** (docs → fence → behavior) with kill criteria.
4. **Complement, don't compete** with in-flight maintainer/assignee work.
5. **Comment maps** that cite SHAs and change decisions (when writes allowed).
6. **Reliability waves** before architecture RFCs (statedb / gateway refresh analogue).
7. **Muse lock** — skip exact redo of open claims / stuck PRs.
8. **Proof lanes** (kerdoios-style): evidence attached, human merge.

OpenCode analogue waves live in [[inbox/opencode-wave-2026-09-15]].

## Process gates unique to OpenCode

| Gate | OpenCode rule | Hermes-mirror adaptation |
| --- | --- | --- |
| Issue-first | Every PR links `Fixes #N` | Never open PR cold; if need exists and no issue, open **template** issue first (when write lock allows) |
| Templates | Bug / feature / question only; blank → 2h close | Use official templates; no freeform AI essays |
| No AI walls | Long generated text ignored/closed | Short human prose: problem → repro → fix → verify |
| Design review | UI/core features need core-team design before impl | Features → discussion issue; wait. Bugs/docs/LSP/provider quirks → proceed |
| Providers | New providers → [models.dev](https://github.com/anomalyco/models.dev) first | Split: catalog PR then optional opencode wiring |
| Claim | Comment to request assignment | One issue; wait; don't multi-claim (Muse) |
| PR shape | Conventional title, small, verification notes, UI screenshots | Same as Hermes tiny PR + evidence |
| Labels | Seek help-wanted / GFI / bug / perf | **As of 2026-09-15 help-wanted & GFI are empty** — use unassigned `bug` + quiet zero-comment leaves |
| Stack | Bun 1.3+, `bun dev`, packages/opencode|app|desktop|plugin | Local verify with `bun` before PR |

## Factory lock (openclaw-only)

Until CoS lifts the lock for anomalyco:

- ✅ Research via `gh`/docs; write frontier-kb harness/inbox/notes/data.
- ✅ Rank Waves + unclaimed lists; pulse deltas.
- ❌ No origin issues/PRs/comments on `anomalyco/opencode`.
- ❌ No Linear HITL mint from this playbook alone.
- ❌ No contacting peer agents about claiming.

When lock lifts: openclaw (or designated writer) executes Wave G docs leaf or Wave A #42790 after live verify.

## Operating loop (post-lock)

```
1. Pull triage: labeled open bugs + zero-comment no-open-PR filter
2. Muse filter: drop anything with assignee, open PR, or fresh "I'll take this"
3. Pick Wave theme (prefer A provider / D tools / G docs / C reliability docs)
4. Verify on latest release or bun dev against repro
5. Comment-claim ONE issue (short)
6. Implement smallest fix + test; conventional PR title; Fixes #N; verification block
7. If UI/core feature itch → stop; open design/discussion issue only
8. After merge: comment map on cluster issue citing SHA + decision; archive leaf in KB wave
```

## Wave themes ↔ Hermes precedents

| OpenCode Wave | Hermes precedent | Shared discipline |
| --- | --- | --- |
| C server/idle/MCP | state.db / gateway refresh | Reliability first; docs lock inventory |
| A providers/LLM | Provider/portal edges | Tiny adapter fixes; no rewrite |
| B permissions/task | Secrets/permission leaves | Complement; don't fight assigned PRs |
| E MCP lifecycle | Gateway reconnect | Fence + test |
| G docs/DX | Docs sidecar inventory leaves | Lowest friction proof |
| F ACP | Protocol watches | Observe unless assigned gap |
| H UI polish | Bot Screen / voice UX | Design gate = Discord/design-review first |

## Leapfrog (product), not PR spam

From competitor depth 2026-09-15: OpenCode already leads many TUIs on **Scout + `permission.task`**. Factory leapfrogs **into Hermes/OMP**, not by flooding OpenCode with competing agent frameworks:

- Mirror Scout managed-cache + task allowlists in Hermes agent taxonomy.
- Keep OpenCode contributions in CONTRIBUTING-welcome classes (bugs, LSP/formatter, providers, docs, perf).
- Do **not** propose Cursor Projects / Claude plugin-eval / Hermes gateway as drive-by OpenCode core features without design review.

## Confidence & coverage

Triage 2026-09-15: full pass on CONTRIBUTING + agents docs + ~40 recent merges + **41/41** labeled open bugs + ~40 zero-comment opens + claim-comment sampling on ~15 hot bugs. **~3–5%** of all ~4307 open issues by count; **high confidence** on the curated bug/help lanes. Re-run search when rate limits clear; help-wanted may refill.

## Related

- [[harnesses/opencode]]
- [[inbox/opencode-wave-2026-09-15]]
- [[harnesses/hermes]]
- [[notes/harness-evolver-hermes-plan]]
- [[harnesses/omp]]
