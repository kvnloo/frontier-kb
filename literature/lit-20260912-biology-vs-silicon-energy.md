---
id: lit-20260912-biology-vs-silicon-energy
title: "Drosophila brain ~0.12–0.26 μW; CPU/GPU fly sims and 27B VLMs spend watts"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://doi.org/10.1145/3439706.3446898", "https://doi.org/10.1101/2025.08.08.669302", "https://doi.org/10.1097/00004647-200110000-00001", "https://www.pnas.org/doi/10.1073/pnas.172399499", "https://github.com/mattyhempstead/fly-wirehead/blob/main/docs/validation.md"]
harnesses: [cursor]
domains: [physics, neuroscience, information-theory]
confidence: high
tags: [literature, energy, landauer, drosophila, watts]
---

# Drosophila brain ~0.12–0.26 μW; CPU/GPU fly sims and 27B VLMs spend watts

## Claim (one sentence)

A living fruit-fly brain runs on **nanowatts**; that thermodynamic advantage is in the **wet analog substrate** (sparse spikes, local synapses, 3D wire minimization) and **does not transfer** to a von Neumann integration of the same graph, which spends laptop/GPU watts to emulate the nanowatt object.

## Evidence

### Living fly

- Laughlin-style respiration budget for *D. melanogaster* nervous system: **~120 nW** (resting O2, ~5% of resting metabolism to the CNS). Source: [The Physical Design of Biological Systems — Insights from the Fly Brain](https://doi.org/10.1145/3439706.3446898).
- Direct biocalorimetry of explanted brains: **~256 nW** mean in female 10-day-old brains; young female > male by ~10–15%; brain mass-normalized rate ~2.5× ovary/testis. [bioRxiv 2025.08.08.669302](https://doi.org/10.1101/2025.08.08.669302).
- Order of magnitude to remember: **10⁻⁷ W**, not the 10 μW sometimes quoted in emulation blogs.

### Spikes as the energy currency

Attwell & Laughlin 2001 (rodent grey matter, not fly): one cortical spike ≈ **7.1×10⁸ ATP** including synaptic release (~3.84×10⁸ ATP for the AP itself). Energy budget predicts **sparse codes** (they estimate ≤15% of neurons simultaneously active) because signaling is a large fraction of the brain's ATP. Human brain ~**20 W** (Raichle & Gusnard 2002) for ~86B neurons.

Landauer bound for irreversible bit erasure: **kT ln 2 ≈ 3×10⁻²¹ J** at 300 K. Biology is not at the bound, but it is many orders closer than dense GPU matmul for the same bit-erasures, because most "FLOPs" on a GPU are not biologically meaningful operations.

### Silicon copies of the fly

fly-wirehead recommends **16 GB RAM**, a C++17 kernel, and advances **50 ms of neural time per accepted video frame**. Live median **~1.23×10⁶ spikes / simulated second**. Even if the laptop draws only ~15–40 W during the step, that is **~10⁸×** the living brain's power **and** typically not biological real-time. The kernel already skips inactive cells; it still fetches weights from DRAM and integrates floats.

Xenova moves the same graph onto **WebGPU** (closer to the data, still digital, still watts). Neuromorphic (Loihi, analog) is the actual efficiency play; it is not what the meme repos ship.

### Arithmetic we will use later

Using 256 nW living vs 30 W sim at the same spike rate: **~10⁸** joules-per-spike penalty for emulation. This is the inversion: copying the *graph* onto the *wrong physics* destroys the thing people cite as the fly's advantage.

Qwen3.8-27B on an RTX 5090: public decode ~50–140 tok/s at **~380–520 W** GPU draw → **~4–8 J/generated token**. Different unit (token ≠ spike). See [[literature/lit-20260912-qwen38-27b-vs-fly-snn]].

## Fact vs interpretation

- Fact: measured/estimated fly-brain power is 0.12–0.26 μW; human cortex energy is spike-rate dominated; GPU 27B inference is hundreds of watts.
- Interpretation: "brains are more efficient than compute" is true for **matched tasks on the native substrate**. It is false as a claim that *simulating* a fly on a CPU is an efficient AI, and false as a claim that a fly graph will beat a 27B VLM on language.
- HOLD: 1.23e6 spikes/s is the *simulated* MaleCNS under video drive, not a living fly's spike census.

## Links

- [[permanent/perm-20260912-emulation-inverts-biological-efficiency]]
- [[permanent/perm-20260912-physical-computation-is-one-stack]]
- [[literature/lit-20260912-qwen38-27b-vs-fly-snn]]
- [[domains/physics]]
- [[literature/lit-20260911-sol-pi-harness-efficiency]]
