---
id: inbox-frontier-jaz-harness-as-language-2026-09-24
title: "JAZ / Harness-as-Language — minimal invoke (arXiv 2609.26891)"
type: inbox
status: draft
created: 2026-09-24
updated: 2026-09-24
node: frontier
harnesses: [hermes, omp, claude-code]
domains: [ai-ml, frameworks, tool-use, memory, tokenomics]
tags: [inbox, frontier, harness, jaz, arxiv]
---

# JAZ — Harness as a Language (KB footnote)

## Context

### FACT
- **arXiv 2609.26891** (Omar Khattab et al.; Sep 22 ~18:00Z catch-up vs 09-23 cutoff): https://arxiv.org/abs/2609.26891
- Minimalist harness = single LLM primitive **`invoke`**. LLM writes arbitrary executable code incl. recursive `invoke`; all inputs + interaction history are code-env variables. **No** hand-built tools/memory/FS.
- Recall beyond context: **+8%** vs Letta/MemGPT at **½ cost** (StuLife recall-heavy). Continual self-improvement: **+4%** vs ACE at lower cost (AppWorld).

### INTERPRETATION
- Direct “minimal harness = language” companion to Growing Harness / Harness-Zero — code-mode loop may obsolete bolted-on memory/RSI scaffolds.
- Highest-ROI free-tier skim #1 this window for Hermes/OMP research lanes. Effort M; impact **H**; risk M (needs replicated evals).

## Next action

Free-tier skim abstract+method vs Growing Harness (26760). Do **not** Linear. Pair with [[inbox/frontier/arxiv-agent-eval-cluster-2026-09-24]] catch-up row.

## Links

- https://arxiv.org/abs/2609.26891
- Umbrella: [[inbox/frontier/kb-autoresearch-2026-09-24]]
- Related cluster: [[inbox/frontier/skillgym-skills-weights-2026-09-24]], [[inbox/frontier/statecomp-when-to-compress-2026-09-24]]
