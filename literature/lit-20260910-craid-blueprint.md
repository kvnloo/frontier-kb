---
id: lit-20260910-craid-blueprint
title: "C(RAID) from kvnloo/blueprint (CR/CA/CI/CD)"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://github.com/kvnloo/blueprint", "https://github.com/kvnloo/evolve", "https://github.com/kvnloo/aodl/blob/main/spec/craid.md"]
harnesses: [hermes, omp, grok, codex]
domains: [frameworks]
confidence: high
tags: [literature, craid, blueprint, aodl]
---

# C(RAID) from kvnloo/blueprint (CR/CA/CI/CD)

## Claim (one sentence)

C(RAID) is Continuous Research, Analysis, Integration, Deployment — Blueprint's CR/CA/CI/CD loop — and it compiles to HOTL 0.2 as a **named hybrid**, not as a new topology kind.

## Evidence

- [kvnloo/blueprint](https://github.com/kvnloo/blueprint) `claudedocs/03-vision/CR-CA-CI-CD.md` and website `Pipeline.tsx`: R→A→I→D with a feedback loop, three tracks (health, world sim / digital twin, Evolve orchestration).
- Evolve ([kvnloo/evolve](https://github.com/kvnloo/evolve)) was the Claude Flow orchestration track. Distilled into AODL; not a second IR.
- AODL fixture: `examples/valid/craid.json`. Feedback as `dependency` fails: `examples/invalid/craid-feedback-cycle.json`.

## Fact vs interpretation

- Fact: Blueprint names C(RAID) / CR/CA/CI/CD as the shared methodology across tracks.
- Fact: HOTL 0.2 already has sequence, fanout, reducer, human_gate, observation, memory.
- Interpretation: Autonomous product management is C(RAID) over a backlog. Solarpunk is the digital twin of that graph, not the language.
- HOLD: unlabeled `hybrid` remains `not-inferred`. Do not infer swarm from Evolve/Claude Flow.

## Links

- Protocol: [spec/craid.md](https://github.com/kvnloo/aodl/blob/main/spec/craid.md)
- Goal repo: https://github.com/kvnloo/blueprint
- Legacy: https://github.com/kvnloo/evolve
