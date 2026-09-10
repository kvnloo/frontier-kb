---
id: lit-20260910-gsme-self-evolving-harness
title: "GSME: stronger evolver patches a frozen 27B; TB2 +9.3 sealed"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://arxiv.org/abs/2607.13683", "https://arxiv.org/html/2607.13683v1"]
harnesses: [omp, hermes, claude]
domains: [ai-ml, frameworks]
confidence: high
tags: [literature, gsme, terminal-bench, harness-evolution]
---

# GSME: stronger evolver patches a frozen 27B; TB2 +9.3 sealed

## Claim (one sentence)

Pair a frozen task model with a stronger evolver that only *proposes* harness patches; deterministic code owns credit. On qwen3.6-27B that loop credits +9.3 pp on Terminal-Bench 2 sealed test (36.1 → 45.4).

## Evidence

Luo, Wang, Hu, Xue, Deng, arXiv:2607.13683 (2026). Frozen \(M\); evolver \(D\) (Claude Opus 4.8 via Claude Code) diagnoses (where × why) pathologies and writes env-gated patches. GSME archive keyed on pathology, not task. Three gates: validity, activation (patch actually fired), paired \(2\sigma\). Test sealed until the end.

Credited sealed lifts (qwen3.6-27B): TB2 **+9.3**, LiveCode +13.7, Omni-MATH +11.7, BrowseComp+ +13.9, GDPval +9.2, AppWorld +15.5. Retention 86–147% of train lift. SWE-bench +5.1 on n=26 is *not* credited (\(z=0.78\)).

Pathology→patch is model-specific: 27B engagement → verify-finalize; 397B and Gemini 3 Flash careless → submit-verify checklist. The loop transfers; the harness does not.

Vendor qwen3.6-27B TB2.0 card is 59.3 on Harbor/Terminus-2. Their vanilla is a *minimal* harness (~36%), so the +9.3 is lift over that baseline, not vs SWE-2's 92.8 in Devin.

## Fact vs interpretation

- Fact: this is the cleanest 2026 result that a small frozen worker plus a stronger harness-evolver moves Terminal-Bench 2.
- Fact: the evolver here is Opus, not Qwen3.8-27B.
- Interpretation: do not SFT a 27B to "orchestrate OMP." Run an evolver against *our* failure traces with gated credit. Qwen3.8-27B can be the frozen worker; it is not shown as the evolver.

## Links

- Paper: https://arxiv.org/html/2607.13683v1
- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
