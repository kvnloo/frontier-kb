---
id: lit-20260911-sol-pi-harness-efficiency
title: "SoL-Pi: four opt-in Pi extension mechanisms from NVIDIA auto-research"
type: literature
status: active
created: 2026-09-11
updated: 2026-09-11
sources: ["https://github.com/NVlabs/SoL-Pi", "https://nvlabs.github.io/SoL-Pi/", "https://github.com/earendil-works/pi"]
harnesses: [pi, omp, hermes]
domains: [frameworks, tool-use, tokenomics, ai-ml]
confidence: high
tags: [literature, sol-pi, nvidia, context, compaction]
---

# SoL-Pi: four opt-in Pi extension mechanisms from NVIDIA auto-research

## Claim (one sentence)

NVIDIA's SoL-Pi is a standalone MIT Pi extension (`pi.extensions`, tested on `@earendil-works/pi-coding-agent` 0.84.2, commit `22277b7e`) that packages four opt-in efficiency mechanisms — Action Fusion, ObservationPack, Evidence-Preserving Reducer, Online Context Compact — discovered by screening 152 auto-research ideas; it is not a fork of Pi and not a plugin for Hermes.

## Evidence

Pinned checkout: [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) `22277b7e0c3c46ba1259a6687f31fe39ade421a5` (2026-09-11, merge of Action Fusion `file://` path fix). Blog: [nvlabs.github.io/SoL-Pi](https://nvlabs.github.io/SoL-Pi/). Install: `pi install git:github.com/NVlabs/SoL-Pi`. Config: one effective `sol-pi.json` (project `.pi/sol-pi.json` if trusted, else `~/.pi/agent/sol-pi.json`); missing file leaves every mechanism **off**.

### Mechanisms (source, not marketing)

| Mechanism | Harness seam | Behavior |
| --- | --- | --- |
| **Action Fusion** | Replaces built-in `edit`/`write` via `createEditToolDefinition` / `createWriteToolDefinition` | Optional `then_run.{command,timeout}` runs after a successful mutation in the same tool call. Per-file queue; hashes the file immediately before the command and skips if content changed. Does not nest Pi's mutation queue. |
| **ObservationPack** | `pi.on("context")` projection + `obs_recall` | Pure-text tool results >10 KiB are archived under `<sessionDir>/sol-pi/<sessionId>/observation-pack/`. First **2** provider requests still send the full body; later requests get a stable `obs_*` placeholder with head/tail excerpt. Session JSONL is not rewritten. Fail-open. |
| **Evidence-Preserving Reducer** | `tool_result` middleware + nested model | Eligible diagnostic bash (pytest/cargo/make/npm test/go test/…). Archive first. Cheap reducer model (default provider `openai-codex`, model `gpt-5.6-luna`) returns a receipt; **every quoted line must match the archive byte-for-byte**. Secret-ish regex, size, schema, or model failure → original result unchanged. |
| **Online Context Compact** | `update_plan` + `context` / `before_provider_request` + `ExtensionContext.compact()` | Plan-step completion is a compaction candidate. Economic check uses `cacheWriteReadRatio` (default 12.5, GPT-5.6 Sol Standard write/read as of 2026-08-21) and `getContextUsage()`. On select: abort run, compact from `agent_settled`, hidden `sendMessage({triggerTurn:true})` to rebuild the plan. **A Pi build that never emits `agent_settled` starts no boundary compaction.** |

Shared rules in README/SECURITY: no Pi patches; explicit opt-in; preserve evidence; Pi owns auth/provider/shell. EPR may send logs to the reducer model — do not enable for logs that must stay local.

### Author-reported results (blog; not re-run here)

- vs Pi: ~45–49% fewer tokens, ~1/3 lower cost, ~94% of Pi average score (EdgeBench, capability floor).
- vs native Codex/Claude Code harnesses: 35–64% fewer tokens, 50–54% lower list-price API cost.
- Terminal-Bench 4 (63 CPU-only tasks): Codex 18/63 $272.35; Pi 18/63 $286.45; SoL-Pi 15/63 $211.12. SoL-Pi solved fewer tasks; per-solved cost $14.07 vs Codex $15.13.
- Swarm (one nonrandomized 2h trial): Sol + 20 SoL-Pi workers 1,127 cycles / $60.11 vs 20 stock Pi 1,366 / $82.12 vs single Sol 1,333 / $39.20. Authors say this does not isolate which mechanism caused the gain.

Auto-research: 152 ideas → 4 survivors; ~1/40 conversion; EdgeBench held out from search; capability floor forbids saving by stopping early or hiding evidence.

## Fact vs interpretation

- Fact: SoL-Pi is a TypeScript Pi extension using public `ExtensionAPI` (`session_start` register, `registerTool`, `context`, `tool_result`, `compact`, session dir).
- Fact: defaults are all-off; `agents-install.md` is the all-enabled agent protocol.
- Fact: package name `sol-pi`, `"pi": { "extensions": ["./src/sol-pi/index.ts"] }`, `"private": true`, peerDeps on `@earendil-works/pi-*`.
- Interpretation: OMP still honors `pi.extensions` and rewrites `@earendil-works/*` onto host shims, but the stock SoL-Pi factory statically imports OCC/`findCutPoint`, which OMP 18.1.17's shim lacks — so the default entry fails even with OCC off. Hermes cannot load the TS package; a Python plugin port is required. See permanents.
- HOLD: EdgeBench/TB4/swarm numbers are author-reported; TB4 shows a solve-rate drop (18→15/63) that the 94% EdgeBench floor does not hide.

## Links

- Repo: https://github.com/NVlabs/SoL-Pi
- Blog: https://nvlabs.github.io/SoL-Pi/
- Compat: `docs/compatibility.md` in that repo
- [[permanent/perm-20260911-sol-pi-is-pi-public-extension-not-core-patch]]
- [[permanent/perm-20260911-omp-can-load-sol-pi-via-legacy-shim]]
- [[permanent/perm-20260911-hermes-sol-pi-is-a-python-plugin-port]]
- [[permanent/perm-20260911-observationpack-is-projection-not-history-rewrite]]
- [[permanent/perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[harnesses/pi]] · [[harnesses/omp]] · [[harnesses/hermes]]
