---
id: harness-hermes
title: Hermes Agent
type: harness
status: draft
created: 2026-09-10
updated: 2026-09-10
urls:
  - https://github.com/NousResearch/hermes-agent
  - https://hermes-agent.nousresearch.com/
capabilities:
  - Built-in learning loop: skills from experience, FTS5 session search, agent-curated memory
  - Messaging gateway: Telegram, Discord, Slack, WhatsApp, Signal, Email
  - Multi-backend compute: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox
  - Nous Portal provider bundle; cron scheduler; subagents
gaps_vs_peers:
  - No native DAP debugger support (omp/crush lead here)
  - Rust-less (Python/uv) heavier resource profile than omp
  - Subagent worktree isolation less explicit than firstmate/crush
omp_actionable: true
tags: [harness]
---
# Hermes Agent

Snapshot: Self-improving agent with closed learning loop; built by Nous Research.
Strengths: Messaging gateway across platforms; run anywhere compute backends; scheduled automations; skill creation from experience.
Gaps: Python/uv stack heavier than omp Rust core; no real DAP integration; crew worktree isolation less explicit than crush/firstmate.
Sources: https://github.com/NousResearch/hermes-agent, https://hermes-agent.nousresearch.com/
