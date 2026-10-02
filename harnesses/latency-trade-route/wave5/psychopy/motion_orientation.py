#!/usr/bin/env python3
import argparse
import csv
import random
import time
from pathlib import Path

from psychopy import core, visual
from psychopy.hardware import keyboard


def parse_speeds(value):
    return [float(x.strip()) for x in value.split(",") if x.strip()]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--condition", default="baseline")
    p.add_argument("--trials-per-speed", type=int, default=30)
    p.add_argument("--speeds", type=parse_speeds, default=parse_speeds("2,4,8,12,16"))
    p.add_argument("--monitor", default=None)
    p.add_argument("--output", type=Path, default=None)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--windowed", action="store_true")
    return p.parse_args()


def main():
    args = parse_args()
    rng = random.Random(args.seed)

    if args.output is None:
        stamp = time.strftime("%Y%m%d-%H%M%S")
        args.output = Path(f"motion-clarity-{args.condition}-{stamp}.csv")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    win_kwargs = dict(
        fullscr=not args.windowed,
        color=(-0.5, -0.5, -0.5),
        units="deg",
        waitBlanking=True,
    )
    if args.monitor:
        win_kwargs["monitor"] = args.monitor

    win = visual.Window(**win_kwargs)
    kb = keyboard.Keyboard()

    fixation = visual.TextStim(win, text="+", height=0.5, color="white", units="deg")
    patch = visual.Rect(
        win,
        width=2.0,
        height=2.0,
        pos=(10.0, -6.0),
        fillColor="black",
        lineColor="black",
        units="deg",
    )

    gabor = visual.GratingStim(
        win,
        tex="sin",
        mask="gauss",
        sf=2.0,
        size=3.0,
        contrast=1.0,
        units="deg",
    )

    trials = []
    for speed in args.speeds:
        for _ in range(args.trials_per_speed):
            trials.append((speed, rng.choice((-45.0, 45.0))))
    rng.shuffle(trials)

    fields = [
        "trial",
        "condition",
        "speed_deg_s",
        "orientation_deg",
        "expected_key",
        "key",
        "correct",
        "rt_s",
        "stimulus_duration_s",
        "flip_onset_s",
    ]

    try:
        with args.output.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for trial_index, (speed, orientation) in enumerate(trials):
                fixation.draw()
                patch.fillColor = "black"
                patch.lineColor = "black"
                patch.draw()
                win.flip()
                core.wait(rng.uniform(0.6, 1.0))

                expected = "left" if orientation < 0 else "right"
                start_x = -8.0
                duration = 0.35
                frame_period = win.monitorFramePeriod or (1.0 / 60.0)
                frames = max(1, round(duration / frame_period))

                kb.clearEvents()
                win.callOnFlip(kb.clock.reset)

                flip_onset = None
                for frame in range(frames):
                    elapsed = frame * frame_period
                    gabor.ori = orientation
                    gabor.pos = (start_x + speed * elapsed, 0.0)
                    gabor.draw()

                    patch.fillColor = "white" if frame == 0 else "black"
                    patch.lineColor = patch.fillColor
                    patch.draw()

                    t = win.flip()
                    if frame == 0:
                        flip_onset = t

                response = None
                timer = core.Clock()
                while timer.getTime() < 1.2:
                    keys = kb.getKeys(
                        keyList=["left", "right", "escape"],
                        waitRelease=False,
                        clear=True,
                    )
                    if keys:
                        response = keys[0]
                        if response.name == "escape":
                            return
                        break
                    core.wait(0.001)

                writer.writerow(
                    {
                        "trial": trial_index,
                        "condition": args.condition,
                        "speed_deg_s": speed,
                        "orientation_deg": orientation,
                        "expected_key": expected,
                        "key": "" if response is None else response.name,
                        "correct": int(response is not None and response.name == expected),
                        "rt_s": "" if response is None else response.rt,
                        "stimulus_duration_s": duration,
                        "flip_onset_s": flip_onset,
                    }
                )
                f.flush()

        print(f"wrote {args.output}")
    finally:
        win.close()
        core.quit()


if __name__ == "__main__":
    main()
