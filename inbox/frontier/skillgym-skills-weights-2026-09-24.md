---
id: inbox-frontier-skillgym-skills-weights-2026-09-24
title: "SkillGym — skills into weights (+19.1pp Terminal-Bench 2.1)"
type: inbox
status: draft
created: 2026-09-24
updated: 2026-09-24
node: frontier
harnesses: [claude-code, hermes, omp]
domains: [ai-ml, frameworks, eval, tool-use]
tags: [inbox, frontier, skills, training, arxiv]
---

# SkillGym — skills→weights (KB footnote)

## Context

### FACT
- **arXiv 2609.27717:** https://arxiv.org/abs/2609.27717 — Skill→task pipeline + code checkers; **2,756** envs / **8,364** trajectories (avg **49** tool calls, **>60k** tokens).
- Under Claude Code, SFT on Qwen3.5-35B-A3B: **+199 Elo** GDPval-AA v2; **+19.10pp** Terminal-Bench 2.1; **+28.13 / +12.38pp** SkillsBench v1.1 w/ & w/o skills.
- SkillGym-Agent 35B **51.47%** skill-assisted SkillsBench — beats reported Sonnet 4.6 / GPT-5.4 Mini / DeepSeek V4 Pro.

### INTERPRETATION
- Skills-as-weights leapfrog for Hermes Desktop skills / Claude Code SKILL.md plane — train on verified harness trajectories, don’t only inject markdown.
- Effort M–H; impact **H**; risk M (data/harness licensing). Pairs with SEP-2640 Skills-over-MCP transport.

## Next action

Free-tier skim method + licensing posture. Cross-link SEP-2640 in [[inbox/frontier/harness-release-cluster-2026-09-24]]. No Linear.

## Links

- https://arxiv.org/abs/2609.27717
- https://modelcontextprotocol.io/extensions/skills/overview
- Umbrella: [[inbox/frontier/kb-autoresearch-2026-09-24]]
- Related: [[inbox/frontier/jaz-harness-as-language-2026-09-24]]
