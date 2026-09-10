---
id: perm-20260910-harness-compute-split
title: Harness↔compute split is the durable architecture
type: permanent
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, opencode, claude-code]
domains: [ai-ml]
confidence: medium
tags: [permanent, sandbox, compute, architecture]
---
# Harness↔compute split is the durable architecture

## Idea (atomic)
The harness (orchestration, UI, policy) and the compute plane (sandbox, terminal backend, tool runtime) must be separable; every leapfrog harness will build on this split.

## Why it matters for our harnesses
[[harnesses/omp|OMP]] runs persistent Python/Bun workers with a loopback bridge to the agent. [[harnesses/hermes|Hermes]] runs anywhere via local/Docker/SSH/Modal/Daytona/Vercel backends. [[harnesses/opencode|OpenCode]] ships a desktop app alongside the terminal CLI. [[harnesses/claude-code|Claude Code]] exposes the Computer Use tool as a separate automation plane. The shared lesson: keep compute pluggable and harness-centric.

## Related
- [[literature/sandbox-harness-split|Literature: sandbox / harness↔compute split]]
- [[harnesses/omp|OMP]]
