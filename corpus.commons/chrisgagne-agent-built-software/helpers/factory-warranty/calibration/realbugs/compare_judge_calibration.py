#!/usr/bin/env python3
"""Does the CLI-backed judge score the same as the API judge?

Per PREREG-judge-calibration-2026-10-22.md: compares the five calibration pull requests as the API judge scored
them (inside the full 23-pull-request run) with the same five as the CLI-backed judge scored them. Prints the
per-pull-request averages the head-to-head rule uses, and the gap.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
API = HERE / "results/v7-opus-own/scoring/results.json"
CLI = HERE / "results/cal-cli-opus-own/scoring/results.json"
FINDINGS = HERE / "results/cal-cli-opus-own/findings"


def pr_keys() -> list[str]:
    keys = []
    for f in sorted(FINDINGS.glob("*.json")):
        pr = json.loads(f.read_text())["pr"]
        owner_repo = pr["repo"].split("github.com/")[1].replace("/", "_")
        keys.append(f'{owner_repo}_{pr["pr_number"]}-{pr["head"][:8]}')
    return keys


def subset(path: pathlib.Path, keys: list[str]) -> dict:
    data = json.loads(path.read_text())
    by_key = {p["pr_key"]: p["metrics"] for p in data["per_pr"]}
    missing = [k for k in keys if k not in by_key]
    if missing:
        raise SystemExit(f"{path}: no scores for {missing}")
    rows = [by_key[k] for k in keys]
    n = len(rows)
    out = {
        "precision": 100 * sum(r["overall"]["grounded_precision"] for r in rows) / n,
        "recall": 100 * sum(r["overall"]["grounded_recall"] for r in rows) / n,
        "candidates": sum(r["overall"]["candidate_count"] for r in rows),
        "matched_tp": sum(r["overall"]["matched_tp_count"] for r in rows),
        "unmatched_tp": sum(r["overall"]["unmatched_tp_count"] for r in rows),
        "high_matched_tp": sum(
            r.get("by_severity", {}).get("high", {}).get("matched_tp_count", 0) for r in rows
        ),
        "per_pr": [
            (k, 100 * by_key[k]["overall"]["grounded_precision"], 100 * by_key[k]["overall"]["grounded_recall"])
            for k in keys
        ],
    }
    return out


def main() -> None:
    keys = pr_keys()
    api = subset(API, keys)
    cli = subset(CLI, keys)
    print(f"{len(keys)} pull requests: {', '.join(keys)}\n")
    print(f"{'judge':<22}{'precision':>11}{'recall':>9}{'cands':>7}{'matched TP':>12}{'high TP':>9}")
    for name, r in (("Anthropic API", api), ("Claude Code CLI", cli)):
        print(
            f"{name:<22}{r['precision']:>10.1f}%{r['recall']:>8.1f}%{r['candidates']:>7}"
            f"{r['matched_tp']:>12}{r['high_matched_tp']:>9}"
        )
    dp = cli["precision"] - api["precision"]
    dr = cli["recall"] - api["recall"]
    print(f"\ngap (CLI - API): precision {dp:+.1f} points, recall {dr:+.1f} points")
    verdict = "within" if abs(dp) < 5 and abs(dr) < 5 else "outside"
    print(f"pre-registered rule: {verdict} 5 points on both")

    print("\nper pull request (precision / recall)")
    for (k, ap, ar), (_, cp, cr) in zip(api["per_pr"], cli["per_pr"]):
        print(f"  {k:<44} API {ap:5.1f}/{ar:5.1f}   CLI {cp:5.1f}/{cr:5.1f}")


if __name__ == "__main__":
    main()
