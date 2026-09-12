---
id: lit-20260912-mb-few-shot-learners
title: "Mushroom-body motifs beat baselines on few-shot and continual learning; freeze the expansion"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.1126/science.aam9868", "https://doi.org/10.1162/neco_a_01615", "https://doi.org/10.1088/2634-4386/ae9177", "https://doi.org/10.1038/s41586-024-07819-w", "https://doi.org/10.1016/j.neuron.2015.11.003", "https://doi.org/10.1016/j.neuron.2017.01.030"]
harnesses: [cursor, omp]
domains: [neuroscience, ai-ml, learning-acceleration]
confidence: high
tags: [literature, mushroom-body, few-shot, flyhash, spi-fly]
---

# Mushroom-body motifs beat baselines on few-shot and continual learning; freeze the expansion

## Claim (one sentence)

Learners that copy **sparse PN→KC expansion + WTA + dopamine-gated KC→MBON updates** beat matched hashing, few-shot, olfactory, and class-incremental baselines; neuroscience forbids training the expansion and forbids treating PAM11 as a scalar trading reward.

## Evidence

**Motif distillations that beat baselines**

| Work | Task | Result vs baseline |
| --- | --- | --- |
| Dasgupta / Navlakha Science 2017 FlyHash | LSH | MNIST k=4 mAP 16.0% → 44.8% vs Gaussian LSH |
| DevFly NeurIPS 2022 | Developmental wiring | +9% to +106% vs random FlyLSH depending on k |
| FlyVec ICLR 2021 | Binary embeddings | Beats binarized GloVe/word2vec at short hashes |
| Shen / Navlakha Neural Comp 2023 FlyModel | Class-incremental MNIST-20 / CIFAR-100 | ≥0.19 / ≥0.15 above EWC/GEM/replay-free; no backprop |
| Spi-Fly 2026 | Spiking olfaction | Best few-shot vs BPTT; CL holds; ~10⁵× less off-chip memory; 6-bit |
| MothNet 2019 | 1–10 samples/class MNIST | 70–80%, beats kNN/SVM/MLP/CNN in that regime |
| KCNet 2021 | Odor perception + MNIST | Beats XGBoost on odor; 0.9735 MNIST |
| Robinson 2023 PAM-α1 replay | CIFAR-100 CL | LTM phase +20%, within 2% of non-incremental bound |

**Neuroscience constraints (do not violate in a connectome sim)**

- Hige 2015: pairing odor with a DAN → **odor-specific LTD** at KC→MBON (~90% EPSC drop). No KC excitability change. Compartment-confined.
- Litwin-Kumar 2017: KC in-degree ~7 **maximizes dimension**; supervised plasticity **on expansion synapses favors dense wiring** — that is leaving the MB.
- Aso & Rubin 2016 / Yamagata 2015 / Ichinose 2015: **typed DANs**. PAM-α1 (biological PAM11) is **high-capacity LTM**, not a generic reward pulse. α1 ↔ MBON-α1 loop consolidates.
- Huang / Luo Nature 2024: STM (PPL1-γ1pedc / γ2α′1) then LTM gated by weakened MBON→DAN feedback. Reduced recurrent model, not 166k SGD.
- Handler 2019: shift CS–US by **<1 s** and valence **flips** (DopR1 depression vs DopR2 potentiation).
- Felsenberg 2018: extinction is a **new opposing memory**, not overwrite.

Stonkfly/wirehead PAM11-as-video-reward is the wrong teacher, wrong timescale, and the wrong compartment.

## Fact vs interpretation

- Fact: MB-like algorithms win where data are scarce and classes arrive sequentially. Biology localizes plasticity to KC→MBON.
- Interpretation: this is the fly’s contribution to **our** factory — a specialist learner next to Qwen, same shape as [[permanent/perm-20260910-evolver-lifts-frozen-policy]] (freeze worker, patch a tiny surface).
- HOLD: offline SVM/GNB still win when they see the whole set; BPTT wins with many epochs. MB motifs are **few-shot / CL / hashing**, not ImageNet SOTA.

## Links

- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
