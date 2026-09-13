---
id: lit-20260913-tmnf-c-malecns-trackmania
title: "TMNF-C: MaleCNS mushroom body learns TrackMania; PN drive is engineered car state"
type: literature
status: active
created: 2026-09-13
updated: 2026-09-13
sources: ["https://github.com/adonis-singh/TMNF-C", "https://github.com/kvnloo/TMNF-C", "https://github.com/adonis-singh/TMNF-C/tree/main/python/tmnf_fly", "https://github.com/adonis-singh/TMNF-C/releases/tag/fly-v1"]
harnesses: [cursor]
domains: [neuroscience, ai-ml, physics]
confidence: high
tags: [literature, fly, tmnf, mushroom-body, gymnasium]
---

# TMNF-C: MaleCNS mushroom body learns TrackMania; PN drive is engineered car state

## Claim (one sentence)

[adonis-singh/TMNF-C](https://github.com/adonis-singh/TMNF-C) (operator fork [kvnloo/TMNF-C](https://github.com/kvnloo/TMNF-C)) is a **Gymnasium TrackMania Forever** simulator whose optional `tmnf_fly` stack uses real MaleCNS PN→KC / KC→MBON counts and DAN reward-prediction error — but the thing that *learns laps* is driven by a **random projection of the RL car observation**, not the fly's compound eye.

## Evidence

Upstream README + [`python/tmnf_fly/README.md`](https://github.com/adonis-singh/TMNF-C/blob/main/python/tmnf_fly/README.md). Operator forked it 2026-09-13. Original code MIT (adonis-singh); game assets are not in the repo.

**Two drivers, not one:**

| Path | What is biological | What is engineered | Outcome they report |
| --- | --- | --- | --- |
| **Mushroom-body learner** (`train_mb.py`) | 686 ALPN, 4,064 KC, 97 MBON, 340 DAN, 15 compartments; KC→MBON LTD via PAM (+RPE) / PPL1 (−RPE); no gradients | 193-D car state + one-hot action → fixed random sparse PN projection; potential-shaped race reward; 50 ms decisions | A04: finishes appear minute 3–5 (best 6.29–6.65 s vs author 5.95 s). Frozen greedy rarely finishes; showcase laps are training-time or ε=0.02 |
| **Reflex driver** (`drive.py`) | Zhao 2025 eyemap (852 ommatidia/eye), flyvis 721-column optic lobe, MaleCNS rate graph (~165k neurons / 15.3M edges), Giant Fiber / LC4 / HS pathways | Gains; Embree ray-cast retina | Avoids walls; stalls 150–320 m; **finishes nothing** |

Honest limits they already wrote: candidate actions share ~50% KC code (value barely distinguishes steer vs gas); frozen policy 0/2048 greedy finishes on A04 after 5 min; C03 6-action 60 min: 0 finishes.

Pure-RL (non-fly) PPO/TD3 **does** beat author medals on four tracks — a different object than the MB.

Fruit fly *Drosophila melanogaster* MaleCNS v1.0 (166,700 neurons). Not a house fly. Not SWE-bench.

## Fact vs interpretation

- Fact: KC→MBON plasticity is the only learned graph they train; that matches [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]].
- Fact: PN encoding for the learner is **not** the retina. The eye exists on the reflex/video path.
- Interpretation: this is a **later visuo-motor gym** and a live example of DAN-gated MB learning, not a FlyForge P0 and not “the fly drives better than Qwen.” Direct-input / engineered-encoder skeptic is mandatory if we ever score it ([[permanent/perm-20260912-direct-input-control-is-mandatory]]). Digital Sphinx still applies: finishing A04 ≠ connectome fidelity ([[literature/lit-20260912-digital-sphinx]]).
- HOLD: we did not reproduce their GPU runs or open `TmForever.exe`. Game assets stay local. Do not vendor TMNF-C into [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab). `make_env("tmnf")` should fail closed until after the P1 control table.

## Links

- [[literature/lit-20260912-mb-few-shot-learners]]
- [[literature/lit-20260912-optic-lobe-visual-front-end]]
- [[literature/lit-20260912-digital-sphinx]]
- [[literature/lit-20260912-consume-gym-do-not-fork-engine]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[permanent/perm-20260913-tmnf-c-is-a-later-gym-not-p0]]
- [[inbox/cursor/inbox-cursor-tmnf-c-20260913]]
