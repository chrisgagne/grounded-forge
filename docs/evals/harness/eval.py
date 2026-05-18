#!/usr/bin/env python3
"""Blind LLM-judge runner for the comparative eval.

The four methods (A, B, C, D; see ../methodology.md) are run manually by
the operator in their natural product surface and pasted into
{manual-dir}/{prompt-stem}-{A|B|C|D}.md. This script loads those paste-
results, picks a rubric (essay or default) from ./judge-prompts/, and asks
a blind judge in a fresh API session to score and rank them.

The judge is the only thing this script runs. Method execution is your job
in Claude.ai, Claude Code, or the built app folder.

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=sk-ant-...

    # Collect the four answers manually, save to _evals/manual/:
    #   _evals/manual/e01-stakeholder-conflict-A.md
    #   _evals/manual/e01-stakeholder-conflict-B.md
    #   _evals/manual/e01-stakeholder-conflict-C.md
    #   _evals/manual/e01-stakeholder-conflict-D.md

    # Run the judge:
    python eval.py e01-stakeholder-conflict

    # Or against a different prompts/manual/out directory:
    python eval.py e01-stakeholder-conflict --prompts-dir ./prompts --manual-dir _evals/manual --out-dir _evals/results

Default paths assume the script lives at docs/evals/harness/ in this repo.
Output and manual-paste directories default to _evals/ (gitignored) so
private runs don't pollute the public tree.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import re
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Install the Anthropic SDK first: pip install anthropic", file=sys.stderr)
    sys.exit(1)

HARNESS_DIR = Path(__file__).resolve().parent
REPO_ROOT = HARNESS_DIR.parent.parent.parent
PROMPTS_DIR_DEFAULT = HARNESS_DIR / "prompts"
JUDGE_PROMPTS_DIR = HARNESS_DIR / "judge-prompts"
MANUAL_DIR_DEFAULT = REPO_ROOT / "_evals" / "manual"
OUT_DIR_DEFAULT = REPO_ROOT / "_evals" / "results"

JUDGE_MODEL_DEFAULT = "claude-opus-4-7"


def parse_prompt_file(path: Path) -> tuple[str, str]:
    """Return (title, body). Title is line 1 (`# Title`); body is everything after the first `---`."""
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text else path.stem
    parts = text.split("\n---\n", 1)
    body = parts[1].strip() if len(parts) == 2 else text
    return title, body


def load_paste_results(manual_dir: Path, prompt_stem: str) -> dict[str, str]:
    """Read {manual-dir}/{prompt-stem}-{A|B|C|D}.md and return a dict of available methods."""
    results = {}
    for method in ("A", "B", "C", "D"):
        path = manual_dir / f"{prompt_stem}-{method}.md"
        if path.exists():
            text = path.read_text(encoding="utf-8").strip()
            if text:
                results[method] = text
    return results


def judge_prompt(rubric: str) -> str:
    """Read judge-prompts/{rubric}.md."""
    path = JUDGE_PROMPTS_DIR / f"{rubric}.md"
    if not path.exists():
        available = ", ".join(p.stem for p in JUDGE_PROMPTS_DIR.glob("*.md"))
        raise SystemExit(f"Rubric '{rubric}' not found. Available: {available}")
    return path.read_text(encoding="utf-8")


def run_judge(client: anthropic.Anthropic, model: str, rubric_text: str, prompt: str, method_answers: dict[str, str], seed: int) -> dict:
    """Shuffle the four method answers, ask the judge to score and rank, decode back to method codes."""
    rng = random.Random(seed)
    items = list(method_answers.items())
    rng.shuffle(items)

    label_to_method = {f"answer_{i + 1}": m for i, (m, _) in enumerate(items)}
    answers_block = "\n\n".join(
        f"## answer_{i + 1}\n\n{ans}" for i, (_, ans) in enumerate(items)
    )

    user_message = f"## Prompt\n\n{prompt}\n\n## Answers to evaluate\n\n{answers_block}"

    resp = client.messages.create(
        model=model,
        max_tokens=4000,
        system=rubric_text,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = "".join(block.text for block in resp.content if hasattr(block, "text"))

    json_match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not json_match:
        return {"error": "could not find JSON in judge response", "raw": raw, "label_to_method": label_to_method}
    try:
        parsed = json.loads(json_match.group(0))
    except json.JSONDecodeError as e:
        return {"error": f"could not parse judge JSON: {e}", "raw": raw, "label_to_method": label_to_method}

    decoded_ranking = [label_to_method[label] for label in parsed.get("ranking", []) if label in label_to_method]
    decoded_scores = {
        label_to_method[label]: scores
        for label, scores in parsed.get("scores", {}).items()
        if label in label_to_method
    }

    return {
        "ranking": decoded_ranking,
        "scores": decoded_scores,
        "rationale": parsed.get("rationale", ""),
        "label_to_method": label_to_method,
        "raw": raw,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("prompt_stem", help="prompt file stem, e.g. 'e01-stakeholder-conflict'")
    parser.add_argument("--prompts-dir", default=str(PROMPTS_DIR_DEFAULT), help=f"prompts directory (default: {PROMPTS_DIR_DEFAULT.relative_to(REPO_ROOT)})")
    parser.add_argument("--manual-dir", default=str(MANUAL_DIR_DEFAULT), help=f"manual paste-result directory for A, B, C, D (default: {MANUAL_DIR_DEFAULT.relative_to(REPO_ROOT)}; gitignored)")
    parser.add_argument("--out-dir", default=str(OUT_DIR_DEFAULT), help=f"output directory for judge result JSON (default: {OUT_DIR_DEFAULT.relative_to(REPO_ROOT)}; gitignored)")
    parser.add_argument("--rubric", default="essay", help=f"judge rubric name (file under {JUDGE_PROMPTS_DIR.relative_to(REPO_ROOT)}/, without .md). Default: essay.")
    parser.add_argument("--seed", type=int, default=1, help="shuffle seed for blind labelling (default: 1)")
    parser.add_argument("--model", default=JUDGE_MODEL_DEFAULT, help=f"model for the blind judge (default: {JUDGE_MODEL_DEFAULT})")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY in the environment.", file=sys.stderr)
        return 1

    prompt_path = Path(args.prompts_dir) / f"{args.prompt_stem}.md"
    if not prompt_path.exists():
        print(f"Prompt file not found: {prompt_path}", file=sys.stderr)
        return 1

    manual_dir = Path(args.manual_dir)
    paste_results = load_paste_results(manual_dir, args.prompt_stem)
    if len(paste_results) < 2:
        print(f"Need at least 2 paste-results in {manual_dir} for prompt {args.prompt_stem}. Found: {sorted(paste_results.keys())}", file=sys.stderr)
        return 1

    title, prompt_body = parse_prompt_file(prompt_path)
    rubric_text = judge_prompt(args.rubric)

    print(f"Judging {args.prompt_stem} ({title}) with rubric '{args.rubric}', seed {args.seed}.")
    print(f"Methods loaded: {sorted(paste_results.keys())}")

    client = anthropic.Anthropic()
    result = run_judge(client, args.model, rubric_text, prompt_body, paste_results, args.seed)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = out_dir / f"{stamp}-{args.prompt_stem}-judge-seed{args.seed}.json"
    out_path.write_text(json.dumps(result, indent=2) + "\n")

    if "error" in result:
        print(f"\nJudge error: {result['error']}", file=sys.stderr)
        print(f"Raw response saved to {out_path}")
        return 1

    print(f"\nRanking: {' > '.join(result['ranking'])}")
    print(f"\nScores:")
    for method, scores in result["scores"].items():
        score_str = ", ".join(f"{k}={v}" for k, v in scores.items())
        print(f"  {method}: {score_str}")
    print(f"\nRationale: {result['rationale']}")
    print(f"\nSaved to: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
