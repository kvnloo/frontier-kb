---
id: harness-pi
title: pi
type: harness
status: active
created: 2026-09-09
updated: 2026-09-11
urls:
  - https://github.com/earendil-works/pi
  - https://pi.dev/
  - https://github.com/NVlabs/SoL-Pi
  - https://nvlabs.github.io/SoL-Pi/
capabilities:
  - Minimal tool loop (read/write/edit/bash)
  - Public ExtensionAPI + pi install git:/npm:
  - RPC + session tree + native compaction
  - SoL-Pi opt-in efficiency extension (0.84.2)
gaps_vs_peers:
  - No LSP/DAP (omp)
  - No messaging gateway (hermes)
  - SoL-Pi OCC depends on agent_settled (0.84.2)
omp_actionable: true
confidence: high
tags: [harness, sol-pi]
---

# pi

Mario Zechner / Earendil `pi` (`@earendil-works/pi-coding-agent`). SoL-Pi's only first-party host.

## Snapshot

Four tools, extension modules, no opinions. SoL-Pi (`pi install git:github.com/NVlabs/SoL-Pi`) is the NVIDIA efficiency layer: Action Fusion, ObservationPack, Evidence-Preserving Reducer, Online Context Compact. Tested pin **0.84.2**. Mechanisms default off.

## Strengths

Public extension events (`context`, `tool_result`, `before_provider_request`, `agent_settled`, `session_before_tree`) are stable enough that NVIDIA refused to vendor Pi. Config discovery uses `CONFIG_DIR_NAME` + `getAgentDir()` + `isProjectTrusted()`.

## Gaps (leapfrog targets)

Pi is the research substrate, not the daily IDE. OMP already forked it and added hashline edits, LSP, subagents. SoL-Pi savings vs native Codex/Claude are author-reported on EdgeBench; TB4 63-task slice shows SoL-Pi solving **fewer** tasks (15 vs 18).

## Sources

- https://pi.dev/
- https://github.com/earendil-works/pi
- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260911-sol-pi-is-pi-public-extension-not-core-patch]]
- [[harnesses/omp]]
