# Pass I quotations audit: barbrook-johnson-systems-mapping (2026-10-15)

**Mode:** quotations. Deep reference read in full (374 of 374 lines). Source: `corpus.commons/demo/sources/converted/barbrook-johnson-systems-mapping.md` (9,124 lines; passages read around each hit). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 8 (3 interrupted, 1 missing, 4 no-quote).
- Quotation-corrected: 1 in the deep ref, 1 in a distillation (distillation-only defect).
- Marker-corrected: 4 in the deep ref.
- Derived-tier prose corrected to match a marker change: 1 (stakeholder-engagement evidence-continuity note).
- Stripped: 0.
- Left as is (conversion noise): 2 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 133 | missing: two sentences joined by an ellipsis in reverse order. "Our experiences over the last ten years…" comes first in the source; "PSM has evolved a lot…" comes about 30 lines later | Split into two quotes in source order: "Our experiences over the last ten years, as we have developed Participatory Systems Mapping (PSM), are one of the core motivations for this book" [V]; "PSM has evolved a lot over the last ten years" [V] | src 3299–3300, 3332 |
| 330 | no-quote: Key-statistics row lists Kim's eight archetypes unquoted under `[V]` | `[V]` → `[BT]` (the row already names Kim 2000). The names are Kim's, which the source credits (it sets each name in its own quote marks, across a page break). The `[V]` quote of the framing phrase at line 121 stays | src 2926–2935 |
| 354 | no-quote: "Named as one of the three failures…" describes the source, it does not quote it | `[V]` → `[AP]`; citation now adds About the Book, the only place the source numbers the three as (i), (ii), (iii). Ch 1 lists the same three without numbers | src 239–243; 1284–1286 |
| 355 | no-quote: "Named as second failure" | `[V]` → `[AP]`, About the Book added to the citation | src 239–243; 1284–1286 |
| 356 | no-quote: "Named as third failure and recurring concern…" | `[V]` → `[AP]`, About the Book added to the citation | src 239–243; 1284–1286 |

## Changes, derived tier

- `distillations/stakeholder-engagement/barbrook-johnson-systems-mapping-stakeholder-engagement.md:190`: the quote "who has on-the-ground knowledge / strategic overview" compressed two clauses with a slash. Now "who has on-the-ground knowledge and who has a strategic overview" [V], as the source reads (src 3566–3568; the converted text carries a soft hyphen in "on-the-ground"). The "who is often overlooked" fragment keeps its `[V]`.
- `distillations/stakeholder-engagement/barbrook-johnson-systems-mapping-stakeholder-engagement.md:235`: the evidence-continuity note said the positions against "black-box" modelling and the horrendogram failure mode are `[V]` in the deep ref. After the deep 354–356 marker changes that is no longer true. It now says the validation-as-quantitative-truth position is `[V]`, the black-box and horrendogram positions are `[AP]`, and the horrendogram passage itself is quoted `[V]` (Ch 1).
- Propagation grep of the light ref and all five distillations for "evolved a lot", "Our experiences over", "drifting goals", "black-box", "paralysing", "three failures", "on-the-ground", "surprised just how much": no other copy of a wrong quotation or marker. The archetype rows in decision-making (40) and software-business (38) put `[V]` only on the quoted phrase "outline common and intuitive types of core system engines", which matches the source; the names follow unquoted and carry `[BT]`. Software-business 72 and 235, aar 111 and the light ref (21, 93) are unmarked paraphrase. The light ref's "one of three historical failures" (93) is supported by About the Book (src 239–243).
- No change alters a claim the light ref carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 307** (interrupted): the Ch 12 take-home quote runs across the running header and page number `12 CONCLUSION` / `181` between "how much" and "they gain from this" (src 8692–8701). The words are contiguous on the page.
- **Decision-making 77** (interrupted): the same break inside "surprised just how much they gain" (src 8692–8701).

## Triage cross-check

- **Stakeholder-engagement :190** (interrupted, compressed with '/'): fixed in place; quote restored to the source's full clause. See derived tier above.
- **Deep :133** (missing, elision pieces out of order): fixed by splitting into two quotes in source order. See table.
- **Deep :330** (no-quote, archetype list): fixed; `[V]` → `[BT]` (the row already names Kim 2000).
- **Deep :354, :355, :356** (no-quote, descriptive entries): fixed; `[V]` → `[AP]`. These describe how the source frames the three problems; they are not quotations.

Every triage row was addressed.

## Checker counts

- Before: 70 apostrophe, 57 initial, 3 interrupted, 1 missing, 4 no-quote (8 failing).
- After: 70 apostrophe, 57 initial, 2 interrupted (2 failing, both the conversion noise listed above).

## Open

- Stamp left as is (quotations mode). No commit made; no build run.
- Derived-provenance stamps for the light ref and five distillations are stale against the edited deep ref; the parent re-stamps.
