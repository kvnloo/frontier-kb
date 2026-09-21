---
id: inbox-frontier-codex-message-board-2026-09-21
title: "Codex α — LocalAgentMessageBoard + ToolPolicy"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [codex]
domains: [ai-ml, frameworks, tool-use]
tags: [inbox, frontier, codex, multi-agent]
---

# Codex agent message board (α — watch GA)

## Context

### FACT
- **0.155.1** + **0.156.0-alpha.6–14:** `LocalAgentMessageBoard` — SQLite, SessionId-scoped; page≤50 / preview 20k; 9 collaboration tools; feature `agent_message_board` **OFF by default**; tree-shared + ID-only notify.
- `ToolPolicy` freezes sandbox/exec at startup (cannot relax mid-session); Guardian uses applied instruction snapshot.
- Also: voice playback preserve; TUI compact layouts; reasoning-summary default off in new TUI sessions.

### INTERPRETATION
- First-class local multi-agent durable messaging in-flight. Architecture leap for Hermes/OMP multi-agent boards — **watch GA**; do **not** mint Linear from α.

## Next action

Watch rust-v0.156 GA before KB release-note promotion. Steal ToolPolicy startup-immutable model as research pattern only. No Linear.

## Links

- https://github.com/openai/codex/releases/tag/rust-v0.155.1
- openai/codex PRs #46959–#47042 · #46999 · #46580
