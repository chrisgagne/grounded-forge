#!/usr/bin/env python3
"""Answer quote-check regression tests: `.claude/skills/answer-from-corpus/check_quotes.py`.

The check exists because answers put a summary layer's wording in quote marks as the
author's own (the Gemini Notebook evaluation, October 2026: a distillation's list item
quoted as Dekker; a light reference's paraphrase quoted as Dekker; a reworded Brush
question). Each case writes a hermetic corpus (project mode) or app (app mode) and an
answer, runs the real CLI with --json, and checks the status each quotation lands at.

No test framework, matching tests/check-verbatim.test.py: each case succeeds silently or
raises; the runner collects failures, prints a summary, exits non-zero.

Usage:
    python3 tests/check-quotes.test.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / ".claude" / "skills" / "answer-from-corpus" / "check_quotes.py"

SOURCE = """Chapter 8

Adding just a little bit more technology will likely create new work for people,
new error opportunities and new path-
ways to breakdown.

People do not come to work to do a bad job. The question is not how we get rid
of bad apples, but in what way we are responsible for creating them.
"""

REFERENCE = """# Dekker, Field Guide (light)

Core reframes: avoid firing or sanctioning people simply because they were involved in an
incident; ask what is responsible, not who.
"""

INDEX = {"refs": {"000": {"slug": "sample-human-error-guide", "author": "Dekker, Sidney", "title": "The Field Guide to Understanding 'Human Error'"}}}

DISTILLATION = """# Dekker — *The Field Guide to Understanding 'Human Error'* — AAR Application Guide

**Source Framework:** Sidney Dekker. *The Field Guide to Understanding 'Human Error'*. 3rd ed. 2014.

## The four false quick fixes

1. Reprimand
2. Retrain
3. Add a little more technology (creates new work and new error modes)

> "People do not come to work to do a bad job." (Ch 1) [V]
"""


def project(tmp: Path) -> Path:
    root = tmp / "corpus"
    (root / "sources" / "converted").mkdir(parents=True)
    (root / "references").mkdir()
    (root / "sources" / "converted" / "sample-human-error-guide.md").write_text(SOURCE)
    (root / "references" / "sample-human-error-guide.md").write_text(REFERENCE)
    (root / "reference-index.json").write_text(json.dumps(INDEX))
    return root


def app(tmp: Path) -> Path:
    root = tmp / "app"
    (root / "distillations" / "aar").mkdir(parents=True)
    (root / "distillations" / "aar" / "sample-human-error-guide-aar.md").write_text(DISTILLATION)
    return root


def run(root: Path, answer: str, inputs: list[Path] | None = None) -> dict:
    args = [sys.executable, str(SCRIPT), "-", "--root", str(root), "--json"]
    for p in inputs or []:
        args += ["--input", str(p)]
    r = subprocess.run(args, input=answer, capture_output=True, text=True)
    if r.returncode not in (0, 1):
        raise AssertionError(f"exit {r.returncode}: {r.stderr}")
    return json.loads(r.stdout)


def statuses(result: dict) -> list[str]:
    return [x["status"] for x in result["results"]]


def case_project_source_quote_passes(tmp):
    r = run(project(tmp), 'Dekker puts it plainly: "the question is not how we get rid of bad apples".\n')
    assert statuses(r) == ["ok"], r


def case_project_line_break_hyphen_and_ellipsis(tmp):
    r = run(project(tmp), 'Dekker warns that "adding just a little bit more technology ... new pathways to breakdown".\n')
    assert statuses(r) == ["ok"], r


def case_project_reference_wording_is_layer(tmp):
    r = run(project(tmp), 'Dekker says to avoid "firing or sanctioning people simply because they were involved in an incident".\n')
    assert statuses(r) == ["LAYER"], r


def case_project_reworded_quote_is_missing(tmp):
    r = run(project(tmp), 'Dekker says "people never come to work to do a bad job".\n')
    assert statuses(r) == ["MISSING"], r


def case_unattributed_quote_is_not_checked(tmp):
    r = run(project(tmp), 'Tell the VP: "we will own every fix by Friday".\n')
    assert r["checked"] == 0 and r["unattributed"] == 1, r


def case_title_is_skipped(tmp):
    r = run(project(tmp), 'Dekker, in "The Field Guide To Understanding Error", says much.\n')
    assert r["checked"] == 0, r


def case_input_material_passes(tmp):
    notes = tmp / "notes.txt"
    notes.write_text("Honestly, I think he just wasn't paying attention; he's fairly new.\n")
    r = run(project(tmp), 'Dekker would ask about the manager\'s view, "he just wasn\'t paying attention".\n', [notes])
    assert statuses(r) == ["input"], r


def case_app_distillation_prose_is_layer(tmp):
    r = run(app(tmp), 'It is one of Dekker\'s false quick fixes, "add a little more technology".\n')
    assert statuses(r) == ["LAYER"], r


def case_app_marked_verbatim_passes(tmp):
    r = run(app(tmp), 'Dekker: "people do not come to work to do a bad job".\n')
    assert statuses(r) == ["ok"], r


def case_two_quotes_on_a_line_dont_pair_across(tmp):
    r = run(project(tmp), 'Labels like "complacency" or inattention, Dekker says, "the question is not how we get rid of bad apples".\n')
    assert statuses(r) == ["ok"], r


def case_app_source_header_and_accented_author(tmp):
    root = tmp / "app2"
    (root / "distillations" / "aar").mkdir(parents=True)
    (root / "distillations" / "aar" / "gagne-field-guide-aar.md").write_text(
        "# Field Guide, AAR Distillation\n\n**Source:** Chris Gagné (2020). *The Field Guide to Scrum Events*. CC BY 4.0.\n\n"
        "Retrospectives are where teams inspect how they work.\n")
    r = run(root, 'Gagné writes that "retrospectives are where teams inspect how they work".\n')
    assert statuses(r) == ["LAYER"], r


CASES = [v for k, v in sorted(globals().items()) if k.startswith("case_")]


def main() -> int:
    failures = []
    for case in CASES:
        with tempfile.TemporaryDirectory() as d:
            try:
                case(Path(d))
            except Exception as e:  # noqa: BLE001 - report every failure, keep going
                failures.append(f"{case.__name__}: {e}")
    for f in failures:
        print("FAIL", f)
    print(f"{len(CASES) - len(failures)}/{len(CASES)} check-quotes cases passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
