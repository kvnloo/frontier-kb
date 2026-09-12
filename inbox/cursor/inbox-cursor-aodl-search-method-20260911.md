---
id: inbox-cursor-aodl-search-method-20260911
title: "AODL research search: alias queries, DuckDuckGo, agent-reach"
type: inbox
status: draft
created: 2026-09-11
updated: 2026-09-11
node: cursor
harnesses: [cursor]
domains: [information-theory, frameworks, cs]
tags: [inbox, aodl, craid, search]
---

# Alias search for orchestration (same structure, different labels)

## Context

Continuous Research for AODL. Tavily MCP was down. Used DuckDuckGo via `ddgs` plus agent-reach Jina Reader (`https://r.jina.ai/URL`), `gh`, and arXiv `id_list`.

Native `ddgs` backend `duckduckgo` returned no results from this IP (html.duckduckgo.com/lite served an anomaly/botnet interstitial). `ddgs text -b auto` / `brave` worked (398 hits / 50 alias queries / 395 unique URLs / 58 arXiv ids). That is a metasearch through the DDGS client the user asked for, not Google CSE.

Information-theoretic move: treat labels as a lossy codec. Query the **invariants** (ports, authority, bounded mutation, evidence, human gates, intent≠plan≠observed) and the **aliases** (swarm, crew, vibe graphing, choreography, sheaf, CRDT, harness, skill, MCP, A2A, AG-UI). Maximize coverage of the concept, not the token "AODL".

## Next action

CoS: promote the companion inbox notes to literature/permanent. AODL tree: `docs/research-craid-20260911.md` (working capture, not a schema change).

## Links

- [[inbox/cursor/inbox-cursor-aodl-papers-20260911]]
- [[inbox/cursor/inbox-cursor-aodl-formalism-20260911]]
- [[inbox/cursor/inbox-cursor-aodl-lab-protocols-20260911]]
- https://github.com/kvnloo/aodl/blob/main/docs/research-craid-20260911.md
- https://github.com/Panniantong/Agent-Reach
