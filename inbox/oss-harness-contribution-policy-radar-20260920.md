---
id: inbox-20260920-oss-harness-contribution-policy-radar
title: "OSS harness contribution policy radar"
type: inbox
status: draft
created: 2026-09-20
updated: 2026-09-20
node: cos
harnesses: [fx, pi, nano-rlm, prime-agent, opencode, goose, aider, cline, openhands, codex, mini-swe-agent, swe-agent]
domains: [ai-ml, software-engineering]
tags: [inbox, oss, harness, contribution-policy, architecture]
---

# OSS harness contribution policy radar

## Context

Before contributing broadly across agent harnesses, treat each upstream's contribution policy as part of its public architecture. The goal is not PR volume. The goal is to learn each codebase, identify the smallest useful slice that matches maintainer intent, validate it in the repo's own terms, and carry reusable architectural lessons into frontier-kb.

Research memory and execution state stay separate:

- **frontier-kb** stores public evidence, harness notes, atomic architectural claims, and cross-harness comparisons.
- **verified-oss-loop** should own claims, leases, verification receipts, and contribution execution.
- Upstream writes follow each repository's own gate. A repo that wants an issue, discussion, invitation, or Ready state must receive that first.

## Policy radar

| Harness | Upstream intake / PR gate | Local verification and style | Architecture lesson for contribution work | Safe initial contribution posture |
|---|---|---|---|---|
| **fx** | Small reviewable changes; draft PR early after focused verification. PR needs one intent label. | Zig 0.16+; `zig fmt src/`, `zig build`, `zig build test`; exercise `./zig-out/bin/fx`, not an installed binary. | CLI-first; typed contracts; permission-first; composition root stays small. Explicitly decide module ownership, persistence, text/JSON output, tests/docs. | Narrow correctness, latency, MCP, or contract-coherence slice with an actual binary repro. |
| **Pi** | New-contributor issues/PRs are auto-closed by default. Do not open a PR until a maintainer explicitly approves the proposed contribution with `lgtm`. | `npm run check`, `./test.sh`; no destructive git; do not edit changelog. | Core is intentionally minimal. Features that do not belong in core should be extensions. Contributor must understand interactions and explain them. | Reproduce one issue, trace core-vs-extension ownership, propose the smallest fix, wait for approval, then implement. |
| **nano-rlm** | No separate CONTRIBUTING.md found. AGENTS.md requires draft PRs and conventional branch/title prefixes. | Always `uv run`; `uv run pytest tests/`; plain-function tests; conservative test additions; minimal exception handling. | Persistent IPython + ACP runtime contract + supervisor-owned agents/jobs/inboxes. Lifecycle and ownership semantics are first-class. | Small lifecycle/correctness slice with focused tests and explicit invariants. |
| **Prime Agent** | Public contributions begin in Discussions. Unsolicited PRs are not reviewed; Issues track maintainer-accepted work. PRs are limited to maintainers and explicitly vouched trusted contributors. | Approved work must be focused, tested, and locally checked; changes use per-package `.changes/` fragments. | Pi-based full harness with persistent RLM / continual-harness layers. Contribution trust is deliberately staged. | Discussion, reproduction, investigation, testing, or docs first. Do not open code PRs without invitation. |
| **OpenCode** | Every PR must reference an existing issue. UI/core features need design review before implementation. | Small focused PRs; explain why the fix works; test locally; screenshots/recordings for UI; conventional titles. | Product spans core/server, TUI, shared web app, and desktop surfaces. Maintainers explicitly reject low-context AI walls. | Bug, provider, perf, LSP/formatter, or environment-specific issue with evidence and an existing issue. |
| **Goose** | Issue is the record. External implementation starts only after the issue reaches **Ready**; PR must link that Ready issue and remain inside approved design. | Verification must be described. Maintainers ask contributors not to open many PRs in parallel. | Current agent-loop migration temporarily requires behavioral changes to be considered across legacy and state-machine paths. | Help refine Accepted/design work or take one Ready issue at a time. |
| **Aider** | Small changes may go directly to PR; significant changes should be discussed in an issue first. Individual CLA required. | `pytest`; PEP8; Black/isort; max 100-column lines; project asks contributors not to add type hints. | Mature CLI harness with relatively conventional OSS entry path. Benchmark results are also welcomed contributions. | Small bug/docs/benchmark evidence; issue first for architecture changes. |
| **Cline** | Most contributions begin with an Issue. Features require maintainer approval before PR; tiny bug/typo/type fixes are exceptions. | Single-purpose PRs, conventional commits, rebase main, tests, screenshots for UI. | Extension/product behavior has a stronger design gate than trivial correctness work. | Good-first/help-wanted issue or tiny self-contained fix. |
| **OpenAI Codex** | Current policy does **not** accept external code contributions or PRs. | N/A for external code contributions. | External contribution surface is diagnosis rather than implementation. | High-quality issue, reproduction, logs, root-cause analysis, or design discussion only. |
| **OpenHands** | Small fixes welcome; larger changes should be discussed with maintainers first. Enterprise subtree is separately licensed and does not accept external PRs. | Conventional PR titles; issue linkage; UI evidence; changelog for user-visible changes. | Large multi-surface system, so scope selection matters more than raw implementation speed. | Good-first/help-wanted issue or narrow OSS-core bug. |
| **mini-swe-agent** | Contributions explicitly welcomed for docs/examples, models, environments/deployments, and labeled issues. | pre-commit; `pytest -n auto`; keep generated code and tests concise. | Deliberately minimal: bash-only agent, linear history, stateless subprocess actions. Prefer a new version of one of the four components over complicating an existing component. | Excellent architecture-learning target: narrow correctness or component variant that preserves minimalism. |
| **SWE-agent** | Issues/PRs welcome; discuss larger code changes first. | Follow repo dev/test instructions and scope larger work through an issue. | Richer sibling to mini-swe-agent, useful for comparing when a harness actually benefits from more interface machinery. | Target a well-scoped issue and compare the design against mini-swe-agent before adding complexity. |

## Maintainer behavior sampled

Policy files are necessary but not sufficient. Recent merged work suggests different practical preferences:

- **fx** is currently merging compact, typed slices around libfx controls, MCP state classification, failure handling, and cleanup. Several changes are deliberately stacked rather than combined into a monolith.
- **Pi** is merging concrete correctness and UX fixes such as stale image races, autocomplete ranking, CJK path completion, event unsubscription, and eval validation. The examples are usually tied to a specific issue and have explicit validation.
- **nano-rlm** accepts deeper architecture work when it is divided into explicit lifecycle slices. Recent merged slices separate supervisor-owned handles, messaging, shell jobs, and kernel recovery rather than presenting one giant orchestration rewrite.
- **mini-swe-agent** rewards very small production diffs with unusually strong causal tests. Recent fixes isolate billing on parse failures and distinguish malformed tool calls from true truncation.
- **Goose** shows strong evidence of maintainer-directed work and Ready-state discipline. Recent merged fixes often explain the user symptom, root cause, design boundary, and validation in detail.

## Cross-harness learning questions

For every harness, capture the same architectural dimensions so the KB becomes comparative rather than anecdotal:

| Dimension | Question |
|---|---|
| Control loop | What is the irreducible model → action → observation loop? |
| State | What survives a turn, process restart, compaction, or subagent boundary? |
| Execution | Stateful shell/kernel, stateless process, typed tools, or a mixture? |
| Extension boundary | Which changes belong in core versus plugin/extension/component variants? |
| Context | Linear transcript, reducer/compactor, persistent execution state, or external memory? |
| Concurrency | Who owns child agents, jobs, cancellation, budgets, and cleanup? |
| Provider boundary | Where are model-specific quirks normalized? |
| Security | Where are permissions, credentials, environment filtering, and sandbox boundaries enforced? |
| Observability | What timings, usage, traces, receipts, or replay artifacts are first-class? |
| UX contract | Which architectural choices exist because of a visible user failure mode? |
| Test philosophy | Unit isolation, real-process integration, live-model eval, benchmark, or all of the above? |
| Maintainer API | What evidence must exist before a contribution is welcome? |

## Architectural contrasts worth turning into permanent notes

**Statefulness is a design choice, not a maturity ladder.** mini-swe-agent intentionally uses independent subprocess calls and a linear history because this improves inspectability and sandbox portability. nano-rlm intentionally keeps a persistent Python kernel and supervisor-owned resources because recursive research benefits from live computational state. Neither design should be copied into another harness without preserving the problem it solves.

**Contribution policy is part of the harness API.** Pi's approval gate, Goose's Ready state, Prime Agent's Discussion/vouch path, OpenCode's issue/design gate, and fx's early draft-PR workflow are materially different integration contracts. An automated contributor that ignores them is architecturally incompatible even when its patch is technically correct.

**The reusable unit is an invariant, not a patch.** Examples: one canonical MCP status classifier, billed calls count against cost even when parsing fails, child lifecycle ownership survives handle loss, and a composition root does not accumulate business logic. frontier-kb should retain those invariants so later agents can recognize the same class of bug in other repositories.

## Next action

Process this capture into canonical harness notes, starting with the three requested harnesses: expand `harnesses/fx.md`, refresh `harnesses/pi.md`, and create `harnesses/nano-rlm.md`. Then create one permanent note for the “maintainer policy as integration contract” invariant and one atlas comparing state, execution, context, concurrency, extension boundaries, observability, and contribution gates across harnesses.

After that, scan live issues only in repositories whose policy permits unsolicited issue-level participation. Generate candidate contributions as evidence-backed hypotheses, not PRs. Before any upstream write, record the policy gate and required validation in the candidate so verified-oss-loop can enforce it.

## Links

- https://github.com/vercel-labs/fx
- https://github.com/earendil-works/pi
- https://github.com/PrimeIntellect-ai/nano-rlm
- https://github.com/PrimeIntellect-ai/prime-agent
- https://github.com/anomalyco/opencode
- https://github.com/aaif-goose/goose
- https://github.com/Aider-AI/aider
- https://github.com/cline/cline
- https://github.com/All-Hands-AI/OpenHands
- https://github.com/openai/codex
- https://github.com/SWE-agent/mini-swe-agent
- https://github.com/SWE-agent/SWE-agent
- https://github.com/kvnloo/verified-oss-loop
