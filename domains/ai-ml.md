---
id: domain-ai-ml
title: ai-ml
type: moc
status: active
created: 2026-09-09
updated: 2026-09-10
tags: [moc, domain]
---

# ai-ml

Map of content for [[atlas/home]].

## Coding-agent post-training

SWE-2 is in-harness RL on Kimi K3, not a plugin. Qwen3.8-27B is a worker. Nemotron 3 Super is an in-product planner.

- [[literature/lit-20260910-swe-2-pareto-rl]]
- [[literature/lit-20260910-swe-1-7]]
- [[literature/lit-20260910-oss-coding-plugins]]
- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[literature/lit-20260910-rst-terminal-sft]]
- [[permanent/perm-20260910-swe-2-is-a-posttrained-model]]
- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]

## Architecture search over IR

ReAct / planner-executor / debate / RLM / tree search as topologies of one \(O_t\) transition system. Architecture search = search over AODL/HOTL programs, not hardcoded `planner(); coder(); reviewer()`.

- [[permanent/perm-20260817-aodl-ir-first]]
- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[literature/lit-20260817-aodl-voice-transcript]]
