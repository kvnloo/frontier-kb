---
id: lit-20260910-mcp-dual-stack
title: MCP 2026-07-28: dual-stack + Tasks
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources:
  - https://blog.modelcontextprotocol.io/posts/2026-07-28/
  - https://github.com/can1357/oh-my-pi
  - https://github.com/charmbracelet/crush
harnesses: [omp, crush, hermes, opencode]
domains: []
confidence: medium
tags: [literature, mcp, dual-stack, tasks]
---
# MCP 2026-07-28: dual-stack + Tasks

## Claim (one sentence)
The MCP 2026-07-28 announcement (dual-stack protocol + Tasks) raises the bar for harnesses: a harness must expose both protocol modes and a task abstraction that maps to first-class worktrees/subagents.

## Evidence
- The MCP blog post dated 2026-07-28 announces the dual-stack protocol and Tasks.
- omp's README documents `task` fan-out into isolated worktrees with typed results — the concrete realization of Tasks.
- crush advertises MCP extensibility (http, stdio, sse) as a first-class capability.
- Hermes and OpenCode both advertise MCP compatibility in their READMEs.

## Fact vs interpretation
- Fact: MCP announced dual-stack protocol + Tasks on 2026-07-28.
- Interpretation: harnesses must now expose both protocol stacks and a task/worktree abstraction, otherwise they fall behind the protocol baseline.

## Links
- https://blog.modelcontextprotocol.io/posts/2026-07-28/
- https://github.com/can1357/oh-my-pi
- https://github.com/charmbracelet/crush
