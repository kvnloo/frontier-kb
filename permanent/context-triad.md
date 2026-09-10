---
id: perm-20260910-context-triad
title: Context triad: clear → compact → memory
type: permanent
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [claude-code, omp, hermes]
domains: [ai-ml]
confidence: medium
tags: [permanent, context, compaction, memory]
---
# Context triad: clear → compact → memory

## Idea (atomic)
A harness is only complete when it owns all three context planes: a clear workspace (read/lsp), a compact stream (compaction), and persistent memory (memory tool / Dreams / hindsight).

## Why it matters for our harnesses
The triad maps directly to [[harnesses/claude-code|Claude Code]] (compaction, Memory, Dreams), [[harnesses/omp|OMP]] (hashline edits, stream rules, hindsight memory), and [[harnesses/hermes|Hermes]] (FTS5 session search, agent-curated memory). Any harness missing one leg of the triad is structurally incomplete and will lose long-lived context across sessions.

## Related
- [[literature/context-triad|Literature: context triad]]
- [[literature/mcp-dual-stack|MCP dual-stack + Tasks]]
