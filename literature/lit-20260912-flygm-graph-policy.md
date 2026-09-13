---
id: lit-20260912-flygm-graph-policy
title: "FlyGM: connectome as a trained graph policy, with rewire/MLP controls"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://arxiv.org/abs/2602.17997", "https://doi.org/10.1038/s41586-024-07939-3"]
harnesses: [cursor]
domains: [ai-ml, neuroscience]
confidence: medium
tags: [literature, fly, flygm, policy, distillation]
---

# FlyGM: connectome as a trained graph policy, with rewire/MLP controls

## Claim (one sentence)

FlyGM (Jin & Sui; arXiv:2602.17997) is the closest published precedent for the operator’s **train / fine-tune on the graph** idea: FlyWire structure as a directed message-passing policy, imitation then PPO, compared to degree-preserving rewire, random graph, and MLP — on **simulated fly locomotion**, not Hermes recovery or language.

## Evidence

*Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly*. Static structure = adult Drosophila whole-brain connectome; nodes partitioned afferent / intrinsic / efferent; edges = measured connectivity. Training: imitate pretrained flybody MLP expert trajectories, then PPO. Reports higher sample efficiency and orientation stability vs those baselines on gait initiation, walking, turning, flight, without per-task architecture retuning.

This is **anatomy as initialization plus trained dynamics**, which is Stage 2–4 of the FlyForge program. It is not a frozen LIF playback (Shiu, stonkfly, fly-wirehead). It still has engineered interfaces and a physics body. Digital Sphinx remains in force: locomotion success can be decoder-heavy; FlyGM’s value is that it **ran the rewire/MLP table**, which FLM’s relabel-without-refit did not.

FlyVis (Lappalainen et al., Nature 2024) stays the vision-side efficiency reference: 45,669 units, ~1.51M connections, **734 free parameters** in the visual core via type sharing. That is the motif-distillation existence proof on motion, not a whole-CNS policy.

## Fact vs interpretation

- Fact: FlyGM trains a connectome-structured controller and includes topology controls. Task domain is embodied locomotion in a biomechanical fly.
- Interpretation: copy the **training + control table**, not the body. Our P0 is a bounded Hermes action contract with the same control table (MLP, GRU, direct-input, rewire, fixed reservoir, motif student). Do not treat FlyGM walking as evidence that MaleCNS will beat Qwen on SWE-Pro.
- HOLD: independent replication and joules unpublished here. FlyWire (female brain) ≠ MaleCNS v1.0 (male CNS). Transfer unvalidated.

## Links

- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[literature/lit-20260912-digital-sphinx]]
- [[literature/lit-20260912-optic-lobe-visual-front-end]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
