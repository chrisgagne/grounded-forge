# Pass I quotations audit: open-practice-library (2026-10-15)

**Mode:** quotations. Deep reference read in full (341 of 341 lines). Source: `corpus.commons/demo/sources/converted/open-practice-library.md` (22,348 lines; passages read around each hit). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 14 (10 near, 3 interrupted, 1 missing).
- Quotation-corrected: 8 lines in the deep ref (65, 95, 124, 133, 168, 176, 235, 241).
- Marker-corrected: 2 lines in the deep ref (65: README quotation under `[V]` replaced with `[AP]` on the frontmatter plus a conversion-gap note; 211: verbatim subtitle under `[AP]` → `[V]`).
- Stripped: 1 (deep 65: the README quotation; the converted source does not carry it).
- Derived-tier edits: 6 lines in 4 distillations (4 from the checker, 2 by propagation).
- Left as is (conversion noise): 3 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 65 | missing: "Update it with your changes and remember to append your `github` username to the end of the authors list" [V], cited to `README.md`, "Content Writers" | The README is not in the converted source (the corpus holds only the 266 practice pages; deep line 80 already records the same gap). Quotation stripped. The line now says what the source carries: an `authors:` metadata field, often with several handles (Continuous Delivery three, Continuous Integration seven) [AP], cited to those practices' frontmatter, with a `[conversion gap: …]` note. "Contribution history, not a single byline" is now stated as this reference's reading of the multi-name lists, not as the source's words. "GitHub handles" became "author handles": the source does not say what the handles are | src 1162 (Continuous Delivery metadata), 1241 (Continuous Integration metadata); no README text anywhere in the source |
| 95 | near: Lean Coffee's two bullet items joined with an added full stop | Quoted as two items: "Lean Coffee started in Seattle in 2009 by Jim Benson and Jeremy Lightsmith" [V]; "A structured, but agenda-less meeting. Participants gather, build an agenda, and begin talking" [V] | src 3486–3488 |
| 124 | near: footnote marker "(*)" after "Defence/defense" dropped without notice; "layered security" in quotes | Lead words now unquoted, then two quotations: "sometimes referred to as 'layered security'", "is an approach to securing … solution" [V]. The `(*)` marker points to a spelling note (src 1293) and stays outside the quotation | src 1280–1284 |
| 133 | near: Evals quote set em dashes where the source has none. The converted text renders the dash before "giving" as a list bullet (`* giving`) and prints a hyphen before "but" | Split at the bullet rather than copy it: "… They serve the same purpose as Test Automation", "giving you confidence that your system behaves correctly - but they are fundamentally different. **Traditional tests give you certainty. Evals give you confidence.**" [V]. "Test Automation" is a link in the source; link markup only | src 1822–1828 |
| 168 | near: AEIOU's five blockquoted bold items joined with commas and a full stop | Now "AEIOU stands for:" "A - Activities", "E - Environments", "I - Interactions", "O - Objects", "U - Users". "This heuristic framework provides … ethnographic studies" [V] | src 9792–9808 |
| 176 | interrupted (triage): OKR quotation dropped "The definition of the outcome that you are striving to achieve." with no ellipsis | Ellipsis added: "OKRs have two parts: The Objective - The what … The Key Result - The how" [V] | src 13571–13581 |
| 211 | marker: "Understand, prioritise, and clarify items in the backlog" is the subtitle's opening words, verbatim, under `[AP]` | `[AP]` → `[V]` | src 17536 |
| 235 | near: Kanban's five bullet items joined with commas | Lead-in and each item quoted separately: "… based in the following practices:" "Visualize the workflow", "Limit Work in Progress (WIP)", "Manage flow", "Make Process Policies Explicit", "Feedback loops" [V] | src 21086–21098 |
| 241 | near: Chaos Engineering quote lower-cased "With" after the ellipsis | Now "… With chaos engineering" | src 20002–20009 |

## Changes, derived tier

| File:line | Finding | Change |
|---|---|---|
| aar 18 | near: Establish Shared Principles quote moved the full stop inside the inner quote ("'what they will do.'") | Now "'what they will do'." as the source punctuates (src 1785) |
| retro 14 | near: same as aar 18 | Same fix |
| software-business 66 | near: Kanban bullet list quoted inline (same defect as deep 235) | Each item quoted separately |
| stakeholder-engagement 34 | near: Formal Relational Contract quote replaced ". We" with "... we", an ellipsis marking no omission | Now "trust. We believe" (src 11318–11323) |
| aar 30 | propagation (checker did not flag; the first quotation carries no marker of its own): same em-dash Evals wording as deep 133 | Same split as deep 133 |
| software-business 36 | propagation (checker did not flag; quote sits inside italics): same Evals wording as deep 133 | Same split as deep 133 |

Propagation grep of the light ref and all five distillations for each corrected wording ("Lean Coffee started", "structured, but agenda", "layered security", "Defence/defense", "same purpose as Test", "AEIOU stands", "Kanban is a framework", "Visualize the workflow", "predict the unpredictable", "with chaos engineering", "OKRs have two", "The Objective", "append your", "authors list", "clarify items", "what they will do", "Transactional (legal)"): hits only in the lines above. Distillation notes that describe the deep ref's markers (aar 135, retro 160, software-business 265, stakeholder-engagement 220, decision-making 202) stay true.

**Light ref, line 71 (fixed by the parent):** it said authors are "a contribution history, not a byline" and quoted the README's contributor workflow ("hit the Improve or Add new button to launch the CMS; … append your github username to the authors list"). Neither is in the converted source (grep for "Add new", "launch the CMS", "github username" and "authors list" finds no such passage), and the propagation grep above missed the lowercase "github" wording. The line now calls `authors` "a list of contributor handles, often several per practice" and says the pull-request workflow is described in the README, which is not part of the converted source, matching deep 65 and 80.

## Left as is (conversion noise)

- **Deep 96** (interrupted): the Five Whys quote runs across link markup, "made up by [Taiichi Ohno](https://en.wikipedia.org/wiki/Taiichi_Ohno "Taiichi Ohno") at Toyota" (src 2148–2150). No words dropped.
- **Retro 18** (interrupted): the same Five Whys quote and link markup as deep 96.
- **Deep 176** (now `page` after the fix): the checker reads the list numerals "1." / "2." in the gap as page numbers, and the source carries zero-width no-break spaces (U+FEFF) inside "OKRs" and both "The" (src 13575–13581). The ellipsis covers the dropped definition; the quoted words match.

## Triage cross-check

- **Deep 65** (missing, README "append your username" quote): confirmed absent. No README text is in the converted source, which holds only the practice pages. Quotation stripped; the line now cites the `authors:` frontmatter the source does carry, marked `[AP]`, with a conversion-gap note.
- **Deep 176** (interrupted, OKR "two parts" quote with words dropped): fixed with an ellipsis; the remaining checker line is conversion noise (list numerals, U+FEFF).

## Checker counts

- Before: 10 apostrophe, 1 initial, 10 near, 3 interrupted, 1 missing (14 failing).
- After: 10 apostrophe, 1 initial, 1 page, 2 interrupted (3 failing, all conversion noise listed above).

## Open

- Stamp left as is (quotations mode). No commit made, no build run, derived-tier stamps not refreshed.
- Light ref line 71 ("a contribution history, not a byline"): see the derived-tier note above.
- Outside a quotations pass but noticed: deep 135, 240 and 320 put quotations under `[BT]` alone (the page sets them in quotation marks without naming a speaker). They match the source (checked by grep against the flattened text), but the checker skips them because they carry no `[V]`. A full Pass I should decide whether they take `[V] [BT]`.
