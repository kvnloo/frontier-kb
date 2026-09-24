---
id: inbox-frontier-arxiv-agent-eval-cluster-2026-09-24
title: "arXiv agent/eval cluster — Sep 22–24 secondary + catch-up"
type: inbox
status: draft
created: 2026-09-24
updated: 2026-09-24
node: frontier
harnesses: [hermes, omp, claude-code]
domains: [ai-ml, eval, frameworks, tool-use]
tags: [inbox, frontier, arxiv, eval]
---

# arXiv agent/eval cluster (thin)

## Context

### FACT — Sep 22–23 catch-up (not yet in vault inbox; prior cadence stopped 09-17 on main)

| id | title | 1-line FACT |
|---|---|---|
| [2609.26760](https://arxiv.org/abs/2609.26760) | Growing Harness | compile control→code; −76–92% LLM calls vs tool-calling |
| [2609.26779](https://arxiv.org/abs/2609.26779) | CliffCompaction | truncate/drop only, never rephrase; ~50% cost; +10pp Terminal TTS |
| [2609.26761](https://arxiv.org/abs/2609.26761) | A2M | MCP metadata hijack; 93.6% malicious invoke / 32.4× Cognitive DoS |
| [2609.26777](https://arxiv.org/abs/2609.26777) | SWE-Serve | serving E2E rejects ~1/3 local-green patches |

### FACT — Sep 24 secondary / thin primaries

| id | title | 1-line FACT |
|---|---|---|
| [2609.28416](https://arxiv.org/abs/2609.28416) | AEWM | edit task-state; EditAct +3.2–6.7 avg |
| [2609.28449](https://arxiv.org/abs/2609.28449) | SWE-Flux | runtime reasoning; best model **37%** |
| [2609.27532](https://arxiv.org/abs/2609.27532) | ProCredit | turn-attributed progress credit; +4.1pp @4B |
| [2609.27571](https://arxiv.org/abs/2609.27571) | FDE-Bench | deploy/IaC agents; readiness = largest fail stage |
| [2609.27276](https://arxiv.org/abs/2609.27276) | DRSR | set-deletion risk; −20.8% tokens |
| [2609.27332](https://arxiv.org/abs/2609.27332) | GEM | evidence-preserving compress; Top-3 0.31→0.69 |

Primaries elevated elsewhere: JAZ 26891 · SkillGym 27717 · StateComp 27298 · TwinCheck 26911.

### INTERPRETATION
- Catch-up Growing/Cliff pair with JAZ/StateComp this tick; A2M pairs TwinCheck; SWE-Serve/SWE-Flux/FDE are eval substrates not product pins.
- Elevate Growing Harness + CliffCompaction to focused notes next cadence if still unmerged elsewhere.

## Next action

Free-tier skim order after primaries: **26760 → 26779 → 26761**. No Linear.

## Links

- Umbrella: [[inbox/frontier/kb-autoresearch-2026-09-24]]
- Primaries: [[inbox/frontier/jaz-harness-as-language-2026-09-24]], [[inbox/frontier/statecomp-when-to-compress-2026-09-24]], [[inbox/frontier/twincheck-tool-verification-2026-09-24]]
