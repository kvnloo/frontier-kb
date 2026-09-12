---
id: lit-20260912-flm-and-fly-hf-language-reservoirs
title: "FLM and fly-hf: the graph can talk; wiring is not shown to help language"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://artificialscientific.com/papers/flies-are-all-you-need", "https://huggingface.co/ngxson/fly-hf", "https://doi.org/10.3390/biomimetics10050341"]
harnesses: [cursor]
domains: [ai-ml, neuroscience]
confidence: high
tags: [literature, fly, flm, reservoir, language]
---

# FLM and fly-hf: the graph can talk; wiring is not shown to help language

## Claim (one sentence)

Two 2026 language-reservoir prototypes show that MaleCNS can **participate** in next-token prediction; neither shows that fly wiring beats a parameter-matched adapter, and both are dominated by the **interface** (readout / frozen LM), not by biological competence.

## Evidence

### FLM — connectome-conditioned LM (Flies Are All You Need)

[artificialscientific.com/papers/flies-are-all-you-need](https://artificialscientific.com/papers/flies-are-all-you-need). Frozen **LFM2.5-1.2B-Instruct** (1.17B) + full retained MaleCNS (166,700 nodes, 25,582,938 directed edges) as a token-driven reservoir. Only a **278,528-parameter** readout is trained. Unsigned averaging dynamics, not Shiu LIF. Authors derive a **0.6-per-token contraction** on raw-state dependence on initialization.

Confirmation set: 32 conversations, 1,236 assistant target tokens, three fit seeds.

| Condition | NLL (nats/token) |
| --- | ---: |
| Frozen backbone | 1.381995 |
| Fly readout | 1.359816 ± 0.000110 |
| Direct-input readout (matched params) | **1.359328 ± 0.000108** |
| Relabeled, no refit | 1.381265 ± 0.000802 |
| No edges | 1.381995 (exact) |

Fly minus direct-input = **+0.000488** nats/token (interval +0.00000502 to +0.00104). All three seeds favor direct input. Graph residual changes the top token at 1.51% ± 0.047% of positions. Disconnection removes the residual exactly. Relabeling (isomorphic graph, **unretrained** readout) is not a topology control.

Authors’ own conclusion: auditable connectome-**conditioned** conversation, **not** a replacement for pretrained language and **not** evidence that fly wiring improves language modeling. Title cadence is not a replacement claim for attention.

### fly-hf — native reservoir LM (no backbone)

[ngxson/fly-hf](https://huggingface.co/ngxson/fly-hf) (`ngxson/fly-llm-hf` in some citations). Central-brain subset: **49,393** units, ~9.05M directed edges, frozen CSR. Rate-based leaky tanh, spectral radius 0.99, signs from predicted neurotransmitter (Shiu convention). Tokens enter 14,069 sensory-facing cells as an 8-group delay line. Trainable **52.8M** parameters, of which **50.6M are the readout** to a 1024-token byte-level BPE. TinyStories: 1000 train / 100 holdout, deliberately overfit (train 0.86, val 3.99). Local grammar; weak long-range coherence.

Degree-preserving permute at 30 epochs: train 0.77 / val **4.27** vs real wiring train 1.02 / val **3.84**. Real wiring fits slower, generalizes a bit better — same qualitative story as Costi on time series, on a toy LM. Readout from only 1,314 descending neurons failed to memorize (train 4.7 after 12 epochs). Optic lobes and VNC dropped. Custom `trust_remote_code` model; not GGUF.

## Fact vs interpretation

- Fact: FLM’s matched direct-input adapter slightly **beats** the fly residual on the published confirmation set. fly-hf’s parameter count is an interface fact, not a 49k-neuron “small model.”
- Interpretation: any table that omits a direct-input / degree-preserving rewire is not an architecture result. FLM’s strong contraction may **suppress** the dynamical regimes Costi used to distinguish topology — so FLM does not refute connectome reservoirs on other tasks.
- HOLD: neither study is independently replicated here. Dataset overlap of FLM’s synthetic conversations with backbone pretraining is unknown (authors say so).

## Links

- [[literature/lit-20260912-costi-connectome-reservoir]]
- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
