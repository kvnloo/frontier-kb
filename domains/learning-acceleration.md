---
id: domain-learning-acceleration
title: learning-acceleration
type: moc
status: active
created: 2026-09-11
updated: 2026-09-12
tags: [moc, domain, learning, neuroscience, synergy]
---

# learning-acceleration

Map of content for [[atlas/home]]. This cluster is the **human half** of the vault: how to encode, retrieve, rest, measure, and prune so frontier LLM knowledge actually sticks.

The vault is a brain. Notes are neurons. Wikilinks are candidate synapses. Human and agent use **potentiates**; unused edges **decay**; noise is **pruned**, never silently deleted.

## Protocol stack (fact vs design)

Four public teaching/protocol surfaces, distilled into vault policy. None of this is medical advice. It is a learning-system design.

| Source | Public claim we use | Vault translation |
|--------|---------------------|-------------------|
| Justin Sung | Encoding quality > exposure time; higher-order processing builds schema | Encode studio before retrieval. Distill, don't highlight. |
| Andrew Huberman | Plasticity needs alert focus, then rest (NSDR/sleep) to consolidate | Ultradian 90-min cycle + rest gate after encode |
| Bryan Johnson | Measure, don't guess. Sleep and protocol beat motivation | Learning biomarkers on `/measure`. Nightly prune loop. |
| Rhonda Patrick | Aerobic + resistance work raises BDNF; brain is metabolic | Move phase before encode. No all-nighter cram loop. |

## Atomic claims

- [[permanent/perm-20260911-encoding-beats-exposure]]
- [[permanent/perm-20260911-plasticity-needs-alert-then-rest]]
- [[permanent/perm-20260911-measure-the-learning-loop]]
- [[permanent/perm-20260911-bdnf-is-a-learning-prerequisite]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
- [[permanent/perm-20260911-human-agent-synergy-is-the-loop]]
- [[permanent/perm-20260911-distill-then-retrieve-llm-frontier]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[literature/lit-20260912-mb-few-shot-learners]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
- [[permanent/perm-20260912-anatomy-is-init-not-a-faithful-brain]]
- [[literature/lit-20260912-flyforge-research-roadmap]]

## Literature

- [[literature/lit-20260911-justin-sung-higher-order-encoding]]
- [[literature/lit-20260911-huberman-plasticity-alert-rest]]
- [[literature/lit-20260911-bryan-johnson-measure-dont-guess]]
- [[literature/lit-20260911-rhonda-patrick-bdnf-exercise]]
- [[literature/lit-20260911-synaptic-pruning-as-kb-policy]]
- [[literature/lit-20260911-synaptic-homeostasis-sleep-shy]]
- [[literature/lit-20260911-llm-frontier-teaching-surface]]

## Loop

1. Frontier / humans **encode** new LLM notes (higher-order, schema-first).
2. Humans **retrieve**; agents **search/fire**. Co-activation strengthens synapses.
3. Nightly `scripts/synapse_loop.py` decays idle edges and proposes prunes.
4. CI + GraphQL expose the living graph to [humanity-vault](https://github.com/kvnloo/humanity-vault).

See `inbox/learning-acceleration-wave-2026-09-11.md`.
