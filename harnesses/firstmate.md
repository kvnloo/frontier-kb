---
id: harness-firstmate
title: firstmate
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls: ["https://github.com/kunchenguid/firstmate"]
tags: [harness]
---

# firstmate

Captain/crew orchestrator. Fleet state lives in `FM_HOME` (not this vault). Public-research writes go to `FRONTIER_KB_DSN` on host 0 with `KB_WRITER=firstmate-<host>`. Secondmates inherit the DSN; they do not share a git working tree.

Skill: `skills/frontier-kb`. See [[literature/lit-20260910-kb-mesh-pair-keel]].
