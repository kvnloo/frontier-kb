---
id: harness-hermes
title: hermes
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls: ["https://github.com/NousResearch/hermes-agent"]
tags: [harness]
---

# hermes

Nous Hermes Agent: Kanban scheduler, gateway/peer A2A, Telegram router.

## Orchestration IR (proposal only)

Hermes has execution primitives (Kanban, runs, leases, review, goal/judge) but no machine-readable topology vocabulary. HOTL 0.1/0.2 is the proposed IR at [kvnloo/aodl](https://github.com/kvnloo/aodl); **not merged**, no second scheduler.

- Catalog id `hermes`: [harnesses/catalog.json](https://github.com/kvnloo/aodl/blob/main/harnesses/catalog.json)
- [[literature/lit-20260817-hotl-01-issue-88589]] — upstream [issue #88589](https://github.com/NousResearch/hermes-agent/issues/88589)
- [[literature/lit-20260817-hotl-02-spec]]
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-no-aodl-repo]]

Starmap/learning graph is a time-axis **projection** of memory, not orchestration edge semantics.

## Keel

- [[literature/lit-20260910-keel-level0-evidence-surface]]
