---
id: harness-codex
title: codex
type: harness
status: draft
created: 2026-09-09
updated: 2026-09-24
urls:
  - https://github.com/openai/codex
  - https://openai.com/index/introducing-the-agents-api/
  - https://openai.com/index/introducing-gpt-live-1-in-the-api/
tags: [harness]
---

# codex

Snapshot: openai/codex OSS harness; Agents API hosted path Sep 10; 0.155 α daemon_auto_start / `--no-daemon` / Guardian / MCP readOnly / sandbox per-op.
Strengths: hosted + OSS dual surface; progressive tools + parallel subagents.
Gaps: alpha daemon maturity; steal patterns only — no fork until drain.
Sources: https://openai.com/index/introducing-the-agents-api/ · https://github.com/openai/codex


## Cadence 2026-09-24

### FACT
- GA pin remains **rust-v0.156.1**. Watch **rust-v0.158.0-alpha.3–8**: Guardian auth/env binding (thread-owned always-on); AgentControl via ThreadManager; network-policy on history/image/ChatGPT backend; RouteAwareClientPool.
- URL: https://github.com/openai/codex/releases/tag/rust-v0.158.0-alpha.8

### INTERPRETATION
- Keep alpha watch separate from consumer pin. No Linear mint from α. Sleep HOLD on pin stamps.
