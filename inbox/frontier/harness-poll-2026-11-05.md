---
id: inbox-frontier-harness-poll-2026-11-05
title: "Harness release poll, 2026-11-05 (data/sources.yaml)"
type: inbox
status: draft
created: 2026-11-05
updated: 2026-11-05
node: frontier
harnesses: [hermes, omp, codex, claude-code, pi, fx, crush, opencode, o8, firstmate, prime-intelligence]
domains: [ai-ml, frameworks, tool-use]
tags: [inbox, frontier, poll, releases]
---

# Harness release poll, 2026-11-05

Polled every GitHub target in `data/sources.yaml` with `gh api repos/<repo>/releases` and `repos/<repo>` (read-only, public metadata). Latest release, last push and stars.

| harness | repo | latest release | last push | stars |
|---|---|---|---|---:|
| omp | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | v18.16.0 (2026-11-02) | 2026-11-05 | 37946 |
| hermes | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | v0.23.0 (2026-11-05) | 2026-11-05 | 260863 |
| grok | [xai-org/grok-build](https://github.com/xai-org/grok-build) | no releases | 2026-09-29 | 27698 |
| codex | [openai/codex](https://github.com/openai/codex) | rust-v0.168.0-alpha.7 (2026-11-05) | 2026-11-05 | 133345 |
| claude | [anthropics/claude-code](https://github.com/anthropics/claude-code) | v2.1.318 (2026-11-04) | 2026-11-05 | 154669 |
| pi | [earendil-works/pi](https://github.com/earendil-works/pi) | v1.5.0 (2026-11-02) | 2026-11-05 | 120300 |
| sol_pi | [NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) | no releases | 2026-11-05 | 3639 |
| sol_pi (fork) | [kvnloo/SoL-Pi](https://github.com/kvnloo/SoL-Pi) | no releases | 2026-10-04 | 0 |
| fx | [vercel-labs/fx](https://github.com/vercel-labs/fx) | v0.0.16 (2026-10-29) | 2026-11-05 | 3760 |
| crush | [charmbracelet/crush](https://github.com/charmbracelet/crush) | v0.100.0 (2026-11-05) | 2026-11-05 | 28968 |
| opencode | [anomalyco/opencode](https://github.com/anomalyco/opencode) | process-daemon-v0.5.0 (2026-11-05) | 2026-11-05 | 224795 |
| aider | [Aider-AI/aider](https://github.com/Aider-AI/aider) | v0.86.0 (2025-08-09) | 2026-05-22 | 49973 |
| continue | [continuedev/continue](https://github.com/continuedev/continue) | v2.1.0-vscode (2026-06-19) | 2026-11-05 | 36412 |
| firstmate | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | no releases | 2026-11-05 | 8610 |
| firstmate (fork) | [kvnloo/firstmate](https://github.com/kvnloo/firstmate) | no releases | 2026-11-05 | 0 |
| o8 | [hurttlocker/o8](https://github.com/hurttlocker/o8) | v0.1.815 (2026-10-31) | 2026-11-05 | 23 |
| aodl | [kvnloo/aodl](https://github.com/kvnloo/aodl) | no releases | 2026-11-05 | 1 |
| pi_autoresearch | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | v1.9.0 (2026-10-07) | 2026-10-07 | 8216 |
| prime_intelligence | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | v0.10.2 (2026-10-28) | 2026-11-05 | 22597 |
| mini_swe_agent | [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) | v2.4.6 (2026-07-23) | 2026-11-02 | 9112 |
| live_swe_agent | [OpenAutoCoder/live-swe-agent](https://github.com/OpenAutoCoder/live-swe-agent) | v1.0.0 (2025-11-17) | 2026-01-19 | 468 |
| opendev | [opendev-to/opendev](https://github.com/opendev-to/opendev) | v0.1.9 (2026-07-10) | 2026-08-08 | 852 |
| specforge | [sgl-project/SpecForge](https://github.com/sgl-project/SpecForge) | no releases | 2026-11-05 | 1266 |

## Notable since the last vault update (main 0bd2738, 2026-10-19)

- **Hermes v0.23.0 "The Hearth Release" (2026-11-05)**: Webapp serving the Desktop workspace from your own gateway; one gateway owns every conversation (CLI, TUI, Desktop, ACP, bots and cron no longer run separate agent copies); inline images in CLI/TUI; `/rewind` (Esc Esc) with edit, resend or fork; one Desktop window across many gateways; self-running Group Chats in Bot Mode. Since v0.22.0: ~1,950 merged PRs, 666 contributors. https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0
- OMP v18.16.0 (11-02), Pi v1.5.0 (11-02), Claude Code v2.1.318 (11-04), Crush v0.100.0 (11-05), Codex rust-v0.168.0 alphas (11-05).
- Grok Build has no GitHub releases and no push since 09-29; Aider has had no release since 2025-08.

## Vault state

Main last merged on 2026-10-19 (#25). Seven research PRs are still open (#21, #23, #26, #29, #30, #33, #37). Merging them is a public-repo write, so it needs the owner.
