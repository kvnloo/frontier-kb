---
id: lit-20260910-oss-coding-plugins
title: "OSS coding scaffolds, compound routers, and small models vs SWE-2"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://github.com/SWE-agent/mini-swe-agent", "https://arxiv.org/abs/2511.13646", "https://docs.openhands.dev/", "https://arxiv.org/abs/2603.05344", "https://github.com/opendev-to/opendev", "https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Super/OpenScaffoldingResources", "https://huggingface.co/Qwen/Qwen3.8-27B", "https://github.com/QwenLM/Qwen3.8", "https://github.com/QwenLM/Qwen3.8/issues/179", "https://arxiv.org/abs/2509.23045", "https://deepswe.datacurve.ai/", "https://github.com/sgl-project/SpecForge"]
harnesses: [omp, hermes, opencode, claude, codex, grok, pi]
domains: [ai-ml, frameworks, tool-use, skills]
confidence: medium
tags: [literature, scaffolds, orchestrator, qwen, nemotron]
---

# OSS coding scaffolds, compound routers, and small models vs SWE-2

## Claim (one sentence)

There is no OSS drop-in that reproduces SWE-2 inside an arbitrary existing harness; the real OSS menu is (1) replace-the-harness scaffolds, (2) compound model routing inside *one* harness, (3) small specialist or worker models you *bind as the loop model*, and (4) serving speedups that do not raise solve rate.

## Evidence

### 1. Scaffolds that *are* the harness (not plugins)

- **mini-SWE-agent** ([repo](https://github.com/SWE-agent/mini-swe-agent)): ~100-line bash-first agent; litellm/OpenRouter; advertised >74% SWE-bench Verified. Princeton's default for FT/RL so you do not overfit a giant scaffold. DeepSWE 1.1 public board runs on mini-swe-agent. SWE-bench Pro recent frontier rows also moved here.
- **Live-SWE-agent** (arXiv:2511.13646, [OpenAutoCoder](https://github.com/OpenAutoCoder/live-swe-agent)): YAML overlay on mini-swe-agent. Step-reflection prompt asks the model to *create/revise Python tools* at runtime. Claims 77.4% SWE-bench Verified (no test-time scaling) and 45.8% SWE-Bench Pro. LLM-agnostic; no extra training. Still a scaffold, not a sidecar for Claude Code.
- **OpenHands Software Agent SDK** (docs + arXiv:2511.03690): MIT, model-agnostic loop, tools, condenser, skills, Docker/remote workspace. Nemotron 3 Super reports 60.47% SWE-bench Verified *in this harness*. You swap the LLM; you do not wrap OMP.
- **OpenDev** (arXiv:2603.05344, [opendev-to/opendev](https://github.com/opendev-to/opendev)): Rust terminal agent. Five independently bound workflow slots — Normal / Thinking / Compact / Critique / VLM. Compound AI system (Zaharia et al.). Closest OSS *architecture* to "small model guides, big model executes," but it *is* the harness.
- **Qwen Code / Qwen-Agent**: first-party Qwen terminal agent and tool-calling framework. Compatibility, not a universal plugin.

### 2. Compound routing (planner ≠ worker)

- NVIDIA cookbook: **Nemotron 3 Super** (120B-A12B) as orchestrator/planner; **Nemotron 3 Nano** as worker. SWE-bench Verified: OpenHands 60.47%, OpenCode 59.20%. PinchBench (OpenClaw) 85.6%. Config examples bind Super into OpenCode/OpenClaw/Kilo/OpenHands — again, as the *brain of that product*, not as a meta-controller of Claude Code.
- OpenDev's Thinking vs Normal slots are the same idea with user-chosen models (e.g. frontier execute, cheaper compact).

### 3. Small/open models as the *loop*, not as a guide

**Qwen3.8-27B** (Apache 2.0, HF card, 2026-08): dense 27B VLM, thinking on by default, `reasoning_effort` xhigh/medium/low. Vendor numbers (mostly Claude Code harness):

| Eval | Qwen3.8-27B | Notes |
| --- | --- | --- |
| Terminal-Bench 2.1 (Terminus) | 73.0 | vs SWE-2 92.8 in Devin CLI |
| SWE-bench Pro | 61.7 | Claude Code, temp 1.0, 256K; refined task list |
| DeepSWE 1.1 | 42.2 | Claude Code; DeepSWE public board also lists 42.2 as vendor-reported |
| QwenSWEBench | 79.0 | in-house, Claude Code, avg@3 |

Simon Willison (2026-08-16): 27B *can* drive Pi as a local coding agent; default xhigh overthinks; MTP speculative decode helps latency, not quality.

**Harness, not weights, moves 27B scores.** Qwen3.8 issue #179 on Qwen3.6-27B SWE-bench Pro: same checkpoint, mini-swe-agent, bash-only ~27–37% vs `str_replace_editor` ~49–51% pass@1 (CI covers the 53.5 card number). qwen-code `edit`/`write_file` did **not** lift vs bash (McNemar p=1.00).

**Kimi-Dev** (arXiv:2509.23045): Agentless workflow training as skill prior, then 5k public trajectories SFT into SWE-Agent. 60.4% SWE-bench Verified workflow; 48.6% as agent. Shows SFT *into a scaffold*, not a meta-orchestrator sitting in front of someone else's loop.

No public 2026-09-10 artifact of the form "SFT Qwen3.8-27B that wraps OMP/Hermes/Claude Code and lifts TB2.1/SWE-bench." Search surface: Nemotron Super (orchestrator *inside* OpenHands/OpenCode), OpenDev slots, SWE-grep (closed retrieval specialist), SWE-agent-LM 7B/32B (older, scaffold-SFT).

### 4. Serving, not intelligence

**SpecForge / SpecBundle / DSpark**: Cognition used these to keep SWE-2 RL rollouts cheap. Community draft models speed SGLang. They are plug-n-play for *inference*, not for solve rate.

### 5. Benchmarks (do not mix)

- SWE-2 numbers are Devin CLI (open-weight) / native lab harnesses.
- DeepSWE 1.1: 113 original tasks, 91 repos, 5 languages; public board = mini-swe-agent; Cognition reports SWE-2 73.0% (Devin).
- Terminal-Bench 2.1: SWE-1.7 post used Claude Code / Codex / Devin CLI, 4h timeout.
- Qwen TB2.1 is Terminus harness. Cross-harness deltas of 10+ points are normal.

## Fact vs interpretation

- Fact: mini-swe-agent, OpenHands SDK, OpenDev, Live-SWE-agent, Qwen3.8-27B, Nemotron 3 Super, SpecForge exist and are OSS or open weights.
- Fact: SWE-2 / SWE-grep weights are not.
- Interpretation: "plug-n-play to any harness" oversells every OSS option. You either (a) swap the product, (b) bind a second model in a product that already has planner/worker slots, or (c) post-train a specialist with a typed I/O contract (retrieval, compact, critique).
- HOLD: Live-SWE-agent 77.4% Verified and Qwen 61.7% SWE-bench Pro are author-reported; DeepSWE's own paper exists specifically because mined-GitHub benches saturate and leak.

## Links

- [[literature/lit-20260910-swe-2-pareto-rl]] · [[literature/lit-20260910-swe-grep]]
- mini-swe-agent: https://github.com/SWE-agent/mini-swe-agent
- OpenDev: https://arxiv.org/abs/2603.05344
- Qwen3.8-27B: https://huggingface.co/Qwen/Qwen3.8-27B
- DeepSWE: https://deepswe.datacurve.ai/
