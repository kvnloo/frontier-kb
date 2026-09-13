---
id: perm-20260912-distill-motifs-not-upload-the-graph
title: "Distill fly motifs; do not upload the graph"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor, omp]
domains: [ai-ml, physics, neuroscience]
confidence: high
tags: [permanent, motifs, opteran, flyhash]
---

# Distill fly motifs; do not upload the graph

## Idea (atomic)

What transfers out of Drosophila is a **small set of algorithms**: T4/T5 elementary motion detectors, LPLC2 loom geometry, mushroom-body sparse hashing + DAN-gated adapters, a 3-neuron VNC CPG, BANC-style local loops with sparse descending handles. Opteran/Centeye/FlyHash already ship or beat baselines on those. Compiling 166k LIF cells onto GPU or Loihi is a lab accelerator; it inverts biology’s joules and does not fly a drone.

## Why it matters for our harnesses

Same move as [[permanent/perm-20260910-small-models-are-workers-or-specialists]]: bind **specialists**, do not replace Qwen3.8-27B. A loom/EMD front-end or FlyModel-style few-shot memory can sit beside the SVLM. A MaleCNS worker cannot.

## Related

- [[literature/lit-20260912-neuromorphic-and-robot-motifs]]
- [[literature/lit-20260912-mb-few-shot-learners]]
- [[literature/lit-20260912-optic-lobe-visual-front-end]]
- [[permanent/perm-20260912-emulation-inverts-biological-efficiency]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
- [[permanent/perm-20260912-anatomy-is-init-not-a-faithful-brain]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
