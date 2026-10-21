# Pass I quotations audit: liberating-structures-handbook (2026-10-15)

**Mode:** quotations. Deep reference read in full (279 of 279 lines). Source: `corpus.commons/demo/sources/converted/liberating-structures-handbook.md` (2,767 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 38 (19 near, 6 page, 4 interrupted, 5 missing, 4 no-quote). The 4 interrupted and 5 missing lines all came from the Levels of Accountability ladder (deep 133, decision-making 101).
- Quotation-corrected: 14 lines in the deep ref (45, 77, 81, 91, 93, 105, 115, 133, 137, 192, 206, 214, 260, 268).
- Marker-corrected: 6 lines in the deep ref (25, 91, 191, 200, 209, 215: `[V]` → `[AP]`).
- Stripped: 1 clause (deep 89).
- Derived-tier edits: 10, in the light ref (46, 76, 78) and four distillations (aar 28, 60; retro 28; decision-making 101; stakeholder-engagement 110, 120, 237).
- Left as is (conversion noise or false positive): 8 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 25 | no-quote (triage): "Ownership is participation in development; buy-in is being convinced after the fact…" is a summary under `[V]` | Marker `[V]` → `[AP]`. The source's own words are already quoted `[V]` at line 17 | src 259–266 |
| 45 | near: "Nothing About Me Without Me" quoted in title case; the source prints the heading in capitals | The section name is a reference, not a quotation: now italic, *Nothing About Me Without Me* | src 46, 453 |
| 77 | near: 'this is what The Client ought to do' closed the inner quote before the source's full stop | Now 'this is what The Client ought to do.' as the source prints it | src 872–873 |
| 81 | near: the seven Appreciative Interviews characteristics, a bulleted list, quoted inline as one string joined by semicolons | Each bullet quoted separately, exact | src 1209–1215 |
| 89 | no-quote: "(which is not wicked because it is a complaint, not a paradox)" under `[V]`; the source gives no reason | Clause stripped. The counter-example is now introduced with the source's own label, "This is not a wicked question" [V] | src 1399–1402 |
| 91 | no-quote: "questions are categorised, prioritised (e.g. dot voting), or read aloud in patterns" under `[V]`; also near: the four suggested prompts, a bulleted list, quoted as one string | The procedure clause is now a paraphrase marked `[AP]` and matches the source (categorise, prioritise by "dot voting", or read them all out loud and talk in small groups about patterns); the `[V]` stays on the "courageous and provocative" quotation. Each prompt quoted separately, exact | src 2044–2078 |
| 93 | near: the TRIZ quote closed an inner quotation mark after "1940s." that the source never closes, and joined the two passages with an ellipsis inside it | Split into two exact quotations: TRIZ is "a problem-solving … in the 1940s"; "As a Liberating Structure, we're only going to use one piece of the TRIZ approach". The source's own opening quotation mark (src 1316) is left unclosed in the source; noted, not copied | src 1316–1325 |
| 105 | near: the four Mulago criteria, printed as bullets, quoted inline joined by semicolons | Each criterion quoted separately, exact | src 955 |
| 115 | no-quote (triage): Café Agreements and talking object named in italics under `[V]` with no quotation | Now quoted in the source's words: "Conversation Café Agreements" ("Open-mindedness", "Acceptance", "Curiosity", "Discovery", "Sincerity", "Brevity") and a "talking object". `[V]` kept | src 1449–1458, 1472 |
| 133 | 4 interrupted, 5 missing, 2 near: the ladder was quoted as joined "Level — 'phrase'" pairs ("Take Action and Learn — Make it happen, renewal", etc.) that the source never prints; "Denial — 'Woe is me'" and "'This has nothing to do with me.'" added a dash and a full stop; the four further labels were italic under `[V]` (a no-quote on the re-run) | The converted page prints the seven levels as one list and the seven disposition phrases as a second list in the same order. Each is now quoted separately, exact, with the order stated; the bottom layer reads "Denial" ("Woe is me") and "This has nothing to do with me"; the four further labels are quoted | src 1853–1919 |
| 137 | near: the Yes And quote ended 'yes and but', where the source closes the passage with "yes and but." | The quotation now ends at "accept the offer"; the last phrase is quoted on its own: the most common response is "yes and but" | src 2235–2249 |
| 191 | key-statistics row: a count (~32) and summary under `[V]`, with the group names quoted in title case ("Seeing Complexity", "Random Thoughts") | Marker `[AP]`; group names now italic and given in full (*Seeing Complexity and Complex Systems*, *Random Thoughts*) | src 167, 178, 2275, 2432 |
| 192 | near (triage): "4-tops (that seat 4-6 people)" | Quote mark moved to match the source: "4-tops" (that seat 4-6 people) | src 308 |
| 200 | key-statistics row: Wise Crowds phase timings, unquoted summary under `[V]` | Marker `[AP]` | Wise Crowds section |
| 206 | key-statistics row: "1 to 5" unquoted under `[V]` | Now the source's words, "a scale of 1-5"; `[V]` kept | src 1685 |
| 209 | key-statistics row: Six Words criteria abbreviated, unquoted under `[V]` | Marker `[AP]` (the exact criteria are quoted at line 105) | src 955 |
| 214 | key-statistics row: "3 sequential questions in the named order", unquoted under `[V]` | Now: 3 questions, asked "in the following order"; `[V]` kept | src 1725 |
| 215 | key-statistics row: four pattern-language primitives, summary under `[V]` | Marker `[AP]` (the full passage is quoted `[V]` at line 19 and in the blockquote at 181) | src 2755 |
| 260 | near: same inner-quote close as 77 | Now 'this is what The Client ought to do.' | src 872–873 |
| 268 | paraphrase "wait at least 20" under `[V]` (not flagged; found while working 212) | Now quoted: "wait at least 20 seconds" | src 2589 |

## Changes, derived tier

Propagation grep of the light ref and all five distillations for each corrected wording (Café Agreements, Third Ear, not wicked / complaint, 1940s, Less than 8, read aloud, dot voting, Nothing About Me Without Me, Seeing Complexity, 4-tops, ought to do, Denial, Woe is me, Take Action and Learn, Make it happen, nothing to do with me, It's my fault, yes and but, at least 20, participation in development, What questions would you most, TRIZ is, "Why?", 1 to 5, talking object). Fixed:

- **Light ref 46:** "Third Ear and Third Eye" quoted as one phrase → "Third Ear" and "Third Eye" (src 1212).
- **Light ref 76:** bottom layer "Denial / 'This has nothing to do with me.'" → "Denial" ("Woe is me") and "This has nothing to do with me" (src 1914–1917).
- **Light ref 78:** ("the most common response is 'yes and but'") → ("The most common response is, 'yes and but.'") (src 2235–2249).
- **aar 28** and **retro 28** (near): "Denial / Woe is me" → "Denial" ("Woe is me").
- **aar 60** (near): "Why?" at least five times → "WHY?" at least five times (src 1060).
- **decision-making 101** (2 interrupted): "Take Action and Learn / Make it happen, renewal" and "Wait 'n Hope / Somebody should do something" → "Take Action and Learn" ("Make it happen, renewal") and "Wait 'n Hope" ("Somebody should do something").
- **stakeholder-engagement 110** (near): "WHAT? SO WHAT? NOW WHAT?" (three sub-headings with text between them, src 1728–1742) → "WHAT?", "SO WHAT?", "NOW WHAT?".
- **stakeholder-engagement 120** (not flagged, same composite): "Take Action and Learn / Make it happen" → "Take Action and Learn" ("Make it happen").
- **stakeholder-engagement 237:** the evidence-marker note said the deep ref has "no `[AP]` or `[AR]` markers"; after the marker changes above that was false. Now notes `[AP]` on a few paraphrases.

The other marker-continuity notes (aar 140, retro 164, decision-making 185, software-business 226) stay true: each passage they name is still `[V]` (or `[BT]`) in the deep ref.

- Light ref 135 and retro 32 (fixed by the parent after this log): both carried the reason removed from deep 89. Light ref 135 now says only that the handbook's example of a question that is not wicked is a gripe about headquarters; retro 32 says the handbook gives no reason and reads the example against its definition (no embedded paradox or tension). Source: "This is not a wicked question:" (src 1399).

## Left as is (conversion noise or false positive)

- **Deep 99, aar 34, retro 22** (page): the Mini Constellations quotation runs across the list number "1." (src 1803–1806). List numbering, not a dropped word.
- **Deep 129, stakeholder-engagement 121** (page): "Expanding the periphery" runs across the list numbers "1." and "2." (src 2006–2018).
- **Deep 147** (page): the Tic Tac Toe quotation runs across the list numbers "4." and "5." (src 2360–2366).
- **Software-business 170** (2 near): "Choosing Space" and "Aesthetics Are Important" are the distillation's `(Source: "…")` citation labels, not quotations; the source prints the headings in capitals (src 299, 328). The same title-case label convention runs through every distillation.
- **Deep 277** (apostrophe, not failing): the front-matter quote crosses bold markers `** **` in the converted text (src 11); markup noise.

## Triage cross-check

- **Deep 25** (no-quote, paraphrase under `[V]`): fixed, marker now `[AP]`; the source's words are quoted at line 17.
- **Deep 115** (no-quote, paraphrase under `[V]`): fixed, the agreements and talking object now quoted in the source's words.
- **Deep 192** (near, "4-tops (that seat 4-6 people)"): fixed, quote mark moved to close after "4-tops" as the source does.

## Checker counts

- Before (7 files): 123 apostrophe, 22 initial, 19 near, 6 page, 4 interrupted, 5 missing, 4 no-quote (38 failing).
- After (7 files): 127 apostrophe, 22 initial, 2 near, 6 page (8 failing, all listed under "Left as is"). The full-set re-run reported one more no-quote (deep 133, the four ladder labels); that was fixed and the deep ref re-checked alone: 47 apostrophe, 11 initial, 3 page. Apostrophe rose by 4 because split list quotations are now checked one by one.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Claims the derived tier carries that the deep ref no longer does: the deep ref no longer says the bozos question is not wicked "because it is a complaint, not a paradox" (the source gives no reason). The light ref 135 ("Complaints about other groups are not wicked.") and retro 32 ("— a complaint, not a paradox") still carry that gloss; re-derive.
- Outside a quotations pass but noticed: deep 15 adds "if the patterns are named and shared" after two accurate quotations under one `[V]`; deep 265 adds an interpretive note ("the surrounding text is concerned with the over-specification failure mode") after a `[V]` quotation. A full Pass I should check both against the source.
