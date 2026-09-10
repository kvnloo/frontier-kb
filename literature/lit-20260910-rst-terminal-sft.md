---
id: lit-20260910-rst-terminal-sft
title: "RST: SFT/PPO on Qwen3.5-27B lifts Terminal-Bench 2"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://arxiv.org/abs/2608.05466"]
harnesses: [omp, hermes, claude]
domains: [ai-ml]
confidence: medium
tags: [literature, rst, terminal-bench, qwen, sft]
---

# RST: SFT/PPO on Qwen3.5-27B lifts Terminal-Bench 2

## Claim (one sentence)

Recursive Synthetic Terminal Tasks (RST) SFT plus agentic PPO on Qwen3.5-27B lifts Terminal-Bench 2 / Hard / Long-Horizon by up to ~10 points (PPO 49.44 / 32.00 / 22.07; +20.0% / +41.2% / +21.9% relative to base) — that is weight training, not a harness plugin.

## Evidence

Li, Shi, Li et al., arXiv:2608.05466v3 (2026-08-12). 15 recursive rounds, 37,484 verified terminal tasks at ~$0.05 each. Rejection-sampled Qwen3.5 trajectories → SFT on 27B and 122B-A10B, then PPO on 27B.

This answers "is there a smaller SFT 27B for TB2.1?" for the *worker weights*, not for a guide sitting in front of another harness. Qwen3.8-27B is a later dense model; this paper is 3.5.

## Fact vs interpretation

- Fact: published 27B SFT/PPO gains on Terminal-Bench 2 exist for Qwen3.5.
- Interpretation: to copy this you need the task flywheel + RL in *your* harness, which is the SWE-2 recipe at 27B scale — still not plug-n-play onto OMP.

## Links

- https://arxiv.org/abs/2608.05466
- [[literature/lit-20260910-swe-2-pareto-rl]]
- [[permanent/perm-20260910-swe-2-is-a-posttrained-model]]
