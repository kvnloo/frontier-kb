#!/usr/bin/env python3
import argparse
import csv
import math
import statistics
from collections import defaultdict


def percentile(values, q):
    values = sorted(values)
    if not values:
        return float("nan")
    idx = round((len(values) - 1) * q)
    return values[idx]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv", nargs="+")
    args = p.parse_args()

    groups = defaultdict(list)
    for path in args.csv:
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                if row["timeout"] == "1" or not row["key_rt_s"]:
                    continue
                groups[row["condition"]].append(
                    (float(row["key_rt_s"]) * 1000.0, int(row["correct"]))
                )

    for condition, rows in sorted(groups.items()):
        rts = [rt for rt, _ in rows]
        accuracy = sum(ok for _, ok in rows) / len(rows)
        correct_rts = [rt for rt, ok in rows if ok]
        print(f"condition={condition}")
        print(f"  n={len(rows)}")
        print(f"  accuracy={accuracy:.4f}")
        if correct_rts:
            print(f"  correct_rt_median_ms={statistics.median(correct_rts):.3f}")
            print(f"  correct_rt_p10_ms={percentile(correct_rts, .10):.3f}")
            print(f"  correct_rt_p90_ms={percentile(correct_rts, .90):.3f}")
            print(f"  correct_rt_p95_ms={percentile(correct_rts, .95):.3f}")
            print(f"  correct_rt_mean_ms={statistics.fmean(correct_rts):.3f}")
            if len(correct_rts) > 1:
                print(f"  correct_rt_sd_ms={statistics.stdev(correct_rts):.3f}")
        print()


if __name__ == "__main__":
    main()
