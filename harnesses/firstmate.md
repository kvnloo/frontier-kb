---
id: harness-firstmate
title: firstmate
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls:
  - https://github.com/kunchenguid/firstmate
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
tags: [harness]
---
# firstmate

Snapshot: Talk to one agent, ship with a crew; an agent distro, not a CLI.
Strengths: Explicit crew orchestration with disposable worktrees; zero-token event-driven supervision; restart-proof; opt-in Relay.
Gaps: Thin distro over harness primitives (no engine of its own); Relay strictly limited; depends on supported harness as primary runtime.
Sources: https://github.com/kunchenguid/firstmate

Captain/crew orchestrator. Fleet state lives in `FM_HOME` (not this vault). Public-research writes go to `FRONTIER_KB_DSN` on host 0 with `KB_WRITER=firstmate-<host>`. Secondmates inherit the DSN; they do not share a git working tree.

Skill: `skills/frontier-kb`. See [[literature/lit-20260910-kb-mesh-pair-keel]].
