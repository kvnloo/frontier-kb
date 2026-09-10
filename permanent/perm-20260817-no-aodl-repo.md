---
id: perm-20260817-no-aodl-repo
title: "AODL was never published as its own git repo"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes]
domains: [frameworks]
confidence: high
tags: [permanent, aodl, provenance]
---

# AODL was never published as its own git repo

## Idea (atomic)

The formal language lives as:

1. ChatGPT voice thread (not fully recovered; likely `chatgpt.com/c/WEB:ad8ba5d2-…`)
2. Hermes paste `118824` (complete 9.3k excerpt)
3. HOTL 0.1 + 0.2 docs on groot (`t_7432ab2d`, `t_83991e68`)
4. GitHub issue [NousResearch/hermes-agent#88589](https://github.com/NousResearch/hermes-agent/issues/88589)

There is no `kvnloo/aodl`. `kvnloo/flow` is a Ratatui swarm TUI. zerOS `AgentCoreLanguage.jsx` + `docs/research/2026-07-13-agent-orchestration-topologies.md` are **badge UI**, not the calculus. Desktop `ao` is a different product.

If a public AODL repo is created later, it should start from HOTL 0.2 IR/schema/validator, not from a new DSL.

## Why it matters for our harnesses

Do not invent a second spec. Extend #88589 / HOTL 0.2. Dash should not grow a parallel orchestration language.

## Related

- [[literature/lit-20260817-aodl-voice-transcript]]
- [[literature/lit-20260817-hotl-02-spec]]
- [[harnesses/hermes]]
