---
id: perm-20260910-scaffold-tool-shape-dominates
title: "Edit-tool shape can move 27B scores by ~20 points"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, opencode]
domains: [tool-use, frameworks]
confidence: high
tags: [permanent, scaffold, str-replace]
---

# Edit-tool shape can move 27B scores by ~20 points

## Idea (atomic)

On Qwen3.6-27B SWE-bench Pro, holding checkpoint and mini-swe-agent fixed, bash-only edits sat ~27–37% pass@1; SWE-agent `str_replace_editor` reached ~49–51% (CI includes the 53.5 card). Qwen-code `edit`/`write_file` matched bash (McNemar p=1.00). For small models, the editor ABI is a first-class eval variable, not a detail.

## Why it matters for our harnesses

Before we SFT a 27B "orchestrator," audit OMP/Hermes file-edit tools against `str_replace` semantics. A bash-only inner loop will understate any local Qwen. When comparing to SWE-2, also name the harness (Devin CLI vs Terminus vs Claude Code vs mini-swe-agent); mixing them is how 10-point ghosts appear.

## Related

- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[harnesses/omp]]
- [[harnesses/hermes]]
