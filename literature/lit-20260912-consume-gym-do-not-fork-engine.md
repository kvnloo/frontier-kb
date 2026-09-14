---
id: lit-20260912-consume-gym-do-not-fork-engine
title: "Speed-up is a Gymnasium env contract, not a FlyGym or OpenEvolve fork"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-13
sources: ["https://github.com/Farama-Foundation/Gymnasium", "https://github.com/NeLy-EPFL/flygym", "https://neuromechfly.org/migration/", "https://github.com/huggingface/OpenEnv", "https://github.com/algorithmicsuperintelligence/openevolve", "https://github.com/NeLy-EPFL/flygym-gymnasium", "https://github.com/kvnloo/TMNF-C", "https://github.com/adonis-singh/TMNF-C"]
harnesses: [cursor]
domains: [ai-ml, frameworks, neuroscience]
confidence: high
tags: [literature, gym, flygym, openevolve, evolution]
---

# Speed-up is a Gymnasium env contract, not a FlyGym or OpenEvolve fork

## Claim (one sentence)

Forking NeuroMechFly or OpenEvolve would **delay** FlyForge: the missing object is a Gymnasium `reset`/`step` gym for **Hermes recovery**; the experiment engine (control table, ΔHV, fail-closed Tinker) stays ours.

## Evidence

The operator ask was: speed up by forking the ideal OSS repo; “just fork the gym and improve the engine.”

| Candidate | What it actually is | If we forked it as the project |
| --- | --- | --- |
| [FlyGym 2.x](https://github.com/NeLy-EPFL/flygym) | Drosophila **body** (see, smell, walk). 2.x **dropped** Gymnasium for ~10× vs 1.x | Months of MuJoCo/Warp; P0 recovery never appears; walking ≠ verified recovery ([[literature/lit-20260912-digital-sphinx]]) |
| [flygym-gymnasium](https://github.com/NeLy-EPFL/flygym-gymnasium) | Legacy 1.x API, explicitly not the fast path | Forking the *slower* API to “speed up” |
| [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) | AlphaEvolve clone: LLM mutates **code**, MAP-Elites on `combined_score` | Replaces experiment genomes + mandatory direct-input with a coding agent. Different species (research-strategy), not P0 |
| [OpenEnv](https://github.com/huggingface/OpenEnv) | Docker/HTTP Gymnasium-style agent envs | Right *shape* for a later real Hermes sandbox; overkill for in-process P0 |
| [TMNF-C](https://github.com/kvnloo/TMNF-C) | TrackMania Forever + MaleCNS MB dopamine learner (PN drive is engineered car state) | Later visuo-motor gym. `make_env("tmnf")` fails closed. Not P0 ([[literature/lit-20260913-tmnf-c-malecns-trackmania]]) |
| [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | `reset` / `step` / Discrete / Box | **Consume the contract.** Do not vendor Farama into frontier-kb |

`hermes_recovery` lives in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) (`evolution_lab.gym.HermesRecoveryEnv`). `make_env("flygym")`, `make_env("openevolve")`, and `make_env("tmnf")` fail closed so a future agent cannot “swap in the famous repo” and think P0 is done.

Engine split that actually saves time:

1. **Gym** = observation, action, expert/verifier (`hermes_recovery` in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab); later FlyGym as a second registered name).
2. **Engine** = genomes, ridge students, Pareto, MAP-Elites, promotion (keep).
3. **Mutation backend** = OpenEvolve or Cursor/OpenRouter later, mutating genomes or code, scored by *this* gym.

VOL P0 [evolution-lab#2](https://github.com/kvnloo/evolution-lab/issues/2) is closed. Linear [PER-1524](https://linear.app/0ism/issue/PER-1524) is Done. TMNF-C is [evolution-lab#14](https://github.com/kvnloo/evolution-lab/issues/14) (`needs-discussion`).

## Fact vs interpretation

- Fact: FlyGym 2.x authors say leaving Gymnasium was a reason for the CPU speed-up. OpenEvolve’s genome is a program. Our genome is JSON (architecture × curriculum × training × evaluation).
- Interpretation: “Fork the gym” means implement/register envs on the standard API. “Improve the engine” means keep ΔHV + control table and plug backends (Tinker, OpenEnv HTTP) into that gym — not rewrite OpenEvolve’s `combined_score` loop until P0 exists.
- HOLD: no FlyGym, OpenEvolve, or TMNF-C subtree is vendored. A GitHub fork of FlyGym is only justified if we must patch NeuroMechFly internals for a visuo-motor task; that is not P0. Game assets for TMNF stay off-repo.

## Links

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-chatgpt-evolution-lab-share]]
- [[literature/lit-20260912-neuromorphic-and-robot-motifs]]
- [[literature/lit-20260913-tmnf-c-malecns-trackmania]]
- [[permanent/perm-20260913-tmnf-c-is-a-later-gym-not-p0]]
- [[permanent/perm-20260912-gym-is-the-task-engine-is-ours]]
- [[permanent/perm-20260912-experiments-are-the-population]]
- [[inbox/cursor/inbox-cursor-gym-not-fork-20260912]]
