---
id: harness-omp
title: OMP (oh-my-pi)
type: harness
status: draft
created: 2026-09-10
updated: 2026-09-10
urls:
  - https://github.com/can1357/oh-my-pi
  - https://omp.sh/
capabilities:
  - Subagents, LSP, DAP, plan mode, hindsight memory, hashline edits, stream rules
  - Multi-model (60+ providers), Rust core, persistent Python/Bun worker
  - First-class task fan-out into isolated worktrees, reviewer model
  - Native terminal TUI with MCP/http/stdio/sse extensibility
gaps_vs_peers:
  - No built-in agent crew orchestration (firstmate/crush cover this)
  - No cross-platform messaging gateway (hermes covers Telegram/Discord)
  - Lacks secondmate persistent multi-client workspace (crush serve does multi-client)
omp_actionable: true
tags: [harness]
---
# OMP

Snapshot: Most capable agent surface shipped; fork of Pi. ~80k Rust core lines.
Strengths: LSP/DAP wired in; real debugger; time-traveling stream rules; subagent fan-out.
Gaps: No persistent multi-agent crew management; no messaging gateway (hermes does this); multi-client workspace is missing vs crush serve.
Sources: https://github.com/can1357/oh-my-pi, https://omp.sh/
