---
id: perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi
title: "Hermes↔Pi plugin compatibility is a host port, not a shared ABI"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [pi, omp, hermes]
domains: [frameworks]
confidence: high
tags: [permanent, sol-pi, plugins, adapter]
---

# Hermes↔Pi plugin compatibility is a host port, not a shared ABI

## Idea (atomic)

A thin binary adapter that loads Pi `ExtensionAPI` packages inside Hermes (or Hermes `plugin.yaml` packages inside Pi) is not thin. Pi plugins are TypeScript factories on `registerTool` / `on("context"|"agent_settled"|…)`. Hermes plugins are Python `register(ctx)` with `pre_llm_call`, `transform_tool_result`, and at most one `ContextEngine`. Those surfaces drift independently. Share **policy** (pack after 2 full sends, quote-verify, fusion queue) across two host ports. Do not invent a third plugin ABI.

## Why it matters for our harnesses

OMP is the exception: it already rewrites `@earendil-works/*` onto `legacy-pi-coding-agent-shim`, so `omp install github:NVlabs/SoL-Pi` is the adapter. Hermes Agent Plugins v1.0.0 is a compatibility layer for *Hermes-owned* portable components, not Pi extensions. Using `transform_tool_result` as ObservationPack would persist truncation; SoL-Pi does not. OCC needs `agent_settled`; Hermes has no such event. Leapfrog is `~/.hermes/plugins/sol-pi/` implementing the four mechanisms on Hermes hooks, not a TS import and not an origin PR.

## Related

- [[permanent/perm-20260911-sol-pi-is-pi-public-extension-not-core-patch]]
- [[permanent/perm-20260911-hermes-sol-pi-is-a-python-plugin-port]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- Hermes docs: plugins, hooks, context-engine plugin
- [[harnesses/hermes]] · [[harnesses/pi]]
