---
id: inbox-frontier-statecomp-when-to-compress-2026-09-24
title: "StateComp — learn when history is safe to compress (−52% tokens)"
type: inbox
status: draft
created: 2026-09-24
updated: 2026-09-24
node: frontier
harnesses: [hermes, omp, claude-code, pi]
domains: [ai-ml, frameworks, tokenomics, memory]
tags: [inbox, frontier, compaction, arxiv]
---

# StateComp — when-to-compress (KB footnote)

## Context

### FACT
- **arXiv 2609.27298 StateComp:** https://arxiv.org/abs/2609.27298 — KEEP/READY router on frozen-LM hiddens; WorkBuddyBench: **−52.27%** agent+summarization tokens at maintained performance; **12.67×** faster representation extraction.
- Secondary (same batch; one-liners only):
  - **DRSR 2609.27276** set-deletion risk — WorkBuddyBench Full260 reward **0.699→0.802**, tokens **−20.8%**; Eval40 **−35.9%** tokens. https://arxiv.org/abs/2609.27276
  - **GEM 2609.27332** evidence-preserving compress — Top-3 retention **0.31→0.69**; tokens **−21.4%**. https://arxiv.org/abs/2609.27332

### INTERPRETATION
- Compaction plane next to CliffCompaction (faithful truncate/drop) — state-conditioned **timing** of compress vs truncate/drop.
- Effort M; impact **H**; risk L–M. Relevant to Hermes compression watermark + OMP Mythos/Anthropic compact-2026-09-04.

## Next action

Skim StateComp router vs CliffCompaction (26779) catch-up in [[inbox/frontier/arxiv-agent-eval-cluster-2026-09-24]]. No Linear. No pin stamps (sleep HOLD).

## Links

- https://arxiv.org/abs/2609.27298
- https://arxiv.org/abs/2609.27276 · https://arxiv.org/abs/2609.27332
- Umbrella: [[inbox/frontier/kb-autoresearch-2026-09-24]]
- Related: [[inbox/frontier/twincheck-tool-verification-2026-09-24]]
