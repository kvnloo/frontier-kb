---
id: harness-mini-swe-agent
title: mini-swe-agent
type: harness
status: active
created: 2026-09-20
updated: 2026-09-20
urls:
  - https://github.com/SWE-agent/mini-swe-agent
capabilities:
  - Minimal bash-only software-engineering agent
  - Linear model history
  - Stateless per-action subprocess execution
  - Local, container, Singularity, bubblewrap, and remote environments
confidence: high
tags: [harness, mini-swe-agent, swe-bench, minimal]
---

# mini-swe-agent

[mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) is a deliberately minimal software-engineering agent from the SWE-agent/SWE-bench ecosystem.

## Snapshot

Its research value comes from what it refuses to add:

- the model can solve tasks with Bash rather than a large bespoke tool surface
- conversation history remains linear
- actions use independent subprocess execution rather than a persistent shell session
- environment implementations swap execution substrates without changing the core agent idea

This makes it a strong control when evaluating whether richer harness machinery actually earns its complexity.

## Contribution contract

The project explicitly welcomes documentation/examples, model support, environment/deployment support, and work on labeled issues.

Design guidance:

- keep the project minimal, hackable, and high-quality
- prefer a new version of one of the core components instead of making an existing component increasingly configurable/complex
- place shared utilities in a small utils boundary when behavior is genuinely common
- keep generated/model-written code and tests concise
- run pre-commit and `pytest -n auto`

## Current high-value signal: submission protocol

Issue #938 shows that a valid benchmark submission can be silently discarded when shell startup output appears before the sentinel line. The run then continues to its step limit and is scored like an empty-patch model failure.

PR #939 repairs Docker by scanning output for the exact sentinel rather than requiring it on line zero.

The deeper class-of-bug is duplicated protocol ownership. The same `_check_finished` sentinel parser appears in at least seven environment implementations:

- local
- docker
- singularity
- contree
- bubblewrap
- swerex_modal
- swerex_docker

The control-flow docs encode the same line-zero assumption.

A useful follow-up is not another Docker patch. It is one small shared pure submission-parser helper with a parameterized regression suite so all environments implement one termination protocol.

A framed/out-of-band sentinel could reduce false positives further, but that is a larger protocol change and should be separate from the current benchmark-correctness repair.

## Current high-value signal: cost accounting

Issue #935 / PR #936 addresses Portkey responses with missing or zero `usage.total_tokens`, which can otherwise crash or derive a negative prompt count. An existing contributor already has a narrow fix and independent validation, so the productive action is review rather than duplication.

## Cross-harness lens

Compare mini-swe-agent directly against nano-rlm:

- stateless subprocess vs persistent kernel
- linear transcript vs compacted/addressable history
- no supervisor-owned resource graph vs explicit child/job ownership
- simple environment substitution vs richer runtime contracts

The question is not which is more advanced; it is which invariants each architecture makes cheap.

## Sources

- https://github.com/SWE-agent/mini-swe-agent
- https://github.com/SWE-agent/mini-swe-agent/blob/main/docs/contributing.md
- https://github.com/SWE-agent/mini-swe-agent/issues/938
- https://github.com/SWE-agent/mini-swe-agent/pull/939
- https://github.com/SWE-agent/mini-swe-agent/issues/935
- https://github.com/SWE-agent/mini-swe-agent/pull/936
