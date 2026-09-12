---
id: perm-20260911-omp-can-load-sol-pi-via-legacy-shim
title: "OMP can load SoL-Pi as a git plugin; OCC likely no-ops without agent_settled"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [omp, pi]
domains: [frameworks, tokenomics]
confidence: medium
tags: [permanent, sol-pi, omp, shim]
---

# OMP can load SoL-Pi as a git plugin; OCC likely no-ops without agent_settled

## Idea (atomic)

Oh My Pi still installs `pi.extensions` packages (`omp install github:NVlabs/SoL-Pi` / `omp plugin link`) and rewrites `@earendil-works/*` onto `legacy-pi-coding-agent-shim` (exports `createEditToolDefinition` / `createWriteToolDefinition`, `CONFIG_DIR_NAME` = `.omp`, `getAgentDir()`). Action Fusion + ObservationPack + EPR therefore have a real load path. Online Context Compact's compact-and-continue sequence listens for Pi `agent_settled`; OMP's catalog has `agent_end` (notify-only) and `session_stop` instead, and NVIDIA's own compat note says a host that never emits `agent_settled` starts **no** boundary compaction.

The stock SoL-Pi **entrypoint** still statically imports OCC, which names `findCutPoint` from `@earendil-works/pi-coding-agent`. OMP 18.1.17's shim does not export that symbol, so the default factory fails to load even when `onlineContextCompact` is false. Phase 0 on OMP is therefore a thin wrapper that imports only Action Fusion + ObservationPack (local smoke: `sol-pi-omp`). Do not Discord-architect this into omp core.

## Why it matters for our harnesses

Phase 0 is install + `sol-pi.json` with only `actionFusion` and `observationPack` true (no extra model calls, no abort/continue). Config lands at `.omp/sol-pi.json` / `~/.omp/agent/sol-pi.json` because SoL-Pi uses `CONFIG_DIR_NAME`, not a hardcoded `.pi`. If OCC is wanted later, an OMP-side adapter should map settle → `session_stop` / `waitForIdle` + `ctx.compact()` rather than asking NVIDIA to support OMP.

Live smoke (this VM, 2026-09-11): `omp plugin install /tmp/SoL-Pi` listed `sol-pi` v0.1.0; `omp plugin doctor` reports the package ok. Stock entry still needs the wrapper to avoid `findCutPoint`. Shim coverage for `modelRegistry.complete()`, `isProjectTrusted()`, and TUI `ctx.ui.setStatus` still needs a session smoke. `github_writes=0` on `can1357/oh-my-pi`.

## Related

- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- OMP: `docs/extension-loading.md`, `packages/coding-agent/src/extensibility/legacy-pi-coding-agent-shim.ts`, test `legacy-pi-edit-write-tools.test.ts` (#7094)
- OMP issue #2166 (Pi packages load after `omp install`; `-e git:…` is not implemented)
- [[harnesses/omp]] · [[harnesses/pi]]
