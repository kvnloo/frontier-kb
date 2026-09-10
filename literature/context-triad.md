---
id: lit-20260910-context-triad
title: Context triad: clear → compact → memory (Dreams)
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources:
  - https://platform.claude.com/docs/en/build-with-claude/compaction
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
  - https://platform.claude.com/docs/en/managed-agents/dreams
  - https://omp.sh/
harnesses: [claude-code, omp, hermes]
domains: []
confidence: medium
tags: [literature, context, compaction, memory, dreams]
---
# Context triad: clear → compact → memory (Dreams)

## Claim (one sentence)
The context triad — clear (workspace), compact (stream), memory (persistent) — is the architecture every harness must implement, and Claude Code documents it explicitly across compaction, Memory, and Dreams.

## Evidence
- Claude compaction docs define compaction as a core agent capability.
- Claude Memory tool docs define persistent state across conversations.
- Claude Dreams docs define long-term memory persistence.
- omp's omp.sh meta-description advertises "hindsight memory" and its README documents stream rules that "survive compaction".

## Fact vs interpretation
- Fact: Claude documents compaction, Memory, and Dreams as separate first-class primitives.
- Interpretation: the triad is the durable model for harness context — clear workspace + compact stream + persistent memory; any harness missing one leg is incomplete.

## Links
- https://platform.claude.com/docs/en/build-with-claude/compaction
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- https://platform.claude.com/docs/en/managed-agents/dreams
- https://omp.sh/
