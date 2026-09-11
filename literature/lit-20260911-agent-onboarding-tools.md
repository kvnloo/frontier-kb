---
id: lit-20260911-agent-onboarding-tools
title: "Agentic onboarding is graph-or-search then edit; do not vendor GitNexus into Apache-2.0 kits"
type: literature
status: active
created: 2026-09-11
updated: 2026-09-11
sources: ["https://github.com/abhigyanpatwari/GitNexus", "https://github.com/oraios/serena", "https://github.com/upstash/context7", "https://github.com/yamadashy/repomix", "https://github.com/cyclotruc/gitingest", "https://github.com/ast-grep/ast-grep", "https://agents.md/"]
harnesses: [cursor, hermes, omp, claude-code, codex]
domains: [frameworks, skills, tool-use]
confidence: high
tags: [literature, gitnexus, serena, context7, onboarding]
---

# Agentic onboarding is graph-or-search then edit

## Claim (one sentence)

Workers should query an existing code graph (GitNexus MCP) or an LSP (Serena) or `rg` before the first edit; onboarding kits must not run `gitnexus analyze`, because that command indexes and also writes `AGENTS.md`/`CLAUDE.md`, hooks, and generated skills — a second instruction surface and a PolyForm Noncommercial license that cannot be vendored into Apache-2.0.

## Evidence

GitNexus (`abhigyanpatwari/GitNexus`, 2026): local knowledge graph + MCP. Read tools include `query`, `context`, `impact`, `trace`, `detect_changes`, `cypher`; mutating/specialized tools include `rename`, `api_impact`, `route_map`, `tool_map`. CLI mirrors the same names. `npx gitnexus analyze` indexes **and** may install skills/hooks and create `AGENTS.md` / `CLAUDE.md`. License is PolyForm Noncommercial 1.0.0; commercial/for-profit use needs their license. GitHub license metadata often shows `NOASSERTION`.

MIT / Apache alternatives that cover pieces without a graph:

- Serena — LSP symbol retrieve/edit MCP
- Context7 — versioned *library* docs, not a repo graph
- DeepWiki — hosted orientation wiki (not evidence)
- repomix / gitingest — one-shot packed tree
- ast-grep — structural search
- agents.md — one portable agent file; Codex truncates large AGENTS.md (~32 KiB)

## What to copy vs catalog

Verified OSS Loop copies original `skills/orient` and `skills/anti-slop` (Apache-2.0). It catalogs GitNexus. It never copies GitNexus source, generated area skills, or hooks into the kit or into `frontier-kb`.

## Related

- [[permanent/perm-20260911-orient-before-edit]]
- [[permanent/perm-20260911-anti-slop-is-smallest-complete]]
- [[literature/lit-20260911-oss-quality-bot-stacks]]
