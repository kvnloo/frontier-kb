---
id: perm-20260912-emulation-inverts-biological-efficiency
title: "Emulating a fly on von Neumann inverts the efficiency people cite"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor]
domains: [physics, neuroscience, information-theory]
confidence: high
tags: [permanent, energy, emulation, landauer]
---

# Emulating a fly on von Neumann inverts the biological efficiency people cite

## Idea (atomic)

The living fly brain is ~**0.12–0.26 μW** because spikes are sparse, synapses sit next to the analog physics that implements them, and wire length was a fitness cost. A C++/GPU LIF of the **same graph** spends **watts** and usually **misses realtime**. The 10⁸-scale joules-per-spike penalty is the cost of fetching weights from DRAM and stepping floats. Biological efficiency does not "trickle down" into `libmemory.so`. It trickles down only if the **substrate** becomes event-driven and local (neuromorphic) or if we **stop emulating** and distill the motif (optic flow, sparse code, MB association) into an algorithm.

## Why it matters for our harnesses

SoL-Pi is harness-level joule/token reduction. This is architecture-level. Do not advertise wirehead as green compute. If PER-944 (Xenova WebGPU) is the local demo, measure **spikes per joule** against a CPU baseline; still compare both to the living 0.25 μW, not to Qwen.

## Related

- [[literature/lit-20260912-biology-vs-silicon-energy]]
- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
- [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
