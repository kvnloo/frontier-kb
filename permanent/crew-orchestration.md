---
id: perm-20260910-crew-orchestration
title: Crew orchestration is the next leapfrog target
type: permanent
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [firstmate, crush, omp, opencode]
domains: [ai-ml]
confidence: medium
tags: [permanent, crew, orchestration, multi-client]
---
# Crew orchestration is the next leapfrog target

## Idea (atomic)
The next leapfrog for coding harnesses is not a bigger model but a visible crew: a first mate that dispatches, supervises, and reconciles isolated workers in real time.

## Why it matters for our harnesses
[[harnesses/firstmate|firstmate]] already proves the pattern (one liaison, visible crew, disposable worktrees, zero-token supervision). [[harnesses/crush|Crush]] exposes multi-client shared workspace presence via serve. [[harnesses/omp|OMP]] has subagents but no crew reconciliation layer. [[harnesses/opencode|OpenCode]] has @general but no crew model. The gap to close: [[harnesses/omp|OMP]] needs a [[literature/crush-multi-client|multi-client shared workspace]] reconciliation layer.

## Related
- [[literature/crush-multi-client|Literature: Crush serve multi-client]]
- [[literature/durable-workflows|Literature: durable workflows]]
