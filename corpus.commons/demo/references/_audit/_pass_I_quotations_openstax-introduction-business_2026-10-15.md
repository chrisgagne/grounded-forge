# Pass I quotations audit: openstax-introduction-business (2026-10-15)

**Mode:** quotations. Deep reference read in full (910 of 910 lines). Source: `corpus.commons/demo/sources/converted/openstax-introduction-business.md` (53,932 lines; passages read around each hit). Scope open (CC BY 4.0), so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the three distillations (decision-making, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 8 (1 interrupted, 7 no-quote).
- Quotation-corrected: 1 line in the deep ref (485: paraphrase under `[V]` replaced by the source's words).
- Marker-corrected: 0.
- Stripped: 0.
- Derived-tier edits: 0.
- Left as is: 7 lines (1 conversion noise, 6 checker noise on correct figure claims).

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 485 | no-quote: "The *marketing concept* uses customer needs and wants as the starting point for product development [V]" is a paraphrase under `[V]`; the source never says "starting point" | Now: The *marketing concept* is "the use of marketing data to focus on the needs and wants of customers in order to develop marketing strategies" [V]; using it "means the product is created after market research is used to identify the needs and wants of the customers" [V] (Ch 11.1). Both match the source; the second drops the source's italics on "after". The claim is unchanged: the second quotation is the passage the paraphrase summarised | src 29522–29526, 29558–29562 (Ch 11.1, "The Marketing Concept") |

## Changes, derived tier

- None. Propagation grep of the light ref and all three distillations for "marketing concept" and "starting point": the only hit is the light ref (57), "The marketing concept uses customer needs as the starting point for product development.", unmarked paraphrase, supported by src 29558–29562. Left as is.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.
- The distillation lines in the report are all `apostrophe` or `initial` (no failing line).

## Left as is (conversion noise)

- **Deep 483** (interrupted): the marketing definition runs across the footer and running header `This OpenStax book is available for free at http://cnx.org/content/col25734/1.7` / `Chapter 11 Creating Products and Pricing Strategies to Meet Customers' Needs 413` between "finding out the needs and" and "wants of potential buyers" (src 29481–29489). The words are contiguous on the page.

Checker noise on figure claims. Each of these `[V]` segments is a figure claim, which the protocol's statistics convention marks `[V]`. The checker misses the figure because it splits the sentence at the period in "U.S." or strips the figures as a parenthetical. Each figure was checked against the source and matches:

- **Deep 37**: minorities to 56% by 2060, U.S. Census Bureau projection; from "more than 38 percent" today (src 1691, 1695–1699). Split at "U.S.".
- **Deep 99**: corporate philanthropy "exceeds more than $19 billion annually" (src 5695–5697). Split at "U.S.".
- **Deep 145**: 72/4/15, 10/15/27, 18/81/58 percent, Table 4.1, sourced to the U.S. Bureau of the Census, *Statistical Abstract* (src 9643–9647, 9695–9701). All figures sit in parentheses.
- **Deep 159**: "about 8.9 million direct jobs with a $890 billion economic output for the U.S. economy" (src 10760–10762). Split at "U.S.".
- **Deep 412**: flextime "in use at 57 percent of U.S. companies" (src 24885). Split at "U.S.".
- **Deep 722**: about 9,500 funds, more than $40 trillion worldwide, about 94 million individuals (src 45344–45350). Split at "U.S.".

## Triage cross-check

- **Deep 485** (no-quote, paraphrase under `[V]`, "The *marketing concept* uses customer needs and wants as the starting point for product development"): fixed. The source's definition and its "created after market research" sentence are now quoted. See table.
- **The other six no-quote lines** (37, 99, 145, 159, 412, 722): the triage classed them as noise, and each was checked against the source. All are correct figure claims; the checker loses the figure at a "U.S." split or inside a parenthetical. Left as is (see above).

Every triage row was addressed.

## Checker counts

- Before: 10 apostrophe, 19 initial, 1 interrupted, 7 no-quote (8 failing); 50 figure claims not checked.
- After: 10 apostrophe, 19 initial, 1 interrupted, 6 no-quote (7 failing, all noise listed above); 50 figure claims not checked.

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Figure precision (fixed by the parent after this log): deep 37 and key-statistics row 825 gave "~38%" where the source says "more than 38 percent" (src 1691, 4230); deep 99 gave "~$19 billion" where the source says "exceeds more than $19 billion" (src 5695). All three are `[V]` figure claims, so the "~" now reads "more than" (row 825: ">38%").
- Checker: a `[V]` figure claim containing "U.S." or with its figures in parentheses reports as no-quote. Six of this source's seven no-quote lines are that false positive.
