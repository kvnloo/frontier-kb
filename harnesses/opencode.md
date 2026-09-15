---
id: harness-opencode
title: OpenCode
type: harness
status: active
created: 2026-09-09
updated: 2026-09-15
urls:
  - https://github.com/anomalyco/opencode
  - https://opencode.ai
  - https://opencode.ai/docs
  - https://opencode.ai/docs/agents
  - https://github.com/anomalyco/opencode/blob/dev/CONTRIBUTING.md
  - https://github.com/anomalyco/models.dev
  - https://opencode.ai/discord
capabilities:
  - OSS AI coding agent (TypeScript/Bun monorepo; default branch dev)
  - Surfaces: TUI (SolidJS + opentui), web UI (packages/app), desktop Electron beta, IDE extensions label lane
  - Headless API server (opencode serve / bun dev serve, default :4096) + web attach
  - Primary agents Build (full tools) + Plan (edit/bash ask/deny); hidden compaction/title/summary agents
  - Subagents General, Explore (read-only), Scout (clone dependency into managed cache for upstream cross-ref)
  - Fine-grained permissions (ask/allow/deny) incl. bash globs, permission.task subagent allowlists, doom_loop, hidden Task-only subagents, steps cap (maxSteps deprecated)
  - MCP extensibility; plugins (@opencode-ai/plugin, .opencode/plugins, skills); LSP permission key
  - Multi-provider via models.dev + OpenCode Zen curated list; /connect; Console/Go subscription plane
  - Sessions: child-session nav, share links, undo/redo, AGENTS.md project init
  - ACP surface in-flight (label:acp; V2 port issue exists); Slack package present
  - Install: npm/bun/brew/mise/nix/scoop/choco/pacman + desktop DMG/exe/AppImage
gaps_vs_peers:
  - No messaging gateway across Telegram/Discord/Slack/WhatsApp as Hermes product surface (Slack package ≠ Hermes gateway)
  - No persistent crew/worktree orchestration like firstmate; Plan/Build + Task subagents are lighter than OMP fan-out + Firstmate crews
  - No native DAP debugger / stream rules / hashline edits (OMP/Crush LSP+DAP lead)
  - No Claude-class plugin eval ablation+CI; no Cursor Projects durable coordinator+subscriptions artifact
  - No Hermes learning loop (FTS5 session search, skill-from-experience, cron fleet)
  - Compaction is hidden agent summarizer — not OMP Anthropic remote/cache-preserving compaction catalog axis
  - Sandbox/egress is permission globs, not Claude per-command allowed_domains under sandboxed auto
  - help-wanted / good-first-issue labels drained (0 open 2026-09-15); contribution friction high (issue-first, design review, no AI walls)
  - No Pi ExtensionAPI / SoL-Pi first-party host path
omp_actionable: true
confidence: high
tags: [harness, opencode]
---

# OpenCode

Snapshot: Open-source AI coding agent (`anomalyco/opencode`, MIT, ~207k★, default branch `dev`). Latest release sampled **v1.18.31** (2026-09-14). TypeScript/Bun monorepo with TUI + web + desktop beta + headless server.

Strengths: Massive OSS adoption; multi-surface (TUI/web/desktop); mature agent taxonomy (Build/Plan + Explore/Scout) with `permission.task` / `steps` / Scout managed-cache clone; plugins + skills + MCP; providers via models.dev; explicit CONTRIBUTING gates (issue-first, design review for UI/core).

Gaps: No Hermes-class gateway/learning loop; no OMP DAP/stream-rules depth; no Cursor Projects coordinator; no Claude plugin-eval CI; contribution lane is careful/high-friction (not biome-hostile, but no open help-wanted pool).

Factory posture: **openclaw-only** for origin GitHub writes — this note is KB/plan only. Do not open anomalyco issues/PRs/comments from factory until lock lifts.

## Snapshot

| Axis | State (2026-09-15) |
| --- | --- |
| Repo | https://github.com/anomalyco/opencode (`dev`) |
| Stars / open issues | ~207585★ / ~4307 open via search (~5784 `open_issues_count` includes PRs) |
| Labeled open bugs | **41** (primary curated lane) |
| help-wanted / GFI open | **0 / 0** (historical totals 63 / 34, all closed) |
| Core packages | `packages/opencode` (core+server), `tui`, `app`, `desktop`, `plugin`, `sdk`, `llm`, `slack`, `docs`, `protocol`, … |
| Dev | Bun 1.3+; `bun install && bun dev`; `bun dev serve` / `web` / desktop |

## Capability matrix vs peers

| Capability | OpenCode | Hermes | OMP | Claude Code | Cursor | Codex | Crush |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TUI | Strong (opentui) | CLI/gateway | Strong | CLI | IDE-first | CLI | Strong Charm TUI |
| Web UI | Yes (`app`) | Dashboard | Limited | Remote/web | IDE | — | — |
| Desktop | Electron beta | Desktop/Cloud | — | — | IDE | — | — |
| Agents / subagents | Build/Plan + General/Explore/Scout + Task perms | Subagents + kanban/CoS | Typed fan-out + worktrees | Workflows + subagents | Projects coordinator | Agents + ExternalMessage | Session agent |
| MCP | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Permissions / sandbox | Fine globs + task allowlists | Keel/HITL | Obfuscation + auth-gateway | Per-cmd `allowed_domains` | Product sandbox | OS sandbox | MCP perms |
| Compaction / memory | Hidden compact/title/summary agents | FTS5 + skills memory | Local + Anthropic **remote** compaction | Compaction + Memory + Dreams | Project shared context | Compaction | Session context |
| Providers | models.dev + Zen + many | Nous Portal + multi | 60+ | Anthropic-first | Multi | OpenAI-first | Multi + ChatGPT sub |
| Plugins / skills | `.opencode` plugins/skills | Hermes plugins | omp plugins + marketplace | Plugins + **plugin eval** | Rules/skills | Extensions | MCP |
| Sessions | Child sessions, share, undo | state.db sessions | Session tree | Remote sessions | Projects | resume/fork | Sessions |
| CI / evals | Repo tests; no public plugin-eval product | abeval/traps (internal) | Dense tests | **plugin eval** ablation CI | — | Guardian alpha | — |
| ACP | Label + V2 port (#35457 assigned) | — | — | — | — | — | — |

Leapfrog targets (complement, don't compete): Scout+`permission.task` DX already ahead of many TUIs — **mirror into Hermes `/agents`**. Gaps to close vs peers for *our* products: Projects-class durable coordination, plugin-eval ablation, provider-owned compaction, messaging gateway, DAP — not "another Build agent".

## CONTRIBUTING / contribution ethos

Source: https://github.com/anomalyco/opencode/blob/dev/CONTRIBUTING.md

- Prefer: bug fixes, LSPs/formatters, LLM perf, new providers (via **models.dev** first), env quirks, missing standard behavior, docs.
- **UI or core product feature → design review with core team before implementation.**
- Labels to seek: `help-wanted`, `good first issue`, `bug`, `perf` — but **help-wanted/GFI currently empty**.
- **Issue-first:** every PR must reference an existing issue (`Fixes #N`); PRs without issues may close.
- Small focused PRs; conventional titles (`feat:`, `fix:`, `docs:`, … + optional scope).
- **No AI-generated walls of text** on issues/PRs.
- Templates mandatory (bug / feature / question); blank/non-compliant → comment + **auto-close in 2h** (`needs:compliance`).
- Claim: leave a comment; maintainers may assign unless already working it.
- UI PRs need screenshots; logic PRs need verification notes.

Factory consensus: careful lane — issue-first, no AI walls. High-friction, not AI-hostile like biome.

## Recent merge themes (sampled ~40 merged PRs, 2026-09-14/15)

codemode interpreter hardening; AI provider/cache/`prompt_cache_key` allowlists; content-policy error classification; TUI/app composer attachments + form drafts; session-ui websearch provider labels; client inbox event preservation; Console key routing; ACP-adjacent session restore already in v1.18.31 release notes. Maintainers heavy: `@rekram1-node`, `@kitlangton`, `@nexxeln`, `@opencode-agent` bots, community `@Hona`/`@OpeOginni`.

## Strengths

- Multi-surface product (TUI/web/desktop/server) with shared SolidJS UI.
- Agent taxonomy + Scout clone-cache + task permission DX is documentation-complete (agents page updated ~Sep 14).
- Provider ecosystem + Zen; plugin package first-class.
- Clear contribution guardrails (reduces drive-by architecture PRs).

## Gaps (leapfrog targets)

1. **Reliability idle/auth/MCP** — long-lived server/auth reconnect (Hermes statedb/gateway reliability wave analogue).
2. **Permission/task enforcement bugs** on V2 — soft-claimed swarm; skip exact redo (Muse lock style).
3. **Provider edge cases** — credentialless enablement, custom OpenAI-compat context length, websearch whitelist.
4. **Eval/quality loop** — no Claude `plugin eval` equivalent for OpenCode plugins/skills.
5. **Orchestration product** — no Cursor Projects coordinator+subscriptions; Hermes CoS remains the OSS analogue to strengthen elsewhere.
6. **Debugger/LSP depth** — CONTRIBUTING welcomes LSPs/formatters; DAP still peer gap vs OMP.

## Triage notes

Cache: [[data/opencode-triage-2026-09-15.json]] (and `/workspace/opencode-triage-2026-09-15/`). Wave plan: [[inbox/opencode-wave-2026-09-15]]. Playbook: [[notes/opencode-hermes-playbook-mirror]].

NVIDIA cookbook binds Nemotron 3 Super as loop model for OpenScaffolding (59.20% SWE-bench Verified) — Super is in-harness planner, not an external wrapper. [[literature/lit-20260910-oss-coding-plugins]]

## Sources

- https://github.com/anomalyco/opencode
- https://github.com/anomalyco/opencode/blob/dev/CONTRIBUTING.md
- https://opencode.ai/docs · https://opencode.ai/docs/agents
- Pulse: `/workspace/multi-harness-pulse-2026-09-15.md`
- Depth: `/workspace/competitor-depth-dx-2026-09-15.md` (Scout + `permission.task`)
