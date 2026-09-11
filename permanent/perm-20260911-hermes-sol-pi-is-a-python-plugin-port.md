---
id: perm-20260911-hermes-sol-pi-is-a-python-plugin-port
title: "Hermes SoL-Pi is a standalone Python plugin, not a TS import"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [hermes]
domains: [frameworks, tokenomics]
confidence: high
tags: [permanent, sol-pi, hermes, plugins]
---

# Hermes SoL-Pi is a standalone Python plugin, not a TS import

## Idea (atomic)

Hermes cannot import SoL-Pi. The four mechanisms map onto existing plugin seams: Action Fusion → wrap file tools + `terminal` with `then_run`; ObservationPack → archive + **request-time projection** (context engine `select_context`, not a one-shot `transform_tool_result`); EPR → `transform_tool_result` + auxiliary/reducer model with quote-verify; OCC → plan-boundary trigger around the built-in compressor, because only **one** `ContextEngine` may be registered.

## Why it matters for our harnesses

Ship `~/.hermes/plugins/sol-pi/` (or a pip extra) with `register(ctx)`. Do not PR the mechanisms into `NousResearch/hermes-agent` (vendor plugins stay out; `github_writes=0`). Do not replace the default context engine unless the port *composes* with `ContextCompressor` — replacing it drops Hermes' existing compression. `transform_tool_result` mutates what is appended to history; SoL-Pi ObservationPack deliberately does not. Using that hook for packing would skip the two full sends and break resume-after-compaction unless the archive + `obs_recall` tool are also registered.

## Related

- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260911-observationpack-is-projection-not-history-rewrite]]
- [[permanent/perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi]]
- Hermes docs: plugins, hooks (`transform_tool_result`, `pre_llm_call`), context-engine plugin
- [[harnesses/hermes]]
