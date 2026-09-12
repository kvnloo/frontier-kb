---
id: perm-20260912-p0-is-verified-hermes-recovery
title: "P0 is a verified Hermes recovery controller, not MaleCNS SGD"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [hermes, omp, cursor, pi]
domains: [ai-ml, frameworks, tool-use]
confidence: high
tags: [permanent, fly, p0, hermes, recovery]
---

# P0 is a verified Hermes recovery controller, not MaleCNS SGD

## Idea (atomic)

First experiment: **typed operational events → bounded recovery action → external verifier**, with Qwen as teacher/fallback and a small GRU as the student to beat. Anatomy search, 10K–27B midpoints, and native fly language models are later or parallel. A specialist that does not beat the GRU is not a research win even if it beats Qwen on that bounded task.

## Why it matters for our harnesses

Hermes already has Kanban, runs, leases, and a secret/vault split. The controller must consume **sanitized** fields and escalate; it must not see `bws` payloads or vault fill. Keel L0 already forbids the default router from executing project work — the fly/GRU student is the same shape: verifiable output type, not a prose orchestrator ([[permanent/perm-20260910-specialist-subagent-handoff]]). PER-944 stays a WebGPU viewer. Claimable P0 is [evolution-lab#2](https://github.com/kvnloo/evolution-lab/issues/2); Linear [PER-1524](https://linear.app/0ism/issue/PER-1524) stays Backlog.

## Related

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[permanent/perm-20260912-fly-specialist-is-an-aodl-port]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
- [[harnesses/hermes]]
- [[literature/lit-20260910-keel-level0-evidence-surface]]
