---
id: lit-20260912-qwen38-27b-vs-fly-snn
title: "Qwen3.8-27B vs MaleCNS SNN: different objects, do not score on one ladder"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://github.com/AlibabaCloud-Official/Qwen3.8-27B", "https://ai-tldr.dev/models/qwen3-8-27b/", "https://blog.vineethvijay.com/posts/bandwidth-not-capacity-qwen3-8-27b.html", "https://github.com/mattyhempstead/fly-wirehead", "https://male-cns.janelia.org/"]
harnesses: [omp, hermes, cursor, pi]
domains: [ai-ml, neuroscience, physics]
confidence: high
tags: [literature, qwen, svlm, fly, comparison]
---

# Qwen3.8-27B vs MaleCNS SNN: different objects, do not score on one ladder

## Claim (one sentence)

Qwen3.8-27B is a **27B dense multimodal worker** (language, tools, computer-use); the MaleCNS sim is a **166k-cell sparse SNN with ~26M frozen evolutionary edges** for insect sensorimotor structure — comparing them on SWE-bench is undefined for the fly, and comparing them on visuo-motor joules is undefined for Qwen.

## Evidence

### Qwen3.8-27B (the SVLM in our vault)

Already encoded: [[permanent/perm-20260910-small-models-are-workers-or-specialists]]. Vendor card (Apache-2.0, Aug 2026): native VLM, 262K context (YaRN to 1M), Gated DeltaNet + Gated Attention, thinking knobs.

| Benchmark (vendor, often Claude Code harness) | Qwen3.8-27B |
| --- | --- |
| Terminal-Bench 2.1 Terminus | 73.0 |
| SWE-bench Pro | 61.7 |
| DeepSWE 1.1 | 42.2 |
| OSWorld-Verified | 84.3 |

RTX 5090 inference (independent blogs): NVFP4 decode ~55–140 tok/s depending on MTP/D-Flash; GPU **~400 W** class. Energy **~4–8 J/token** at 50–100 tok/s. Fits one 24–32 GB card at 4-bit.

### MaleCNS SNN (the meme)

| Quantity | MaleCNS / wirehead | Qwen3.8-27B |
| --- | --- | --- |
| Degrees of freedom | 1.67e5 neurons, 2.56e7 directed edges (~1e3× fewer than 27B params) | 27e9 params (+ vision encoder) |
| Inductive bias | 400 Myr of *Drosophila* evolution, compiled into anatomy | SGD on tokens/images/video |
| Plasticity at runtime | 7,835 KC→MBON edges, uncalibrated | none (weights frozen at inference) or LoRA/SFT/RL |
| Native task | optic flow, flight, walk, taste, courtship, sparse associative memory | next-token + tool_call + GUI |
| SWE-bench Pro | not defined (no tokenizer, no tools) | 61.7 |
| Living power | ~0.25 μW | n/a |
| Silicon run | laptop/GPU watts, often slower than realtime | ~400 W GPU |
| I/O | identified cell types | tokens, pixels as patches |

A 27B transformer is not "bigger fly." Residual-stream channels are not Kenyon cells. Self-attention is global dense mixing; the fly is sparse, delayed, locally wired, and **mostly not plastic**.

### What would a fair contest look like?

1. **Fly-native closed loop** (walk, odor approach, loom escape) on a body: connectome SNN with a correct VNC pinout should beat a 27B that has never been RL'd in that body, *per joule of living tissue*. On a GPU, the 27B may still win on wall-clock by throwing watts at a learned policy.
2. **Language / SWE**: Qwen wins by construction. The fly has no language cortex.
3. **Hybrid harness**: Qwen as language planner; fly SNN as sensorimotor specialist; vault synapses as durable claims. Same pattern as "27B is a worker, Nemotron Super is an in-harness planner" — add a *third* specialist, do not replace the worker.

## Fact vs interpretation

- Fact: Qwen3.8-27B is a 27B VLM with published coding-agent scores; MaleCNS is a 166k-neuron connectome; wirehead does not emit tokens.
- Interpretation: "optimize the fly until it matches Qwen" is a category error. Optimize the fly until it is a **better fly-shaped worker**; keep Qwen as the language worker.
- HOLD: vendor SWE-bench numbers mix harnesses; we already refuse 10-point ghosts ([[permanent/perm-20260910-scaffold-tool-shape-dominates]]).

## Links

- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
- [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
- [[literature/lit-20260912-biology-vs-silicon-energy]]
