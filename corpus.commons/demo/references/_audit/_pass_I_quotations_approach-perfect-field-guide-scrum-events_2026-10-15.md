# Pass I quotations audit: approach-perfect-field-guide-scrum-events (2026-10-15)

**Mode:** quotations. Deep reference read in full (367 of 367 lines). Source: `corpus.commons/demo/sources/converted/approach-perfect-field-guide-scrum-events.md` (923 lines; passages read around each hit). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 44 (2 glyph, 30 near, 11 interrupted, 1 no-quote).
- Quotation-corrected: 3 lines in the deep ref (205, 303, 344).
- Marker-corrected: 1 line in the deep ref (146: `[V]` → `[AP]`).
- Stripped: 0.
- Derived-tier edits: 0 (no wrong quotation or marker was copied there).
- Left as is (conversion noise or verbatim to a cited passage): 40 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 146 | no-quote: the four Parking Lot examples paraphrased under `[V]` | `[V]` → `[AP]` with its own (Daily Scrum, "Tips") citation; "a stakeholder with questions" now "with questions or concerns", as the source has it. The quotation before it ("Anyone, including those outside the team … fully voluntary at this point") stays `[V]` and is word for word | src 492–507 |
| 205 | near: the three sub-bullets joined with semicolons where the source ends each with a period | Semicolons → periods ("*Sprint Backlog*. The well-being … *Scrum Team*. The effectiveness …") | src 666–672 |
| 303 | glyph: "1-3 hours per sprint" | En dash, as the at-a-Glance table prints it: "1–3 hours per sprint" | src 67 |
| 344 | interrupted: "(ap.tips/tradeoffs)" dropped between "*Sprint Goal*." and "Attempting" with no ellipsis | Shortlink restored, matching the same quotation at deep 114 | src 402–406 |

## Changes, derived tier

- None. Propagation grep of the light ref and all five distillations for each corrected wording ("firm commitment", "tradeoffs", "Parking Lot", "edge case", "face-to-face", "Objective data", "progress against", "well-being of the people", "1-3 hours", "1–3 hours", "scenario"):
  - decision-making 26 already carries "(ap.tips/tradeoffs)"; decision-making 14 and 177, and software-business 14 and 26, quote shorter spans of the same tip that do not cross the shortlink. All match the source.
  - stakeholder-engagement 42 quotes one Parking Lot example word for word, "A stakeholder has questions or concerns they'd like to bring to the *Scrum Team*." [V] (src 507). No other file copies the paraphrased example list.
  - The light ref (31, 37, 39, 114) gives the firm-commitment tip and the Parking Lot unquoted, as paraphrase.
- The distillations' evidence-marker notes (aar 120, retro 155, decision-making 212, software-business 222, stakeholder-engagement 223) stay true: none describes the Parking Lot examples' marker.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

Words match the source in every line below; the checker's `near` comes from how the conversion renders quotation marks, emphasis, links and bullets.

- **Spaced quotation marks around emphasis** (`“ _Ready_ ”`, `“ _Done_ .”`), which the deep ref gives as `'*Ready*'` / `'*Done*.'`: deep 36 (src 110–111), 101 (src 365–367), 176 (src 592–593), 178 (src 598–599), 256 (src 810), 279 (src 873–877), 230 and retro 24 (`_Definition of “Done”_`, src 732–736; retro 24's `...` marks the dropped "For each item … You'll find that").
- **Link markup cutting through the quotation** (`[” (ap.tips/dor ) … ](http://…)`): deep 74 (src 222–224), 104 (src 374–377), 212 (src 683–684), 189, 352, decision-making 42, software-business 14 (both quotations), 32 and 104, stakeholder-engagement 36 (the "Don't demonstrate" tip, src 626–629, which also splits the emphasis as `_Scrum_ _Team_`).
- **Emphasis glued to a hyphen** (`_Capacity_ -adjusted`): deep 95 and 312, aar 22 (src 270–272).
- **Bullets joined with no change to the words**: deep 138 (the three Scrum Guide questions, src 469–476), 152 (src 529–537), 343 (src 131–133), 205 after the fix (the remaining difference is the period inside `_Sprint Backlog._` / `_Scrum Team._`), stakeholder-engagement 46 (src 658–661).
- **Nested quotation marks rendered as single quotes**: deep 105 (src 379–386), 122 ("Also known as “Standup.”", src 425; the lower-case "also" is the deep ref's run-in).
- **Footer inside the quotation** ("© 2020, Approach Perfect, Limited. https://approachperfect.com 6" plus the licence line): the coffee-drinker quotation at deep 99 and 348, decision-making 34, software-business 16 and 40, stakeholder-engagement 54 and 98 (src 349–357); the Backlog Refinement agenda at deep 272 (footer "… 15", src 845–866). No source word dropped.
- **Table-cell line breaks** (`<br>`): deep 199 and stakeholder-engagement 46, "Others must not attend unless freely invited by all on the *Scrum Team*" (src 67).
- **Deep 272, bullets joined with semicolons:** the source's five sub-bullets carry no terminal punctuation (src 848–866); the semicolons only mark the list breaks and no source character is replaced. The quotation ends at "makes the final decision" with no closing parenthesis, as the source does.
- **Deep 281, the source's own stray mark:** the source prints "Build the Right Product “ by" (src 886), a space and an opening quotation mark where the closing one belongs. The deep ref gives the title in single quotes; the words match.
- **Deep 295, verbatim to the first cited passage:** "1-2 hours per week of *Sprint* duration" matches the at-a-Glance cell ("Typically 1-2<br>hours per week<br>of_Sprint_<br>duration", src 64), which prints a hyphen. The checker matched the Sprint Planning Timing line instead ("1–2", src 202), because the cell's glued `of_Sprint_` stops the table match.

## Triage cross-check

- **Deep 146** (no-quote, paraphrase under `[V]`): fixed. The four examples are paraphrase of src 498–507; marker now `[AP]`.
- **Deep 344** (interrupted, URL parenthetical dropped with no ellipsis): fixed. "(ap.tips/tradeoffs)" restored (src 403); the quotation now matches deep 114 and decision-making 26.

## Checker counts

- Before: 76 apostrophe, 2 glyph, 28 initial, 30 near, 11 interrupted, 2 cross-source, 1 no-quote (44 failing).
- After: 76 apostrophe, 1 glyph, 28 initial, 30 near, 10 interrupted, 2 cross-source (41 failing, all listed under "Left as is"). The near count holds at 30 because deep 205 stays `near` on bullet and emphasis noise after its punctuation fix.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
