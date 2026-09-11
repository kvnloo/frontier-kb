---
id: inbox-sol-pi-wave-20260911
title: "SoL-Pi ingest + OMP/Hermes integration plan (2026-09-11)"
type: inbox
status: draft
created: 2026-09-11
updated: 2026-09-11
node: cursor
harnesses: [pi, omp, hermes]
domains: [frameworks, tokenomics, tool-use]
tags: [inbox, sol-pi, nvidia]
---

# SoL-Pi wave

User ask 2026-09-11: clone https://github.com/NVlabs/SoL-Pi and figure out how to integrate it into oh-my-pi and Hermes; store research in frontier-kb.

Checkout: `/tmp/SoL-Pi` @ `22277b7e` (NVlabs/SoL-Pi). Fork already exists at `kvnloo/SoL-Pi`. Vault merge is this wave. Public OSS only — no Hermes personal memory.

Processed:

- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260911-sol-pi-is-pi-public-extension-not-core-patch]]
- [[permanent/perm-20260911-omp-can-load-sol-pi-via-legacy-shim]]
- [[permanent/perm-20260911-hermes-sol-pi-is-a-python-plugin-port]]
- [[permanent/perm-20260911-observationpack-is-projection-not-history-rewrite]]
- [[permanent/perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi]]
- [[harnesses/pi]] stub → active
- [[harnesses/omp]] / [[harnesses/hermes]] SoL-Pi sections

## Next action

1. CoS: HITL merge this vault wave (schema CI). Postgres ingest on host 0 after merge (`FRONTIER_KB_DSN` was not available in this VM).
2. OMP: stock SoL-Pi entry fails on OMP 18.1.17 (`findCutPoint` missing from the legacy shim). Phase 0 is a wrapper that imports Action Fusion + ObservationPack only. Discord-first if a core change is needed; do not origin-write until Todo.
3. Hermes: standalone Python plugin on Hermes hooks, not a TS/Pi ABI adapter. Do not vendor into `hermes-agent`.
4. Do **not** reopen secret-portal / Cursor-cloud factory cards. Dedup vs [[permanent/perm-20260910-no-universal-harness-plugin]]: SoL-Pi is the Pi-API exception, not a universal scaffold.

## Links

- https://github.com/NVlabs/SoL-Pi
- https://nvlabs.github.io/SoL-Pi/
- https://github.com/can1357/oh-my-pi/blob/main/docs/extension-loading.md
- https://hermes-agent.nousresearch.com/docs/developer-guide/plugins
- Linear [PER-1402](https://linear.app/0ism/issue/PER-1402/hitl-frontier-kb-pr-sol-pi-omphermes-integration-research)
