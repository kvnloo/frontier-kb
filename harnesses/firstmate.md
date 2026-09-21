---
id: harness-firstmate
title: firstmate
type: harness
status: active
created: 2026-09-09
updated: 2026-09-21
urls:
  - https://github.com/kunchenguid/firstmate
  - https://github.com/kvnloo/firstmate
capabilities:
  - Agent distro for running a crew of agents (one liaison dispatches/supervises; not a new app to install)
  - Disposable git worktrees / isolated secondmates per task
  - Event-driven zero-token supervision via turn-end backstop hooks
  - Project modes: no-mistakes, direct-PR, local-only; +yolo merge autonomy
  - Optional Relay for public mentions (X/Discord)
  - Supports harnesses as primary: Claude Code, Grok, Pi, omp, Codex, OpenCode, Cursor
gaps_vs_peers:
  - Thin wrapper, not a standalone agent engine; depends on verified harness primitives
  - Relay capped at 3 follow-ups / 7 days
  - No built-in model selection UI beyond supported harness
omp_actionable: true
tags: [harness, distro]
---
# firstmate

Snapshot: Talk to one agent, ship with a crew; an agent distro, not a CLI.
**As of 2026-09-21:** AFK/away posture (`state/.afk-contract`) words-as-mandate + wedge-defer + idempotent inbox JSON.
Strengths: Explicit crew orchestration with disposable worktrees; zero-token event-driven supervision; restart-proof; opt-in Relay.
Gaps: Thin distro over harness primitives (no engine of its own); Relay strictly limited; depends on supported harness as primary runtime.
Sources: https://github.com/kunchenguid/firstmate

[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) — fork [kvnloo/firstmate](https://github.com/kvnloo/firstmate).

**Not a harness.** Agent distro: `AGENTS.md` + skills + `bin/` that turn a primary CLI (Claude Code, Grok, Pi, OMP, Codex, OpenCode, Cursor Agent) into a captain liaison. Crewmates ship from disposable treehouse worktrees.

Hard rule 1 matches Keel L0's *shape*: the liaison does not execute project work. Merge still needs the captain's word.

Canonical id lives in [kvnloo/aodl `harnesses/catalog.json`](https://github.com/kvnloo/aodl/blob/main/harnesses/catalog.json) under `distros.firstmate`, not `supported`.

Keel L9 already names Firstmate as an optional subordinate executor. Do not replace Hermes Kanban or dump Keel levels 1–10 into this fork.

Captain/crew orchestrator. Fleet state lives in `FM_HOME` (not this vault). Public-research writes go to `FRONTIER_KB_DSN` on host 0 with `KB_WRITER=firstmate-<host>`. Secondmates inherit the DSN; they do not share a git working tree.

Skill: `skills/frontier-kb`. See [[literature/lit-20260910-kb-mesh-pair-keel]].
