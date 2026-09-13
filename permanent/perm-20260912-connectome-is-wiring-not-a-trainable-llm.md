---
id: perm-20260912-connectome-is-wiring-not-a-trainable-llm
title: "A connectome is compiled wiring, not a 166k-parameter LLM"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor]
domains: [neuroscience, ai-ml, cs]
confidence: high
tags: [permanent, connectome, snn, llm]
---

# A connectome is compiled wiring, not a 166k-parameter LLM

## Idea (atomic)

MaleCNS is a **sparse adjacency with biological labels**. The meme kernels run leaky-integrate-and-fire on that graph. That is a neural network, but it is not an LLM: there is no tokenizer, no residual stream, no next-token objective, and almost all weights are **evolutionary**, not SGD. Giving it a "task" means soldering a new pinout (pixels → photoreceptors, motor cells → action). It does not become Qwen by adding loss.

## Why it matters for our harnesses

Do not route SWE, planning, or KB synthesis through a fly SNN. Treat it as an **embodiment / visuo-motor specialist** if we wire it at all. `kvnloo/fly-wirehead` is the Shorts fork of Stonkfly, not FlyWire itself.

## Related

- [[literature/lit-20260912-fly-connectome-task-meme]]
- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
