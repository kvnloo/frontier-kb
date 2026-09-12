---
id: domain-ai-ml
title: ai-ml
type: moc
status: active
created: 2026-09-09
updated: 2026-09-12
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

## Connectome SNN vs SVLM (2026-09-12)

Qwen3.8-27B remains the language/tool worker. A MaleCNS SNN is a sensorimotor specialist, not a second SVLM. Optimize mushroom-body + pinout + substrate; do not score the fly on SWE-bench.

FlyForge program: P0 is Hermes recovery under joules/success. FLM’s direct-input control slightly beats the fly residual on language NLL. fly-hf’s 50.6M readout dominates its 52.8M trained params. Evolution Lab (`apps/evolution-lab`) is the runner: genomes, ΔHV, MAP-Elites, honest dashboard.

- [[literature/lit-20260912-chatgpt-evolution-lab-share]]
- [[permanent/perm-20260912-experiments-are-the-population]]

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[literature/lit-20260912-flm-and-fly-hf-language-reservoirs]]
- [[literature/lit-20260912-flygm-graph-policy]]
- [[literature/lit-20260912-costi-connectome-reservoir]]
- [[literature/lit-20260912-connectome-to-function]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-joules-per-verified-success]]
- [[permanent/perm-20260912-anatomy-is-init-not-a-faithful-brain]]
- [[literature/lit-20260912-fly-connectome-task-meme]]
- [[literature/lit-20260912-qwen38-27b-vs-fly-snn]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
- [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
- [[literature/lit-20260912-connectome-genuine-apps]]
- [[literature/lit-20260912-mb-few-shot-learners]]
- [[literature/lit-20260912-neuromorphic-and-robot-motifs]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
- [[permanent/perm-20260912-connectome-is-a-lab-instrument]]

## Architecture search over IR

ReAct / planner-executor / debate / RLM / tree search as topologies of one \(O_t\) transition system. Architecture search = search over AODL/HOTL programs, not hardcoded `planner(); coder(); reviewer()`.

- [[permanent/perm-20260817-aodl-ir-first]]
- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[literature/lit-20260817-aodl-voice-transcript]]
