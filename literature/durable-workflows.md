---
id: lit-20260910-durable-workflows
title: Durable workflows — Claude workflows parity is the baseline
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources:
  - https://code.claude.com/docs/en/workflows
  - https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows
  - https://opencode.ai/docs/agents
  - https://agentskills.io/
harnesses: [claude-code, opencode, omp, hermes, crush]
domains: []
confidence: medium
tags: [literature, workflows, durable-workflows]
---
# Durable workflows — Claude workflows parity is the baseline

## Claim (one sentence)
Durable workflows are the new minimum surface for coding harnesses: Claude Code's workflows engine, OpenCode's agents, and agentskills.io all converge on the same pattern — explicit, inspectable, versionable task plans executed by a harness.

## Evidence
- Claude Code docs expose `workflows` as a first-class agent feature; the cookbook shows dynamic workflows with subagents and hooks.
- OpenCode ships two built-in agents (build, plan) plus a `@general` subagent switchable via Tab.
- agentskills.io documents an open standard for agent skills, and Hermes explicitly advertises agentskills.io compatibility in its README.
- omp's `.omp/skills/` and `.omp/commands/` mirror this skill-command layer.

## Fact vs interpretation
- Fact: the four products above all expose a workflow/agent/skills surface.
- Interpretation: "durable workflows" is the shared abstraction — the harness must make work inspectable, replayable, and composable, not just interactive.

## Links
- https://code.claude.com/docs/en/workflows
- https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows
- https://opencode.ai/docs/agents
- https://agentskills.io/
