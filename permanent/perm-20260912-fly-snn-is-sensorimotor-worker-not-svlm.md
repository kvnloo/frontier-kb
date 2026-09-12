---
id: perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm
title: "The fly SNN is a sensorimotor worker; Qwen3.8-27B remains the SVLM worker"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [omp, hermes, cursor, pi]
domains: [ai-ml, neuroscience, frameworks]
confidence: high
tags: [permanent, qwen, fly, worker, svlm]
---

# The fly SNN is a sensorimotor worker; Qwen3.8-27B remains the SVLM worker

## Idea (atomic)

Qwen3.8-27B stays the **language/tool/computer-use worker** (TB2.1 73, SWE-Pro 61.7). A MaleCNS SNN, if we bind one, is a **different specialist**: visuo-motor closed loop, not an SVLM. It will not post 61.7 on SWE-bench. It should not be asked to. Scoring them on one ladder is how 10-point ghosts and 10⁸-watt myths get into the vault.

## Why it matters for our harnesses

Keep the existing bind: Qwen3.8-27B as OMP/Hermes/Pi worker, thinking on, `qwen3_coder` parser. If PER-944 ever leaves backlog, it is a **browser embodiment demo**, not a planner swap. Planner remains in-harness (Nemotron Super path) or evolver-around-frozen-worker.

## Related

- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
- [[permanent/perm-20260910-specialist-subagent-handoff]]
- [[literature/lit-20260912-qwen38-27b-vs-fly-snn]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
