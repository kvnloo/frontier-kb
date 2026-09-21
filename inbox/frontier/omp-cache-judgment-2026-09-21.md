---
id: inbox-frontier-omp-cache-judgment-2026-09-21
title: "OMP v18.2.6/7 — cache-head anchor + JudgmentHandle break"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [omp]
domains: [ai-ml, frameworks, tokenomics, tool-use]
tags: [inbox, frontier, omp, cache, judgment]
---

# OMP cache-head + judgment migration (KB footnote)

## Context

### FACT
- **v18.2.6 / #12431:** Anthropic prompt-cache breakpoint anchors on **last stable system segment**; stable-system fingerprint **ignores recall**. Previously restart→recall refreshed systemPrompt bytes → full ~45k tools+system head re-bill; now **suffix only**.
- **v18.2.7:** semantic `find` tool + CLI; `judge_batch` / `jevify` bounded fan-out + **reattach across turns**; live TypeSafe judge-model discovery; Handlebars `SYSTEM_TEMPLATE.md` with conflict rules vs full `systemPrompt`; Glyph Protocol; Anthropic imports → `@oh-my-pi/pi-ai/providers/anthropic`.
- **Breaking:** `JudgmentHandle` + judgment-in-`wait()` **removed**; `judge()` awaited; bash `env` removed.

### INTERPRETATION
- Strongest OMP cost-hygiene + typed bulk-eval deepen since 18.2.4 judgment wave. Does **not** reopen OMP-1..7 — migration note only.
- Hermes steal candidates: #12431 cache-head anchor; find-over-grep priority; judge_batch reattach pattern.

## Next action

Hold **OMP-1..7**. Productize judgment/find on free-tier research path only. Note JudgmentHandle + Anthropic import break for any consumer.

## Links

- https://github.com/can1357/oh-my-pi/releases/tag/v18.2.6
- https://github.com/can1357/oh-my-pi/releases/tag/v18.2.7
- Sibling baseline: [[inbox/frontier/omp-judgment-plane-2026-09-17]]
