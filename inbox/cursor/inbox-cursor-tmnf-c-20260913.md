---
id: inbox-cursor-tmnf-c-20260913
title: "Cursor: TMNF-C fork captured; evolution-lab fail-closes, does not fork"
type: inbox
status: draft
created: 2026-09-13
updated: 2026-09-13
node: cursor
harnesses: [cursor]
domains: [ai-ml, neuroscience]
tags: [inbox, wave, fly, tmnf]
confidence: high
---

# TMNF-C fork

## Context

Operator added [kvnloo/TMNF-C](https://github.com/kvnloo/TMNF-C) (fork of adonis-singh/TMNF-C) and asked to put it in this vault and decide what belongs in evolution-lab.

## Next action

1. Do **not** `git submodule` TMNF-C, FlyGym, or OpenEvolve into evolution-lab or this vault.
2. Do **not** replace `hermes_recovery`. Do not mint Linear Todo. PER-1525 stays Backlog until P1 is promoted `claimable`.
3. evolution-lab [issue #14](https://github.com/kvnloo/evolution-lab/issues/14) stays `needs-discussion`. Fail-closed `make_env("tmnf")` belongs in the lab PR on this wave; do not implement a TrackMania env.
4. Game assets / Wine / `TmForever.exe` stay on the operator machine. Agents do not need them for P0/P1.

## Links

- [[literature/lit-20260913-tmnf-c-malecns-trackmania]]
- [[permanent/perm-20260913-tmnf-c-is-a-later-gym-not-p0]]
- [[literature/lit-20260912-consume-gym-do-not-fork-engine]]
