---
id: perm-20260912-experiments-are-the-population
title: "Experiments are the population; the frontier is the fitness"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor, hermes]
domains: [ai-ml, statistics, frameworks]
confidence: high
tags: [permanent, fly, evolution, pareto]
---

# Experiments are the population; the frontier is the fitness

## Idea (atomic)

Do not optimize “a fly” or “a Qwen.” Evolve **experiment genomes**. An idea reproduces when it creates new Pareto territory (Δ hypervolume) or occupies a MAP-Elites niche that was empty. A failed run that kills a hypothesis is a win if we record it. The free teacher/rule baseline is allowed on the all-systems front; **learned** students are scored on a separate learned-only front so a zero-parameter oracle cannot hide the control table.

## Why it matters for our harnesses

This is the factory loop that can actually use many Cursor agents without turning into 100 copies of the same prompt. [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) is the local P0 implementation: Hermes recovery, ridge readouts, JSONL archive, honest dashboard. `tinker_sft` and `fly_sim` must **fail closed** until they are real. Same rule as AODL fail-closed codecs.

## Related

- [[literature/lit-20260912-chatgpt-evolution-lab-share]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-joules-per-verified-success]]
