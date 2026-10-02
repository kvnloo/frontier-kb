# PsychoPy — human-response measurement layer

PsychoPy is actively maintained and explicitly targets precise psychophysics/neuroscience experiments.

Use it as the human-measurement layer rather than building timing code from scratch.

## Experiment A — simple choice response

Randomly present a left/right target.

On the same display flip:

- show the target;
- flash a photodiode patch;
- reset the response clock.

Record:

- requested/actual flip time
- photodiode t10/t50/t90
- key/button timestamp
- correctness

Run enough randomized trials per condition to estimate the full response-time distribution.

## Experiment B — moving-detail discrimination

Use a moving Gabor/Landolt-C-like target and vary speed.

For each display/render condition estimate the speed at which the user can still identify the target orientation at a fixed accuracy criterion.

Compare:

- persistence baseline
- BFI/strobe conditions
- refresh rates
- frame-generation states

This gives a motion-clarity behavioral metric rather than relying on subjective "looks clearer."

## Experiment C — latency perturbation JND

Inject controlled extra delay in known increments while keeping all other rendering behavior fixed.

Use forced-choice trials to estimate when participants can discriminate which interval felt more responsive.

Do **not** infer clinical/neuroscience traits from individual results; this is a systems/perception calibration task.

## Experimental design

Prefer:

- within-subject randomized blocks
- hidden condition labels
- warm-up block
- equal trial counts
- accuracy + RT together
- raw trial-level data

Never interpret a faster RT as a win if accuracy falls.
