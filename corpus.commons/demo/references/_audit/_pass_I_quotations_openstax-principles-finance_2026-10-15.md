# Pass I (quotations mode): openstax-principles-finance, 2026-10-15

**Scope:** quotation and `[V]`-marker fixes reported by `scripts/check-verbatim.py`, plus quotations found wrong while working them. Deep reference read in full (852/852 lines). Source: `corpus.commons/demo/sources/converted/openstax-principles-finance.md` (35,453 lines); every fix below was checked against it, with source line numbers given. The `Pass I applied` stamp is left unchanged.

**Files checked:** the deep reference, plus the three distillations (`decision-making`, `software-business`, `stakeholder-engagement`). The distillations had no actionable checker lines, only `apostrophe` and `initial` ones, which need no fix.

## Counts

- Actionable checker lines worked: 22 (18 no-quote, 1 near, 1 missing, 2 interrupted), plus 1 unreported `[V]` defect (line 830). All 18 rows of the human triage are covered below.
- Quotation-corrected: 2 (lines 415, 569).
- Quotation marks added or source wording quoted, `[V]` kept: 12 (lines 27, 33, 36, 130, 175, 537, 573, 803, 828, 829, 831, 832), plus line 830.
- Marker-corrected `[V]` → `[AP]`: 7 (lines 13, 34, 35, 45, 153, 616; the split segments at 36, 537, 573 and 830 also carry a new `[AP]` on their paraphrased half).
- Stripped: 0.
- Left as is: 2 (lines 569 second quote, 604; conversion noise).

## Checker before / after

- Before: `13 apostrophe, 23 initial, 1 near, 2 interrupted, 1 missing, 18 no-quote; 27 figure claim(s) not checked`
- After: `13 apostrophe, 23 initial, 2 interrupted; 26 figure claim(s) not checked`

## Changes (deep reference line numbers)

- **13** (thesis; triage: paraphrase under `[V]`). The three-areas sentence is the ingester's paraphrase, with "maximise" and other changes (src 863, 879, 934, 959). `[V]` → `[AP]`.
- **27** (triage: source words, unquoted). The sentence is word for word src 870–871. Added quotation marks; `[V]` kept.
- **33** Default risk (source words, unquoted). The span matches src 1120. Added quotation marks.
- **34** Inflation risk (paraphrase). Source: "investors have less purchasing power from the realized cash flows from an investment due to rising prices or inflation" (src 1125–1127). `[V]` → `[AP]`.
- **35** Diversifiable risk (paraphrase; src 1129–1131). `[V]` → `[AP]`.
- **36** Non-diversifiable risk. Quoted the source span "what remains after portfolio diversification has eliminated unnecessary diversifiable risk" (src 1134–1136) as `[V]`; "measured with beta" is now `[AP]`.
- **45** Primary/secondary market (paraphrase). The Ch 1.5 wording puts "new" and "used" in their own quotation marks (src 1611–1612). The unquoted form appears only in Ch 12.1 (src 20248), a different section. `[V]` → `[AP]`.
- **130** CPI (paraphrase). Rewrote it so the quoted span is the source's own sentence: the BLS "divides these purchases into eight major categories: …" (src 4830–4831); `[V]` kept.
- **153** Spot exchange rate (paraphrase; src 5399–5400: "the price you would pay to purchase Mexican pesos right now"). `[V]` → `[AP]`.
- **175** Revenue recognition. Quoted the source: "involves recording sales or fees earned within the period earned" (src 6442); `[V]` kept.
- **415** (near). The quote wrapped the source's own quotation in nested marks and lower-cased the sentence opening. Now it reads: the payment of dividends to shareholders is "almost a last resort for corporate management" [V] (src 18536). The light ref and the distillations already quote only the "almost a last resort…" span, so nothing needed propagating.
- **537** Beta (paraphrase). Quoted "The measure of how much a stock moves with the market is known as its beta" (src 25973–25974) `[V]`; "it measures the stock's systematic risk" is now `[AP]` (src 25972).
- **569** (missing; triage: reworded a→the criterion). The source reads "The NPV method provides a criterion for whether or not a project is a good project" (src 26984–26985). Corrected to: the NPV method "provides a criterion for whether or not a project is a good project".
- **573** IRR (paraphrase). Quoted the source definition "the discount rate that sets the present value of the cash inflows equal to the present value of the cash outflows" (src 27114–27115) `[V]`; "the discount rate at which NPV equals zero" is now `[AP]` (src 27118, 27219). Section anchor corrected to the source heading "Internal Rate of Return (IRR) Calculation" (src 27112).
- **616** After-tax cost of debt `Rd × (1 - T)` (no-quote). The equation image was dropped in conversion; the converted text has only the surrounding prose, with a gap (src 28404–28406). No verbatim text supports `[V]`. `[V]` → `[AP]`.
- **803** Key-statistics row (`[V]` on an unquoted table cell). The value cell now quotes "approximately a dozen stocks" (src 25876–25877); `[V]` kept.
- **828** Carlos Slim Helu (cited-person entry). Replaced the description with his quotation as the source gives it (src 19838–19839); anchor is now (Ch 12, "Why It Matters").
- **829** Sam Ewing (cited-person entry). Replaced "quoted defining inflation in folksy terms" (an evaluative label the source doesn't use) with the quotation (src 20371–20372, Ch 12.2).
- **830** Ted Williams (not reported; the "30 per cent" figure masked the no-quote case). Quoted "Baseball is the only field of endeavor where a man can succeed three times out of ten and be considered a good performer" (src 14540–14541) `[V]`; the contrast with capital decisions is now `[AP]` (src 14541–14544). Anchor: (Ch 9, "Why It Matters").
- **831** Mark Twain (cited-person entry). Replaced the description with the full quotation (src 19826–19827).
- **832** Winston Churchill (cited-person entry). Quoted "Those that fail to learn from history are doomed to repeat it" (src 19833–19834).

## Left as is

- **569** (second quote, `interrupted`). "does not always provide a good solution … pursue them all" is continuous in the printed text. The gap in the converted file is a footnote about the financial calculator and a running header ("474 16 • How Companies Think about Investing") at a page break (src 26986–26993). That is conversion noise, not a defect.
- **604** (`interrupted`). The quote runs across a page break; the gap holds page furniture ("Access for free at openstax.org", running header "16.6 • Using Excel to Make Company Investment Decisions 487"; src 27758–27766). Conversion noise.
- All `apostrophe` (13) and `initial` (23) lines in the deep reference and the distillations. These are straight vs curly apostrophes and sentence-initial case only, which need no fix.

## Derived tier

- **Propagation grep:** I searched the light reference and all three distillations for each corrected wording (the nested Buffett quote, "the criterion for whether", the IRR, spot-rate, CPI, primary-market and beta definitions, and the five cited-person entries). None of them carries the wrong wording, so no derived-tier edits were made.
- **For the parent:** none of these edits changes a claim's substance. Lines 829 and 830 drop evaluative descriptions ("folksy terms", "benchmark") that the light ref and the distillations don't carry. The derived-provenance stamp will be stale against the edited deep reference; re-stamp or re-derive at the parent's discretion.

## Open

- None from the checker. Line 616's formula and line 45's Ch 1.5 wording come from the conversion: an equation image dropped in the first case, curly-quoted "new"/"used" in the second. Both are paraphrased, so neither is a quotation defect.
