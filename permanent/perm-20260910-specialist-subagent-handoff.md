---
id: perm-20260910-specialist-subagent-handoff
title: "Specialist subagents need a typed hand-off, not a summary"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp, hermes, cursor, claude, devin]
domains: [tool-use, skills, ai-ml]
confidence: high
tags: [permanent, subagent, retrieval, swe-grep]
---

# Specialist subagents need a typed hand-off, not a summary

## Idea (atomic)

The portable Cognition pattern is not "a small model orchestrates." It is: a fast specialist with a **verifiable output type** (SWE-grep: file + line ranges; F-β precision-heavy) that the main agent consumes without inheriting the specialist's junk tokens. Summaries from a weak model poison a strong one. RL works here because the reward is deterministic.

## Why it matters for our harnesses

If we add a Qwen/Nemotron "guide" in front of OMP or Hermes, the interface must be structured (paths, ranges, plan DAG, failing tests) — not prose. Retrieval is the proven first slot. Compact and critique are the OpenDev slots that already exist as a design. Do not start with a free-form orchestrator.

## Related

- [[literature/lit-20260910-swe-grep]]
- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
