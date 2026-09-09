---
id: tokenomics-retrospective
title: "Tokenomics Retrospective: Pattern Catalog for Intelligent Token Optimization"
type: permanent
status: draft
created: 2026-09-09
updated: 2026-09-09
harnesses: [hermes, voyager]
domains: [ai-ml]
confidence: medium
tags: [tokenomics, optimization, retrospective, skills]
---

# Tokenomics Retrospective: Pattern Catalog for Intelligent Token Optimization

## Problem Statement

After successful task completion (Done status), analyze whether the same outcome could have been achieved with fewer tokens. Update prompts and skills for future tasks based on these learnings. This retrospective analysis creates a feedback loop: successful trajectories inform skill extraction and prompt refinement, reducing cost while maintaining quality.

## Ranked OSS Tools & Research

### Active Tool Ecosystem

1. **ClawTrace/CostCraft** — https://github.com/epsilla-cloud/clawtrace · https://arxiv.org/abs/2604.23853  
   Trace-based cost attribution and optimization framework for agentic workflows

2. **Trace2Skill** — https://github.com/Qwen-Applications/Trace2Skill · https://arxiv.org/abs/2603.25158  
   Automatic skill extraction from successful agent trajectories (Qwen Applications)

3. **agenttrace** — https://github.com/luoyuctl/agenttrace  
   Lightweight agent execution tracing library for cost and performance analysis

4. **ccusage** — https://github.com/ryoppippi/ccusage  
   Command-line token usage analyzer for LLM API calls

5. **Hermes Skills + Trajectories**  
   Docs: https://hermes-agent.nousresearch.com  
   - Skills system: session-bound skill acquisition and management
   - Trajectory format: structured execution traces with tool calls
   - Session storage: preserves successful patterns for reuse
   - Closest to first-party `skill_manage` automation among OSS harnesses

6. **AWM (Agent Workflow Memory)** — https://github.com/zorazrw/agent-workflow-memory · https://arxiv.org/abs/2409.07429  
   Memory system for storing and retrieving successful agent workflows as reusable recipes

7. **Voyager** — https://github.com/MineDojo/Voyager  
   Lifelong learning agent with curriculum-driven skill library (Minecraft domain)

8. **GEPA (General Episodic Policy Approximation)** — https://github.com/gepa-ai/gepa · https://arxiv.org/abs/2507.19457  
   Offline policy learning from agent trajectories with token/$ metrics

## Key Papers & Adjacent Research

### Core Reading

- **Reason Wide Not Deep** — https://arxiv.org/abs/2608.07885  
  *FACT:* Paper demonstrates that expanding search breadth (parallel reasoning paths) outperforms depth-first chains for complex reasoning tasks.  
  *INTERPRETATION:* Suggests token savings via earlier success detection in wide search; applies to multi-attempt agent strategies.

- **FrugalGPT & Cascade Models**  
  *Adjacent pattern:* Model cascading (cheap → expensive) reduces cost on easy queries; less applicable to complex agentic workflows where task difficulty is unknown a priori.

### Caution: Compression ≠ Retrospective Optimization

**LLMLingua-style prompt compression** — A priori pruning of prompts before execution.  
*RISK:* For agent systems, premature compression can degrade tool-use accuracy and reasoning quality. Retrospective analysis (post-success) avoids this pitfall by preserving full context during execution and optimizing only after validation.

## Adoptable Patterns (Linear HITL Preserved)

These patterns support tokenomics optimization while maintaining human-in-the-loop approval for skill/prompt changes:

1. **TraceCard Post-Done**  
   After Done status, generate trace summary with token attribution per tool/skill. Review identifies high-cost, low-value steps.

2. **Prune-Only Proposals**  
   Automated analysis proposes removals (redundant steps, unused tools), not additions. Human reviews before merge.

3. **Preserve vs Prune Decision Trees**  
   Flag trajectory segments: critical (preserve), redundant (prune candidate), experiment (A/B test).

4. **Passive Corpus Distillation**  
   Accumulate successful trajectories in read-only corpus. Periodic batch analysis identifies common patterns for skill extraction—HITL gates skill admission.

5. **AWM Recipes**  
   Store workflow templates from high-value tasks. Future tasks match against recipe library; if hit, use compressed workflow.

6. **Success-Gated Skill Admission**  
   New skills enter library only after ≥N successful uses in production traces. Filters noise.

7. **Offline GEPA with Token/$ Metric**  
   Train lightweight policy on historical trajectories optimizing for (success_rate / cost). Deployed policy suggests next actions; agent can override.

8. **Observability First**  
   Instrument before optimizing. Trace all tool calls, token counts, latencies. Dashboard highlights cost outliers.

## Empty Notes: First-Party Auto Cost→Skill

**OBSERVATION:** No mainstream first-party harness (Claude Code, OpenCode, Aider, Continue, OpenMind Projects) currently implements automatic cost-driven skill extraction in production.

- **Claude Code / Cursor Cloud Agents:** Manual skill authoring; no auto-extraction from traces
- **OpenCode / Aider:** Focus on context management, not post-hoc skill mining
- **Continue:** Extension-based; no trajectory → skill pipeline
- **OpenMind Projects:** Research-oriented; lacks production auto-optimization

**Hermes is the closest:** `skill_manage` capability allows session-local skill acquisition, though not explicitly cost-driven.

## Zer0 Mapping (Implementation Held)

This section documents the planned implementation architecture for frontier-kb and the agent factory. **Implementation is held pending Linear HITL approval.**

### Components

1. **Frontier-KB Note**  
   *Status:* This file (`notes/tokenomics-retrospective.md`)  
   *Role:* Knowledge reference for tokenomics patterns

2. **Factory Skill: `skills/token-postmortem/SKILL.md`**  
   *Status:* Held (not created)  
   *Role:* Executable skill for agents to run post-Done analysis  
   *Inputs:* Task ID, trajectory file, token log  
   *Outputs:* Markdown report with prune proposals + skill extraction candidates

3. **Linear Done Template Checklist**  
   *Status:* Held (not created)  
   *Role:* Add "Run token-postmortem?" checkbox to Done workflow  
   *Trigger:* Manual opt-in per task; no automatic runs

4. **First Experiment Design**  
   *Scope:* 3 Done leaves (completed tasks)  
   *Success criteria:* ≥20% token/$ reduction on ≥2/3 shadow runs (rerun with optimized prompts)  
   *Output:* One general prune rule (e.g., "remove redundant file reads")  
   *Gate:* HITL reviews prune rule before merge to skills library

### Governance

- **CoS owns merge:** All skill updates require Chief of Staff approval
- **Shadow runs mandatory:** Optimization claims validated via controlled reruns
- **No silent deploys:** Changes to prompt/skill library are user-visible in PRs

## Related

- [[literature/reason-wide-not-deep]] (when created)
- [[permanent/agent-skill-libraries]] (when created)
- [[harnesses/hermes]] (when created)

## Confidence Note

*Medium confidence:* Tools and papers are publicly documented; adoption patterns reflect 2026-09 landscape. Implementation patterns are untested in our specific factory context—first experiment will refine.
