---
id: perm-20260912-mushroom-body-is-the-only-plastic-specialist
title: "The mushroom body is the fly's LoRA; the rest of the graph stays frozen"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor, omp]
domains: [neuroscience, ai-ml, learning-acceleration]
confidence: high
tags: [permanent, mushroom-body, lora, plasticity]
---

# The mushroom body is the fly's LoRA; the rest of the graph stays frozen

## Idea (atomic)

Flies do not backprop the optic lobe. They learn in the **mushroom body**: Kenyon cells, dopaminergic teachers (PAM / PPL), mushroom-body output neurons. Stonkfly/wirehead already restrict plasticity to ~7.8k KC→MBON edges. That is the same shape as **freeze the backbone, train the adapter** — and the same shape as [[permanent/perm-20260910-evolver-lifts-frozen-policy]] (freeze the worker, patch the harness) and [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]] (potentiate used synapses, do not rewrite the whole vault).

## Why it matters for our harnesses

If we "optimize the fly," we calibrate **that** specialist (eligibility traces, DAN timing, rest, decay) against Huang 2024, with held-out odor/visual associations. We do not sprinkle `eta` on 25.6M edges. Global SGD on the connectome would destroy the compiled prior Shiu showed was doing the work.

## Related

- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
- [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
