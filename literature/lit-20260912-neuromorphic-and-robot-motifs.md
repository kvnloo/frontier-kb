---
id: lit-20260912-neuromorphic-and-robot-motifs
title: "Ship fly motifs on milliwatt silicon; Loihi FlyWire is a lab accelerator"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://arxiv.org/abs/2508.16792", "https://www.nature.com/articles/s41467-024-45063-y", "https://opteran.com/opteran-mind", "https://www.centeye.com/", "https://doi.org/10.1038/s41592-024-02497-y", "https://doi.org/10.1038/s41586-025-09029-4", "https://doi.org/10.1101/2025.09.12.675944", "https://eon.systems/updates/embodied-brain-emulation"]
harnesses: [cursor]
domains: [physics, ai-ml, neuroscience, cs]
confidence: high
tags: [literature, neuromorphic, loihi, opteran, flygym, pugliese]
---

# Ship fly motifs on milliwatt silicon; Loihi FlyWire is a lab accelerator

## Claim (one sentence)

The only whole-fly-graph neuromorphic run is Sandia’s FlyWire-on-12×Loihi-2 (speedup vs Brian2, **no published joules**); robots that actually navigate steal **EMD / loom / CX / CPG** motifs onto ARM, analog, or tiny SNNs — Opteran and Centeye are the OEM path, not MaleCNS-on-a-drone.

## Evidence

### Connectome-on-chip (lab)

Wang et al. arXiv 2508.16792: ~140k FlyWire neurons / ~50M synapses on **12 Loihi 2 chips**. Compiler: Brian2 → STACS → NxCore. Shared-axon routing cut max fan-in 10,356 → 165. Sugar-neuron task: 1 s sim in **12.4 ms** vs Brian2 4.42 s (~350×) at low background; ~3× at 40 Hz. **Energy for this workload unpublished.** Not MaleCNS, no VNC, no cameras in the loop. TrueNorth fan-in 256 cannot host this graph.

SpiNNaker: Schoepe et al. Nat Commun 2024 — T4/T5-like EMDs on a 2.3 kg robot (corridor centering). Physiology-constrained, **not** the 140k graph. No joules.

Analog EMD (Harrison / Koch, 1997–2003) remains the energy champion: collision chip **140 µW** total, **18 nW/pixel**. Pre-connectome, circuit-constrained. Still the honest milliwatt story.

### Motifs that ship

- **Opteran** (Sheffield): insect vision + path integration as **software on Rockchip ARM + cheap cameras**. Warehouse robots; Airbus/ESA trials. They discarded the graph. Paying OEMs.
- **Centeye**: insect optic-flow chips, ~240 mW, ~1 g, DARPA/SBIR. Not a connectome.
- **CurvACE**: 630 ommatidia, **0.9 W**, 1.75 g — sensor, not a brain.
- Generic milliwatt SNNs (Speck, Pulsar, Akida) are **not** fly-constrained.

### Embodiment: three classes

| Class | Example | Motors |
| --- | --- | --- |
| (a) Graph hits identified MNs | Shiu MN9; Pugliese MN rates | No physics body |
| (b) Animation / DN buttons | Eon 2026: DNa01/02, oDN1, aDN1, MN9 → **imitation** NeuroMechFly gaits | Looks like a fly; VNC skipped |
| (c) Fly-shaped RL | FlyBody (DeepMind+Janelia, Nature 2025) walk+flight; FlyGym HybridController | Best locomotion; wiring unused |

**No published stack drives real joints from VNC motor neurons.** Closest: FANC MN–muscle atlas → Pugliese rates → FlyMimic Hill-type muscles (ICLR 2026) — not yet closed.

BANC’s architectural lesson: **distributed local loops + sparse DNs**. That is the robot API. 166k LIF on a RoboBee is the wrong compile.

## Fact vs interpretation

- Fact: FlyWire@Loihi exists; Eon closed a 15 ms sensory→LIF→DN-label→body loop; FlyGym 2.x is ~60× realtime on GPU Warp; FlyBody flies in MuJoCo.
- Interpretation: “neuromorphic fly brain” in 2026 is a **neuroscience supercomputer**. The efficiency stack that could ship is analog EMD + event readout + tiny CX/MB/CPG, matching [[permanent/perm-20260912-emulation-inverts-biological-efficiency]].
- HOLD: dividing Hala Point 2.6 kW by 12 and calling it FlyWire energy is false.

## Links

- [[literature/lit-20260912-optic-lobe-visual-front-end]]
- [[literature/lit-20260912-biology-vs-silicon-energy]]
- [[permanent/perm-20260912-distill-motifs-not-upload-the-graph]]
- [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
