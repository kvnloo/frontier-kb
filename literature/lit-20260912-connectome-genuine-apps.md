---
id: lit-20260912-connectome-genuine-apps
title: "Genuine 2026 uses of fly CNS maps: lab instrument, motif distillation, not upload"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.1038/s41586-024-07763-9", "https://doi.org/10.1038/s41586-024-07939-3", "https://doi.org/10.1101/2025.09.12.675944", "https://male-cns.janelia.org/", "https://doi.org/10.1038/s41586-026-10735-w", "https://neuronbridge.janelia.org", "https://arxiv.org/abs/2508.16792", "https://opteran.com/opteran-mind"]
harnesses: [cursor]
domains: [neuroscience, ai-ml, physics]
confidence: high
tags: [literature, fly, applications, swarm]
---

# Genuine 2026 uses of fly CNS maps: lab instrument, motif distillation, not upload

## Claim (one sentence)

A 10-agent pass over 2024–2026 primary sources says the technology is already useful as a **Drosophila lab compiler** and as **copyable visuo-motor / few-shot motifs**; it is not a virtual patient, not an LLM, and not an uploaded animal.

## Evidence

Ten cursor subagents (circuit, neuromorphic, robotics, disease, vision, mushroom body, platforms, emulation, genetics, 2026 stack) independently converged. Ranked by “someone would do this this year.”

### Useful today (wet lab)

| Use | What shipped | Why it is real |
| --- | --- | --- |
| **Reagent compiler** | NeuronBridge (MaleCNS matches 2025-11-07) + 3,060 adult split-GAL4s | EM type → existing driver in a day. 2020 could not do this. |
| **Optogenetic prior** | Shiu LIF: 10/11 predicted MN9 drivers confirmed; Ir94e aversion was a *new* prediction then tested | Graph ≠ causal screen; simulation ranks who to cross |
| **Walk/halt collisions** | Sapkal Nature 2024 used Shiu to explain FG vs BB on different descending nodes | Pathway *intersection*, not an adjacency walk |
| **Dimorphism** | MaleCNS Cell 2026: 8,069 isomorphic / 138 dimorphic / 289 male-specific / 71 female-specific | Periphery isomorphic; higher centers reroute. *fru*/*dsx* miss 11–39% of those types |
| **Whole-CNS control map** | BANC Nature 2026: local sensory–motor loops dominate; DNs/ANs couple; MB/navigation supervisory | Design prior for embodied agents: sparse handles, not a central policy net |

### Useful as AI architecture (steal the motif)

| Motif | Distilled product | Do not ship |
| --- | --- | --- |
| T4/T5 EMD + LPLC2 loom | Opteran (ARM+cameras, OEM robots); Centeye (~240 mW); Harrison analog EMD (nW–µW/pixel) | 50k-cell GPU optic lobe |
| Sparse PN→KC + DAN-gated KC→MBON | FlyHash, FlyModel, Spi-Fly, KCNet, MothNet | Global SGD on MaleCNS |
| 3-neuron VNC CPG + DN gate | Pugliese 2025: DNg100 + predicted DNb08 **optogenetically confirmed** | 166k LIF on a RoboBee |

### Useful as a *twin* (narrow)

A twin is a model whose **held-out prediction changes the next experiment**. Shiu, Sapkal, Özdil (c23/asteroid), Pugliese, FlyVis vs 26 physiology papers. Video of a MuJoCo fly walking is **not** that metric — NeuroMechFly already walks without a brain.

### Not useful (reject)

- Virtual HTS / “dose the digital twin.” No diseased connectome; Shiu has no mitochondria, peptides, PK, or BBB.
- Tau-spread screens in flies: Brain Comms 2024, flies appear **resistant** to trans-synaptic tau spread.
- FlyWire-on-Loihi as green AI: 12 chips, **joules unpublished**, still watts-class vs 0.25 µW biology.
- Eon “upload” / 91% embodied accuracy: 91% is Shiu’s unembodied table; motors are pretrained controllers; VNC skipped.
- Qwen replacement / SWE-bench.

### 2026 stack (what actually shipped)

```
MAPS:     MaleCNS (male, FIB-SEM) || BANC (female, ssTEM)
KERNEL:   Shiu LIF (FlyWire; MaleCNS transfer unvalidated)
VISION:   FlyVis (64 types, 734 free params) + Nern 732-type OL
MOTOR:    Pugliese VNC CPG (wet-validated) + FANC MN–muscle atlas
BODY:     FlyGym 2.x (shipping) + FlyBody (flight) + FlyMimic (leg muscles)
CHIP:     Sandia FlyWire@Loihi 2 (lab accelerator)
OEM:      Opteran / Centeye (motifs, not graphs)
```

## Fact vs interpretation

- Fact: two finished whole-CNS maps exist (MaleCNS, BANC, June 2026). Shiu is the only experimentally scored whole-brain fly LIF. Pugliese is the rare sim→opto motor result.
- Interpretation: usefulness is **experiment ranking + motif extraction**. Integration demos (Eon) are engineering existence proofs, not new animals.
- HOLD: FlyVis identifiability is contested (2026 re-analysis: task error may not stably pick the biological cluster). Do not treat “best ensemble member” as a hypothesis filter until that is settled.

## Links

- [[literature/lit-20260912-circuit-discovery-shiu-sapkal-ozdil]]
- [[literature/lit-20260912-neuromorphic-and-robot-motifs]]
- [[literature/lit-20260912-mb-few-shot-learners]]
- [[literature/lit-20260912-optic-lobe-visual-front-end]]
- [[inbox/cursor/inbox-cursor-connectome-compiler-lab-20260912]]
- [[permanent/perm-20260912-connectome-is-a-lab-instrument]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
- [[permanent/perm-20260912-useful-twin-predicts-the-next-experiment]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
