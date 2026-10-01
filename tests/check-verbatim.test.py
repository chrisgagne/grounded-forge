#!/usr/bin/env python3
"""Verbatim-check regression tests: the matching ladder in `scripts/check-verbatim.py`.

The check exists so a Pass I auditor gets every `[V]` and blockquote mismatch in
one run. It is only useful if conversion noise reads as a match and an author's
changed character never does. Each case below writes one quotation into a
hermetic deep reference, runs the real CLI against a synthetic converted source
(passed with --source, so no corpus is touched), and checks the level it lands at.

Cases mirror the Pass I audit fixtures where they can: 05 (apostrophe style →
apostrophe, not failing), 06 (capitalisation tidy → near), 07 ([V] on a paraphrase → no-quote),
09 (silently shortened quote → interrupted or missing).

No test framework, matching tests/derived-provenance.test.py: each case succeeds
silently or raises; the runner collects failures, prints a summary, exits non-zero.

Usage:
    python3 tests/check-verbatim.test.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check-verbatim.py"

ZWSP = chr(0x200B)

SOURCE = f"""# Chapter 4

## Schedules of Reinforcement

In other words, the performance-contingent (or ratio) reward schedules generally lead to better
behavior than the time-contingent (or interval) schedules, regardless of whether such schedules are
fixed or variable.

Supervisors said: I don't give high ratings because I don't want people to think they can stop trying.

Managers who **plan** carefully find that the fexibility they need comes from re-{ZWSP}mapping the
organi-
zation every quarter, not from the "big bang" reorganisation.

Relationship conflict, unlike task and process conflict, tends to corrode the trust that teams depend on.

Feedback is widely recognized by educators as the most
51
effective tool for experiential teaching.

The first step is to listen. Then the second step is to summarise what you heard, and only then the third step is to respond.

Work is an activity that produces something of value for other people.

The second resource is called role perceptions—how employees believe their jobs are done.

A ﬁnal word on ﬁxing things that are not broken.
"""

# (label, deep-ref line, expected kind or None for a clean match)
CASES = [
    ("exact through conversion noise",
     'Managers find that "they need comes from re-mapping the organization every quarter, not from the \'big bang\' reorganisation" [V] (Ch 4).',
     None),
    ("exact through a ligature glyph",
     '"A final word on fixing things that are not broken" [V] (Ch 4).',
     None),
    ("exact with trailing comma inside the closing quote",
     'Work is "an activity that produces something of value for other people," [V] (Ch 4).',
     None),
    ("exact with an ellipsis elision",
     '"The first step is to listen ... the third step is to respond" [V] (Ch 4).',
     None),
    ("exact with a bracketed insertion",
     '"Relationship conflict [between members] tends to corrode the trust that teams depend on" [V] (Ch 4).',
     None),
    ("citation titles are not checked",
     'The text says "Work is an activity that produces something of value" [V] (Ch 4, "Some Title Not In Source").',
     None),
    ("fixture 05: apostrophe style → apostrophe",
     '> "I don’t give high ratings because I don’t want people to think they can stop trying."',
     "apostrophe"),
    ("a dash set open where the source sets it closed is exact",
     '"The second resource is called role perceptions — how employees believe their jobs are done" [V] (Ch 4).',
     None),
    ("a changed dash → glyph",
     '"The second resource is called role perceptions – how employees believe their jobs are done" [V] (Ch 4).',
     "glyph"),
    ("an illustrative phrase a sentence before the [V] is not checked",
     'Teams say "we will look into it" and move on. The text is blunt: "Work is an activity that produces something of value" [V] (Ch 4).',
     None),
    ("fixture 06: capitalisation tidy → near",
     '"The performance-contingent (or ratio) reward schedules generally lead to better Behavior than the time-contingent (or interval) schedules" [V] (Ch 4).',
     "near"),
    ("first-letter case only → initial",
     'They note that "An activity that produces something of value" [V] (Ch 4).',
     None),
    ("page number inside the passage → page",
     '"widely recognized by educators as the most effective tool for experiential teaching" [V] (Ch 4).',
     "page"),
    ("fixture 09: shortened without an ellipsis → interrupted",
     '"Then the second step is to summarise what you heard, and the third step is to respond" [V] (Ch 4).',
     "interrupted"),
    ("fixture 09: reworded → missing",
     '"Relationship conflict tends to erode the trust that teams rely on" [V] (Ch 4).',
     "missing"),
    ("fixture 07: [V] on a paraphrase → no-quote",
     'The source defines work as producing value for others [V] (Ch 4).',
     "no-quote"),
    ("a quoted remark ending its own sentence is not checked",
     'The team said "we were running out of time." The text is blunt: "Work is an activity that produces something of value" [V] (Ch 4).',
     None),
    ("a quotation ending in a full stop just before its [V] is checked",
     'The text is plain. "Relationship conflict tends to erode the trust that teams rely on." [V] (Ch 4).',
     "missing"),
    ("a ligature the converter cut short → ligature",
     '"Managers who plan carefully find that the flexibility they need" [V] (Ch 4).',
     "ligature"),
    ("a figure claim is counted, not flagged",
     '| Reward schedules compared | 4 | [V] (Ch 4) |',
     None),
]


def run(deep: Path, source: Path) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(deep), "--source", str(source), "--json", "--no-corpus-search"],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    return proc.returncode, json.loads(proc.stdout)


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        source = tmpd / "source.md"
        source.write_text(SOURCE, encoding="utf-8")
        deep = tmpd / "case-deep.md"
        lines = ["# Synthetic deep reference", ""]
        expect: dict[int, tuple[str, str | None]] = {}
        for label, text, kind in CASES:
            lines.append(text)
            expect[len(lines)] = (label, kind)
            lines.append("")
        deep.write_text("\n".join(lines), encoding="utf-8")

        code, out = run(deep, source)
        got: dict[int, set[str]] = {}
        for f in out["findings"]:
            got.setdefault(f["line"], set()).add(f["kind"])
        for line, (label, kind) in expect.items():
            kinds = got.get(line, set())
            if label.startswith("first-letter"):
                kind_ok = kinds == {"initial"}
            else:
                kind_ok = kinds == ({kind} if kind else set())
            if not kind_ok:
                failures.append(f"{label}: expected {kind or 'no finding'}, got {sorted(kinds) or 'no finding'}")
        if out["figure_claims_unchecked"] != 1:
            failures.append(f"figure claims: expected 1 counted, got {out['figure_claims_unchecked']}")
        if code != 1:
            failures.append(f"exit status with failing findings: expected 1, got {code}")

        # `initial` alone does not fail the run.
        only_initial = tmpd / "initial-deep.md"
        only_initial.write_text('# x\n\nThey note that "An activity that produces something of value" [V] (Ch 4).\n', encoding="utf-8")
        code, _ = run(only_initial, source)
        if code != 0:
            failures.append(f"exit status with only an initial finding: expected 0, got {code}")

    total = len(CASES) + 3
    if failures:
        print(f"{len(failures)} of {total} checks failed:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"All {total} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
