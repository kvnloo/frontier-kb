---
id: inbox-opencode-wave-20260915
title: OpenCode contribution waves (Hermes-style) — 2026-09-15
type: inbox
status: draft
created: 2026-09-15
updated: 2026-09-15
node: cos-executor
harnesses: [opencode]
domains: [ai-ml, frameworks]
tags: [inbox, opencode, wave, hermes-mirror]
---

# OpenCode waves — Hermes-style contribution plan

## Context

Deepen `anomalyco/opencode` contribution posture inside frontier-kb only. **Factory lock: openclaw-only** for origin GitHub writes — do **not** open issues/PRs/comments on anomalyco, do **not** mint Linear HITLs from this wave. Mirror Hermes quality motion: Wave/meta consolidations → verify-first → tiny mergeable slices → complement don't compete → Muse-lock skip of claimed leaves → kerdoios-style proof lanes when lock lifts.

Upstream ethos (CONTRIBUTING): issue-first; no AI walls; UI/core need design review; small PRs; templates mandatory; blank → 2h auto-close; providers via models.dev first.

Triage snapshot: ~4307 open issues; **41** labeled open bugs; **0** open `help-wanted` / `good first issue` (labels drained). Recent merges: codemode, AI cache/provider fixes, TUI/app composer, Console routing (see harness note).

Sources: [[harnesses/opencode]] · [[notes/opencode-hermes-playbook-mirror]] · `data/opencode-triage-2026-09-15.json`

## Next action

When origin write lock lifts (or via openclaw): pick **Wave A or D** leaf from Unclaimed list below; comment-claim one issue; ship tiny PR with `Fixes #N` + verification. Until then: keep KB fresh on pulse; do not contact other agents.

---

## Wave A — Provider / LLM edge reliability

| | |
| --- | --- |
| **Theme** | Credentialless providers, truncated tool args, custom OpenAI-compat metadata, websearch whitelist, Poe/gateway quirks |
| **Why** | CONTRIBUTING explicitly welcomes provider/LLM perf/env quirks; high mergeability; complements Hermes Nous Portal work without competing |
| **Issue cluster** | [#42790](https://github.com/anomalyco/opencode/issues/42790) credentialless empty API key; [#36766](https://github.com/anomalyco/opencode/issues/36766) truncated OpenAI tool args (**soft-claimed**); [#44307](https://github.com/anomalyco/opencode/issues/44307) websearch whitelist (**PR open — skip**); [#38620](https://github.com/anomalyco/opencode/issues/38620) Anthropic thinking+tool replay 400; [#42818](https://github.com/anomalyco/opencode/issues/42818) Poe tools; [#40908](https://github.com/anomalyco/opencode/issues/40908) dynamic context length (feature — design gate); [#38509](https://github.com/anomalyco/opencode/issues/38509) online models stuck Build |
| **Leaf shapes** | (1) Issue-first bug: treat empty `apiKey` as unset for credentialless enablement — reproduce on V2 catalog path. (2) Docs-only: document credentialless provider config. (3) models.dev PR first if new provider (#43067 QwenCloud). |
| **Claim risk** | Medium — #36766/#44307 crowded; #42790 had closed PRs (verify still broken before claim) |
| **Unclaimed vs claimed** | Prefer **#42790**, **#38509**, **#40908** (0 comments); skip #44307 / soft-claim swarms |

## Wave B — Permissions / Task / subagent contracts (V2)

| | |
| --- | --- |
| **Theme** | `permission.task`, pending permission listing, per-target subagent enforcement, Scout/General tool exposure |
| **Why** | Matches depth DX (Scout + permission.task); Hermes `/agents` leapfrog mirror; core correctness |
| **Issue cluster** | [#37650](https://github.com/anomalyco/opencode/issues/37650) search metadata breaks pending permission listing (**PR reopen path — claimed**); [#35238](https://github.com/anomalyco/opencode/issues/35238) per-target subagent perms (**claimed**); [#36761](https://github.com/anomalyco/opencode/issues/36761) expose valid subagent IDs (**PR #43282 stuck — Muse skip**); [#36347](https://github.com/anomalyco/opencode/issues/36347) preserve permission/question waits across restart |
| **Leaf shapes** | Comment-map only until lock lifts: cite SHAs + which assertion still fails. Tiny test-only flake fixes adjacent (#37321 — has open PR). New leaves only if verify shows gap with **no** open PR. |
| **Claim risk** | **High** — comment-claim culture strong; Muse lock: skip exact redo |
| **Unclaimed vs claimed** | Treat cluster as **claimed/contested**; factory watches, does not stampede |

## Wave C — Session / server / idle reliability (Hermes statedb analogue)

| | |
| --- | --- |
| **Theme** | Long-lived server CPU/alloc loops, SSE disconnect wedges, idle auth+MCP reconnect, shell output caps stranding sessions |
| **Why** | Same quality motion as Hermes state.db / gateway refresh waves — reliability > features; operators feel it |
| **Issue cluster** | [#36677](https://github.com/anomalyco/opencode/issues/36677) allocation loop; [#36311](https://github.com/anomalyco/opencode/issues/36311) SSE 100% CPU; [#43444](https://github.com/anomalyco/opencode/issues/43444) auth/MCP after idle (**open PR #43558 — skip**); [#45099](https://github.com/anomalyco/opencode/issues/45099) shell output bypasses tool limits (**stood down — PRs exist**); [#34853](https://github.com/anomalyco/opencode/issues/34853) serialize prompt settlement |
| **Leaf shapes** | Reproduce idle MCP reconnect on macOS sleep; docs runbook for `opencode serve` reconnect; tiny reconnect hook if still broken after #43558 merges |
| **Claim risk** | Medium-high on hot bugs; prefer docs/repro comments when write lock allows |
| **Unclaimed vs claimed** | Hot bugs mostly soft-claimed; **docs/repro** leaves safer |

## Wave D — Tool correctness micro-bugs (LSP/formatter-friendly lane)

| | |
| --- | --- |
| **Theme** | Glob/read/grep/HTML tool edge cases; formatter/LSP additions (CONTRIBUTING favorites) |
| **Why** | Small focused PRs; easy verification; low design-review surface |
| **Issue cluster** | [#47421](https://github.com/anomalyco/opencode/issues/47421) Glob hidden files (**open PR — skip**); [#47419](https://github.com/anomalyco/opencode/issues/47419) Read pagination blank line (closed bot PR — **re-verify**); [#47413](https://github.com/anomalyco/opencode/issues/47413) legacy agent Markdown model variant; [#47409](https://github.com/anomalyco/opencode/issues/47409)/[#47407](https://github.com/anomalyco/opencode/issues/47407) HTML conversion; [#45293](https://github.com/anomalyco/opencode/issues/45293) grep empty on missing path (**open PRs — skip**); [#45304](https://github.com/anomalyco/opencode/issues/45304) ESC rejects background question (**open PR**) |
| **Leaf shapes** | After verify `dev` still broken + no open PR: one tool + one test. Or net-new LSP/formatter via issue template (issue-first). |
| **Claim risk** | Medium — kitlangton often opens then closes exploration PRs; always re-check open PR search |
| **Unclaimed vs claimed** | **#47419 / #47413 / #47409** candidates if still red on `dev` with no open PR |

## Wave E — MCP lifecycle

| | |
| --- | --- |
| **Theme** | Runtime MCP mutation vs tool registry race; remote OAuth Windows; optimistic UI |
| **Why** | MCP is peer-table stakes; Hermes also stresses gateway reconnect |
| **Issue cluster** | [#39902](https://github.com/anomalyco/opencode/issues/39902) MCP mutations before registry reconciliation (soft claim + closed PR); [#44700](https://github.com/anomalyco/opencode/issues/44700) Windows OAuth; [#34860](https://github.com/anomalyco/opencode/issues/34860) optimistic UI (enhancement/tui — design); [#43444](https://github.com/anomalyco/opencode/issues/43444) idle MCP (Wave C) |
| **Leaf shapes** | Lifecycle fence test; Windows OAuth repro matrix; avoid UI enhancement without design review |
| **Claim risk** | Medium |
| **Unclaimed vs claimed** | Prefer Windows OAuth if unassigned; skip UI until design |

## Wave F — ACP / protocol port

| | |
| --- | --- |
| **Theme** | ACP V2 core/API port |
| **Why** | Protocol plane quiet industry-wide; OpenCode already labeled; strategic but **not** first leaf |
| **Issue cluster** | [#35457](https://github.com/anomalyco/opencode/issues/35457) Port ACP support to V2 (**assigned @nexxeln — skip**) |
| **Leaf shapes** | None for factory — watch only; optional comment map citing ACP v2 draft when write lock allows |
| **Claim risk** | Locked to assignee |
| **Unclaimed vs claimed** | **Claimed** |

## Wave G — Docs / DX / Zen-Go console (low blast)

| | |
| --- | --- |
| **Theme** | Docs omissions, Copilot URL, Console/Go usage messaging |
| **Why** | Docs explicitly welcome; lowest design friction; Hermes-style docs-first leaves |
| **Issue cluster** | [#48823](https://github.com/anomalyco/opencode/issues/48823) Go docs omit DeepSeek V4.1 Flash promotion (**0 comments, no PR — prime**); [#45302](https://github.com/anomalyco/opencode/issues/45302) Incorrect GitHub Copilot API URL (**open PR — skip**); [#44171](https://github.com/anomalyco/opencode/issues/44171) Sync enabled models (Nice To Have — UI/design) |
| **Leaf shapes** | Docs PR `docs: …` with `Fixes #48823`; screenshot-free |
| **Claim risk** | Low on #48823 |
| **Unclaimed vs claimed** | **#48823 unclaimed** |

## Wave H — Desktop / TUI UX polish (design-gated)

| | |
| --- | --- |
| **Theme** | Tab focus, undo after interrupt, background hints, Think+Patch indicators |
| **Why** | Visible UX but CONTRIBUTING requires design review / screenshots for UI |
| **Issue cluster** | [#47514](https://github.com/anomalyco/opencode/issues/47514) Cmd+number refocus (**PR exists — skip**); [#39736](https://github.com/anomalyco/opencode/issues/39736) undo after interrupt (**multi-claim**); [#36940](https://github.com/anomalyco/opencode/issues/36940) background hint (**PR**); [#44164](https://github.com/anomalyco/opencode/issues/44164) unify Thinking/Patch indicators; [#41454](https://github.com/anomalyco/opencode/issues/41454) image path omitted (**claimed**) |
| **Leaf shapes** | Only after design ack; else skip |
| **Claim risk** | High contention |
| **Unclaimed vs claimed** | Mostly claimed; **#44164** quieter but UI |

---

## Unclaimed actionable ranking (E/I/R)

Prefer: no assignee, no open PR, ≤1 claim comment, bug/docs/provider/tool, small blast. Rank 1=best next.

| Rank | Issue | Why | E | I | R | URL |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | #48823 Go docs omit DeepSeek Flash usage promotion | Docs-only; 0 comments; no PR | 1 | 3 | 1 | https://github.com/anomalyco/opencode/issues/48823 |
| 2 | #42790 Credentialless providers require empty API key | Clear V2 catalog bug; 0 comments; prior PRs closed — re-verify | 2 | 4 | 2 | https://github.com/anomalyco/opencode/issues/42790 |
| 3 | #38509 Online models stuck in Build (Ollama ok) | 0 comments; env quirk lane | 3 | 3 | 3 | https://github.com/anomalyco/opencode/issues/38509 |
| 4 | #47419 Read tool skips blank line at pagination boundary | Micro tool bug; closed exploration PR — re-verify on `dev` | 2 | 3 | 2 | https://github.com/anomalyco/opencode/issues/47419 |
| 5 | #47413 Legacy agent Markdown loses model variant | Config/agent parse; verify no open PR | 2 | 3 | 2 | https://github.com/anomalyco/opencode/issues/47413 |
| 6 | #47409 Core HTML conversion loses inline-code backticks | Tool correctness | 2 | 3 | 2 | https://github.com/anomalyco/opencode/issues/47409 |
| 7 | #47407 HTML conversion hangs when code block exceeds budget | Perf+correctness | 2 | 4 | 2 | https://github.com/anomalyco/opencode/issues/47407 |
| 8 | #40908 Dynamic context length for OpenAI-compatible providers | Feature — issue already open; may need design note | 3 | 4 | 2 | https://github.com/anomalyco/opencode/issues/40908 |
| 9 | #39902 MCP mutations vs tool registry reconciliation | Soft claim + closed PR — only if still broken & claim expired | 3 | 4 | 3 | https://github.com/anomalyco/opencode/issues/39902 |
| 10 | #38620 Errored-message replay 400 Anthropic thinking+tools | Unassigned labeled bug; check claim comments | 3 | 4 | 3 | https://github.com/anomalyco/opencode/issues/38620 |
| 11 | #37372 Empty reasoning-only recorded as success | Labeled core bug; draft PR may exist — verify | 2 | 4 | 3 | https://github.com/anomalyco/opencode/issues/37372 |
| 12 | #36117 Await catalog readiness for model/provider reads | Prior PR noted in comments — verify merge state | 2 | 3 | 3 | https://github.com/anomalyco/opencode/issues/36117 |
| 13 | #34853 Serialize V2 prompt settlement around events | Core race; low comments | 3 | 4 | 3 | https://github.com/anomalyco/opencode/issues/34853 |
| 14 | #44171 Sync enabled models across clients | Nice To Have; UI/design gate | 3 | 2 | 2 | https://github.com/anomalyco/opencode/issues/44171 |
| 15 | #43067 QwenCloud International provider | models.dev first; feature template | 2 | 2 | 2 | https://github.com/anomalyco/opencode/issues/43067 |
| 16 | #42818 Poe provider tool failure 1.18.18 | Provider quirk; may be stale vs 1.18.31 — verify | 2 | 3 | 2 | https://github.com/anomalyco/opencode/issues/42818 |
| 17 | #44700 MCP OAuth Windows token exchange | Platform quirk; check assignees | 3 | 3 | 2 | https://github.com/anomalyco/opencode/issues/44700 |
| 18 | #36677 Long-lived V2 allocation loop | High impact perf; contested/hard | 4 | 5 | 4 | https://github.com/anomalyco/opencode/issues/36677 |
| 19 | #36311 SSE disconnect 100% CPU | High impact; hard | 4 | 5 | 4 | https://github.com/anomalyco/opencode/issues/36311 |
| 20 | #43791 Classify plain AI SDK stream errors | Has open PR — **watch only** | 2 | 3 | 2 | https://github.com/anomalyco/opencode/issues/43791 |

**Explicit Muse skips (do not redo):** #35457 (ACP assigned), #36761 (PR stuck discourse), #35238/#37650/#39736/#36940/#47514/#45099/#43444/#44307/#45293/#45304/#47421 (open or active PRs/claims).

## Links

- [[harnesses/opencode]]
- [[notes/opencode-hermes-playbook-mirror]]
- [[harnesses/hermes]] · [[notes/harness-evolver-hermes-plan]]
- https://github.com/anomalyco/opencode/blob/dev/CONTRIBUTING.md
- https://opencode.ai/docs/agents
