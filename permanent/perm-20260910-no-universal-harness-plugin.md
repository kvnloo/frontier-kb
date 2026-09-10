---
id: perm-20260910-no-universal-harness-plugin
title: "There is no universal OSS harness plugin"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, opencode, claude, codex]
domains: [frameworks, ai-ml]
confidence: high
tags: [permanent, scaffolds, harness]
---

# There is no universal OSS harness plugin

## Idea (atomic)

mini-SWE-agent, OpenHands SDK, OpenDev, Live-SWE-agent, and Qwen Code improve SWE-bench/TB numbers by *being* the agent loop. They are model-agnostic products, not plugins that wrap an existing product. Live-SWE-agent is the closest to "drop-in intelligence" and it is a YAML overlay on mini-swe-agent, not on OMP.

## Why it matters for our harnesses

Leapfrog is not "import OpenHands into OMP." It is: (1) steal typed slots (plan / execute / compact / critique) if we do not have them, (2) optionally *replace* a weak inner loop for eval (mini-swe-agent for DeepSWE/SWE-bench apples-to-apples), (3) never claim a scaffold lift as a model lift.

## Related

- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-scaffold-tool-shape-dominates]]
- [[harnesses/omp]]
- [[harnesses/opencode]]
