---
id: inbox-cursor-aodl-lab-protocols-20260911
title: "MCP, A2A, AG-UI, A2UI, skills, harnesses are adapters under AODL"
type: inbox
status: draft
created: 2026-09-11
updated: 2026-09-11
node: cursor
harnesses: [cursor, hermes, omp, grok, codex, claude, pi, fx]
domains: [frameworks, tool-use, skills]
tags: [inbox, aodl, mcp, a2a, ag-ui, harness]
---

# Labs already speak AODL in three protocol layers

## Context

AG-UI docs state the split: **AG-UI** = agent↔user, **MCP** = agent↔tools/data, **A2A** = agent↔agent. A2UI is Google's agent-generated UI format (messages, not executable code). Agent Skills are packaged procedures. OpenAI harness engineering treats the **repo** as system of record and humans as specifiers of intent + feedback loops.

AODL join:

| Layer | Protocol / product | HOTL |
|---|---|---|
| User | AG-UI, A2UI, Dash, Solarpunk $\tau$ | decoder of declared metadata + observed $S_t$ |
| Tools | MCP, skills, plugins | `tool` / `service` nodes + ports |
| Peers | A2A, Hermes A2A, FIPA | `message` / `delegation` |
| Control plane | LangGraph, Kanban, Codex loop | compiled plan, not intent |
| Observed | OTel, PROV, traces, `/roster` | observed $V$ / event log |

Do not collapse MCP into $\mathcal{O}_t$. Do not treat Cursor cloud agents, Claude Code, Codex, Hermes, or OMP as extra harness ids. Catalog stays `hermes omp o8 grok codex claude pi fx`. Firstmate is a distro. o8 is a control room.

Harness evolution papers (Evo-Bench, Live-SWE-agent, Agentic Harness Engineering) are **search over compiled $\Pi$**, which is exactly the 0.2 line "architecture search is search over programs in this IR."

## Next action

Compiler profiles, not new ids. Frontier-kb already lists poll URLs in `data/sources.yaml`; add AG-UI / A2UI / $\lambda_A$ / Pact only if CoS wants them as poll targets.

## Links

- https://docs.ag-ui.com/introduction
- https://a2a-protocol.org/latest/specification/
- https://modelcontextprotocol.io/specification/2026-07-28
- https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/
- https://agentskills.io/
- https://openai.com/index/harness-engineering/
- https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- [[harnesses/hermes]]
- [[permanent/perm-20260817-market-is-allocation-policy]]
