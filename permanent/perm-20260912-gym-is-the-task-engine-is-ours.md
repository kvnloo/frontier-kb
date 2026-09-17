---
id: perm-20260912-gym-is-the-task-engine-is-ours
title: "Gym is the task; the engine stays ours"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-13
harnesses: [cursor, hermes, opencode]
domains: [ai-ml, frameworks]
confidence: high
tags: [permanent, gym, evolution, fly]
---

# Gym is the task; the engine stays ours

## Idea (atomic)

A gym is `reset` / `step` plus a verifier. An experiment engine is genomes, selection (ΔHV, MAP-Elites), and fail-closed backends. Speed comes from **registering tasks on the gym contract**, not from forking FlyGym or OpenEvolve over the control table.

## Why it matters for our harnesses

P0 env id is `hermes_recovery` in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab). Fly-wirehead is not a gym. Tinker is a training backend behind the same env. OpenCode/OpenRouter may later mutate genomes; they do not own scoring. `make_env` refuses `flygym` / `openevolve` / `tmnf` so we cannot accidentally replace Hermes recovery with walking, LLM-rewritten scripts, or TrackMania.

## Related

- [[literature/lit-20260912-consume-gym-do-not-fork-engine]]
- [[literature/lit-20260913-tmnf-c-malecns-trackmania]]
- [[permanent/perm-20260913-tmnf-c-is-a-later-gym-not-p0]]
- [[permanent/perm-20260912-experiments-are-the-population]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
