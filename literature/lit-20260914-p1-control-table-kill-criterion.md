---
id: lit-20260914-p1-control-table-kill-criterion
title: "P1 control table: mushroom-body specialist hits confirm 1.00; kill criterion does not fire"
type: literature
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "https://github.com/kvnloo/evolution-lab"
  - "https://github.com/kvnloo/evolution-lab/issues/3"
  - "https://linear.app/0ism/issue/PER-1525"
harnesses: [cursor]
domains: [ai-ml, neuroscience, frameworks]
confidence: high
tags: [literature, flyforge, p1, mushroom-body, hermes]
---

# P1 control table: mushroom-body specialist hits confirm 1.00; kill criterion does not fire

## Claim (one sentence)

On the locked Hermes delayed-cue split, a mushroom-body analogue (frozen sparse PN→KC on engineered Hermes PNs, plastic KC→MBON only) matches teacher confirm **1.00** at **640** weights and ~31% of MLP proxy-cost; GRU **and** direct-input still do **not** dominate the fly reservoir on val, so the P1 kill criterion does not fire, and MaleCNS SGD remains refused anyway.

## Evidence

Measured 2026-09-14 on [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) at local HEAD `20555e7` (`python -m evolution_lab table --level 1` on locked `data/p0/`, `SPLIT_SEED = 20260912`). Hosted joules stay unknown. Encoder is **flatten + last-step + max-over-time** of the 15-D Hermes event, **not** the compound eye and **not** MaleCNS.

| Family | Confirm | Val | Params |
| --- | ---: | ---: | ---: |
| teacher (`rule`) | 1.000 | 1.000 | 0 |
| `direct_input` | 0.792 | 0.625 | 75 |
| `mlp` | 1.000 | 1.000 | 4032 |
| `gru` | 0.917 | 0.896 | 3000 |
| `fixed_reservoir` | 1.000 | 0.958 | 3264 |
| `rewired_reservoir` | 1.000 | 1.000 | 3264 |
| `local_plasticity` | 1.000 | 0.979 | 640 |

Kill: GRU val 0.896 and direct-input val 0.625 do not both dominate reservoir val 0.958 → `gru_and_direct_dominate_reservoir: false`. Scientific policy `always_refuse_malecns_sgd: true` regardless. Motif student is the useful object: `python -m evolution_lab advise '{"sandbox_alive":0}'` → `restart_sandbox`; `--family local_plasticity` fits the KC→MBON specialist.

Teacher proxy-cost is ~0, so `cost_vs_teacher` is not energy. `cost_vs_mlp ≈ 0.31` for the mushroom-body student.

Closed-loop (student trained on last-step labels, then rolled out in `hermes_recovery` for 24 seeds): mean reward **~0.56** with first-frame padding, **~0.37** with zero-pad. Teacher closed-loop stays **1.00**. That gap is P3/DAgger (train on states the student visits), not a P1 last-step failure.

## Fact vs interpretation

**Fact:** last-step locked-split accuracies above; Tinker/FlyGym still fail closed; X credits for this run were depleted (SHERWOOD clip already treated as a FlyWire badge, not a trader).

**Interpretation:** this is Track A (shared numerical features), not visuo-motor TMNF, not a DEX, not a Qwen replacement. Closed-loop student states remain P3/DAgger (measured ~0.56 mean reward vs teacher 1.00). The engine commits live on `cursor/p1-control-table-9425` locally; this environment cannot push `kvnloo/evolution-lab` (Cursor GitHub App is not installed there; see inbox).

## Links

- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[inbox/cursor/inbox-cursor-p1-control-table-20260914]]
- Linear [PER-1525](https://linear.app/0ism/issue/PER-1525)
- GitHub [evolution-lab#3](https://github.com/kvnloo/evolution-lab/issues/3)
