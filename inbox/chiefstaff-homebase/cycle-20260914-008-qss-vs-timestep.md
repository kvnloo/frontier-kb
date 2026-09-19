---
id: homebase-cycle-20260914-008-qss-vs-timestep
title: "Cycle 8: QSS (state quantization) vs time-step ODE; HLA still unverified"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, qss, devs, research-cycle]
---

# Cycle 8 — quantized-state integration vs fixed-step ODE

## Question
If facility **ops** are discrete-event and **court physics** are ODE (cycle 7), can **QSS** (quantize state, keep time continuous) replace a uniform `dt` stepper for sparse hybrid contacts **without** becoming a second scoring authority or a custom kernel?

## Hypothesis
**H (tested):** QSS is the **dual** of time discretization: events fire when a quantized state leaves a hysteresis band, and those events are **exact DEVS**. That is a **solver/scheduler contract**, not a sport-rules oracle and not a reason to promote charter H3.

**Avoid:** Re-citing FMI clocks (c1), brand CCD (c2), DTDL (c4), jobs/SoA (c5), Modelica sample/hold / Ptolemy directors (c7). Do not treat Wikipedia as primary.

## Host
Measured 2026-09-14 ~13:28 CDT: load **1.89 / 4.17 / 6.38**, Mem 23 Gi, **~6.4 Gi available**, swap ~31 Gi used. Cycle 7 gate for net/rally tape: **loadavg-1m < 4 and Mem available > 8 Gi**. 1-minute load was < 4 but **RAM gate failed** → **experiment not executed**. By ~13:33 load rose to **6.31 / 6.46 / 6.70**, Mem ~6.8 Gi available. QMD: 0 collections; no index mutation. No GPU.

## Primary sources retrieved

Retrieved (full pages / PDF text, not snippets-only):

- Kofman & Junco, *Quantized-State Systems: A DEVS Approach for Continuous System Simulation*, TRANSACTIONS of SCS, Vol. 18 No. 1, 2001, pp. 2–8. PDF: https://www.fceia.unr.edu.ar/~kofman/files/qss.pdf (10 pages; `file` PDF 1.3).
- arXiv **2512.17855** (2025): *On General Linearly Implicit Quantized State System Methods* (Bergonzi et al.) — HTML abstract.
- arXiv **2006.05495** (2020): *retQSS: … Particle Systems in Reticulated Geometries* (Santi et al.) — HTML abstract.

**Discarded / blocked:**

- IEEE `https://standards.ieee.org/ieee/1516.1/5898/` HTTP 200 but title **IEEE 1302-2019** (EMI gaskets) — wrong document (same class of failure as cycle 7’s 1516 URL → C57.168).
- `https://standards.ieee.org/ieee/1516/7343/` already discarded cycle 7.
- SISO HLA PDG URLs 404; MSCO / NATO HLA PDFs 000 (no bytes).
- arXiv API `Rate exceeded`; guessed id `1211.4974` is **unrelated** Kawamura et al. numerics complexity — **not QSS**.
- Wikipedia QSS/HLA extracts retrieved; **secondary only**, not used as support.

### Kofman & Junco 2001 (primary)

QSS: continuous-time systems whose **inputs are piecewise constant** and whose **states**, after a **quantization function with hysteresis**, become piecewise constant (states themselves piecewise linear). Hysteresis **ε** prevents infinitely many transitions in finite time.

Associated QSS of `ẋ = f(x,u)`, `y = g(x,u)` is `ẋ = f(q,u)`, `y = g(q,u)` with `q = b(x)` componentwise.

QSS is **exactly** a DEVS model. It is a **model approximation** of the original ODE: some **stability** properties are conserved; **Theorem 6**: if `f` is Lipschitz on the non-saturation region, QSS trajectories **converge** to the ODE solution as quantization intervals → 0 (saturation bounds fixed).

Stiff RLC example (eigenvalues −1 and −10000): QSS **304** internal transitions, abs error < 10⁻² vs closed form. Authors report Euler needing **>150000** steps, RK4 **>90000**, Matlab ode45 **>30000**, ode113 **>60000** for similar error; **ode15s 81 steps**. That comparison is **their 2001 Matlab run**, not a Homebase bench — do not import the step counts as our measurement.

### LIQSS 2025 / retQSS 2020 (primary abstracts)

LIQSS generalization (2512.17855): new linearly implicit QSS families claim **stability, global error bound, and efficient event handling** vs classic integrators; two application examples only in the abstract.

retQSS (2006.05495): QSS **discrete-event** particle tracking **agnostic of domain**; Modelica for hybrid specs; **state-events** of particle–mesh hits become **time-events**. Performance claim is for **discontinuity-dominated** particle/mesh cases, not pickleball scoring.

## Support / refute

- **Supported:** Time-step ODE and QSS are **dual discretizations**. Sparse hybrid contacts (net, floor, occupancy) match **event-when-quantum-crossed** better than a uniform 120 Hz tick **as a numerical idea**.
- **Supported:** QSS **is DEVS**, so it sits on the same **scheduler/domain split** as cycle 7 (ops calendar vs court continuous) without requiring Ptolemy/Modelica as a shipping kernel.
- **Supported (retQSS abstract):** Translating **geometric state-events** to **time-events** is the same *kind* of move as localizing first-contact then scoring (cycle 2) — still **not** a scoring oracle.
- **Not supported:** Homebase must implement QSS/LIQSS; QSS beats RK4 on pickleball; 304 vs 150000 steps applies here; HLA time management (lookahead, federate clocks) — **unverified**.
- **Refuted this cycle:** That IEEE 1516.1 HTML is a usable primary (wrong standard). That RAM>8 Gi tape gate was met (6.4 Gi available). That arXiv `1211.4974` is QSS.

## Fact vs interpretation

- **Fact:** Quoted QSS definition, hysteresis, DEVS exactness, Theorem 6 Lipschitz convergence, authors’ stiff-system step counts; IEEE 1516.1 URL served 1302-2019; arXiv titles/abstracts as retrieved.
- **Interpretation:** A Homebase **event calendar** could schedule **quantum-crossing** (or analytic TOI) independently of **display dt**; RK4 can remain the in-play integrator (H1/H2).
- **Not fact:** Measured conservation; QSS vs RK4 on rally tape; HLA TM.

## Benchmark provenance

**not executed** (Mem available 6.4 Gi < 8 Gi; later loadavg-1m 6.31). No artifact under `evidence/cycle-008-*`. Kofman 2001 step counts are **citation**, not our run.

## Decision

Keep charter H1–H3. Add Pareto axis: **fixed-step ODE vs QSS/DEVS quantized state** as *solver contract*, sibling to DES-ops vs ODE-court (c7) and FMI communication points (c1). **Do not** promote H3. **Do not** treat QSS as a second physics authority for score.

**Next:** pinned **net/rally tape** (segment-plane vs discrete vs TOI) when loadavg-1m < 4 **and** Mem available > 8 Gi; else **HLA 1516.1/.2 Time Management from a verified PDF** (not standards.ieee.org HTML) or a **tiny CPU QSS vs RK4 on a Lipschitz scalar ODE** (held-out closed form; 120 s / 2 threads / 1 GiB) if RAM still < 8 Gi but loadavg-1m < 4.

## Limitations

- Kofman 2001 is first-order QSS with hysteresis; later QSS2/QSS3/LIQSS not fully read (abstracts only).
- retQSS/LIQSS claims unbenchmarked here.
- HLA still blocked (wrong IEEE pages, 404/000 PDFs).
- Wikipedia unused for claims.
- Host swap 31–32 Gi used; experiment policy remains research-only under RAM pressure.

## Dedup

Does not re-fetch FMI/CCD/DTDL/jobs/Modelica/Ptolemy. Does not rerun AABB. Does not claim scoreboard independence. Does not keep the 800 KiB PDF in the KB.

## URLs

- https://www.fceia.unr.edu.ar/~kofman/files/qss.pdf
- https://arxiv.org/abs/2512.17855
- https://arxiv.org/abs/2006.05495
- Discarded: https://standards.ieee.org/ieee/1516.1/5898/ (IEEE 1302-2019)
- Discarded: https://arxiv.org/abs/1211.4974 (not QSS)
