---
id: lit-20260912-digital-sphinx
title: "Digital Sphinx: behavioral fidelity is not biological fidelity"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.64898/2026.03.20.713233", "https://github.com/Brunton-Lab/DigitalSphinx2026", "https://github.com/michaela10c/connectome-fidelity"]
harnesses: [cursor]
domains: [neuroscience, ai-ml]
confidence: high
tags: [literature, fly, sphinx, fidelity, eon]
---

# Digital Sphinx: behavioral fidelity is not biological fidelity

## Claim (one sentence)

Brunton, Abe, Hu, and Tuthill (2026) show that a *C. elegans* connectome driving a MuJoCo *Drosophila* body through a **trained decoder** produces highly realistic fly walking that teaches nothing about either animal — so walking GIFs, Eon “upload” videos, and choreographed fly-wirehead swipes are not fidelity evidence.

## Evidence

Preprint: *The digital sphinx: Can a worm brain control a fly body?* doi:[10.64898/2026.03.20.713233](https://doi.org/10.64898/2026.03.20.713233). Code: [Brunton-Lab/DigitalSphinx2026](https://github.com/Brunton-Lab/DigitalSphinx2026). eLife reviewed preprint 111516.

Construction: 302-cell hermaphrodite worm connectome, graded (mostly non-spiking) activations, synapse counts signed by neurotransmitter; fly body with 42 leg actuators and 148 proprioceptive sensors; **DRL trains only the map from worm motor-neuron activations to fly torques**. Connectome weights/cellular parameters are not optimized. Result: realistic walking; biologically meaningless.

The Transmitter coverage: written in response to Eon Systems’ “uploaded fly” announcement. NeuroMechFly already walks without a brain; Sphinx shows the remaining peril — even a “brain in the loop” can be a dummy if the interface is the learner.

Follow-on: [michaela10c/connectome-fidelity](https://github.com/michaela10c/connectome-fidelity) (built on FlyVis) asks whether **representational geometry** can distinguish real vs random wiring when behavior cannot. That is a candidate **P5** metric, not a P0 blocker.

## Fact vs interpretation

- Fact: a trained interface + body can imitate locomotion without the claimed brain being the controller.
- Interpretation: every connectome-as-policy paper (FlyGM, Eon, fly-wirehead motor overlay) must declare what was trained. If only the decoder/readout/animation clock learns, the graph is a feature map, not a discovered animal. Same logic as FLM’s direct-input control.
- HOLD: Sphinx does not prove fly graphs are useless. It forbids using behavioral resemblance as the pass condition. [[permanent/perm-20260912-useful-twin-predicts-the-next-experiment]] remains the lab-twin metric; Sphinx is the embodiment-demo metric.

## Links

- [[literature/lit-20260912-flygm-graph-policy]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[permanent/perm-20260912-useful-twin-predicts-the-next-experiment]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[literature/lit-20260912-fly-connectome-task-meme]]
