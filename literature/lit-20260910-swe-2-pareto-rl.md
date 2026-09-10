---
id: lit-20260910-swe-2-pareto-rl
title: "SWE-2: Pareto-informed multi-effort RL on Kimi K3"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://cognition.com/blog/swe-2", "https://cognition.com/blog/swe-1-7", "https://arxiv.org/abs/2607.24653", "https://arxiv.org/abs/2603.18567", "https://github.com/sgl-project/SpecForge"]
harnesses: [devin, omp, hermes, claude, codex, grok, opencode]
domains: [ai-ml, frameworks, tool-use]
confidence: high
tags: [literature, swe-2, cognition, rl, pareto]
---

# SWE-2: Pareto-informed multi-effort RL on Kimi K3

## Claim (one sentence)

SWE-2 is a proprietary post-trained coding *model* (Kimi K3 2.8T + Cognition RL in the Devin harness), not an OSS plugin you can drop onto OMP/Hermes/Claude Code; the transferable pieces are the training recipe and a few OSS serving tools, not the weights.

## Evidence

Cognition, 2026-09-10 ([blog](https://cognition.com/blog/swe-2)):

- Post-trained from Kimi K3 (Moonshot, arXiv:2607.24653), already RL'd for agentic coding. Cognition RL still adds ~5–6 points and shifts the whole cost–performance frontier.
- Ships in Devin Desktop/CLI (rolling to Web and Fusion). Evaluated in Devin CLI for open-weight models; Anthropic/OpenAI/xAI use their native harnesses (Appendix A).
- Headline scores (best effort): FrontierCode 1.1 Main 50.0%; DeepSWE 1.1 73.0%; Terminal-Bench 2.1 92.8%; Terminal-Bench 4 27.3%.
- vs K3: 44.2 / 68.5 / 88.3 / 21.5. vs SWE-1.7: 42.0 / 37.7 / 81.5 / 7.6.
- Behavior: SWE-2 medium first-edit median 18 steps vs 48 for SWE-1.7; 58% fewer turns and 81% less cost than SWE-1.7 on FrontierCode 1.1 Main. Gains are focused exploration, not more tools. High/max still plan and verify more.

Recipe (not a harness):

1. **Cost-penalized reward** `R = S - λ_e C` in one RL run for all effort levels. `λ_e` is the local slope of the base model's Pareto frontier at effort `e`. Linear cost is forced if expected reward may depend only on average cost and solve rate (Appendix B).
2. **Length-weighted group baseline** `b̂ = Σ R_i L_i / Σ L_i` as a cheap proxy for the Greensmith/Bartlett/Baxter optimal baseline. Used since SWE-1.6; lowers train–inference KL vs mean group baseline.
3. **Rollout serving:** prefill delayer (+10–20% TPM/TPS); DSpark speculative decoding; online draft-model training via SpecForge after acceptance decayed; NVFP4/FP8 + QAT. Memory and KL better than SWE-1.7 despite ~3× parameters.
4. **Data:** 3× RL environments, instruction-following overlays, verifier flywheel using prior SWE-2 checkpoints (K3 is resourceful enough to reward-hack weaker graders).

Kimi K3's own post-training (contrast): 3 domains × 3 effort experts, then multi-teacher on-policy distillation, plus per-problem token budgets. SWE-2 trains all efforts end-to-end instead.

OSS cited as *infra*, not as plug-ins: SpecForge (arXiv:2603.18567), DSpark (arXiv:2607.05147). SpecForge speeds decoding; it does not raise SWE-bench solve rate by itself.

## Fact vs interpretation

- Fact: SWE-2 is K3 post-trained by Cognition, served in Devin, with the scores and recipe above.
- Fact: SpecForge/DSpark are OSS serving/training tools Cognition used for RL rollouts.
- Interpretation: there is no SWE-2-shaped "drop this into any harness" artifact. A factory that wants SWE-2 *gains* must either buy Devin, post-train its own policy in-harness, or compose smaller specialist/routing layers (see related).
- HOLD: Terminal-Bench 4 is still far from Fable 5.1 (55.8%) and GPT-6 Astra (57.9%). SWE-2's TB2.1 number is not a TB4 story.

## Links

- Primary: https://cognition.com/blog/swe-2
- Lineage: [[literature/lit-20260910-swe-1-7]] · [[literature/lit-20260910-swe-grep]]
- OSS survey: [[literature/lit-20260910-oss-coding-plugins]]
- Kimi K3: https://arxiv.org/abs/2607.24653
- SpecForge: https://github.com/sgl-project/SpecForge
