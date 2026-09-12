---
id: lit-20260912-chatgpt-flyforge-share
title: "ChatGPT share: FlyForge — architecture prior, not a Qwen replacement"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://chatgpt.com/share/6aa4e9ce-e88c-83ea-bf45-0e9496a1ad6f?ogimg=plain", "https://artificialscientific.com/papers/flies-are-all-you-need", "https://huggingface.co/ngxson/fly-hf"]
harnesses: [cursor, hermes]
domains: [ai-ml, neuroscience, frameworks]
confidence: high
tags: [literature, fly, flyforge, chatgpt, roadmap]
---

# ChatGPT share: FlyForge — architecture prior, not a Qwen replacement

## Claim (one sentence)

The shared thread titled **Research fly vision claims** is a two-turn research program: use fly wiring as a **starting architecture**, then test whether training and compression produce a specialist that moves a **quality/resource frontier** — it is not a claim that a fly brain replaces Qwen3.8-27B.

## Evidence

Share: [chatgpt.com/share/6aa4e9ce-e88c-83ea-bf45-0e9496a1ad6f](https://chatgpt.com/share/6aa4e9ce-e88c-83ea-bf45-0e9496a1ad6f?ogimg=plain). Title on the page: **ChatGPT - Research fly vision claims**. Recovered as a user prompt plus one assistant reply (the rest of the HTML payload is search snippets, not extra turns).

### Operator prompt (verbatim gist)

Research cutting-edge fruit-fly brain applications. Build an artifact comparing fly-model efficiency vs LLMs by giving the **same task** to Qwen3.8-27B, DeepSeek, and others. Then train / super-fine-tune on multiple tasks, distill, artificially grow and reorganize the network, and search for an optimal architecture between ~10k and 27B along a Pareto frontier.

### Assistant reply (what it actually argued)

The idea is a **credible research program**. Stronger than “fly plays Doom.” The assistant did **not** run the fly-versus-LLM benchmarks. It built a proposed **FlyForge** dashboard/kit (12 application areas, 16 candidate architectures, 31 sources) whose performance chart stays empty until measurements are imported.

Hard constraints it set:

1. Do not assume the fly replaces Qwen.
2. “Efficient” is **deployment cost** = encoding + policy execution + decoding + runtime overhead + fallback — not neuron-count vs parameter-count.
3. Same-task means the same **information, action contract, and external verifier**, not the same English prompt.
4. Two tracks: **shared-feature** (identical numerical observations) vs **end-to-end** (each system pays for its own encoder). A student that still calls Qwen is a **hybrid** and must be counted as one.
5. First niche: a small persistent **Hermes recovery/escalation controller** on typed operational events (no plaintext secrets), not SWE-bench.
6. Architecture branches: fixed reservoir → type-tied graph → trainable/reorganized graph → motif-distilled controller. Mandatory controls: direct-input, degree-preserving rewire, GRU/MLP.
7. Distillation stages: lock task+verifier → distill verified decisions → DAgger on student states → grow/reorganize (RigL/Net2Net) → lesion/perturb to explain → freeze and confirm.
8. Connectome-to-Function (arXiv:2609.06093, 2026-09-05) is a **later** architecture generator on ~100–330 mouse nodes, not a MaleCNS SGD starting point.
9. Digital Sphinx: plausible behavior can come from the **interface and body**.
10. First milestone: **one reproducible Hermes recovery task** with a conventional recurrent baseline, a fixed connectome candidate, and topology/interface controls. Parallel, non-blocking: reproduce `ngxson/fly-hf` vs a matched non-connectome LM.

Proposed product target (research, not measured): retain ≥95% of a reference controller’s verified success while cutting total deployment cost ≥50%, with no extra hard-policy violations. Beating an oversized LLM on a bounded task is **not** enough; the student must beat or complement a competent small conventional controller.

## Fact vs interpretation

- Fact: the share contains one user research brief and one assistant program. No FlyForge measurements were run. FLM, fly-hf, Costi, FlyVis, FlyGM, Shiu, and Digital Sphinx are cited as published objects, not as our results.
- Interpretation: this is the factory research program that sits on top of the vault’s earlier “distill motifs, do not upload” cluster. The assistant’s Hermes-first niche matches our harness graph; SWE-bench as a fly task does not.
- HOLD: FlyForge.html/zip artifacts from the ChatGPT sandbox are not in this workspace. Reconstruct the protocol here; do not pretend we have their importer.

## Links

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-flm-and-fly-hf-language-reservoirs]]
- [[literature/lit-20260912-costi-connectome-reservoir]]
- [[literature/lit-20260912-digital-sphinx]]
- [[literature/lit-20260912-flygm-graph-policy]]
- [[literature/lit-20260912-connectome-to-function]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[inbox/cursor/inbox-cursor-flyforge-roadmap-20260912]]
