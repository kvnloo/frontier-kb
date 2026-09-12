# Evolution Lab

Experiment engine for the FlyForge / Hermes-recovery research program.

The object under optimization is **the frontier of measured systems**, not “make a fly beat Qwen.” Every candidate is an **experiment genome**. Selection is Pareto hypervolume + MAP-Elites niches, with a promotion ladder so most ideas die at a seconds-scale sanity test.

This package implements the **local P0 loop**. Tinker SFT/RL and Cursor Cloud Agent fan-out are declared backends, not fake training runs.

## Goal

> Continuously discover, verify, and explain computational systems that expand the achievable frontier between capability and resources.

## P0 task

Typed Hermes recovery events → bounded action `{retry, restart_sandbox, escalate, noop, page_human}` → external verifier. Secret-bearing observations fail closed at level 0.

Control table (must always be in the archive together):

| Genome | Question |
| --- | --- |
| `teacher_rule` | reference policy |
| `direct_input` | last-step linear control (FLM lesson) |
| `mlp` | flattened history, no recurrence |
| `gru` | recurrent compression |
| `fixed_reservoir` | frozen sparse recurrent + readout |
| `rewired_reservoir` | degree-preserving-ish random graph, **refit** |

## Run

From the `frontier-kb` repo root:

```sh
PYTHONPATH=apps/evolution-lab python3 -m evolution_lab seed
PYTHONPATH=apps/evolution-lab python3 -m evolution_lab run --level 1
PYTHONPATH=apps/evolution-lab python3 -m evolution_lab evolve --generations 2
PYTHONPATH=apps/evolution-lab python3 -m evolution_lab dashboard
PYTHONPATH=apps/evolution-lab python3 -m evolution_lab gym-smoke
PYTHONPATH=apps/evolution-lab python3 -m unittest discover -s apps/evolution-lab/tests -p 'test_*.py'
```

Logs: `apps/evolution-lab/runs/<run_id>/archive.jsonl`  
Dashboard: `apps/evolution-lab/runs/<run_id>/dashboard.html`

On the delayed-cue recovery task (L1, this workspace): teacher **1.00**, mlp/fixed-reservoir/rewire **1.00**, gru **~0.92**, direct-input **~0.79**. The all-systems 2-D front is the free teacher; learned students are compared on `front_learned`. Hosted joules stay unknown.

## Gym (do not fork FlyGym or OpenEvolve)

The speed-up is a **Gymnasium `reset`/`step` contract**, not a GitHub fork of a locomotion sim or an AlphaEvolve clone.

| Name | Role here |
| --- | --- |
| `hermes_recovery` | P0 gym. Owned in this package (`evolution_lab.gym`). |
| [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | API we duck-type. Do not vendor the library until a wrapper needs it. |
| [FlyGym 2.x](https://github.com/NeLy-EPFL/flygym) | Later **registered env** for loom/walk. Pip/consume; FlyGym 2 left Gymnasium on purpose (~10×). Forking `flygym-gymnasium` is the slow path. |
| [OpenEnv](https://github.com/huggingface/OpenEnv) | Later HTTP/Docker sandbox when recovery is a real Hermes session. |
| [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) | Later **mutation backend** (LLM rewrites code). Not the gym. Not the control table. `make_env("openevolve")` fails closed. |

`make_env("flygym")` and `make_env("openevolve")` refuse. L1 scoring stays batch ridge on frozen episodes; `gym-smoke` is the closed-loop teacher check.

## What this is not

- Not MaleCNS LIF playback ([kvnloo/fly-wirehead](https://github.com/kvnloo/fly-wirehead) stays a pinout demo).
- Not a Tinker client. `tinker_sft` / `tinker_rl` backends refuse until wired.
- Not an AODL runtime. The specialist remains an HOTL **port**; this engine records metrics for that port.
- Not a FlyGym fork and not an OpenEvolve rewrite.
