#!/usr/bin/env python3
"""Verbatim-check regression tests: the matching ladder in `scripts/check-verbatim.py`.

The check exists so a Pass I auditor gets every `[V]` and blockquote mismatch in
one run. It is only useful if conversion noise reads as a match and an author's
changed character never does. Each case below writes one quotation into a
hermetic deep reference, runs the real CLI against a synthetic converted source
(passed with --source, so no corpus is touched), and checks the level it lands at.

Cases mirror the Pass I audit fixtures where they can: 05 (apostrophe style →
apostrophe, not failing), 06 (capitalisation tidy → near), 07 ([V] on a paraphrase → no-quote),
09 (silently shortened quote → interrupted or missing). The figure cases hold the
rule that no normalisation lets a changed figure pass: a quote that cuts a number
short at either end never matches. The paged section mirrors
MCDP 1's conversion: running headers and folios between pages, and a quote that
holds both a word split across a line and a compound split across a line.

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

The e"ort to make the o#ce run e#ciently was signi%cant, and the work!ow was the fi rst thing to change.

Satisfaction rose by 3.5 points in the second quarter, while turnover rose by 30 points over the year.

The firm hired 2,500 people that year. The plant closed in 1998. It never reopened.
"""


def page_break(folio: int, header: str = "Field Manual") -> str:
    """A folio at the foot of a page, a form feed, the next page's running header."""
    return f"\n\n{folio}\n\f\f{header}\n\nFM 1\n\n"


# Pages of a converted PDF: a passage runs across each break.
SOURCE += (
    "Mission tactics leave the manner of accomplishing the mission to the subordinate, thereby\n"
    "allowing the freedom to take whatever steps are deemed necessary based on the"
    + page_break(41)
    + "situation. Chance is a universal characteristic of war and a continuous"
    + page_break(42)
    + "source of friction. The enemy must be made to see the situation not only as\n"
    "deteriorating, but deteriorating at an ever-\n"
    "increasing rate, and the situa-\n"
    "tion must change faster than he can follow. Speed over time is tempo, the ability to operate\n"
    "quickly."
    + page_break(43, header="FieId Manual")
    + "Commanders must rely on the initiative of subordinates to locate gaps and must have the\n"
    "flexibility to respond quick-"
    + page_break(44)
    + "ly to opportunities rather than blindly follow predetermined schemes."
    + page_break(45)
    + "Plans will go awry and instructions will be unclear.\n\nKey Point\n\n"
    "Units must adapt to the situation as it changes."
    + page_break(46)
    # A folio set on the running header's own line, with no form feed.
    + "".join(f"Filler paragraph {n} for the handbook.\n\n{n} Doctrine Handbook\n\n" for n in range(60, 64))
    + "Doctrine establishes a particular way of thinking about war\n\n64 Doctrine Handbook\n\n"
    "and a way of fighting, and it provides a philosophy for leading Marines.\n\n"
    + "".join(f"Note {n}.\n\nKey Point\n\n" for n in range(4))
)

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
    ("ligatures written as marks or split off their word → ligature",
     '"The effort to make the office run efficiently was significant, and the workflow was the first thing to change" [V] (Ch 4).',
     "ligature"),
    ("a running header and folio between two pages are dropped",
     '"thereby allowing the freedom to take whatever steps are deemed necessary based on the situation" [V] (p 41).',
     None),
    ("a short fragment across a page break is found",
     '"a continuous source of friction" [V] (p 42).',
     None),
    ("an elided quote whose last piece crosses a page break is found",
     '"Mission tactics leave the manner of accomplishing the mission . . . deemed necessary based on the situation" [V] (p 41).',
     None),
    ("a running header with an OCR slip is dropped",
     '"the ability to operate quickly. Commanders must rely on the initiative of subordinates" [V] (p 43).',
     None),
    ("a word split across a page break is rejoined",
     '"the flexibility to respond quickly to opportunities rather than blindly follow predetermined schemes" [V] (p 44).',
     None),
    ("a folio on the header's line, with no form feed, is dropped",
     '"Doctrine establishes a particular way of thinking about war and a way of fighting" [V] (p 64).',
     None),
    ("a split word and a split compound in one quote are each read as the quote spells them",
     '"deteriorating at an ever-increasing rate, and the situation must change faster than he can follow" [V] (p 42).',
     None),
    ("a split compound quoted as two words → near",
     '"deteriorating at an ever increasing rate, and the situation must change faster than he can follow" [V] (p 42).',
     "near"),
    ("a clause dropped beside a page break → interrupted",
     '"thereby allowing the freedom to take whatever steps are deemed necessary. Chance is a universal characteristic of war" [V] (p 41).',
     "interrupted"),
    ("a recurring line with no page break stays in the text → interrupted",
     '"Plans will go awry and instructions will be unclear. Units must adapt to the situation as it changes" [V] (p 45).',
     "interrupted"),
    ("a figure quoted whole is exact",
     '"Satisfaction rose by 3.5 points in the second quarter" [V] (Ch 4).',
     None),
    ("a figure ending a sentence, the full stop inside the closing quote, is exact",
     '"The plant closed in 1998." [V] (Ch 4).',
     None),
    ("a decimal cut at the point → missing",
     '"Satisfaction rose by 3." [V] (Ch 4).',
     "missing"),
    ("a whole number cut short → missing",
     '"while turnover rose by 3" [V] (Ch 4).',
     "missing"),
    ("a number cut at the thousands separator → missing",
     '"The firm hired 2," [V] (Ch 4).',
     "missing"),
    ("a quote starting inside a number → page",
     '"500 people that year" [V] (Ch 4).',
     "page"),
    ("an elided piece ending inside a number → interrupted",
     '"Satisfaction rose by 3 ... over the year" [V] (Ch 4).',
     "interrupted"),
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
