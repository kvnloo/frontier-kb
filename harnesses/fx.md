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
confidence: high
tags: [harness, fx, zig, mcp]
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

## Cross-harness lens

fx is useful as the “explicit contract + product breadth” comparison point. It has more built-in product surface than Pi or mini-swe-agent, but its contribution rules try to prevent that breadth from collapsing into ad hoc branching.

Questions to keep tracking:

- Which runtime state classifications are duplicated across CLI, UI, model-visible catalogs, and traces?
- Where can latency be removed without creating a second execution path?
- Which permission/MCP invariants can be stated once and tested across every surface?
- Which core behaviors are actually extension candidates rather than permanent product surface?

## Sources

- https://github.com/vercel-labs/fx
- https://github.com/vercel-labs/fx/blob/main/CONTRIBUTING.md
- https://github.com/vercel-labs/fx/blob/main/AGENTS.md
- [[inbox/oss-harness-contribution-policy-radar-20260920]]
