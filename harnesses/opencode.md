---
id: harness-opencode
title: OpenCode
type: harness
status: draft
created: 2026-09-10
updated: 2026-09-10
urls:
  - https://github.com/anomalyco/opencode
  - https://opencode.ai/docs/agents
  - https://opencode.ai
capabilities:
  - Open source AI coding agent (TypeScript)
  - Built-in agents: build (default), plan (read-only), and @general subagent
  - Desktop beta app alongside terminal CLI
  - Plugin/extensibility system (.opencode/plugins, skills)
  - Multi-platform install (npm, brew, mise, nix, scoop, choco, pacman)
gaps_vs_peers:
  - No persistent crew orchestration (firstmate)
  - No messaging gateway (hermes)
  - No native DAP debugger / stream rules (omp)
  - Plan agent is lighter than omp subagents and firstmate crews
omp_actionable: true
tags: [harness]
---
# OpenCode

Snapshot: Open source AI coding agent; 206k+ stars. Two agents (build/plan) + @general subagent.
Strengths: Large OSS adoption; desktop beta; rich plugin + skills system; multi-install paths.
Gaps: No crew orchestration vs firstmate; no messaging gateway vs hermes; no native DAP debugger vs omp.
Sources: https://github.com/anomalyco/opencode, https://opencode.ai/docs/agents
