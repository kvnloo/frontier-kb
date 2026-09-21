---
id: inbox-frontier-kb-autoresearch-2026-09-21
title: "KB autoresearch cadence — 2026-09-21"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [omp, hermes, grok, codex, claude-code, pi, prime-intelligence, o8, firstmate]
domains: [ai-ml, frameworks, tokenomics, tool-use, eval, memory]
tags: [inbox, frontier, kb-autoresearch]
---

# KB autoresearch — 2026-09-21

## Context

Mon cadence after PR #18 (2026-09-17). Window: after 2026-09-17 KB → 2026-09-21. Net-new from lab/harness/depth digests (not full issue dumps):

| plane | signal | primary |
|---|---|---|
| gateway / auto-mode | Claude **2.1.278** server classifier + safeguards pass-through | https://code.claude.com/docs/en/auto-mode-classifier-billing |
| Claude DX | **2.1.277** AGENTS.md modes + proxy-only egress / `headers:` | https://github.com/anthropics/claude-code/releases/tag/v2.1.277 |
| OMP cache | **v18.2.6** #12431 cache-head anchors last stable system (~45k head save) | https://github.com/can1357/oh-my-pi/releases/tag/v18.2.6 |
| OMP judgment | **v18.2.7** find + judge_batch/jevify; JudgmentHandle/`wait()` **removed** | https://github.com/can1357/oh-my-pi/releases/tag/v18.2.7 |
| Codex α | LocalAgentMessageBoard + ToolPolicy (feature OFF; watch GA) | openai/codex rust-v0.156.0-alpha.* |
| pi cache | **0.86** cost-gated warming (`off\|streaming\|idle`, $0.05, 90% lifetime) | https://github.com/earendil-works/pi/releases/tag/v0.86.0 |
| oversight | Anthropic×Accenture embedded evaluation (Sep 18) | https://www.anthropic.com/news/accenture-embedded-evaluation |
| voice / STT | xAI Voice Transcribe **2.0** (~2× accuracy, same price) | https://x.ai/news/grok-voice-transcribe-2 |
| literature | arXiv memory/eval/voice cluster (21187, MDL, MACE, AutoViewMem, …) | 2609.21187 et al. |
| peers (thin) | o8 Brain fail-closed; Firstmate AFK; Prime keep-newest/keep-tail; Crush 0.96 Themes | pulse/depth digests |

Hold: **OMP-1..7**, **hermes-keel L0**, no Linear mint/Done, `github_writes=0` on upstream OSS.

Quiet / already covered in 09-17 notes: Grok Build Memory, Cognition Fusion, Agents API, misalignment framework, OMP judgment baseline through 18.2.4.

## Next action

CoS: merge PR; pin Claude fleets ≥2.1.278; free-tier skim arXiv 21187→21940→22043→21533; steal pi warmer + OMP #12431 into Hermes research only. Watch Codex message board for GA before Linear. Hold OMP-1..7 + keel L0.

## Links

- Focused: [[inbox/frontier/claude-server-classifier-2026-09-21]], [[inbox/frontier/omp-cache-judgment-2026-09-21]], [[inbox/frontier/codex-message-board-2026-09-21]], [[inbox/frontier/pi-cache-warming-2026-09-21]], [[inbox/frontier/anthropic-accenture-eval-2026-09-21]], [[inbox/frontier/xai-voice-transcribe-2-2026-09-21]], [[inbox/frontier/arxiv-memory-eval-cluster-2026-09-21]]
- Sibling digests (box): frontier-lab-radar / multi-harness-pulse / competitor-depth-dx / hermes-repo-intelligence 2026-09-21
