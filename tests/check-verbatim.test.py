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
short at either end never matches, unless what runs on is a note number the
source's own notes vouch for. The paged section mirrors
MCDP 1's conversion: running headers and folios between pages, and a quote that
holds both a word split across a line and a compound split across a line. The
OpenStax sections mirror its two conversions: bold headers with a folio beside a
chapter or section number and no form feed, and pages split by form feeds whose
footers carry a folio that runs with the page count. Each new rule has a guard
beside it: a changed decimal, a prefix hyphen, a recurring line with no page
break, and a page-foot number off the page count all still fail.
The multi-line blocks hold extraction scope: a `[V]` before a colon covers the
list it introduces, and a `[V]` named in the notes section is not a claim, while
a `[V]` on a paraphrase anywhere else still reports no-quote. A quotation
followed only by its citation is checked, while a quoted remark a sentence
before a cited claim still is not. Pandoc's Markdown in the source reads as
its text, while a changed word still fails and a command-line option's `--`
stays two hyphens. A quote's " / " matches a line break in the source (plain,
Pandoc's backslash, a blockquote's, or one a dash closes up) or the source's
own slash, while one over running text still fails.

The resolution cases build a small corpus in a temporary directory: a file
finds its converted source by name, by its source card's link, or by the
quotations it holds; a second conversion of the same book counts as that
source, a book that quotes it whole does not, and a slug no file holds
enough of is reported.

No test framework, matching tests/derived-provenance.test.py: each case succeeds
silently or raises; the runner collects failures, prints a summary, exits non-zero.

Usage:
    python3 tests/check-verbatim.test.py
"""

from __future__ import annotations

import importlib.util
import json
import re
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

Teams should track velocity (ideally 3-4 sprints worth of data) or throughput before they forecast a release.

The result is the "horrendogram" (Penn, 2018); a map nobody can read at a glance.

Women are not projected to reach pay equity until at least 2059, with projections predicting dates as late as 2119.27 These are averages.

The gap has narrowed slowly.26 It widened again in some sectors.28

The survey index stood at 4.12 Overall, the figures held steady.

Earlier surveys found the same.4 The rate rose by 6.5 points.

The gap narrowed again.29 The second index stood at 7.30 Overall it held.

The Sprint Retrospective is timeboxed to three hours for a onemonth Sprint, and each month one team leads it.

Leaders decide onthe-spot when the plan meets a deadend. At the end of the day the dead weight goes on the spot list.

The teams cooperate across the programme.

The caféowner opened early, and the café had one owner.

The plan held for months until minor editsfresh habitsslowly became routine. Fresh habits form slowly as minor edits pile up.

Notes

4. A. Writer, “Earlier Survey,” 2018.
5. B. Writer, “Rate Report,” 2019.
12. C. Writer, “Index Review,” 2020.
27. D. Writer, “Pay Equity Projections,” 2021.
"""

# Pandoc's Markdown left in an EPUB conversion: dashes, an empty page anchor,
# an endnote link with its attribute block, nested spans, backslash escapes, a
# drop cap. A command-line option's "--" beside them, and a true em dash.
SOURCE += r"""
The plan---as written---failed, and the 1990--2000 decade[]{#ch02.html_page_17} saw [the same plan](#notes.html_n4){#ch02.html_n4ref .calibre3} applied [twice]{.italic} by [[nested]{.calibre_1} spans]{.calibre1}. Don\'t pay \$5 for it\! A [D]{.dropcap}rop cap opens the next line.

Run the checker with --all-local to see every finding.

The cost fell — sharply — in the second year.

Is that the whole story? Ask it twice before you answer.

A small trial shows the team where the plan is weak.[3](notes.htm#n3) It can also go badly.[^6^](#foot_6){#ref_6} The review of [2019](https://example.com/archive#2019) stands.

The editor put it plainly: \[W\]e have changed the layout so often that readers must now relearn it each spring.
"""

# Verse and one-sentence paragraphs, which a quote sets on one line with " / ":
# a plain line break, Pandoc's backslash hard break, a blockquote's ">" lines, a
# dash that closes up the break, and a slash the source itself sets.
SOURCE += r"""
Short sentences carry the weight.

Each one stands alone.

We shall not cease\
from exploring the edge.

> First line of the verse
> and the second follows it.

The reader—curious, open—
Will follow you anywhere.

The Principle of Letting Be / Letting Unfold runs through it.
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

# OpenStax running headers set in bold on their own lines, with no form feed:
# the folio beside a chapter number ("48 5 • Criminal Liability") or after a
# section number ("8.1 • ... 267"). And a recurring two-number line whose
# numbers never change, which is no folio and stays in the text.
SOURCE += "".join(
    f"Body paragraph {n} on liability.\n\n**{48 + 2 * n} 5 • Criminal Liability**\n\n"
    f"**Access for free at openstax.org**\n\n"
    f"Body paragraph {n} on marketing.\n\n**8.1 • Entrepreneurial Marketing and the Marketing Mix {267 + 2 * n}**\n\n"
    f"Body paragraph {n} on review.\n\n**2 5 • Review Checklist**\n\n"
    for n in range(5)
)
SOURCE += (
    "The commerce clause gives the federal government broad powers\n\n**58 5 • Criminal Liability**\n\n"
    "**Access for free at openstax.org**\n\nto regulate commerce within each state.\n\n"
    "Guerrilla marketing can help start-ups\n\n**8.1 • Entrepreneurial Marketing and the Marketing Mix 277**\n\n"
    "survive in competitive markets.\n\n"
    "Every review opens with the goals\n\n**2 5 • Review Checklist**\n\nand closes with the actions.\n\n"
)

# A journal's running header: a folio, the journal line and the authors set in
# emphasis, the last ending in a full stop inside the emphasis. No form feed.
SOURCE += "".join(f"Journal body {n}.\n\n{n} \n\n_J Field Stud 12 (2020) 4021_ \n\n_A. Writer et al._ \n\n" for n in range(2, 7))
SOURCE += ("The survey measures how often crews \n\n7 \n\n_J Field Stud 12 (2020) 4021_ \n\n"
           "_A. Writer et al._ \n\nreport near misses to the safety office.\n\n")


def openstax_page(body: str, title: str, odd: bool) -> str:
    """One page of an OpenStax PDF as PyMuPDF converts it: the body, then the
    footer that carries the folio, then a form feed. The folio runs with the
    page count."""
    folio = len(re.findall(r"\f+", SOURCE + body)) + 40
    if odd:
        return f"{body}\n\n6.2 • {title}     {folio}\n\f"
    return f"{body}\n\n{folio}     6 • Contract Law\n\nAccess for free at openstax.org\n\f"


# Paged with form feeds, the headers too long or too rare for the recurrence
# rule: the folio running with the page count marks them. The last page's foot
# carries a number off that count, and stays.
LONG_TITLE = "Remedies for a Breach of Contract in the Modern Business World Today"
for n, body in enumerate([
    "Contract page one.", "Contract page two.", "Contract page three.",
    "In most cases the remedy for a breach of contract", "is money damages. Courts will order specific",
    "performance only when damages fall short. A court may also",
]):
    SOURCE += openstax_page(body, LONG_TITLE, odd=n % 2 == 1)
SOURCE += "rescind the contract and restore the parties\n\nSummary of Contract Law     999\n\f"
SOURCE += "to their positions before it was signed.\n"

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
    ("a digit parenthetical inside the quote stays in it",
     '"Teams should track velocity (ideally 3-4 sprints worth of data) or throughput before they forecast" [V] (Ch 4).',
     None),
    ("an author-year citation inside the quote stays in it",
     'It ends in "the \'horrendogram\' (Penn, 2018); a map nobody can read at a glance" [V] (Ch 4).',
     None),
    ("a changed figure inside the quote's parenthetical → page",
     '"Teams should track velocity (ideally 5 sprints worth of data) or throughput before they forecast" [V] (Ch 4).',
     "page"),
    ("a quote mark closing a quotation opened on an earlier line is not paired with a citation title's",
     '> to be right!" [V] (Part 6, "Some Title Not In Source").',
     None),
    ("a quote before a page citation is checked, not counted as a figure",
     'The text is blunt: "Work is an activity that produces something of no value" (p. 22) [V].',
     "missing"),
    ("a figure ending a sentence, a note number glued after it, is exact",
     '"with projections predicting dates as late as 2119" [V] (Ch 6).',
     None),
    ("a figure ending a sentence, the full stop quoted, a note number glued after it, is exact",
     '"predicting dates as late as 2119." [V] (Ch 6).',
     None),
    ("a decimal before a capital, with no note beside it in sequence → missing",
     '"The survey index stood at 4" [V] (Ch 6).',
     "missing"),
    ("a decimal before a lowercase word, its note in sequence and listed → missing",
     '"The rate rose by 6." [V] (Ch 6).',
     "missing"),
    ("a decimal before a capital, its neighbour in sequence but no note listed for it → missing",
     '"The second index stood at 7" [V] (Ch 6).',
     "missing"),
    ("a figure claim closed by U.S. is counted, not flagged",
     "- *Flextime*: discretion over arrival and departure times; in 57% of U.S. companies [V].",
     None),
    ("a figure claim closed by e.g. is counted, not flagged",
     "Teams average 7 people, e.g. in product groups [V].",
     None),
    ("a figure claim closed by a.m. is counted, not flagged",
     "Stand-ups start at 9 a.m. in most teams [V].",
     None),
    ("a paraphrase after U.S. → no-quote",
     "Teams in the U.S. paraphrase the source here [V] (Ch 4).",
     "no-quote"),
    ("a bold OpenStax header with a folio and a chapter number is dropped",
     '"The commerce clause gives the federal government broad powers to regulate commerce within each state" [V] (Ch 5).',
     None),
    ("a bold OpenStax header with a section number and a folio is dropped",
     '"Guerrilla marketing can help start-ups survive in competitive markets" [V] (Ch 8.1).',
     None),
    ("a recurring two-number line whose numbers never change stays in the text → interrupted",
     '"Every review opens with the goals and closes with the actions" [V] (Ch 2).',
     "interrupted"),
    ("an OpenStax footer whose folio runs with the page count is dropped",
     '"In most cases the remedy for a breach of contract is money damages" [V] (Ch 6).',
     None),
    ("a long OpenStax section header whose folio runs with the page count is dropped",
     '"Courts will order specific performance only when damages fall short" [V] (Ch 6.2).',
     None),
    ("a page-foot line whose number is off the page count stays in the text → interrupted",
     '"A court may also rescind the contract and restore the parties to their positions before it was signed" [V] (Ch 6).',
     "interrupted"),
    ("a compound the converter joined → joined",
     '"timeboxed to three hours for a one-month Sprint" [V] (Ch 3).',
     "joined"),
    ("two joined compounds, one hyphen kept by the converter → joined",
     '"Leaders decide on-the-spot when the plan meets a dead-end" [V] (Ch 3).',
     "joined"),
    ("a joined compound beside an accented letter → joined",
     '"The café-owner opened early" [V] (Ch 3).',
     "joined"),
    ("an em dash the converter dropped is no joined compound, even with a capital → missing",
     '"Minor edits — fresh habits — slowly became routine" [V] (Ch 3).',
     "missing"),
    ("a journal header whose authors end in a full stop inside emphasis is dropped",
     '"The survey measures how often crews report near misses to the safety office" [V] (p 7).',
     None),
    ("a quote ending in a full stop, then its citation, is checked",
     'The text is plain. "Relationship conflict tends to erode the trust that teams rely on." (Ch 4, p. 5) [V].',
     "missing"),
    ("a quote ending in a full stop, then a locator with no digit, is checked",
     '"Work is an activity that produces something of value for other people." (same section) [V]',
     None),
    ("a quote ending in a question mark, then a paragraph locator, is checked",
     'A prompt: "Is that the whole story?" (¶3) [V].',
     None),
    ("a quoted remark before a sentence with words and a citation is not checked → no-quote",
     'Teams say "we will look into it." The text is blunt here (Ch 4) [V].',
     "no-quote"),
    ("a citation-only tail keeps one sentence, not two → no-quote",
     'Teams say "we will look into it." Then they move on. (p. 5) [V]',
     "no-quote"),
    ("pandoc's em dash written --- is exact",
     '"The plan—as written—failed" [V] (Ch 7).',
     None),
    ("pandoc's em dash quoted as written is exact",
     '"The plan---as written---failed" [V] (Ch 7).',
     None),
    ("pandoc's en dash, anchor, endnote link and nested spans read as their text",
     '"the 1990–2000 decade saw the same plan applied twice by nested spans" [V] (Ch 7).',
     None),
    ("pandoc's backslash escapes and a drop-cap span read as their text",
     '"Don\'t pay $5 for it! A Drop cap opens the next line" [V] (Ch 7).',
     None),
    ("a changed word through pandoc markup → missing",
     '"the 1990–2000 decade saw the same tactic applied twice by nested spans" [V] (Ch 7).',
     "missing"),
    ("a quote that keeps pandoc's escaped brackets reads them as the source's",
     '"\\[W\\]e have changed the layout so often that readers must now relearn it each spring" [V] (Ch 7).',
     None),
    ("pandoc's endnote numbers glued to a word are dropped",
     '"shows the team where the plan is weak. It can also go badly. The review of" [V] (Ch 7).',
     None),
    ("a linked number set apart from the word before it stays in the text",
     '"The review of 2019 stands" [V] (Ch 7).',
     None),
    ("a command-line option's -- stays two hyphens",
     '"Run the checker with --all-local to see every finding" [V] (Ch 7).',
     None),
    ("an option's -- quoted as an en dash → glyph",
     '"Run the checker with –all-local to see every finding" [V] (Ch 7).',
     "glyph"),
    ("a -- quoted for the source's em dash → glyph",
     '"The cost fell -- sharply -- in the second year" [V] (Ch 7).',
     "glyph"),
    ("a hyphen after a prefix the source never sets alone → interrupted",
     '"The teams co-operate across the programme" [V] (Ch 3).',
     "interrupted"),
    ("' / ' over the source's paragraph break is exact",
     '"Short sentences carry the weight. / Each one stands alone." [V] (Ch 8).',
     None),
    ("pandoc's backslash hard break reads as a line break",
     '"We shall not cease from exploring the edge" [V] (Ch 8).',
     None),
    ("' / ' over pandoc's backslash hard break is exact",
     '"We shall not cease / from exploring the edge" [V] (Ch 8).',
     None),
    ("' / ' over a blockquote's line break is exact",
     '"First line of the verse / and the second follows it" [V] (Ch 8).',
     None),
    ("' / ' after a dash that closes up the line break is exact",
     '"The reader—curious, open— / Will follow you anywhere" [V] (Ch 8).',
     None),
    ("a slash the source sets matches as written",
     '"The Principle of Letting Be / Letting Unfold runs through it" [V] (Ch 8).',
     None),
    ("' / ' where the source runs on within a line → near",
     '"Is that the whole story? / Ask it twice before you answer" [V] (Ch 7).',
     "near"),
]

# Multi-line cases: (label, [(line, expected kind or None)]). Blank lines are
# written as "" and expect nothing. The notes section runs to the next level-2
# heading, so it comes last, and the line after it is the guard.
BLOCKS = [
    ("a [V] lead-in covers the list below it", [
        ('Reward schedules compared (Ch 4.4, "Schedules of Reinforcement") [V] [BT]:', None),
        ("", None),
        ('1. Ratio schedules "generally lead to better behavior than the time-contingent (or interval) schedules".', None),
        ('2. Work is "an activity that produces something of no value".', "missing"),
        ("3. A plain paraphrase item.", None),
        ('4. An item with its own marker, "a phrase not in the source at all" [AP] (Ch 4).', None),
        ("   A continuation of that item, \"also not in the source anywhere\".", None),
        ("", None),
        ('5. A loose item: "Relationship conflict tends to erode the trust that teams rely on".', "missing"),
        ("", None),
        ('After the list, "a remark the lead-in does not reach" stands alone.', None),
    ]),
    ("a [V] lead-in covers the rest of its line", [
        ('Two passages (Ch 4) [V]: "Work is an activity that produces something of value"; '
         '"Relationship conflict tends to erode the trust that teams rely on".', "missing"),
    ]),
    ("a [V] lead-in over a list whose items carry their own markers", [
        ("Two passages (Ch 4) [V]:", None),
        ('- "Work is an activity that produces something of value" [V] [AE].', None),
        ('- "Relationship conflict tends to erode the trust that teams rely on" [V].', "missing"),
    ]),
    ("a [V] lead-in over a list with no quote → no-quote", [
        ("Two steps (Ch 4) [V]:", "no-quote"),
        ("- Listen first.", None),
        ("- Then respond.", None),
    ]),
    ("a [V] mention in the notes section is not a claim", [
        ("## Citation and Source-Integrity Notes", None),
        ("", None),
        ("**Evidence-marker continuity.** The deep reference carries [V] markers for the author's direct statements.", None),
        ("", None),
        ("- **Evidence-class markers** ([V] verbatim; [AP] author paraphrase) are inline with claims.", None),
        ("", None),
        ('The quoted claim "Relationship conflict tends to erode the trust that teams rely on" is [V] in the deep reference.', "missing"),
        ("", None),
        ("## After the notes", None),
        ("", None),
        ("The source defines work as producing value for others [V] (Ch 4).", "no-quote"),
    ]),
]


def book(title: str, n: int) -> str:
    """A synthetic book: n sentences no other book shares a run of words with."""
    return "\n\n".join(sentence(title, i) + "." for i in range(n)) + "\n"


def sentence(title: str, i: int) -> str:
    """Every run of six words holds the title, so no two books share one."""
    return f"In {title} part {i}, {title} crews logged {i * 7} {title} readings at {title} station {i} before dusk"


def resolution_checks() -> list[str]:
    """Each file finds its converted source by name, by the source card's
    link, or by content; a second conversion of the same book is that source,
    a book that quotes it whole is not. Run against a temporary corpus with
    the module's tier roots pointed at it."""
    spec = importlib.util.spec_from_file_location("check_verbatim", SCRIPT)
    cv = importlib.util.module_from_spec(spec)
    sys.modules["check_verbatim"] = cv
    spec.loader.exec_module(cv)
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp).resolve() / "local" / "corp"
        conv, orig, refs = root / "sources" / "converted", root / "sources" / "original", root / "references"
        for d in (conv, orig, refs):
            d.mkdir(parents=True)
        cv.TIER_ROOTS = {"local": root.parent}
        conv.joinpath("alpha.md").write_text(book("alpha", 40), encoding="utf-8")
        # A second conversion of alpha: one more sentence, the rest the same.
        conv.joinpath("Alpha -- A. Writer -- 2011.md").write_text(
            book("alpha", 40) + "Only this conversion keeps the colophon that closes the book.\n", encoding="utf-8")
        # A third, which its own source card names as a source in its own right.
        conv.joinpath("Alpha Notes.md").write_text(
            book("alpha", 40) + "Only the notes edition prints this errata page at the back.\n", encoding="utf-8")
        orig.joinpath("alpha-notes.source.md").write_text(
            "---\ntitle: Alpha Notes\n---\n\nConverted markdown: [`sources/converted/Alpha Notes.md`](../converted/Alpha Notes.md)\n",
            encoding="utf-8")
        # Beta's converted text under a title-based name, with no card.
        conv.joinpath("Beta Book -- B. Writer -- 2011.md").write_text(book("beta", 40), encoding="utf-8")
        # Gamma's under another name, linked from its source card.
        conv.joinpath("Gamma-Book-2014.md").write_text(book("gamma", 40), encoding="utf-8")
        orig.joinpath("gamma.source.md").write_text(
            "---\ntitle: Gamma\n---\n\nConverted markdown: [`sources/converted/Gamma-Book-2014.md`](../converted/Gamma-Book-2014.md)\n",
            encoding="utf-8")
        # Delta is short; a longer book quotes it whole.
        conv.joinpath("delta.md").write_text(book("delta", 6), encoding="utf-8")
        conv.joinpath("Quoting Book.md").write_text(book("delta", 6) + book("omega", 60)
                                                   + "Only the longer book adds this delta afterword at the end.\n", encoding="utf-8")

        def deep(slug: str, quotes: list[str]) -> Path:
            f = refs / f"{slug}-deep.md"
            f.write_text("# Deep\n\n" + "\n\n".join(f'"{q}" [V] (Ch 1).' for q in quotes) + "\n", encoding="utf-8")
            return f

        files = {
            "alpha": deep("alpha", [sentence("alpha", 3), "Only this conversion keeps the colophon that closes the book",
                                    "Only the notes edition prints this errata page at the back"]),
            "beta": deep("beta", [sentence("beta", i) for i in (1, 2, 3)] + ["In beta part 4, beta teams logged 28 beta readings"]),
            "gamma": deep("gamma", [sentence("gamma", 5), "In gamma part 6, gamma teams logged 42 gamma readings"]),
            "delta": deep("delta", [sentence("delta", 2), "Only the longer book adds this delta afterword at the end"]),
            # Two of four quotes in one file, one in another: no file holds enough.
            "epsilon": deep("epsilon", [sentence("beta", 7), sentence("beta", 8), sentence("gamma", 9),
                                        "A sentence no converted source holds at all"]),
        }
        got: dict[str, tuple[list, str | None]] = {}
        for slug, f in files.items():
            findings, _, err = cv.check_file(f, None, True, {})
            got[slug] = ([(x.line, x.kind, x.note) for x in findings], err)

        def expect(label: str, ok: bool, seen) -> None:
            if not ok:
                failures.append(f"{label}: got {seen}")

        f, err = got["alpha"]
        expect("by name: a quote only a second conversion holds → cross-source, another conversion; "
               "a file with its own source card is no second conversion → wrong-source",
               err is None and [(k, "another conversion" in n) for _, k, n in f]
               == [("cross-source", True), ("wrong-source", False)], got["alpha"])
        f, err = got["beta"]
        expect("by content: a title-named file holding the quotes is the source; a changed word → missing",
               err is None and [k for _, k, _ in f] == ["missing"], got["beta"])
        f, err = got["gamma"]
        expect("by the source card's link; a changed word → missing",
               err is None and [k for _, k, _ in f] == ["missing"], got["gamma"])
        f, err = got["delta"]
        expect("a book that quotes the source whole is no copy of it → wrong-source",
               err is None and [k for _, k, _ in f] == ["wrong-source"], got["delta"])
        f, err = got["epsilon"]
        expect("two of four quotes in one file is too few to resolve → reported, with the closest file",
               err is not None and "Beta Book" in err and "2 of 4" in err, got["epsilon"])
    return failures


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
        for label, block in BLOCKS:
            for j, (text, kind) in enumerate(block, 1):
                lines.append(text)
                if text:
                    expect[len(lines)] = (f"{label} (line {j})", kind)
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
        if out["figure_claims_unchecked"] != 4:
            failures.append(f"figure claims: expected 4 counted, got {out['figure_claims_unchecked']}")
        if code != 1:
            failures.append(f"exit status with failing findings: expected 1, got {code}")

        # `initial` alone does not fail the run.
        only_initial = tmpd / "initial-deep.md"
        only_initial.write_text('# x\n\nThey note that "An activity that produces something of value" [V] (Ch 4).\n', encoding="utf-8")
        code, _ = run(only_initial, source)
        if code != 0:
            failures.append(f"exit status with only an initial finding: expected 0, got {code}")

    resolution = resolution_checks()
    failures += resolution
    total = len(expect) + 3 + 5
    if failures:
        print(f"{len(failures)} of {total} checks failed:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"All {total} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
