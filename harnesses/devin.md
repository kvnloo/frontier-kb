---
id: harness-devin
title: devin
type: harness
status: active
created: 2026-09-10
updated: 2026-09-10
urls: ["https://devin.ai/", "https://cognition.com/blog/swe-2", "https://cognition.com/blog/swe-1-7", "https://cognition.com/blog/swe-grep", "https://docs.devin.ai/desktop/context-awareness/fast-context"]
capabilities: ["swe-2-policy", "swe-1-7", "fast-context-swe-grep", "self-compaction", "devin-cli-eval"]
gaps_vs_peers: ["closed-weights", "not-a-plugin-for-other-harnesses"]
omp_actionable: false
confidence: high
tags: [harness]
---

# devin

Cognition's coding agent (Web / Desktop / CLI). SWE-1.7 and SWE-2 are trained *in this harness*. Open-weight models on Cognition benches are also scored via Devin CLI.

## Snapshot

SWE-2 (2026-09-10): Kimi K3 + Pareto-informed multi-effort RL. FrontierCode 1.1 Main 50.0%, DeepSWE 1.1 73.0%, Terminal-Bench 2.1 92.8%, Terminal-Bench 4 27.3%. Fast Context / SWE-grep is the retrieval subagent (file+line ranges, ≤4 turns × 8 parallel greps).

## Strengths

In-harness RL + verifier flywheel. Effort knobs (medium/high/max) trained in one run. Fast Context is the actual "plugin-shaped" piece — still closed.

## Gaps (leapfrog targets)

Closed policy. Cannot be bolted onto OMP/Hermes. TB4 still weak vs Fable/Astra. Fast Context weights are not OSS.

## Sources

- [[literature/lit-20260910-swe-2-pareto-rl]]
- [[literature/lit-20260910-swe-1-7]]
- [[literature/lit-20260910-swe-grep]]
- [[permanent/perm-20260910-swe-2-is-a-posttrained-model]]
