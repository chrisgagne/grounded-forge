# Pass I quotations audit: open-kanban (2026-10-15)

**Mode:** quotations. Deep reference read in full (176 of 176 lines before edits; 178 after). Source: `corpus.commons/demo/sources/converted/open-kanban.md` (210 lines, read in full). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 10 (7 near, 3 no-quote).
- Quotation-corrected: 7 lines in the deep ref (17, 93, 105, 108, 120, 122, 150).
- Marker-corrected: 0.
- Stripped: 0.
- Derived-tier edits: 3 lines (stakeholder-engagement 24 and 42, software-business 24).
- Left as is (conversion noise): 0. Every failing line was a real quoting slip.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 17 | near: the three-component bulleted list quoted inline as one span joined with semicolons | Each bullet quoted separately, exact: "A set of values that align it with the Agile and Lean Movements for IT and Software Development", "A set of practices that translate those values into action" and "An open source license that allow anyone to build upon it or modify it" | src 60–63 ("Open Kanban Definition") |
| 93 | near: the closing signature quoted with commas the source does not have (it sets the three parts on separate lines) | Now: Joseph Hurtado signs as "Founder AgileLion Institute" and "Kanban Ace Coach - An Open Kanban Method" [V] | src 160–162 |
| 105–107 | near (blockquote): the two permission bullets run inline with a semicolon | Blockquote now ends the lead-in at "fully allows you to:" and gives each bullet as its own quoted list line, exact. The bold span matches the source's bold (src 133) | src 133–135 ("Open Kanban's License") |
| 110 | near: "We only ask you that you:" and its two bullets quoted inline with a semicolon | Now "We only ask you that you:" "Give us credit" and "Contribute your best ideas back to Open Kanban root repository" [V], each exact | src 137–139 |
| 122 | no-quote (triage): Authorship row, names unquoted under `[V]` | The three names are the metadata table's words; quoted them: "Joseph Hurtado" (author); "Annita Yegorova Hurtado" (contributor); "AgileLion Institute" (sponsor). `[V]` kept | src 27–29 (metadata table) |
| 124 | no-quote (triage): "Kanban Ace (Hurtado's own)" unquoted under `[V]` | Now Kanban Ace, "an Agile and Lean Method based on Open Kanban" (Hurtado's own: he signs as "Kanban Ace Coach"). `[V]` kept; both quoted spans exact. "Hurtado's own" stays as the ingester's gloss, outside the quotes, grounded in the signature and in the sponsor's "Our Kanban Ace course" | src 76, 156, 162 |
| 152 | near: inner quotation ended `Efforts'` where the source has `Efforts."` (the period inside the author's quote mark) | Now `'Reduce the Batch Size of your Efforts.'` as at deep 76 | src 118 |

Line numbers after edits; 105 → 105–107 adds two lines, so later rows sit two lower than in the before report (108 → 110, 120 → 122, 122 → 124, 150 → 152).

Rows 114–119, 121 and 123 of the key-counts table also carry `[V]` on unquoted cells, but each holds a figure (5, 4, 3, 4, 3, 3.0, 1.00, 3): they are figure claims, which the checker's convention for stats tables marks `[V]` and counts without checking. Each count is stated or enumerated in the source (src 32, 60, 84–100, 104–121, 129, 133, 37–41, 78). Left as is.

## Changes, derived tier

| File:line | Finding | Change | Source |
|---|---|---|---|
| stakeholder-engagement:24 | no-quote: a `[BT]` marker sat *inside* the Kent Beck quotation ("Like Kent Beck [BT] noticed…"), so the closing `[V]` segment began mid-quote and carried no quoted span | `[BT]` moved out of the quotation: the quote now runs whole, then "(Beck is cited by name [BT].)". Quote matches at initial level (source "like") | src 91 |
| stakeholder-engagement:42 | near: same inline-list slip as deep 110 | Same fix: "We only ask you that you:" "Give us credit" and "Contribute your best ideas back to Open Kanban root repository." | src 137–139 |
| software-business:24 | near: same `Efforts'` slip as deep 152 | `'Reduce the Batch Size of your Efforts.'` | src 118 |

Propagation grep of the light ref and all five distillations for each corrected wording ("set of values that align", "set of practices that translate", "open source license that allow", "Founder AgileLion", "Kanban Ace Coach", "Give us credit", "Share, copy", `Efforts'`, "Hurtado's own", "Annita"): the light ref (13) and the distillations paraphrase the three components and the licence asks without quoting; the light ref's key-counts table (53–57) has no markers; every other `Efforts.'` quotation (light 31, 88; aar 18; retro 18; decision-making 14, 26; software-business 167) already carried the period. "Hurtado's own Kanban Ace" in decision-making 48 and software-business 44 is unquoted prose and the deep keeps the claim. No distillation's marker-continuity note is affected: no marker changed.

No edit changes a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps need re-stamping by the parent.

## Left as is (conversion noise)

- None. The source is markdown-native (no running headers, folios or ligature damage).
- Not noise but also not a defect: deep 41 sets the source's "Muda" as 'Muda' inside the blockquote's outer quote marks (nesting convention), and deep 19 and 157 use marked bracketed insertions ("[but]", "[LGPL v3, MIT]"). The checker passes all three.

## Triage cross-check

Both triage rows were real and are fixed:

- **Deep 120 (now 122)** (no-quote, Authorship row): fixed by quoting the three names from the metadata table (src 27–29); `[V]` now sits on quoted source words.
- **Deep 122 (now 124)** (no-quote, Kanban Ace row): fixed by quoting the source's description of Kanban Ace (src 76) and the signature "Kanban Ace Coach" (src 162); "Hurtado's own" kept as gloss outside the quotes.

## Checker counts

- Before: 24 initial, 7 near, 2 cross-source, 3 no-quote; 8 figure claims not checked (10 failing).
- After: 25 initial, 2 cross-source; 8 figure claims not checked (0 failing). Initial rose by one because the Kent Beck quotation at stakeholder-engagement 24 is now checked as a whole and matches at that level (source "like").

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
