# Pass I quotations audit: openstax-accounting-vol1 (2026-10-15)

**Mode:** quotations. Deep reference read in full (790 of 790 lines). Source: `corpus.commons/demo/sources/converted/openstax-accounting-vol1.md` (44,822 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the three distillations (decision-making, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 12 (1 glyph, 4 near, 3 interrupted, 2 missing, 2 no-quote).
- Quotation-corrected: 7 lines in the deep ref (125, 129, 160, 212, 343, 427, 706).
- Marker-corrected: 1 line in the deep ref (570: one `[V]` → `[AP]`, one `[AP]` → `[V]`).
- Stripped: 0.
- Derived-tier edits: 0 (no wrong quotation or marker was copied there).
- Left as is (conversion noise): 4 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 125 | missing: contra-account quote dropped "an account" | Quote now reads "is an account paired with another account type, has an opposite normal balance to the paired account, and reduces the balance in the paired account at the end of a period" [V] | src 10492–10494 (Ch 4.2) |
| 129 | near: source sets the term in title case, “Cookie Jar Accounting” | Quote now "Cookie Jar Accounting" | src 10273 (Ch 4.1) |
| 160 | no-quote: gross sales and net sales paraphrased under `[V]`; net purchases also paraphrased under the same `[V]` | Quoted all four definitions in the source's words: gross purchases "the original amount of the purchase without considering reductions for purchase discounts, returns, or allowances"; net purchases "equals gross purchases less purchase discounts, purchase returns, and purchase allowances"; gross sales "the original amount of the sale without factoring in any possible reductions for discounts, returns, or allowances"; net sales "equals gross sales less sales discounts, sales returns, and sales allowances". `[V]` kept; the second `[V]` now carries its own (Ch 6.1) citation | src 15337–15340, 15511–15514 (Ch 6.1) |
| 212 | near: the five-item bulleted list was quoted inline with semicolons | Each bullet quoted separately, exact; lead-in now "The system's formal policies and procedures" (paraphrasing the source's lead-in) | src 21515–21526 (Ch 8.2) |
| 343 | glyph: `35-40%` and `2017-2026` in the IFRS Connection quote | En dashes, as the source prints them (`35–40%`, `2017–2026`). The unquoted key-statistics rows (704–705) and the light ref's table keep hyphens; they are not quotations | src 26884–26887 (Ch 10.1) |
| 427 | missing: "that" inserted ("a current situation that has an outcome") | Now A **contingency** "occurs when a current situation has an outcome that is unknown or uncertain and will not be resolved until a future point in time" [V], taking the source's own verb | src 31650–31651 (Ch 12.3) |
| 570 | no-quote: EPS formula in the deep ref's notation under `[V]` | `[V]` → `[AP]`, cited to the "Calculating Earnings per Share" subsection. The converted text does not print the formula (the line "The formula to calculate basic earnings per share is:" is followed by a blank where the image was); the prose supports the numerator ("removing the preferred dividends from net income") and denominator ("weighted average number of shares"). The next quotation, "many financial analysts believe that EPS is the single most important tool in assessing a stock's market price", is word for word and was marked `[AP]`; now `[V]` | src 37788–37790, 37824–37841 (Ch 14.5) |
| 706 | near: key-statistics row, same "cookie jar accounting" casing as 129 | Now "Cookie Jar Accounting" | src 10273 (Ch 4.1) |

## Changes, derived tier

- None. Propagation grep of the light ref and all three distillations for each corrected wording ("opposite normal balance", "gross sales", "net sales", "current situation", "weighted average common", "single most important", "cookie jar", "35-40", "2017-2026", "ensure assets are properly", "every time a sale"): no copied quotation or marker found. The light ref (27, 87, 129) and decision-making distillation (10, 40, 104) say "cookie-jar accounting" as unquoted paraphrase; the light ref's table (91–92) gives `35-40%` and `2017-2026` unquoted.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 62** (interrupted): the utilitarianism quote runs across the running header `**Access for free at openstax.org** **2.1 • Describe the Income Statement… 57**` (src 3758–3769). The `...` covers the dropped "Focusing on consequences … Put simply," (src 3772–3774) and is marked.
- **Deep 166** (near): the checker matched the Key Terms gloss ("every time a sale or purchase of inventory occurs", src 17237, 27924). The deep ref cites Ch 6.2 body text, which reads "every time a sale, or / purchase of inventory, occurs" (src 15768–15775) across the running header `**6.2 • Compare and Contrast Perpetual versus Periodic Inventory Systems 341**`. The quote matches the body text exactly.
- **Deep 270** (interrupted): "the guidelines now allow application to information technology (IT) activities as / well" runs across footnote 11 (Ken Tysiac, Journal of Accountancy), the running header and the page header `**8.7 • … 505**` (src 22655–22667).
- **Stakeholder-engagement 22** (interrupted): the same utilitarianism quote as deep 62, shortened with a marked `...`; the gap holds the running header and the dropped sentences (src 3758–3774).

## Triage cross-check

Every triage row was fixed:

- **Deep 125** (missing, "an account" dropped): restored; the quote now matches src 10492–10494.
- **Deep 160** (no-quote, gross/net sales paraphrase under `[V]`): replaced with the source's own definitions, quoted; the same defect on net purchases in the same sentence was fixed too.
- **Deep 427** (missing, "that" inserted): removed, and the quote now opens at the source's "occurs when", so the lead-in no longer needs "is".
- **Deep 570** (no-quote, EPS formula under `[V]`): marker now `[AP]`. The source prints no formula in the converted text, so no quotation is possible.

## Checker counts

- Before: 22 apostrophe, 1 glyph, 4 initial, 3 interrupted, 3 ligature, 2 missing, 4 near, 2 no-quote (12 failing).
- After: 22 apostrophe, 5 initial, 3 ligature, 3 interrupted, 1 near (4 failing, all conversion noise listed above). Initial rose by one because the "many financial analysts" quote (deep 570) is now checked as `[V]` and matches at that level (source capitalises "Many").

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Outside a quotations pass but noticed: deep 566 ends with a duplicated citation, `(Ch 14.4, "Are Companies Making Fewer Errors in Financial Reporting?")` printed twice. A full Pass I should drop the second.
