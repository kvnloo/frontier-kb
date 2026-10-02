# Motion-orientation task

This task turns motion clarity into a measurable behavioral curve.

A Gabor target moves across the display at one of several speeds and is tilted left or right. The participant reports orientation with the arrow keys.

The first target frame also produces a photodiode edge.

## Run

For meaningful degrees/second, configure the PsychoPy monitor geometry and pass its name:

```sh
python motion_orientation.py \
  --monitor my-display \
  --condition baseline \
  --speeds 2,4,8,12,16 \
  --trials-per-speed 30
```

Repeat under a second display/render condition:

```sh
python motion_orientation.py \
  --monitor my-display \
  --condition bfi \
  --speeds 2,4,8,12,16 \
  --trials-per-speed 30
```

Analyze:

```sh
python analyze_motion.py motion-clarity-*.csv
```

The output is accuracy and correct-response time by target speed.

## Interpretation

A motion-clarity improvement should shift the accuracy-vs-speed curve without hiding a large input-to-photon penalty.

Keep brightness and target contrast documented across persistence/BFI/strobe conditions.
