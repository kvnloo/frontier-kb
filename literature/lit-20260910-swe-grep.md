---
id: lit-20260910-swe-grep
title: "SWE-grep / SWE-grep-mini: RL retrieval subagent, not a coding orchestrator"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://cognition.com/blog/swe-grep", "https://docs.devin.ai/desktop/context-awareness/fast-context", "https://arxiv.org/abs/2606.14066"]
harnesses: [devin, cursor, claude, omp, hermes]
domains: [ai-ml, tool-use, skills]
confidence: high
tags: [literature, swe-grep, subagent, retrieval]
---

# SWE-grep / SWE-grep-mini: RL retrieval subagent, not a coding orchestrator

## Claim (one sentence)

The closest Cognition artifact to a "plug-in that improves any harness" is SWE-grep: a small, RL'd *retrieval* specialist that returns file+line ranges, not a Qwen-sized planner that orchestrates other coding agents.

## Evidence

Cognition, 2025-10-16 ([blog](https://cognition.com/blog/swe-grep)):

- Motivation: Devin/Windsurf trajectories spent >60% of the first turn on context retrieval. Agentic search is slow and pollutes the main agent's context; embeddings miss multi-hop traces.
- Design: up to **8 parallel** tool calls (grep/glob/read) × **4 serial turns** (3 explore + 1 answer). Restricted tool set for Windows + safety.
- Training: multi-turn RL with per-sequence importance sampling; distill SWE-grep → SWE-grep-mini, then more RL. Reward = weighted F1 (F-β, β=0.5, precision-heavy) on files *and* line ranges vs Cognition CodeSearch Eval. No format reward. Zero reward on malformed tool calls. Advantages scaled by mean tool-calls/turn so small models don't game max parallelism with duplicates.
- Serving: Cerebras; SWE-grep-mini >2800 tok/s, SWE-grep >650 tok/s (claimed 20× / 4.5× vs Haiku 4.5 @ 140 tok/s).
- Product: Windsurf Fast Context subagent (Cmd+Enter or auto). Planned for DeepWiki, Devin, Windsurf Tab. Downstream: Sonnet 4.5 + Fast Context same SWE-Bench Verified subset solve rate, lower wall time.

Follow-ons:

- Devin Desktop docs: Fast Context is the same SWE-grep family inside Devin.
- FastContext paper (arXiv:2606.14066, 2026): trains a lightweight repository explorer delegated by a main agent; cites SWE-grep as the industrial prior. Designed to sit in front of scaffolds including mini-SWE-agent.
- Unofficial MCP wrappers exist (e.g. reverse-engineered Windsurf protocol). Not Cognition-supported; treat as HOLD for factory use.

## Fact vs interpretation

- Fact: SWE-grep is a retrieval subagent with a verifiable, non-summary output contract (file/line lists). That is why RL works.
- Fact: it is *not* open weights. Fast Context is a Cognition/Windsurf product.
- Interpretation: the *pattern* is portable (small RL specialist + typed hand-off + main coding model). The weights are not. A Qwen3.8-27B used as the *main* loop is a different bet than a mini retrieval model in front of a frontier worker.
- HOLD: no public evidence that SWE-grep-mini lifts Terminal-Bench 2.1 when bolted onto OMP/Hermes.

## Links

- Primary: https://cognition.com/blog/swe-grep
- Devin: https://docs.devin.ai/desktop/context-awareness/fast-context
- FastContext paper: https://arxiv.org/abs/2606.14066
- Related: [[literature/lit-20260910-swe-2-pareto-rl]] · [[literature/lit-20260910-oss-coding-plugins]]
