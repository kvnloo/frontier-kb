---
id: harness-crush
title: Crush
type: harness
status: active
created: 2026-09-10
updated: 2026-09-20
urls:
  - https://github.com/charmbracelet/crush
capabilities:
  - Terminal coding agent built in Go
  - Multi-provider model abstraction through Fantasy
  - LSP, MCP, skills, hooks, permissions, and background shell jobs
  - SQLite-backed sessions and cross-component pub/sub
confidence: high
tags: [harness, crush, go, charm]
---

# Crush

[Charmbracelet Crush](https://github.com/charmbracelet/crush) is a terminal-first Go coding agent whose current root `AGENTS.md` exposes a detailed architectural map.

## Snapshot

The top-level wiring lives in `internal/app`. Major ownership boundaries include:

- `internal/agent`: session agent, coordinator, prompts, tools, MCP
- `internal/hooks`: independent pre-tool hook engine
- `internal/session` + `internal/db`: SQLite-backed persistence
- `internal/lsp`: code-intelligence lifecycle
- `internal/ui`: Bubble Tea TUI
- `internal/permission`: tool permission policy
- `internal/shell`: command execution and background-job support
- `internal/pubsub`: cross-component messaging

Provider protocol differences are delegated to Charm's `fantasy` abstraction rather than spread across the agent loop.

## Architectural patterns

**Config is a service.** Runtime consumers use `config.Service` instead of global config state.

**Hooks are separate from agent logic.** The hook engine runs shell commands and returns decisions; a decorator wraps tools at the coordinator boundary.

**Persistence is explicit.** SQLite + sqlc owns durable sessions rather than hidden in-memory product state.

**Background execution is first-class.** This is a useful comparison point with nano-rlm's supervisor-owned jobs because lifecycle ownership and cancellation become visible design questions.

## Contribution contract

Charm uses an organization-wide contribution policy:

- bug fixes need clear before/after reproduction, preferably tests
- new features should begin in a GitHub Discussion before a PR
- refactors must explain why they improve the project
- PRs should be marked ready only when complete, with tests/examples/CI passing
- conventional commits are expected
- contributors must have rights to contributed content

Crush adds repository-specific development rules through `AGENTS.md`: Go formatting, explicit errors, context-first APIs, small consuming-package interfaces, parallel tests, mock providers for provider tests, and semantic commits.

## Current high-value signals

Issue #3840 reports a request timeout causing an infinite `errors.Is` traversal and a pegged CPU core. The trace points to a cyclic error chain around `requestTimeoutError`.

PR #3852 already proposes the right narrow fix: before storing a provider wrapper as `timeoutErr.cause`, detect whether that wrapper already unwraps to `timeoutErr`; if so, terminate the chain at `context.DeadlineExceeded`. It adds a regression that proves `errors.Is` terminates.

This is a review/support target, not a duplicate-patch target.

Issue #3878 raises a different lifecycle invariant: an automatically backgrounded process can outlive cancellation because ownership moves from the original tool context to a detached background manager. That is structurally similar to supervisor-owned-job questions in nano-rlm and Continue.

Issue #3867 reports task-objective drift during context compaction: a later follow-up prompt can be mislabeled as the original request after summarization. This is a useful context-state invariant to compare against Pi/OMP/nano-rlm.

## Cross-harness lens

Crush is valuable for studying how a feature-rich terminal harness keeps services separated while sharing a rich TUI and persistent state.

Watch especially:

- cancellation ownership before and after background handoff
- context compaction and preservation of root task intent
- permission ordering relative to hooks and external effects
- provider retry/timeout error chains
- LSP startup and cleanup costs

## Sources

- https://github.com/charmbracelet/crush
- https://github.com/charmbracelet/crush/blob/main/AGENTS.md
- https://github.com/charmbracelet/.github/blob/main/CONTRIBUTING.md
- https://github.com/charmbracelet/crush/issues/3840
- https://github.com/charmbracelet/crush/pull/3852
- [[inbox/oss-harness-candidate-wave-1-20260920]]
