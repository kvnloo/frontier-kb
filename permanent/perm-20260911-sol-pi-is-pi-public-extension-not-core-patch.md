---
id: perm-20260911-sol-pi-is-pi-public-extension-not-core-patch
title: "SoL-Pi is a Pi ExtensionAPI package, not a Pi/OMP/Hermes core patch"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [pi, omp, hermes]
domains: [frameworks]
confidence: high
tags: [permanent, sol-pi, plugins]
---

# SoL-Pi is a Pi ExtensionAPI package, not a Pi/OMP/Hermes core patch

## Idea (atomic)

SoL-Pi's load-bearing contract is Pi's public extension surface (`registerTool`, `on("session_start"|"context"|"tool_result"|…)`, `getAgentDir`/`CONFIG_DIR_NAME`, `SessionManager.getSessionDir()`, `compact()`). NVIDIA forbids vendoring or patching Pi. Leapfrog is therefore: load or reimplement the four mechanisms *outside* harness cores.

## Why it matters for our harnesses

Do not open origin PRs that bake Action Fusion into OMP's edit tool or Hermes `write_file`. OMP already loads third-party `pi.extensions`. Hermes already has general plugins + one context engine. That is the integration shape. Contrasts [[permanent/perm-20260910-no-universal-harness-plugin]]: mini-SWE-agent *is* a harness; SoL-Pi *is* a plugin — but only for hosts that speak Pi's ExtensionAPI.

## Related

- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[permanent/perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi]]
- [[harnesses/pi]]
