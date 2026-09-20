---
id: harness-nano-rlm
title: nano-rlm
type: harness
status: active
created: 2026-09-20
updated: 2026-09-20
urls:
  - https://github.com/PrimeIntellect-ai/nano-rlm
capabilities:
  - ACP-only coding agent runtime
  - Persistent IPython execution environment
  - Recursive supervisor-owned subagents
  - Supervisor-owned shell jobs, inboxes, watches, and lifecycle budgets
  - Context compaction with persistent execution state
confidence: high
tags: [harness, nano-rlm, rlm, acp, ipython]
---

# nano-rlm

[PrimeIntellect-ai/nano-rlm](https://github.com/PrimeIntellect-ai/nano-rlm) is a minimal coding agent built around a persistent IPython environment and optional recursive subagents.

## Snapshot

The default model-facing execution surface is intentionally unusual: one persistent `ipython` tool can reach Python, Bash through `rlm.shell.run`, file work, and orchestration. Native `bash`, `edit`, `fetch`, and `ipython` tool sets can also be selected by the runtime contract.

The harness runs as an Agent Client Protocol agent. Each ACP session owns one persistent RLM engine, and the caller supplies a complete versioned runtime contract rather than relying on ambient process configuration.

## State and ownership

nano-rlm makes ownership explicit:

- the supervisor owns agent identity, task, runtime, lifetime, budgets, and direct-child control
- Python variables hold handles, but losing a variable does not terminate supervisor-owned work
- persistent children can remain idle with their conversation and kernel
- shell jobs survive cell completion and lost handles
- inboxes and watches are supervisor-owned
- closing the ACP session tears down the tree

This is a useful contrast to mini-swe-agent's deliberately stateless subprocess model.

## Compaction model

Compaction replaces model-visible conversational context while keeping the IPython kernel alive. This means “context state” and “execution state” are separate resources.

The session ledger records messages and context windows so omitted details remain addressable after compaction. This is a concrete example of preserving computational state while reducing model context.

## Recovery model

Kernel death does not imply supervisor death. The harness can restart IPython under the same agent identity while preserving conversation, children, shell jobs, and inbox state. Python variables and in-kernel tasks are lost, and interrupted cells are not replayed automatically.

That separation creates strong invariants around idempotency and resource discovery after partial failure.

## Contribution contract

There is no separate `CONTRIBUTING.md` on the current default branch. `AGENTS.md` is the operative local contract:

- use `uv run`, not raw Python
- dependencies go through `pyproject.toml` + `uv sync`
- run `uv run pytest tests/`
- prefer plain-function tests and add tests conservatively
- keep exception handling minimal so failures are visible
- comments describe current constraints, not historical implementation narratives
- branches use `feat/`, `fix/`, `chore/`, `docs/`, or `tests/`
- PRs are opened as drafts
- PR titles use the matching conventional prefix

## Maintainer signals

Recent merged architecture work is large in capability but sliced by ownership boundary: supervisor-owned handles, then messaging/inboxes, then Bash jobs, then kernel recovery. The important pattern is that each PR states what it owns and what remains explicitly out of scope.

Validation is correspondingly concrete: focused tests, real kernels/processes, and when appropriate live protocol/Verifiers checks. This is a good model for deep changes without monolithic PRs.

## Cross-harness lens

nano-rlm is the strongest stateful-harness comparison target in this set.

Study it against mini-swe-agent on:

- persistent vs stateless execution
- supervisor ownership vs process-local ownership
- context compaction vs linear history
- asynchronous children/jobs vs one-step action loops
- recovery after partial failure
- training/provenance semantics for recursive execution

For our own architecture, copy the invariants only when we also need the underlying statefulness. Do not import supervisor complexity merely because it is sophisticated.

## Sources

- https://github.com/PrimeIntellect-ai/nano-rlm
- https://github.com/PrimeIntellect-ai/nano-rlm/blob/main/README.md
- https://github.com/PrimeIntellect-ai/nano-rlm/blob/main/AGENTS.md
- [[inbox/oss-harness-contribution-policy-radar-20260920]]
