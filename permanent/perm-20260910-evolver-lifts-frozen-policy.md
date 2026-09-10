---
id: perm-20260910-evolver-lifts-frozen-policy
title: "An evolver edits the harness around a frozen worker; it does not wrap another product"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, claude]
domains: [ai-ml, frameworks]
confidence: high
tags: [permanent, evolver, qwen]
---

# An evolver edits the harness around a frozen worker; it does not wrap another product

## Idea (atomic)

The 2026 result that matches "small model guides other harnesses" is **harness evolution**: freeze the worker (even 27B), let a second model propose patches to prompts/runtime/config, and let deterministic gates credit them. Qwen3.6-27B can *be* the evolver (Evo-Bench +9.7). A stronger evolver lifting frozen qwen3.6-27B credits +9.3 pp on Terminal-Bench 2. Qwen3.8-27B is a worker, not a published sidecar for OMP.

## Why it matters for our harnesses

Do not SFT a 27B to sit in front of OMP/Hermes/Claude Code. If we want SWE-bench/TB gains without Cognition weights: (1) audit editor ABI, (2) bind 27B as worker, (3) run an offline evolver on our traces with sealed-test credit. That is cheaper than SWE-2-scale RL and actually OSS.

## Related

- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
