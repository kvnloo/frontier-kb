---
id: inbox-frontier-arxiv-memory-eval-cluster-2026-09-21
title: "arXiv Sep 18 — memory / eval / voice / coding-RL cluster"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [omp, hermes]
domains: [ai-ml, memory, eval, tool-use]
tags: [inbox, frontier, arxiv, memory, eval]
---

# arXiv memory/eval cluster (2026-09-18)

## Context

### FACT

| id | title | claim (paper) |
|---|---|---|
| [2609.21187](https://arxiv.org/abs/2609.21187) | When Better Turns Do Not Make Better Agents | SFT lifts gold-history next-turn metrics but **fails closed-loop tool workflows** (Dialpad) |
| [2609.22043](https://arxiv.org/abs/2609.22043) | MDL Memory Decision Layer | Zero-param post-retrieval trust/abstention; ~56% less conflict-hallucination; ~0.14 ms |
| [2609.21533](https://arxiv.org/abs/2609.21533) | MACE / MemGoG | Functional memory units + typed relations; co-evolution; 81.11% vs SAGE 78.97% |
| [2609.21940](https://arxiv.org/abs/2609.21940) | AutoViewMem | Self-configuring orthogonal memory views; beats Mem0/etc on LoCoMo/PersonaMem |
| [2609.22068](https://arxiv.org/abs/2609.22068) | CodeMidas | Mine codebases → verifiable coding RL envs; Terminal-Bench transfer |
| [2609.21967](https://arxiv.org/abs/2609.21967) | NemotronLabs VoiceChat | Open full-duplex S2S + native tool calling; arg grounding weak |
| [2609.21284](https://arxiv.org/abs/2609.21284) | Auth revocation / root-scoped quiescence | Formal revoke semantics for long-running delegated agents |
| [2609.22000](https://arxiv.org/abs/2609.22000) | RecreationWorld | Hybrid GUI+CLI computer-use; verifiable recreation tasks |
| [2609.22086](https://arxiv.org/abs/2609.22086) | Designer-RSI | Procedural NL skill memory from user traffic (230+ tools) |
| [2609.21423](https://arxiv.org/abs/2609.21423) | DENSE | Distill unlabeled trajectories into shortcut trees |
| [2609.21267](https://arxiv.org/abs/2609.21267) | Efficient Benchmarking in Production | Recurring prod-agent eval from 574 historical runs |

Sep 19–20 arXiv empty (weekend). Does not duplicate Sep 16 cluster ([[inbox/frontier/arxiv-agent-cluster-2026-09-16]]).

### INTERPRETATION
- **21187** changes ship gates: report text/tool/closed-loop separately.
- MDL abstention middleware + AutoViewMem/MACE = memory-plane research order for free-tier skim.
- Auth quiescence relevant to keel/Hermes long-running revoke — research only; **keel L0 hold**.

## Next action

Free-tier skim order: **21187 → 21940 → 22043 → 21533 → 22068**. Hold OMP-1..7 / hermes-keel L0. No Linear.

## Links

- Radar digest: `/workspace/frontier-lab-radar-2026-09-21.md`
