---
id: perm-20260910-swe-2-is-a-posttrained-model
title: "SWE-2 is a post-trained model, not a harness plugin"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [devin, omp, hermes]
domains: [ai-ml]
confidence: high
tags: [permanent, swe-2, cognition]
---

# SWE-2 is a post-trained model, not a harness plugin

## Idea (atomic)

SWE-2 is Kimi K3 (2.8T) after Cognition's in-Devin RL. The 5–6 point lift over K3 and the 18-vs-48 first-edit compression vs SWE-1.7 live in the *policy*, which was trained against Devin's tools, verifiers, and cost model. There is no SWE-2 runtime you can attach to OMP, Hermes, or Claude Code.

## Why it matters for our harnesses

Do not hunt for a Cognition-shaped sidecar. If we want those behaviors (focused exploration, end-to-end tests, Pareto-aware effort), we either buy Devin, post-train a policy in *our* loop, or steal the *recipe* (cost-penalized multi-effort RL, length-weighted baseline, verifier flywheel) — not the weights.

## Related

- [[literature/lit-20260910-swe-2-pareto-rl]]
- [[literature/lit-20260910-swe-1-7]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[harnesses/devin]]
