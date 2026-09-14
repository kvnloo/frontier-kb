---
id: lit-20260912-fly-connectome-task-meme
title: "2026 fly-connectome task meme: MaleCNS graph, remapped I/O, not a house fly"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-13
sources: ["https://male-cns.janelia.org/", "https://www.cell.com/cell/fulltext/S0092-8674(26)00942-6", "https://github.com/nftechie/stonkfly", "https://github.com/mattyhempstead/fly-wirehead", "https://huggingface.co/spaces/Xenova/fruit-fly-simulation", "https://eon.systems/updates/weve-uploaded-a-fruit-fly", "https://www.theregister.com/offbeat/2026/09/11/disembodied-fruit-fly-brain-joins-the-crypto-speculation-swarm/5295914", "https://x.com/shmidtqq/status/2098750407770075274"]
harnesses: [cursor]
domains: [neuroscience, ai-ml, physics]
confidence: high
tags: [literature, fly, connectome, malecns, stonkfly, xenova]
---

# 2026 fly-connectome task meme: MaleCNS graph, remapped I/O, not a house fly

## Claim (one sentence)

The September 2026 X/Twitter trend is people taking the **Drosophila melanogaster** (fruit fly, not house fly) MaleCNS v1.0 wiring diagram, dropping it into a leaky-integrate-and-fire kernel, and **remapping sensory/motor pins** so the same graph "trades bitcoin," "watches Shorts," or drives a 3D body — it is not a new general-purpose model and `kvnloo/fly-wirehead` is a Stonkfly-inspired fork, not the scientific original.

## Evidence

### The dataset (original science)

MaleCNS v1.0 (released 2026-06-08; Cell 2026-09-03) is the finished male *Drosophila* central nervous system: **166,700 neurons** spanning brain, optic lobes, and ventral nerve cord, **11,710 types**, ~125 million synaptic contacts. Directed graph used by the meme repos: **25,582,938** connections. Credit: FlyEM / HHMI Janelia, Cambridge Zoology, MRC LMB, Google Research. License **CC BY 4.0**.

This is a different animal and a larger map than FlyWire FAFB (female adult brain, ~140k neurons), which Eon Systems used in March 2026.

### Lineage of "give the fly a task"

| Layer | What it is | Original |
| --- | --- | --- |
| Anatomy | EM reconstruction + synapses | MaleCNS / FlyWire |
| Physiology prior | LIF + synapse-count weights + E/I from transmitter ID | Shiu et al. Nature 2024 (`philshiu/Drosophila_brain_model`) |
| Embodied science demo | Brain → NeuroMechFly / MuJoCo body; walk, groom, sugar-proboscis | Eon Systems, March 2026 |
| Trading meme | Coinbase BTC-USDC RGB chart → photoreceptors; motor/DAN readout → buy/sell/hold; fake PAM11/PPL101 reward | [nftechie/stonkfly](https://github.com/nftechie/stonkfly) (Alex Wormuth) |
| Shorts / "wirehead" | Insect YouTube Shorts → same photoreceptors; choreographed swipe; PAM11 current while video plays | [mattyhempstead/fly-wirehead](https://github.com/mattyhempstead/fly-wirehead); workspace clone `kvnloo/fly-wirehead` |
| Browser | Same 166,700-cell graph, WebGPU kernels, paint-to-stimulate | [Xenova/fruit-fly-simulation](https://huggingface.co/spaces/Xenova/fruit-fly-simulation); Linear [PER-944](https://linear.app/0ism/issue/PER-944) |
| DEX desk skin | FlyWire 139,255 / 54.5M badge on an LLM **agent council** memecoin UI; no MaleCNS LIF kernel on screen | [@shmidtqq SHERWOOD](https://x.com/shmidtqq/status/2098750407770075274) ([[literature/lit-20260913-sherwood-fly-dex-meme]]) |

Stonkfly and fly-wirehead share a C++ dual-compartment kernel, visual projection onto **3,335 R1–R6 + 811 R8** inputs, and an experimental plasticity overlay on **7,835 KC→MBON07/11** edges. Both repos state: wiring is reconstructed; physiology and reward are approximations; **profitable learning, pleasure, and addiction have not been established**.

### What "a task" means here

A task is an **I/O adapter**:

1. Encode an external stream as currents on identified sensory cells (pixels, candles, paint).
2. Integrate the sparse graph at ~0.1 ms steps.
3. Read identified motor or dopamine cells.
4. Optionally inject current into PAM11 (reward) or PPL101 (aversive) cells that the real fly uses for mushroom-body learning — not because the clip or the trade is biologically a reward.

The fly does not choose the next Short. Stonkfly's $1 paper-trade bump is not a learning result (rising BTC makes any buyer look skilled).

## Fact vs interpretation

- Fact: the public graph is MaleCNS v1.0 *Drosophila*, 166,700 neurons, 25.6M directed edges.
- Fact: `fly-wirehead` README names Stonkfly as the neural backend source (pinned commit `78ef3e05`) and MaleCNS as data.
- Interpretation: calling this "training a fly to do jobs" is the meme. Mechanically it is **frozen evolutionary wiring + a tiny uncalibrated eligibility rule + human-chosen pinout**.
- HOLD: Eon's "this is a real uploaded animal" is their stance, not a result we adopt. No consciousness kind. See AODL inbox: no `consciousness` type.

## Links

- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[literature/lit-20260912-biology-vs-silicon-energy]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
- [[literature/lit-20260913-sherwood-fly-dex-meme]]
- [[inbox/cursor/inbox-cursor-fly-connectome-wave-20260912]]
