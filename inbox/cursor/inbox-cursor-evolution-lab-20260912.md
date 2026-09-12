---
id: inbox-cursor-evolution-lab-20260912
title: "Cursor: Evolution Lab engine landed (P0 local loop)"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [ai-ml, frameworks]
tags: [inbox, wave, fly, evolution]
confidence: high
---

# Evolution Lab engine (local P0)

## Context

Operator sent a second ChatGPT share and asked to read the **latest** messages and build the experiment engine. Latest user turn: cloud-agent scale + gamified Pareto loop + evolutionary algorithm + Tinker SFT.

Implemented in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) (not fly-wirehead, not this vault). Control table runs on a delayed-cue Hermes recovery task so last-step direct-input is a real skeptic, not a 100% clone of the teacher.

L1 (this workspace): teacher 1.00, mlp/reservoir/rewire 1.00, gru ~0.92, **direct-input ~0.79**. Joules remain `null` / `joules_unknown: true`. Tinker backend refuses.

## Next action

1. CoS: still no MaleCNS-worker HITL. Optional: “Evolution Lab P0 is the runner for PER-944-adjacent work.” PER-944 stays Backlog viewer. Claimable P0 is [evolution-lab#2](https://github.com/kvnloo/evolution-lab/issues/2); Linear [PER-1524](https://linear.app/0ism/issue/PER-1524) stays Backlog. VOL onboard: [evolution-lab#9](https://github.com/kvnloo/evolution-lab/pull/9).
2. Later: wire Tinker as a real backend; Cursor Cloud Agent launch is orchestrator work, not this package faking 100 VMs.
3. Copy `examples/valid/fly-specialist-port.json` to aodl when that repo is in the workspace.
4. Do not grow fly-wirehead into this engine.
5. Do not submodule FlyGym or OpenEvolve; P0 gym is `hermes_recovery` in [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab).

## Links

- [[literature/lit-20260912-chatgpt-evolution-lab-share]]
- [[permanent/perm-20260912-experiments-are-the-population]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
