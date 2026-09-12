---
id: lit-20260912-circuit-discovery-shiu-sapkal-ozdil
title: "Connectome-constrained dynamics discover circuits the adjacency matrix misses"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.1038/s41586-024-07763-9", "https://doi.org/10.1038/s41586-024-07854-7", "https://doi.org/10.1038/s41467-026-72152-x", "https://doi.org/10.1038/s41586-024-07939-3", "https://doi.org/10.1101/2025.09.12.675944", "https://github.com/philshiu/Drosophila_brain_model", "https://github.com/TuragaLab/flyvis"]
harnesses: [cursor]
domains: [neuroscience, ai-ml]
confidence: high
tags: [literature, shiu, sapkal, ozdil, flyvis, pugliese]
---

# Connectome-constrained dynamics discover circuits the adjacency matrix misses

## Claim (one sentence)

The only adult *Drosophila* papers where a connectome-constrained **dynamical** model generated a non-obvious, then-tested circuit claim are Shiu (Ir94e, water/sugar sharing, JO-F≠aBN1), Sapkal (walk/halt collisions), Özdil (c23/asteroid), and Pugliese (DNb08 CPG driver); FlyVis is the best visual **mechanistic** model but has mostly rediscovered T4/T5.

## Evidence

**Shiu et al. Nature 2024.** Brian2 LIF, FlyWire, `Wsyn = 0.275 mV`. 91% of 164 testable predictions; **84%** excluding the easy true-negative MN9 screen. Blind 106-type SEZ screen: 10/11 predicted MN9-drivers produced rostrum extension; 4/95 predicted negatives false-positive. **New:** Ir94e GRNs inhibit MN9 (previously framed as attractive); optogenetics confirmed suppression of PER to 50 mM sucrose but not 1 M. JO-F synapses onto aBN1 but the LIF predicted (imaging confirmed) it does **not** drive aBN1. Failures: disinhibition at 0 Hz rest (Phantom, Tentacular); neuropeptide Usnea. Shuffle control: true weights → MN9 in 100/100 100 Hz sugar sims; 1/100 shuffled.

**Sapkal et al. Nature 2024.** Independent use of the same LIF. Co-activating walk commands with halt neurons reproduced modular walk-OFF (FG vs BB hit different DNs). Sugar GRNs recruit FG. BRK’s halt was **not** explained by the brain graph → correctly inferred a VNC brake the brain connectome cannot see.

**Özdil et al. Nat Commun 2026.** FlyVis-style nets + NeuroMechFly kinematics predicted broadcast inhibition; optogenetic **c23 / asteroid** stopped grooming. One predicted class tested.

**Lappalainen / FlyVis Nature 2024.** 45,669 neurons, **734 free params**, optic-flow task, no recordings in the loss. Recovers ON/OFF and T4/T5 vs 26 papers. Connectome **and** task both required. TmY3 parallel motion path is a hypothesis, not a new recording. 2026 re-analysis: task error may not stably select the biological ensemble cluster.

**Pugliese, Tuthill, Brunton 2025.** Rate model of MANC front-leg (~4,604 cells). Recovers DNg100; prunes to a 3-interneuron CPG; predicts **DNb08**; confirmed optogenetically. Rate model chosen because some premotor cells are non-spiking — do not force LIF here.

**Why simulate instead of reading the graph.** Synapse count ≠ effective drive (JO-F). Polysynaptic sign + recurrence. Pathway collision (two driven subgraphs). Timing (how T4 becomes DS). In silico screens cheaper than 100 splits — with known failure modes (peptides, inhibition, state).

## Fact vs interpretation

- Fact: these four/five papers are the discovery set. Looming (Croke, Card) is excellent connectomics + opto, mostly **not** a whole-brain LIF.
- Interpretation: “we simulated the fly brain” is a **method**, not a result. The result is a named, tested cell type.
- HOLD: Shiu→MaleCNS transfer is unvalidated. Pospisil “effectome” is a proposed estimator, not an in-vivo map.

## Links

- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[literature/lit-20260912-connectome-genuine-apps]]
- [[permanent/perm-20260912-useful-twin-predicts-the-next-experiment]]
- [[permanent/perm-20260912-connectome-is-a-lab-instrument]]
