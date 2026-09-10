---
id: lit-20260910-kb-mesh-pair-keel
title: "Wire the KB as a DSN on host 0; PAIR routes inference; keel carries envelopes"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://github.com/NVIDIA/Personal-AI-Router", "https://github.com/kvnloo/hermes-keel", "https://github.com/kunchenguid/firstmate", "https://github.com/NousResearch/hermes-agent", "https://github.com/can1357/oh-my-pi"]
harnesses: [omp, hermes, firstmate]
domains: [frameworks, cs]
confidence: high
tags: [literature, mesh, pair, keel, kb]
---

# Wire the KB as a DSN on host 0; PAIR routes inference; keel carries envelopes

## Claim (one sentence)

The factory mesh already has three planes: NVIDIA PAIR (Personal AI Router) for local inference, hermes-mesh-keel for signed intents, and the harnesses (Firstmate / Hermes / OMP) as executors. The public-research KB is a fourth plane: Postgres CAS on host 0, reached by `FRONTIER_KB_DSN`. Do not merge those planes.

## Evidence

### PAIR

NVIDIA [Personal AI Router](https://github.com/NVIDIA/Personal-AI-Router) discovers nodes, manages Ollama/LM Studio, and exposes Ollama/OpenAI-compatible proxies. It does **not** store literature notes, has no Postgres/memory plugin in-tree, and does not pool GPU memory. Wire-up: point Hermes/OMP model endpoints at PAIR as today; give those same processes `FRONTIER_KB_DSN`. PAIR never sees note bodies.

### hermes-mesh-keel

Keel SQLite WAL is outbox/inbox, replay, receipts. It is not a 100-writer research ledger. HOLD: do not set `production_enabled` to attach a KB. After Keel admits a bounded action, the worker uses `kb_store.py put|get|search` with `KB_WRITER=hermes-0` (or omp/firstmate). Envelope log stays local.

### Harnesses

| Harness | How it uses the KB | What not to do |
| --- | --- | --- |
| Hermes | `FRONTIER_KB_DSN` in `~/.hermes/.env` (groot: `/workspace/hermes-home/.env`); skill `skills/frontier-kb` | Do not write the vault from 100 gateway agents |
| OMP | same DSN in process env; project skill in this repo | Do not treat obfuscation restore as storage |
| Firstmate | `FM_HOME` env + skill; secondmates inherit env, not a shared git index | Do not funnel through SQLite `inbox/<node>/` for hot writes |

Host 0: `scripts/install-host-0.sh` starts compose, ingest, user systemd unit, skill symlinks.

## Fact vs interpretation

- Fact: PAIR is an inference router. Keel is a signed-transport worker. This vault's store is Postgres.
- Interpretation: "Wire into the mesh" means one DSN on the tailnet + a skill, not a new protocol.

## Links

- PAIR: https://github.com/NVIDIA/Personal-AI-Router
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
