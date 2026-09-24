---
id: harness-claude-code
title: Claude Code
type: harness
status: draft
created: 2026-09-10
updated: 2026-09-24
urls:
  - https://code.claude.com/docs/en/workflows
  - https://platform.claude.com/docs/en/build-with-claude/compaction
  - https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
  - https://platform.claude.com/docs/en/managed-agents/dreams
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
capabilities:
  - Agent SDK with plan/workflow model + dynamic workflows
  - Compaction (context management) + Memory tool (persistent state)
  - Dreams (long-term memory persistence across conversations)
  - Computer Use tool (native desktop automation)
  - Workflow engine: subagents, hooks, approvals
gaps_vs_peers:
  - Proprietary, subscription-gated (vs openomp/opencode/crush)
  - No multi-platform messaging gateway (hermes)
  - No crew orchestration across worktrees (firstmate)
  - No native cross-terminal TUI parity (omp/crush)
omp_actionable: true
tags: [harness]
---
# Claude Code

Snapshot: Anthropic agent SDK harness; strong compaction/memory/dreams/computer-use primitives.
Strengths: First-class compaction, Memory, Dreams, and Computer Use tool integrations; dynamic workflow SDK.
Gaps: Closed/proprietary vs omp/opencode/crush; no messaging gateway (hermes); no multi-worktree crew orchestration (firstmate).
Sources: https://platform.claude.com/docs/en/build-with-claude/compaction, https://code.claude.com/docs/en/workflows


## Cadence 2026-09-24

### FACT
- **v2.1.281** (2026-09-23T19:19:15Z): Claude apps gateway Desktop keys; Bedrock `assume_role`/guardrails/telemetry attrs; MCP URL elicitation + plugin validate; resume/proxy/cache/advisor repairs; `"attribution": false` footgun on older CLIs.
- URL: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
- Note: 2.1.278 server classifier already documented on unmerged 20260921 PR — not restated here (main baseline is 09-17).

### INTERPRETATION
- Incremental hardening on top of recent Opus-default train. Highest-ROI Hermes steal: resume/proxy/cache + send-now→bg. Sleep HOLD — no pin stamps until go.
