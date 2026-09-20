---
id: atlas-oss-contribution-intelligence
title: "OSS contribution intelligence"
type: atlas
status: active
created: 2026-09-20
updated: 2026-09-20
tags: [atlas, oss, contribution, governance, verification]
---

# OSS contribution intelligence

A cross-repository policy layer for making useful upstream contributions without flattening maintainers' local rules.

## Rule hierarchy

1. **Repository law wins.** CONTRIBUTING.md, AGENTS.md, issue templates, maintainer instructions, and current project-board state override every generalized heuristic.
2. **Universal invariant.** A rule is promoted here only when it expresses a durable correctness/review principle and does not conflict with another repository's legitimate workflow.
3. **Strong default.** A rule is usually beneficial but may have repo-specific exceptions.
4. **Local convention.** Branch names, type-hint preferences, formatter choices, changelog mechanics, and other project-specific choices stay local unless independently justified.

A generalized rule must preserve the *reason* behind its source rule, not blindly copy its exact mechanism.

## Universal invariants

### Understand before mutating

Source signals: Pi, Prime Agent, Goose, OpenCode.

An agent must be able to explain the affected architecture, ownership boundary, failure mechanism, and why the proposed change belongs there before it writes upstream code.

Practical gate:

- read the relevant files in full when making broad changes
- identify the module/service that owns the behavior
- distinguish observed facts from hypotheses
- check current main, not only issue text or an old release
- stop when the ownership contract is unclear

### Problem before implementation

Source signals: Goose, Prime Agent, OpenCode, Cline, Gemini CLI, Qwen Code, Charm.

Search for duplicates and establish a real problem before implementing. Respect the repository's intake state machine: Discussion, Issue, Accepted/design, Ready, maintainer approval, invitation, or no external code contributions.

General form:

> Generate candidates broadly; mutate upstream only after the repository-specific gate is satisfied.

### Small causal slices

Source signals: fx, OpenCode, Cline, Qwen Code, Gemini CLI, Prime Agent.

Prefer the smallest change that repairs one invariant. Separate adjacent improvements unless they must land atomically. Do not hide behavior changes inside cleanup or broad refactors.

This does **not** mean every diff must be tiny. A larger change is acceptable when one indivisible contract requires it and the PR explains why.

### Verification must be falsifiable

Strongest source: Prime Agent; reinforced by Goose, fx, mini-swe-agent.

A regression test should fail when the target behavior is broken. Verification should establish observable behavior, not merely prove that mocks return what they were configured to return.

Preferred evidence order:

- focused deterministic regression
- real process/protocol boundary where practical
- broader relevant suite
- manual or live-model probe only when deterministic local evidence cannot establish the claim

### Do not manufacture green evidence

Source signals: Prime Agent, fx PGSO/CI, Goose.

Retries, sleeps, wider timeouts, exception swallowing, or optional assertions must not be used to turn nondeterminism into apparent correctness.

Nuance: infrastructure may have an explicitly designed bounded retry policy, such as fx's one tmux retry after reset. Preserve that local policy. The universal rule is that retries are never a substitute for fixing or exposing a flaky product/test invariant.

### Readiness should follow events, not hope

Strongest source: Prime Agent.

For concurrency, process lifecycle, sockets, and timing-sensitive work, wait on a concrete completion/readiness signal or use a fake clock. A timeout may bound failure but should not be the event that makes the test pass.

This is a strong default when the project architecture exposes such a signal.

### Current-main evidence outranks stale issue assumptions

Learned repeatedly in this sweep:

- nano-rlm #131 contains hypotheses invalidated by current startup/config architecture
- Continue #12700 describes a released CLI path that current main already bounds
- upstream issues may remain valuable even after their proposed root cause becomes stale

Before contributing, reproduce or trace the claimed invariant on the exact current target revision.

### Preserve exact treatment identity

Source signals: fx contribution/PGSO rules, Prime Agent pre-release evals, our own verified-OSS work.

Evidence belongs to a specific source commit, candidate commit, configuration, toolchain, and benchmark identity. Results from an older candidate do not prove the current head.

**Built artifact identity is part of the treatment.** A source mutation is not sufficient evidence that a candidate changed the runtime. Before benchmarking, record control and candidate artifact hashes and fail closed if an experiment that is supposed to change runtime behavior produces a byte-identical artifact. The first fx autoresearch canary caught exactly this: a mutation targeted a helper path bypassed by native startup, both ReleaseSafe builds succeeded, but control and candidate binaries were identical.

### Security and privacy are part of correctness

Source signals: fx, Codex, Prime Agent, Cline, Goose.

Never place credentials, private prompts, user data, or unrelated private workspace state in public issues, traces, fixtures, commits, or KB notes. Use the repository's private security path for vulnerabilities.

### Contributor responsibility is non-delegable

Source signals: Pi, Prime Agent, Goose, OpenCode.

Using agents is fine where the repository permits it. The contributor remains responsible for understanding the code, reviewing the output, and making claims no stronger than the evidence.

## Strong defaults

### Prefer invariants over symptom patches

When several surfaces encode the same state or protocol, identify whether one canonical owner can prevent the whole bug class.

Examples from current research:

- fx MCP state classification
- mini-swe-agent duplicated submission sentinel parser
- process ownership across foreground/background handoff in Crush/Continue/nano-rlm

Do not centralize merely for aesthetic DRYness. Centralize when duplicated ownership creates divergent behavior.

### Keep tests close to the owning module

Prime Agent explicitly prefers regressions in the existing suite for the broken module. This is a strong default because it reduces one-file-per-issue test sprawl and keeps behavior discoverable.

### Separate deterministic CI from live-model evaluation

fx and Prime Agent make this separation explicit. Live-provider probes are useful evidence but should not silently become the only correctness gate for deterministic behavior.

### Use narrow verification first

fx explicitly asks contributors to run the narrowest relevant check before broad suites. This saves contributor and maintainer time and provides a clearer causal signal.

### Describe user-visible behavior, not implementation history

Source signals: fx changelog/comment guidance, nano-rlm comment rules.

Code comments and release notes should explain current behavior and constraints. Historical narration belongs in issues/PRs when it matters.

## Local-only examples

Do **not** globalize these mechanically:

- Aider: no type hints
- Pi/Prime Agent: top-level imports only
- OpenCode: prefer no `else`, Bun-specific API preferences
- nano-rlm: branch prefixes and draft-PR convention
- fx: exactly one PR intent label
- Gemini CLI: maximum three self-assigned help-wanted issues
- project-specific changelog fragment formats

They may contain useful local lessons, but they are not universal OSS laws.

## Candidate decision record

Before any upstream mutation, record:

- repository + exact target revision
- policy evidence
- allowed next action
- maintainer/design state required
- observed failure or opportunity
- current-main reproduction/trace
- owning module/contract
- falsification test
- smallest candidate slice
- local checks required
- privacy/security review
- evidence that no existing PR already owns the same fix
- what new cross-repo invariant, if any, should be learned afterward

## Learning loop

```text
local policy
  ↓
architecture + current-main evidence
  ↓
candidate invariant
  ↓
cross-repo analogues / counterexamples
  ↓
smallest permitted contribution
  ↓
verification + maintainer review
  ↓
what was accepted/rejected and why
  ↓
promote, revise, or demote generalized rule
```

A maintainer rejection is training data, not a failed loop. Record whether the rejection was about problem priority, ownership, scope, evidence, implementation shape, or project philosophy.

## Related

- [[permanent/perm-20260920-contribution-policy-is-an-integration-contract]]
- [[inbox/oss-harness-contribution-policy-radar-20260920]]
- [[inbox/oss-harness-candidate-wave-1-20260920]]
- [[harnesses/fx]]
- [[harnesses/pi]]
- [[harnesses/nano-rlm]]
- [[harnesses/crush]]
- [[harnesses/mini-swe-agent]]
- [[harnesses/continue]]
