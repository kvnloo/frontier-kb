#!/usr/bin/env python3
import argparse
import csv
import random
import time
from pathlib import Path

from psychopy import core, visual
from psychopy.hardware import keyboard


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--trials", type=int, default=120)
    p.add_argument("--condition", default="baseline")
    p.add_argument("--output", type=Path, default=None)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--windowed", action="store_true")
    p.add_argument("--timeout", type=float, default=1.5)
    return p.parse_args()


def main():
    args = parse_args()
    rng = random.Random(args.seed)

    out = args.output
    if out is None:
        stamp = time.strftime("%Y%m%d-%H%M%S")
        out = Path(f"choice-rt-{args.condition}-{stamp}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)

    win = visual.Window(
        fullscr=not args.windowed,
        color=(-0.5, -0.5, -0.5),
        units="height",
        waitBlanking=True,
    )
    win.recordFrameIntervals = True

    kb = keyboard.Keyboard()
    fixation = visual.TextStim(win, text="+", height=0.05, color="white")
    left_target = visual.Rect(
        win, width=0.10, height=0.10, pos=(-0.25, 0), fillColor="white", lineColor="white"
    )
    right_target = visual.Rect(
        win, width=0.10, height=0.10, pos=(0.25, 0), fillColor="white", lineColor="white"
    )

    # Place under a photodiode. Keep sensor position unchanged across conditions.
    patch = visual.Rect(
        win,
        width=0.10,
        height=0.10,
        pos=(0.44, -0.44),
        fillColor="black",
        lineColor="black",
    )

    fields = [
        "trial",
        "condition",
        "side",
        "expected_key",
        "key",
        "correct",
        "key_rt_s",
        "key_tdown_s",
        "predicted_flip_s",
        "flip_return_s",
        "timeout",
    ]

    try:
        with out.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            f.flush()

            for trial in range(args.trials):
                side = rng.choice(("left", "right"))
                expected = side

                fixation.draw()
                patch.fillColor = "black"
                patch.lineColor = "black"
                patch.draw()
                win.flip()

                core.wait(rng.uniform(0.75, 1.25))

                kb.clearEvents()
                target = left_target if side == "left" else right_target
                target.draw()
                patch.fillColor = "white"
                patch.lineColor = "white"
                patch.draw()

                predicted = win.getFutureFlipTime(clock="now")
                win.callOnFlip(kb.clock.reset)
                flip_return = win.flip()

                # Only the onset frame is white for a clean photodiode edge.
                patch.fillColor = "black"
                patch.lineColor = "black"

                response = None
                timer = core.Clock()
                while timer.getTime() < args.timeout:
                    target.draw()
                    patch.draw()
                    win.flip()

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

                if response is None:
                    row = {
                        "trial": trial,
                        "condition": args.condition,
                        "side": side,
                        "expected_key": expected,
                        "key": "",
                        "correct": 0,
                        "key_rt_s": "",
                        "key_tdown_s": "",
                        "predicted_flip_s": predicted,
                        "flip_return_s": flip_return,
                        "timeout": 1,
                    }
                else:
                    row = {
                        "trial": trial,
                        "condition": args.condition,
                        "side": side,
                        "expected_key": expected,
                        "key": response.name,
                        "correct": int(response.name == expected),
                        "key_rt_s": response.rt,
                        "key_tdown_s": response.tDown,
                        "predicted_flip_s": predicted,
                        "flip_return_s": flip_return,
                        "timeout": 0,
                    }

                writer.writerow(row)
                f.flush()

        intervals_path = out.with_suffix(".frame_intervals.csv")
        with intervals_path.open("w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["frame_interval_s"])
            for interval in win.frameIntervals:
                writer.writerow([interval])

        print(f"wrote {out}")
        print(f"wrote {intervals_path}")
    finally:
        win.close()
        core.quit()


if __name__ == "__main__":
    main()
