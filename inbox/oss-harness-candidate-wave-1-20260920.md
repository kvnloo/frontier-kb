---
id: inbox-20260920-oss-harness-candidate-wave-1
title: "OSS harness candidate wave 1"
type: inbox
status: active
created: 2026-09-20
updated: 2026-09-20
node: cos
harnesses: [fx, nano-rlm, mini-swe-agent]
domains: [software-engineering, ai-ml]
tags: [inbox, oss, contribution, invariants, correctness, latency]
---

# OSS harness candidate wave 1

## Selection rule

Optimize for maintainer minutes saved and durable invariant improvement, not contribution count. A candidate is worth pursuing when it has a concrete user/eval failure, a narrow architectural owner, a falsifiable regression, and a change shape that matches the upstream's contribution contract.

## fx #902 — cold local model first-response timeout

Issue: https://github.com/vercel-labs/fx/issues/902

### Current-main trace

The reported 120 second timeout is not a generic whole-request timeout.

In `src/gateway/chat_completions.zig::post`:

- opening the HTTP request is bounded by `phase_deadline(30_000, request.deadline)`
- after the request body is sent, waiting for `http.receiveHead()` is bounded by `phase_deadline(120_000, request.deadline)`
- once a successful response head arrives, the watch returns to the caller's overall `request.deadline`

Configured providers are parsed by `src/core/config/configured_provider.zig`, whose definition currently has no timeout field and rejects unknown configuration keys.

### Smallest durable slice

Add an optional phase-specific configured-provider field such as `first_response_timeout_ms` or `response_head_timeout_ms`.

Invariant:

> A configured provider may choose how long fx waits for the first HTTP response head, while connection setup and post-head streaming keep their existing independent deadlines.

Suggested shape:

- default 120000 ms, preserving current behavior
- validate a bounded positive integer in configured-provider parsing
- use only for the response-head phase
- continue taking the minimum with the caller deadline
- leave the 30 second connect phase unchanged
- do not special-case localhost or Ollama
- do not include the timeout in `binding_identity()`; that identity is route/credential provenance, not per-request policy

Regression: a loopback configured-provider fixture deliberately delays the response head against a test-scale configured timeout. No cold model or 120 second CI wait is necessary.

Status: upstream comment prepared, but GitHub integration returned 403 on mutation on 2026-09-20. No upstream write occurred.

## nano-rlm #131 — capability determinism vs filesystem isolation

Issue: https://github.com/PrimeIntellect-ai/nano-rlm/issues/131

### Current-main correction

The issue's original skill-race hypothesis does not match current startup ordering.

Current `RLMEngine._start()`:

1. starts the supervisor
2. discovers brokered capabilities
3. writes generated skill modules into `self.session.dir`
4. constructs `IPythonREPL`
5. starts the kernel
6. `IPythonREPL._inject_startup()` calls `discover_skills(self.session.dir)` and imports those modules

Recursive children create their own `Session` before their engine follows the same startup path.

Also, `RLM_MCP_CONFIG` was removed in PR #160 when runtime configuration became ACP-contract-only, so that credential path in the issue is stale on current main.

### Architectural distinction

Session-directory readability is not wholly accidental. PR #173 intentionally exposes queryable conversation history, including explicit session-directory loading, and PR #179 describes the filesystem as shared/trusted rather than an orchestration isolation boundary.

Therefore two separate contracts should be investigated:

**Capability determinism:** every child and restarted kernel must observe the exact brokered skill set promised by its runtime contract.

**Secret/evaluation isolation:** host-private credentials or eval-only authority must never become readable merely because session history is intentionally readable.

A blanket "hide session directories" change would collide with the current recovery/history architecture.

### Best next evidence

- establish the exact commit used for the 85/458 missing-skill observation
- run repeated current-main child spawn + kernel restart coverage and compare the expected brokered skill set against imported globals
- if leakage persists, name the exact current-main file/field containing the sensitive value rather than treating all history metadata as secret

Status: upstream correction comment prepared, but GitHub integration returned 403 on mutation on 2026-09-20. No upstream write occurred.

## mini-swe-agent #938 / PR #939 — submission detection invariant

Issue: https://github.com/SWE-agent/mini-swe-agent/issues/938
PR: https://github.com/SWE-agent/mini-swe-agent/pull/939

### Why it matters

This is benchmark-integrity, not cosmetic behavior. Shell startup output can push the submission sentinel off line zero, causing a valid solution to run until `step_limit` and be recorded as an empty-patch failure.

PR #939 repairs the Docker reproduction by scanning for the sentinel on any output line.

### Class-of-bug trace

The same positional parser currently appears in at least:

- `environments/local.py`
- `environments/docker.py`
- `environments/singularity.py`
- `environments/extra/contree.py`
- `environments/extra/bubblewrap.py`
- `environments/extra/swerex_modal.py`
- `environments/extra/swerex_docker.py`

The control-flow documentation also shows the line-zero contract.

The PR author already notes the duplication and intentionally scoped the submitted patch to Docker.

### Higher-leverage follow-up

Do not duplicate a competing Docker fix. Harden the invariant once.

A minimal shared pure helper under the environment package can accept the standard output record and either return the submission payload / raise `Submitted`, leaving each environment's execution mechanics untouched. Then every environment shares exactly one definition of the submission protocol and one small parameterized regression suite.

This fits mini-swe-agent's own architecture rule: keep components self-contained, use a small utility when behavior is genuinely shared, and avoid making each environment independently more complex.

Important semantic question before centralizing: PR #939 changes the protocol from "marker must be first output line" to "first exact marker line anywhere." That admits a false positive if a normal command prints a file containing the bare marker. The PR documents this tradeoff. If the project wants a stronger protocol later, a framed sentinel or out-of-band completion channel would be safer, but that is a separate behavior change and should not block the current benchmark fix.

## Wave-1 lesson

The useful contribution pattern is different in each repo:

- **fx:** expose one existing hidden phase policy as an explicit typed configuration contract.
- **nano-rlm:** correct stale architectural assumptions before writing code, then turn the valid concern into independently testable contracts.
- **mini-swe-agent:** recognize that a one-file bug is actually a duplicated cross-environment invariant and harden the class without bloating the agent loop.

This is the standard to reuse for future harness scans.
