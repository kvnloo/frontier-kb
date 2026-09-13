---
id: lit-20260912-costi-connectome-reservoir
title: "Costi 2025: full Drosophila connectome as an ESN resists overfitting on chaotic series"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.3390/biomimetics10050341", "https://arxiv.org/abs/2201.09359", "https://esa.int/gsp/ACT/projects/fly_connectome/"]
harnesses: [cursor]
domains: [ai-ml, neuroscience, physics]
confidence: high
tags: [literature, fly, reservoir, esa, cost]
---

# Costi 2025: full Drosophila connectome as an ESN resists overfitting on chaotic series

## Claim (one sentence)

Costi, Hadjiivanov, Dold, Hale, and Izzo (ESA ESTEC / Biomimetics 2025) show that using whole-fly connectome **topology and synaptic-weight distribution** as an echo-state reservoir improves **overfitting resilience** on multivariate three-body trajectories relative to standard random ESNs — a time-series result, not a language or SWE result.

## Evidence

Paper: *The Drosophila Connectome as a Computational Reservoir for Time-Series Prediction*, Biomimetics 10, 341 (2025-05-21). doi:[10.3390/biomimetics10050341](https://doi.org/10.3390/biomimetics10050341). PMC [12109256](https://pmc.ncbi.nlm.nih.gov/articles/PMC12109256/).

Design: connectivity matrix from the released full connectome; most-connected-neuron subsets with two class-proportion rules; hybrids that keep topology XOR weights; a full-connectome reservoir. Task: chaotic three-body trajectories at increasing forecast horizon.

Reported: connectome-based reservoirs more resilient to overfitting than the standard implementation, especially where overfitting is already likely. **Both** topology and weights contribute (hybrids). Full-graph reservoir: despite many more trained readout parameters, remains resilient and reaches **normalized error below 2%** at **lower** regularisation than smaller reservoirs trained with higher regularisation.

Prior: Morra et al. hemibrain/olfactory Fruit Fly ESNs (arXiv:2201.09359) already reported lower variance and sometimes better Mackey–Glass MSE vs random ESNs. Costi is the first (authors’ claim) full-connectome + weight-distribution characterization at this scale.

ESA ACT project page (`esa.int/gsp/ACT/projects/fly_connectome/`) is the lab home; fetch here returned 409, so do not treat the HTML as recovered.

## Fact vs interpretation

- Fact: this is reservoir **readout** training on a dynamical forecasting task. It is not spikes, not MaleCNS LIF, not Qwen distillation, not embodied control.
- Interpretation: forecasting/temporal-state tasks are a better **first scientific** probe of “does this graph do anything?” than free-form chat. It still does not license “fly is more efficient than Qwen.” FLM’s 0.6/step contraction is a different recurrence and may hide this advantage.
- HOLD: 2 citations at capture. Independent replication and energy accounting are unpublished here. Do not score Costi NRMSE against Qwen NLL.

## Links

- [[literature/lit-20260912-flm-and-fly-hf-language-reservoirs]]
- [[literature/lit-20260912-connectome-to-function]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-joules-per-verified-success]]
