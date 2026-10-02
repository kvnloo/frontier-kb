# PsychoPy choice-response + photodiode harness

This is a deliberately simple first behavioral test.

Each trial:

1. waits a randomized interval;
2. presents a left/right visual target;
3. turns a corner photodiode patch white on the same flip;
4. resets PsychoPy's hardware-keyboard clock on that flip;
5. records the asynchronously timestamped left/right response;
6. returns the patch to black after one frame.

## Install

Use a current PsychoPy environment.

## Run

```sh
python choice_rt_photodiode.py --condition baseline --trials 120
python choice_rt_photodiode.py --condition vrr-on --trials 120
```

Keep the photodiode position fixed.

## Correct response time

The CSV's `key_rt_s` is software-flip referenced.

Once Wave 4 photon data is synchronized, compute:

```text
photon_referenced_rt =
key_press_absolute_time - photon_t10_or_t50
```

Use the same photon fiducial across all conditions.

## Analysis

```sh
python analyze_choice_rt.py choice-rt-*.csv
```

Always report accuracy alongside reaction time.

## Design

Do not run all trials of A and then all trials of B if fatigue/learning could matter. Prefer randomized/alternating blocks across sessions.

This harness intentionally does not implement BFI/strobing itself.
