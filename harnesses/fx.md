---
id: harness-fx
title: fx
type: harness
status: active
created: 2026-09-10
updated: 2026-09-20
urls: ["https://github.com/vercel-labs/fx"]
capabilities:
  - CLI-first Zig coding agent
  - Typed core contracts for sessions, permissions, MCP, skills, runtime
  - Built-in tools plus terminal UI and AI Gateway transport
  - Persistent sessions and bounded subagent children
  - Deterministic startup, runtime, capacity, and PGSO performance benchmarks
confidence: high
tags: [harness, fx, zig, mcp, autoresearch, performance]
---

# fx

[vercel-labs/fx](https://github.com/vercel-labs/fx) is a CLI-first coding agent written in Zig. Canonical id `fx` in the [AODL harness catalog](https://github.com/kvnloo/aodl/blob/main/harnesses/catalog.json).

## Snapshot

The repository makes its architecture unusually explicit:

- `src/main.zig` is a composition root only.
- `src/core/` owns contracts, runtimes, config, sessions, permissions, MCP, and skills.
- `src/tools/` owns built-in tool implementations.
- `src/ui/` owns terminal rendering, event loop, input, and transcript.
- `src/gateway/` owns AI Gateway transport.

The contribution guide treats module ownership, typed contracts, persistence, text/JSON output, docs/tests, and deterministic E2E ownership as questions that should be answered before implementing a feature.

## State and ownership

Runtime state lives under `~/.fx/`. Sessions are portable across workspaces and track their current workspace root. Subagents are ordinary internal sessions with separate history plus a bounded parent-owned registry.

Project configuration is deliberately constrained to repo-safe defaults. Profile-owned provider, model, permission, and UI state is ignored when it appears in project config. MCP project configuration is trust-gated before any project-defined process or network effect.

## Security boundary

fx describes itself as permission-first. The important architectural idea is that authority should be explicit and host-owned rather than inferred from model text, repository text, or ambient state.

This makes permissions, MCP trust, credential persistence, session authority, and subagent delegation good places to look for cross-surface invariant bugs.

## Contribution contract

The upstream contract is implementation-friendly but strict about evidence:

- Preserve CLI-first behavior, explicit contracts, permission-first security, and small reviewable changes.
- Run the narrowest focused check, then `zig build`, `zig build test`, and exercise the actual development binary at `./zig-out/bin/fx`.
- Open a draft PR from a non-main branch after a clean checkpoint.
- Do not mark it ready until Full CI and the final ship gate pass for the exact current commit.
- Every PR has one primary intent label.
- Do not grow `main.zig` with leaf logic, create hidden live-shell-only product state, or add a second execution path without a clear reason.
- New dependencies outside Zig stdlib require discussion.

## Maintainer signals

Recent merged work favors narrow typed slices rather than monoliths: reasoning-effort/fast controls in libfx, shared MCP status classification, authentication-state repair, unsupported-feature behavior, and cleanup overhead. Several MCP changes were intentionally stacked as adjacent slices.

This suggests a productive contribution pattern: find one user-visible inconsistency, trace all surfaces that represent the same state, centralize the invariant once, prove unchanged healthy behavior, and keep the PR small.

## Autoresearch / optimization substrate

We opened upstream issue [#411](https://github.com/vercel-labs/fx/issues/411), **“Add an optional frozen-harness autoresearch loop for measurable local optimizations.”**

As of current main, fx still has no built-in autoresearch controller: there is no `/autoresearch` loop that mutates a candidate, runs a frozen evaluator, and autonomously keeps/discards experiments.

However, fx now has a strong deterministic **judge** substrate:

- `benchmarks/startup.sh` uses Hyperfine to measure process floor plus startup, help, status, doctor, and session-list paths.
- startup benchmarks use 100 measured runs with 10 warmups in CI and feed explicit latency budgets.
- the normal Linux startup gate owns an absolute 2 ms command budget.
- `benchmarks/libfx/bench-runtime.mjs` records prompt-to-fetch, first-body-to-first-text, prompt-to-first-text, prompt-to-completion, request bytes, and streaming workloads.
- libfx capacity benchmarks measure scaled runtime behavior.
- `scripts/pgso/` already implements unusually rigorous control-vs-candidate qualification: immutable artifacts, alternating AB/BA measurement, p50/p95 gates, deterministic behavior corpus, exact source/artifact identities, fail-closed evidence, and separate training vs verification-only workloads.
- `tests/evals/` supplies deterministic and live-model quality/eval surfaces.
- runtime telemetry records thinking duration, turn duration, token progress, and network-call latency.

This changes the architecture question from “how do we build autoresearch?” to:

> **How thin can the experiment controller be when fx already owns the evaluator?**

The preferred research shape is now:

```text
candidate proposer
  → constrained source edit
  → existing frozen fx benchmark/eval command
  → structured evidence
  → KEEP / DISCARD
  → next candidate
```

The proposer should not be allowed to modify the evaluator used to judge itself.

### Best first autoresearch target

Runtime optimization should start with deterministic local metrics rather than live-model quality:

- startup / CLI dispatch
- libfx prompt-to-fetch overhead
- first-body-to-first-text processing overhead
- stream processing throughput
- binary size / PGSO profile choices

Only after the loop proves it can improve those without correctness regressions should it touch broader agent behavior.

### Why this is a reusable OSS pattern

fx demonstrates a useful general principle for autoresearch:

**Build the frozen judge before the autonomous proposer.**

A mature benchmark/qualification system makes an autoresearch controller much safer because the search loop does not need authority to decide what “better” means.

## Cross-harness lens

fx is useful as the “explicit contract + product breadth” comparison point. It has more built-in product surface than Pi or mini-swe-agent, but its contribution rules try to prevent that breadth from collapsing into ad hoc branching.

Questions to keep tracking:

- Which runtime state classifications are duplicated across CLI, UI, model-visible catalogs, and traces?
- Where can latency be removed without creating a second execution path?
- Which permission/MCP invariants can be stated once and tested across every surface?
- Which core behaviors are actually extension candidates rather than permanent product surface?
- Can autoresearch stay outside the product core while reusing the repository's existing frozen judges?

## Sources

- https://github.com/vercel-labs/fx
- https://github.com/vercel-labs/fx/blob/main/CONTRIBUTING.md
- https://github.com/vercel-labs/fx/blob/main/AGENTS.md
- https://github.com/vercel-labs/fx/issues/411
- https://github.com/vercel-labs/fx/blob/main/benchmarks/startup.sh
- https://github.com/vercel-labs/fx/blob/main/benchmarks/libfx/bench-runtime.mjs
- https://github.com/vercel-labs/fx/blob/main/scripts/pgso/README.md
- [[atlas/oss-contribution-intelligence]]
- [[inbox/oss-harness-contribution-policy-radar-20260920]]
