---
id: perm-20260910-small-models-are-workers-or-specialists
title: "Qwen3.8-27B is a worker; Nemotron Super is an in-harness planner"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, opencode, claude, pi]
domains: [ai-ml, frameworks]
confidence: medium
tags: [permanent, qwen, nemotron, orchestrator]
---

# Qwen3.8-27B is a worker; Nemotron Super is an in-harness planner

## Idea (atomic)

Qwen3.8-27B is a strong *loop model* (TB2.1 Terminus 73.0, SWE-bench Pro 61.7, DeepSWE 1.1 42.2 on Claude Code) with thinking/effort knobs. It is not a published SFT "guide" that sits in front of other harnesses. The model NVIDIA actually markets as orchestrator is Nemotron 3 Super, bound *as OpenHands/OpenCode's brain*, with Nano as worker. No 2026-09-10 public checkpoint is "SFT 27B meta-controller for OMP/Hermes/Claude Code."

## Why it matters for our harnesses

Cheap local path: bind Qwen3.8-27B as OMP/Hermes/Pi worker (tool-call parser `qwen3_coder`, thinking on, do not kill thinking to save time). Planner path: if we want a second model, copy OpenDev slots or Nemotron Super-as-planner — still inside *one* harness. Do not expect SWE-2-like TB2.1 92.8 from a 27B sidecar.

## Related

- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-specialist-subagent-handoff]]
- [[permanent/perm-20260910-scaffold-tool-shape-dominates]]
