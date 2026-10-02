# Human/perceptual metric contract

## Physical metrics

Keep from Wave 4:

- input/USB timestamp
- DRM first-pixel
- photon t10
- photon t50
- photon t90

## Behavioral metrics

Per trial record:

- condition
- stimulus ID
- physical stimulus-onset time
- response timestamp
- correctness
- target speed / difficulty
- display mode
- refresh / VRR / BFI / FG state

Derived:

```text
reaction_time = response - photon_onset
error_rate
motion_threshold
tracking_error
```

## Analysis rule

Latency optimization is multi-objective.

Always show:

- RT distribution
- accuracy
- physical photon latency
- brightness/duty cycle for BFI
- workload/FPS
- motion-clarity metric

Do not create a single weighted "human performance score" unless the weighting is specified before the experiment.

## Bias control

- randomize condition order
- hide labels where practical
- use warm-up trials
- discard hardware-failed trials using photodiode/trigger receipts, not subjective judgment
- retain raw trial data
- repeat across sessions

## Interpretation

A 3 ms physical latency win may be real even when a behavioral experiment lacks statistical power to detect it.

Conversely, a subjective preference does not prove lower latency.

Keep physical and behavioral claims separate.
