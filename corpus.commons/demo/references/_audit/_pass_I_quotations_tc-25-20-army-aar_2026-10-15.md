# Pass I (quotations mode): tc-25-20-army-aar, 2026-10-15

**Scope:** quotation fixes from `scripts/check-verbatim.py` across the deep reference and this source's four distillations, plus the human triage rows. The `Pass I applied` stamp is left as it is.
**Deep reference:** `corpus.commons/demo/references/tc-25-20-army-aar-deep.md`, read in full (269 of 269 lines).
**Source:** `corpus.commons/demo/sources/converted/tc-25-20-army-aar.md` (Scope: open). Each fix below was checked against the converted text at the source line given.

## Checker counts

| Run | initial | near | page | interrupted | no-quote |
|---|---|---|---|---|---|
| Before | 16 | 11 | 1 | 9 | 9 |
| After | 16 | 0 | 1 | 9 | 0 |

`initial` lines (16) need no fix. The remaining `page` (1) and `interrupted` (9) lines are conversion noise, explained under "Left as is".

## Summary

- Actionable lines worked: 20 (11 near, 9 no-quote).
- Quotations corrected to the source's punctuation: 11 (10 in the deep, 1 in the stakeholder-engagement distillation).
- Source words given quotation marks (marker kept [V]): 8 (deep line 183; table cells at lines 233, 234, 236, 237, 239, 240, 241).
- Markers corrected: 1 (deep line 153, [V] to [AP]).
- Stripped: 0.

## Changes: deep reference

The source sets these passages as lists, one item per line, each item ending in a full stop (or with no punctuation). The deep reference had joined the items with semicolons inside the quotation marks.

- **Line 19 and line 52** (near). "The AAR process has four steps: Step 1. Planning; Step 2. …" The source (lines 267–274) has a colon, then four unpunctuated list items. Split into "The AAR process has four steps": followed by four separately quoted items ("Step 1. Planning", … "Step 4. Following up (using AAR results)").
- **Line 25** (near). Semicolons replaced with the source's full stops (source lines 108–111).
- **Line 58** (near). Semicolons replaced with full stops (source lines 332–336).
- **Line 62, informal evaluations** (near). The quote ran "They are Conducted by…" across the source's "They are-" list lead-in and joined the items with semicolons. Re-quoted as "Informal evaluations are most commonly used at battalion level and below"; they are "Conducted by all leaders in the chain of command. Continuous. Used to provide immediate feedback on training proficiency" (source lines 302–306).
- **Line 62, formal evaluations** (near). Same pattern. The quote now closes after "(TVIs)", and the three list items are quoted with full stops (source lines 309–318).
- **Line 66** (near). Semicolons replaced with full stops (source lines 379–381).
- **Line 95** (near). The six critical events carry no punctuation in the source (lines 606–611). Each is now quoted separately rather than joined with semicolons.
- **Line 126** (near). Semicolons replaced with full stops (source lines 853–857).
- **Line 153** (no-quote; triage row). The seven-BOS list sat under [V] with no quotation marks and read "Mobility/countermobility/survivability". Changed the wording to the source's "Mobility, countermobility, survivability (M, C, S)" (source line 965) and the marker to [AP]. C² is kept because the converted text garbles the superscript as "C [2]".
- **Line 163** (near). Semicolons replaced with full stops (source lines 1021–1027).
- **Line 183** (no-quote; triage row). The text was the source's own words, unquoted, with italics the source doesn't have. Now quoted word for word with the italics removed: "Immediately or shortly after the training event, leaders should conduct a trained-practiced-untrained (T-P-U) assessment and develop a future-training concept" (source lines 1126–1128).
- **Table, line 233** (no-quote; triage row). The cell "Horseshoe" now carries "Horseshoe arrangements encourage discussion and allow everyone to see" (source line 743, Ch 3) and "Seating should be in a horseshoe shape when possible" (source line 1302, App A).
- **Table, line 234** (no-quote; triage row). The cell "Two echelons above" now reads Two levels above: "the headquarters two levels above the unit being evaluated conducts theirs" (source lines 321–322). The section name in the citation is corrected to "The After-Action Review Plan", matching the source heading and line 62.
- **Table, line 236** (no-quote; triage row). The cell now quotes "All incidents or near incidents of fratricide … will be discussed in detail" (source lines 987–989).
- **Table, line 237** (no-quote; triage row). The cell now quotes "Safety should be specifically addressed in every AAR" (source line 1101).
- **Table, line 239** (no-quote; triage row). The cell now quotes the source's three technique headings: "Chronological Order of Events" / "Battlefield Operating Systems (BOS)" / "Key Events/Themes/Issues".
- **Table, line 240** (no-quote; triage row). The cell now quotes the four step items as the source prints them.
- **Table, line 241** (no-quote; triage row). The cell now quotes "trained-practiced-untrained (T-P-U)" (source line 1127).

## Changes: distillations

- **`distillations/stakeholder-engagement/tc-25-20-army-aar-stakeholder-engagement.md` line 30** (near). The same semicolon-joined facilitation-techniques quote as deep line 126. Semicolons replaced with the source's full stops (source lines 853–857).

## Propagation check

I grepped the light reference (`references/tc-25-20-army-aar.md`) and all four distillations for every corrected wording: the semicolon-joined lists, the four-step quote, "They are", "countermobility", T-P-U, "two levels" / "Two echelons", horseshoe, fratricide and safety. The only other copy of a wrong quotation was stakeholder-engagement line 30, fixed above. The light reference has these facts only as unmarked paraphrase ("mobility/countermobility/survivability", "Two echelons above" in its table) and needs no quotation edit.

**Derived-tier claims affected (for the parent to re-derive; not edited here):** `distillations/stakeholder-engagement/tc-25-20-army-aar-stakeholder-engagement.md` line 206 counts the deep reference's markers ("133 [V] markers (on 82 lines), 5 [BT] markers, 1 [AP] marker") and says "The one [AP] marker is the thesis-level paraphrase…". After the line 153 change, the deep carries 2 [AP] and one fewer [V], so both statements are stale. `distillations/retro/tc-25-20-army-aar-retro.md` line 147 says the T-P-U categories are [V] in the deep. That is still true: line 241 keeps [V], now with a quote.

## Left as is (conversion noise)

- **Deep line 29 and line 258** (interrupted). The source has "onthe-spot" (line 129). The line-break hyphen was joined during conversion, and the deep correctly keeps "on-the-spot".
- **Deep line 42** (interrupted). The source has "resourceintensive" (line 153), the same line-break join.
- **Deep line 74, first quote** (interrupted). The source has "platoonlevel" (line 456), the same join, and the quote also spans page furniture ("8", "TC 25-20").
- **Deep line 74, second quote, and decision-making distillation line 42** (interrupted). The source has "deadend" (line 469), a compound join.
- **Deep line 134, retro distillation line 20, and stakeholder-engagement distillation line 20** (interrupted). The source has "openended" (line 900), the same join.
- **Deep line 153** (page). The quote spans a page break ("18", "TC 25-20", page furniture). The converted text also prints "(Figure 42)" for the original "(Figure 4-2)", a line-break hyphen lost in conversion. The quote keeps "Figure 4-2", the TC's own figure number (the figure caption at source line 971 reads "Figure 4-2. The Seven BOS"), rather than copying the garble.
- **16 `initial` lines** (deep and distillations). These are only capital letters changed at the start of a quote. They need no fix.

## Triage cross-check

All 9 triage rows (deep 153, 183, 233, 234, 236, 237, 239, 240, 241) are fixed as described above. The triage's classification held for each row. The figure claims the checker does not check (11, e.g. Figures 2-1, 2-2, 3-1, 4-1, A-1, and table rows 229–232, 235, 238) were outside this run's work list and are left unchanged.

## Open

- Quotations mode only: the deep's non-quotation prose claims were read but not re-traced against the source.

## Derived tier, settled by the parent

- Stakeholder-engagement line 206 now reads 132 [V] markers (on 82 lines) and 2 [AP] markers, and names both [AP] lines: the facilitation-techniques paraphrase (Ch 4, "Introduction and Rules") and the seven-BOS list (Ch 4, Figure 4-2). Counts taken from the edited deep reference. Light reference and distillations restamped against the edited deep.
