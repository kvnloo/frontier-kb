---
id: lit-20260912-connectome-to-function
title: "Connectome-to-Function is a later architecture generator, not P0"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://arxiv.org/abs/2609.06093", "https://arxiv.org/abs/2506.11062"]
harnesses: [cursor]
domains: [ai-ml, neuroscience]
confidence: medium
tags: [literature, fly, generator, reservoir]
---

# Connectome-to-Function is a later architecture generator, not P0

## Claim (one sentence)

arXiv:2609.06093 (2026-09-05) learns a conditional latent over **small local mouse circuits (~100–330 nodes)**, reconstructs edges (AUC up to 0.910), generates candidate graphs, and predicts reservoir scores (cross-validated R² ~0.46–0.87) — useful **after** we have trustworthy architecture–performance pairs, not as the first MaleCNS experiment.

## Evidence

*Connectome-to-Function: Conditional Generative Latent Representations for Reservoir Computing*. Encodes sparse connectome graphs conditioned on neuron type and spatial organization. Generated graphs evaluated as reservoirs on memory, forecasting, and classification. Interpretability sketch: memory ↔ reciprocal recurrence; prediction/classification ↔ spectral properties.

Authors leave cross-species and scale generalization unresolved. Predecessor: *Decoding Cortical Microcircuits* (arXiv:2506.11062) — VAE on mouse visual cortical microcircuits, same reservoir-as-function probe.

FlyForge share maps this to:

```text
Measured (architecture, hardware, score) pairs
        → learned architecture representation
        → proposed new circuit
        → train + measure
        → updated Pareto set
```

Without the first row, this is optimizing a predictor of a task we have not defined.

## Fact vs interpretation

- Fact: published scale is two orders of magnitude below MaleCNS (166,700) and below fly-hf’s 49k subset.
- Interpretation: P4–P6 of the research program. P0 is the Hermes recovery contract and the control table. Searching 10K…1B node counts before a verifier exists is architecture tourism.
- HOLD: R² on reservoir toys is not joules-per-verified-success on Hermes.

## Links

- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[literature/lit-20260912-costi-connectome-reservoir]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
