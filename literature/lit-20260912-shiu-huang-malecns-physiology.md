---
id: lit-20260912-shiu-huang-malecns-physiology
title: "Shiu LIF + Huang mushroom-body rule: connectome constrains, does not train"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.1038/s41586-024-07763-9", "https://github.com/philshiu/Drosophila_brain_model", "https://doi.org/10.1038/s41586-024-07819-w", "https://github.com/nftechie/stonkfly", "https://github.com/mattyhempstead/fly-wirehead/blob/main/docs/model.md"]
harnesses: [cursor]
domains: [neuroscience, ai-ml, cs]
confidence: high
tags: [literature, shiu, huang, lif, mushroom-body, plasticity]
---

# Shiu LIF + Huang mushroom-body rule: connectome constrains, does not train

## Claim (one sentence)

A connectome-constrained leaky-integrate-and-fire model recovers a large fraction of *fly-native* sensorimotor predictions from wiring plus transmitter sign alone; the only biologically motivated learning overlay in Stonkfly/wirehead is a **hypothesis** transplanted from a reduced mushroom-body rate model, not SGD over 166k cells.

## Evidence

### Shiu et al. Nature 2024 (FlyWire female brain)

[Shiu et al. 2024](https://doi.org/10.1038/s41586-024-07763-9) built a whole-brain LIF in Brian2 from FlyWire connectivity and predicted transmitters. One free synaptic scale (`Wsyn = 0.275 mV`). Tested feeding and grooming. **91%** of 164 empirically testable predictions matched (84% excluding split-GAL4 MN9 experiments).

The paper is explicit about what is missing: identical LIF cells, no morphology, no receptor kinetics, no gap junctions, no non-spiking neurons, no neuropeptides, basal firing assumed zero. Connectivity **constrains** a circuit; it does not dictate one mechanism (*C. elegans* / STG caveat in the paper).

Eon and Xenova both cite this model. Transfer to **MaleCNS** (different sex, includes VNC) is an additional unvalidated step. Xenova README: "The original model's validation does not validate this transfer to MaleCNS or the demo's movements."

### Huang et al. Nature 2024 (mushroom body)

[Huang, Luo et al. 2024](https://doi.org/10.1038/s41586-024-07819-w) is the dopamine STM/LTM paper Stonkfly/wirehead point at (`docs` / `neural/rule.py`, DOI `10.1038/s41586-024-07819-w`). In the real fly, **Kenyon cells × dopaminergic neurons × mushroom-body output neurons** store olfactory associative memory. PAM clusters (including PAM11) carry reward; PPL1/PPL101 carry aversive valence. Plasticity is **local to that specialist**, not a global backprop.

Stonkfly/wirehead implement a **baseline-centered anti-Hebbian rate rule** on the **7,835 existing KC→MBON07/11 edges** only. Trace constants, efficacy bounds (0.1–2.0× reconstructed weight), 50 ms weight filter, and `eta=0.001` are declared model choices. The original nine-unit reduced model is **not** substituted for the connectome. Full-graph assays show weights *can* move after PAM11 stimulation; that is a mechanism check, not learned preference.

### Wirehead/Stonkfly kernel (what actually runs)

- Dual-compartment / current-based LIF, 0.1 ms steps, ~1.8 ms axonal delay, 2.2 ms refractory, threshold −45 mV.
- Sparse CSR graph; inactive subthreshold cells skipped when they cannot fire.
- Visual: 90×160 RGB → R1–R6 luminance + R8 color hex mapping.
- Default "reward": **20 mV-equivalent current into 15 annotated PAM11 cells** whenever a video frame is accepted (wirehead) or P&L is positive (Stonkfly).
- Motor overlay (wing/leg/head) is an amplified artistic readout of MN9 / DNp09 / DNa02 rates, plus a **choreographed** foreleg swipe that does not spike the network.

Full-graph numbers from fly-wirehead validation (2026-09-10/11): white vs black 100 ms → 127,378 vs 92,952 spikes; 200 ms PAM11 pulse → 261 vs 0 PAM11 spikes and 3,087 plastic edges moved; median live sample **61,731 spikes / 50 ms** ≈ 1.23 million network spikes per simulated second.

## Fact vs interpretation

- Fact: Shiu shows architecture + E/I + synapse counts carry a lot of *Drosophila* sensorimotor structure.
- Fact: the meme repos freeze almost all of that graph and touch ~0.03% of edges (7,835 / 25.6M).
- Interpretation: "You can train it like a neural net" is true only in the mushroom-body sense (tiny associative specialist) or if you abandon biology and fine-tune the whole adjacency as a sparse ANN — which is a different object.
- HOLD: 91% is FlyWire female feeding/grooming, not MaleCNS trading or TikTok preference.

## Links

- [[literature/lit-20260912-fly-connectome-task-meme]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
