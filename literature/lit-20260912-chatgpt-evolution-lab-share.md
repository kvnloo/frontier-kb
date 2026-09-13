---
id: lit-20260912-chatgpt-evolution-lab-share
title: "ChatGPT share: Evolution Lab — experiments are the population"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://chatgpt.com/share/6aa4ef4a-f390-83e9-8afc-34905baf22eb?ogimg=plain", "https://tinker-docs.thinkingmachines.ai/", "https://sakana.ai/ai-scientist-nature/"]
harnesses: [cursor]
domains: [ai-ml, frameworks, statistics]
confidence: high
tags: [literature, fly, evolution, pareto, tinker]
---

# ChatGPT share: Evolution Lab — experiments are the population

## Claim (one sentence)

The latest turn in the fly-vision thread is **not** another dashboard brief: it asks for an **experiment engine** that treats hypotheses as a population, scores them on Pareto hypervolume and MAP-Elites niches, and uses Cursor agents plus Tinker as backends — while remaining more falsifiable than “make a fly beat Qwen.”

## Evidence

Share: [chatgpt.com/share/6aa4ef4a-f390-83e9-8afc-34905baf22eb](https://chatgpt.com/share/6aa4ef4a-f390-83e9-8afc-34905baf22eb?ogimg=plain) (same titled thread as FlyForge; newer share id).

Operator (latest user turn):

> I like this central theory but it does not take advantage of cloud-agent scale. Design an experiment **engine** with a gamified loop on the Pareto frontier. Evolutionary algorithm over experiments on the fly brain and Qwen. Research sandbox to tinker in. Hook Thinking Machines **Tinker** to SFT our own model.

Assistant: change the abstraction. Fundamental object = **experiment genome** (YAML/JSON: lineage, hypothesis, architecture, curriculum, training, evaluation, objectives). Nested evolution (weights / architecture / curriculum / experiment / research strategy). Selection = Δ hypervolume, not a single score. MAP-Elites keeps a champion **per niche**. Promotion ladder L0–L5 (ASHA-like). Roles: explorers, exploiters, skeptics, replicators, neuroscience, distillers. Tinker is a training **backend**, not “the Qwen script.” Fitness preserves dimensions: ΔHV + novelty + information gain + replication − cost. Goal line to put at the top of the repo:

> Continuously discover, verify, and explain computational systems that expand the achievable frontier between capability and resources.

Precedents named: AlphaEvolve, Sakana AI Scientist-v2, OpenEvolve, PBT, MAP-Elites.

## Fact vs interpretation

- Fact: this is a program for an engine. No 100-agent Tinker run was executed in the share. Qwen3.8-27B is listed as a Tinker-exposed model in their docs, not as a result we measured.
- Interpretation: P0 of [[literature/lit-20260912-flyforge-research-roadmap]] is the first **species** in this engine (Hermes recovery control table), not a competing product. Direct-input remains a mandatory skeptic. Tinker/cloud fan-out stay declared backends until wired; refusing to fake SFT is part of the contract. The engine is [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) under [Verified OSS Loop](https://github.com/kvnloo/verified-oss-loop). Claimable P0 is [evolution-lab#2](https://github.com/kvnloo/evolution-lab/issues/2). Linear [PER-1524](https://linear.app/0ism/issue/PER-1524) stays Backlog.
- HOLD: joules of hosted Qwen remain unknown. MAP-Elites behavior descriptors (family × scale × learning mode) are a first cut, not the only niche axes.

## Links

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[literature/lit-20260912-consume-gym-do-not-fork-engine]]
- [[permanent/perm-20260912-experiments-are-the-population]]
- [[permanent/perm-20260912-gym-is-the-task-engine-is-ours]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-joules-per-verified-success]]
- [[inbox/cursor/inbox-cursor-evolution-lab-20260912]]
