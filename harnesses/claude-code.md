---
id: harness-claude-code
title: Claude Code
type: harness
status: draft
created: 2026-09-10
updated: 2026-09-21
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

**As of 2026-09-21:** v2.1.278 server auto-mode classifier (no charge; gateways must forward safeguards/safeguard_results); v2.1.277 AGENTS.md modes + proxy-only egress.

Snapshot: Anthropic agent SDK harness; strong compaction/memory/dreams/computer-use primitives.
Strengths: First-class compaction, Memory, Dreams, and Computer Use tool integrations; dynamic workflow SDK.
Gaps: Closed/proprietary vs omp/opencode/crush; no messaging gateway (hermes); no multi-worktree crew orchestration (firstmate).
Sources: https://platform.claude.com/docs/en/build-with-claude/compaction, https://code.claude.com/docs/en/workflows
