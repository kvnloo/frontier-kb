---
id: harness-continue
title: Continue
type: harness
status: active
created: 2026-09-20
updated: 2026-09-20
urls:
  - https://github.com/continuedev/continue
capabilities:
  - IDE and CLI coding-agent surfaces
  - Pluggable models/providers
  - Agent-mode terminal and edit tools
  - VS Code and JetBrains integrations
confidence: medium
tags: [harness, continue, ide, cli]
---

# Continue

[Continue](https://github.com/continuedev/continue) spans IDE extensions and a CLI/agent execution path.

## Contribution contract

Continue's public guide welcomes contributors and points to a contribution project board and good-first issues.

The standard code path is fork → feature/fix branch → PR to `main`. Bug reports should include reproduction, expected behavior, and actual behavior. Larger enhancements should begin as issues/discussions. Tests and formatting are part of the review contract, and the project uses a CLA.

Because Continue spans VS Code, JetBrains, GUI, core, and CLI surfaces, a candidate should identify the exact product/runtime version rather than assuming an open issue reflects current `main`.

## Current-main correction: Bash output bounds

Issue #12700 reports that CLI 1.5.46 can return an unbounded 100 kB stdout tool result to the provider loop.

Current `extensions/cli/src/tools/runTerminalCommand.ts` already contains explicit output limits:

- default 50,000 characters
- default 1,000 lines
- limits divided across parallel tool calls
- `truncateOutputFromStart` applied to foreground timeout/background paths

Therefore the issue is useful evidence but is not yet a current-main contribution candidate. We need to determine whether the release was behind a merged fix, whether another result path bypasses truncation, or whether the remaining problem is unbounded buffering/streaming before final truncation.

## Process lifecycle candidate

Issue #12699 reports hangs and orphaned state after tools start background/detached children. Current CLI code has a `BackgroundJobService` and an explicit handoff path for user-requested backgrounding, but a shell command can also create its own descendants independently.

This is worth tracing using the same ownership questions as Crush and nano-rlm:

- which process group owns tool descendants?
- what survives tool resolution?
- what does cancellation promise to kill?
- does explicit background handoff differ from shell-created detached children?
- what lifecycle event tears down jobs on session close?

Do not patch until the stock current-main reproducer confirms the bug is still live.

## Cross-harness lens

Continue is a good place to study how agent invariants survive across CLI and IDE product surfaces. It also provides a useful test for version-aware research: an open issue against a released package may already be addressed in source.

## Sources

- https://github.com/continuedev/continue
- https://github.com/continuedev/continue/blob/main/CONTRIBUTING.md
- https://github.com/continuedev/continue/issues/12699
- https://github.com/continuedev/continue/issues/12700
