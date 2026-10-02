#!/usr/bin/env python3
import argparse
import csv
import statistics
from collections import defaultdict


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv", nargs="+")
    args = p.parse_args()

    grouped = defaultdict(list)
    for path in args.csv:
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                key = (row["condition"], float(row["speed_deg_s"]))
                grouped[key].append(row)

    print("condition,speed_deg_s,n,accuracy,median_correct_rt_ms")
    for (condition, speed), rows in sorted(grouped.items()):
        n = len(rows)
        correct = [r for r in rows if r["correct"] == "1"]
        accuracy = len(correct) / n if n else float("nan")
        rts = [float(r["rt_s"]) * 1000.0 for r in correct if r["rt_s"]]
        med = statistics.median(rts) if rts else float("nan")
        print(f"{condition},{speed:g},{n},{accuracy:.4f},{med:.3f}")


if __name__ == "__main__":
    main()
