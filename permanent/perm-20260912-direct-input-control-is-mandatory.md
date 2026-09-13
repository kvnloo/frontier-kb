---
id: perm-20260912-direct-input-control-is-mandatory
title: "A connectome table without a direct-input control is not an architecture result"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor, hermes]
domains: [ai-ml, neuroscience, statistics]
confidence: high
tags: [permanent, fly, controls, flm]
---

# A connectome table without a direct-input control is not an architecture result

## Idea (atomic)

If a small supervised adapter on the **same inputs** matches or beats the fly residual, the graph has not been shown to help. FLM: fly NLL 1.359816 vs direct-input **1.359328** on 1,236 tokens; disconnection zeroes the residual; relabel-without-refit is **not** a topology control. Digital Sphinx is the same rule for bodies: if the decoder is the learner, the claimed brain is a prop. Every P1 table includes direct-input **and** a **retrained** degree-preserving rewire.

## Why it matters for our harnesses

Otherwise we will ship a MaleCNS-themed LoRA and call it biology. Same mistake as scoring a fly SNN on SWE-bench: the object under test is not the object that improved.

## Related

- [[literature/lit-20260912-flm-and-fly-hf-language-reservoirs]]
- [[literature/lit-20260912-digital-sphinx]]
- [[literature/lit-20260912-flygm-graph-policy]]
- [[permanent/perm-20260912-useful-twin-predicts-the-next-experiment]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
