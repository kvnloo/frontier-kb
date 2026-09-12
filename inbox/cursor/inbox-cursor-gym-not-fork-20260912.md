---
id: inbox-cursor-gym-not-fork-20260912
title: "Cursor: Gymnasium contract for P0; do not fork FlyGym/OpenEvolve"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [ai-ml, frameworks]
tags: [inbox, wave, gym, fly]
confidence: high
---

# Gym contract, not an OSS fork of the engine

## Context

Operator asked how to speed up by forking the ideal OSS repo: fork the gym, improve the engine.

Implemented `evolution_lab.gym` in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab): `hermes_recovery` duck-types Gymnasium. `make_env("flygym"|"openevolve"|"openenv")` fails closed. CLI: `python -m evolution_lab gym-smoke`. L1 ridge archive unchanged.

## Next action

1. Do **not** `git submodule` FlyGym or OpenEvolve into frontier-kb.
2. If a visuo-motor task is locked, `pip install flygym` and wrap 2.x (not flygym-gymnasium) as a second env name.
3. OpenEvolve/OpenRouter belong as a mutation backend after P0 logs exist.
4. Operator GitHub fork of FlyGym is only if we must patch the body model.

## Links

- [[literature/lit-20260912-consume-gym-do-not-fork-engine]]
- [[permanent/perm-20260912-gym-is-the-task-engine-is-ours]]
