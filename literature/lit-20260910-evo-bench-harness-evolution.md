---
id: lit-20260910-evo-bench-harness-evolution
title: "Evo-Bench: a 27B can evolve a frozen policy's harness"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://arxiv.org/abs/2608.09096", "https://arxiv.org/html/2608.09096v1"]
harnesses: [omp, hermes, claude, opencode]
domains: [ai-ml, frameworks]
confidence: high
tags: [literature, evo-bench, harness-evolution, qwen]
---

# Evo-Bench: a 27B can evolve a frozen policy's harness

## Claim (one sentence)

A separate *evolver* model can lift a frozen policy by editing the executable harness, not by wrapping another product: Qwen3.6-27B as evolver gained +9.7 overall on Evo-Bench with DeepSeek-V4-Flash held fixed.

## Evidence

Huang, Yang, Zhou et al., arXiv:2608.09096 (2026). Policy model is frozen. Evolver diagnoses validation failures and revises CodeAct seed harness \(H_0\) (shell + finish only). Held-out eval after freeze.

Open-weight evolver **Qwen3.6-27B**: Search 34.8 (+23.1), Office 38.8 (+0.4), General 50.0 (+1.6), Overall **39.4 (+9.7)** vs CodeAct 29.7. AnytimeVal 46.9. It still froze a worse snapshot than its best (I10 49.7 → I18 45.4) after a verifier crash — 27B can evolve, it cannot yet manage best-revision recovery.

Frontier evolvers (GPT-5.6 Sol +16.6, Opus 4.8 +16.1) approach the human-engineered composite (47.5). Synthesized harnesses transfer across policy families (Qwen / DeepSeek / GLM).

This is not a plugin for OMP. The evolver *rewrites* the policy harness. Closest factory shape: an offline diagnose–edit–eval loop around our loop, not a sidecar in the hot path.

Related 2026 line: HarnessX (arXiv:2606.14249), Meta-Harness (arXiv:2603.28052), Self-Harness (arXiv:2606.09498), AHE (arXiv:2604.25850).

## Fact vs interpretation

- Fact: Evo-Bench isolates harness evolution from policy strength; Qwen3.6-27B is on the open-weight leaderboard as an evolver.
- Fact: Qwen3.8-27B is not in Table 2; do not swap 3.6 and 3.8.
- Interpretation: the "small model guides other harnesses" ask is closest to this evolver loop, not to SFT-27B sitting in front of Claude Code.

## Links

- Paper: https://arxiv.org/html/2608.09096v1
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
