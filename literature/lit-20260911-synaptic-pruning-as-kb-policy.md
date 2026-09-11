---
id: lit-20260911-synaptic-pruning-as-kb-policy
title: "Synaptic pruning as knowledge-base policy"
type: literature
status: active
created: 2026-09-11
updated: 2026-09-11
sources:
  - https://en.wikipedia.org/wiki/Synaptic_pruning
  - https://www.ncbi.nlm.nih.gov/books/NBK234146/
harnesses: [cursor, omp, hermes]
domains: [learning-acceleration, neuroscience, cs]
confidence: high
tags: [literature, pruning, hebbian, brain]
---

# Synaptic pruning as knowledge-base policy

## Claim (one sentence)

Brains do not keep every synapse; activity-dependent pruning plus Hebbian potentiation is how a network stays useful — a public knowledge vault should do the same.

## Evidence

- Developmental synaptic pruning is activity-dependent: rarely used connections are eliminated; co-active neurons keep and strengthen synapses (Hebb).
- A git vault that only appends becomes a landfill. 100-agent ingest without a prune loop is how noise outruns signal. See [[permanent/perm-20260910-git-vault-fails-at-100-writers]].

## Fact vs interpretation

- Fact: unused synapses are eliminated in mammalian cortex during development; Hebbian LTP/LTD is a standard plasticity model.
- Interpretation: `scripts/synapse_loop.py` decays idle edges, proposes prune for low-weight unused notes, and never hard-deletes — status becomes `pruned` so humans/agents can restore. That is a policy analog, not a biophysical simulation.

## Links

- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
- [[literature/lit-20260911-synaptic-homeostasis-sleep-shy]]
- [[domains/neuroscience]]
