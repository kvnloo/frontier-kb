---
id: lit-20260912-consume-gym-do-not-fork-engine
title: "Speed-up is a Gymnasium env contract, not a FlyGym or OpenEvolve fork"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://github.com/Farama-Foundation/Gymnasium", "https://github.com/NeLy-EPFL/flygym", "https://neuromechfly.org/migration/", "https://github.com/huggingface/OpenEnv", "https://github.com/algorithmicsuperintelligence/openevolve", "https://github.com/NeLy-EPFL/flygym-gymnasium"]
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
| [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | `reset` / `step` / Discrete / Box | **Consume the contract.** Do not vendor Farama into frontier-kb |

`hermes_recovery` lives in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) (`evolution_lab.gym.HermesRecoveryEnv`). `make_env("flygym")` and `make_env("openevolve")` fail closed so a future agent cannot “swap in the famous repo” and think P0 is done.

Engine split that actually saves time:

1. **Gym** = observation, action, expert/verifier (this package; later FlyGym as a second registered name).
2. **Engine** = genomes, ridge students, Pareto, MAP-Elites, promotion (keep).
3. **Mutation backend** = OpenEvolve or Cursor/OpenRouter later, mutating genomes or code, scored by *this* gym.

## Fact vs interpretation

- Fact: FlyGym 2.x authors say leaving Gymnasium was a reason for the CPU speed-up. OpenEvolve’s genome is a program. Our genome is JSON (architecture × curriculum × training × evaluation).
- Interpretation: “Fork the gym” means implement/register envs on the standard API. “Improve the engine” means keep ΔHV + control table and plug backends (Tinker, OpenEnv HTTP) into that gym — not rewrite OpenEvolve’s `combined_score` loop until P0 exists.
- HOLD: no FlyGym or OpenEvolve subtree is vendored. A GitHub fork of FlyGym is only justified if we must patch NeuroMechFly internals for a visuo-motor task; that is not P0.

## Links

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260912-chatgpt-evolution-lab-share]]
- [[literature/lit-20260912-neuromorphic-and-robot-motifs]]
- [[permanent/perm-20260912-gym-is-the-task-engine-is-ours]]
- [[permanent/perm-20260912-experiments-are-the-population]]
- [[inbox/cursor/inbox-cursor-gym-not-fork-20260912]]
