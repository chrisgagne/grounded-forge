# Pass I (quotations mode): openstax-economics-3e, 2026-10-15

**Mode:** quotations. Scope: fix what `scripts/check-verbatim.py` reports for the deep reference and this source's three distillations, plus quotations found wrong while doing so; propagate corrected wording to the light reference and distillations. The deep ref's `Pass I applied` stamp is left as it is.

**Inputs:** deep ref `references/openstax-economics-3e-deep.md` (589 lines, read in full); source `sources/converted/openstax-economics-3e.md` (passages read around each finding); checker work list run before this pass; human triage of an earlier checker run (cross-check).

**Scope:** open-nc, so every `[V]` quotation must match the converted source word for word.

## Counts

- Checker findings before (deep ref + 3 distillations): 1 apostrophe, 2 glyph, 6 initial, 5 near, 1 interrupted, 5 missing, 13 no-quote (actionable: 26).
- Checker findings after (same files plus the light ref): 1 apostrophe, 6 initial, 1 interrupted (actionable: 1, left as is, see below). The light ref contributes no findings.
- Quotations corrected or replaced: 15 (deep ref 12: lines 21, 27, 91, 101, 109, 141, 203, 227, 245, 478, 552, 575; light ref 1; distillations 2).
- Markers corrected: 13 (`[V]` removed at 63, 109, 195; `[V]` to `[BT]` at 540, 542, 554, 555, 556, 557, 561, 567, 569, 570).
- Lines stripped: 1 (deep ref Connections entry for Follett/Robbins).
- Initial-capital, apostrophe lines: need no fix.

## Deep reference changes

Line numbers are pre-edit.

| Line | Finding | Change | Source passage |
|---|---|---|---|
| 21 | (unflagged; same defect as 478) quote "an indirect subsidy from consumers to producers" is a section title, recased | Paraphrased; quoted the title exactly: "Protectionism: An Indirect Subsidy from Consumers to Producers" | src 47477 (Ch 34.1 heading) |
| 27 | glyph: quote put an em dash where source has `time-` | Split into two exact spans: "the ultimate scarce resource is time": "everyone, rich or poor, has just 24 expendable hours in the day" | src 1343-1344 |
| 63 | no-quote: trailing `[V]` after two individually marked quotes | Removed the redundant trailing `[V]`; each quote keeps its own | src Ch 2.2 |
| 91 | near: Marshall quote nested with `'...'` and dropped the source's closing punctuation | Quoted only Marshall's words, "whether it is the upper or the under blade of a pair of scissors that cuts a piece of paper"; "like arguing" moved outside quotes as the text's framing | src 4981-4983 |
| 101 | near + missing (triage: verb form changed). "an efficient mechanism for information" is the 4.3 section heading, recased; "convey information about conditions of demand and supply" is a Ch 22.4 sentence ("conveying information about conditions of demand and supply", src 31847), not Ch 4.3, and in a different verb form | Replaced with the Ch 4.3 passage: prices "serve as a remarkable social mechanism for collecting, combining, and transmitting information that is relevant to the market" and serve as "messengers to convey that information to buyers and sellers" [V] | src 6395-6398 |
| 109 | no-quote: `[V]` on a paraphrase of Table 5.2 values; "substitutable items" is not the source's framing | Table values restated without `[V]` (cited to Table 5.2); added the source's own sentence as the `[V]` quote: "demand for necessities such as housing and electricity is inelastic, while items that are not necessities such as restaurant meals are more price-sensitive" | src 7280-7322 |
| 141 | missing (triage: "must accept" for "forces it to accept") | Now: a **price taker** "because the pressure of competing firms forces it to accept the prevailing equilibrium price in the market" [V] | src 11252-11253 |
| 195 | no-quote: trailing `[V]` after two individually marked quotes | Removed the redundant trailing `[V]` | src Ch 13.3 |
| 203 | missing (triage: "their" for "the worker's") | Restored "the value of the worker's marginal productivity to the firm" | src 20530-20532 (Key Terms entry; same rule stated in 14.1) |
| 227 | missing (triage: source typo "program" silently fixed) | Restored source word: "one of the largest assistance program [sic] for low-income groups". Unquoted figures corrected to the source's wording: "as of December 2021, about 25 million eligible workers and families received about $60 billion" (was "about 25 million workers ... in 2021") | src 21358-21359 |
| 245 | missing (triage: behavior localised to behaviour) | Restored "riskier behavior" | src 23092 |
| 478 | near: "an indirect subsidy from consumers to producers" exists only as the section title, in title case | Now quotes the title exactly: "Protectionism: An Indirect Subsidy from Consumers to Producers" [V] | src 47477 |
| 539 | no-quote: `[V]` on a list entry. The entry asserted Follett is not cited (a non-connection) and duplicated the Robbins entry at 570 | Stripped the line | Follett: no hit in source; Robbins: src 2401 |
| 540 | no-quote (Downs) | `[V]` to `[BT]` | src 25489 (Ch 18.1) |
| 542 | no-quote (Kahneman and Tversky) | `[V]` to `[BT]` | src 9037 (6.3), 22731 (16.1) |
| 552 | no-quote (Friedman); also cited as Ch 25, but the passage is in Ch 26.2 | Added the source's quote, "[T]here is always a temporary trade-off between inflation and unemployment; there is no permanent tradeoff" [V]; "long-run" to the source's "long-term"; citation to Ch 26.2 | src 37126-37128 |
| 554 | (not flagged: counted as a figure claim because of "1930s") `[V]` on a paraphrase (Kuznets) | `[V]` to `[BT]` | src 26321 |
| 555 | no-quote (Lucas) | `[V]` to `[BT]` | src 27895 |
| 556 | no-quote (Duflo, Banerjee, Kremer) | `[V]` to `[BT]` | src 1573 |
| 557 | no-quote (Shiller) | `[V]` to `[BT]` | src 31680 (Ch 22.4) |
| 561 | no-quote (Krugman) | `[V]` to `[BT]` | src 46133 |
| 567 | no-quote (John Bates Clark) | `[V]` to `[BT]` | src 19319 (Ch 14.2) |
| 569 | no-quote (Chamberlin); "co-developed" misstates the source, which says two economists developed the theory "independently but simultaneously" | Reworded to the source's account (Harvard; *The Economics of Monopolistic Competition*; 1933, independently of but simultaneously with Joan Robinson); `[V]` to `[BT]` | src 13982-13984 |
| 570 | (not flagged: figure "1932") `[V]` on a paraphrase (Robbins) | `[V]` to `[BT]` | src 2401-2403 |
| 575 | near: same title-as-quote defect as 478 | Now quotes the section title exactly | src 47477 |

## Derived-tier edits (propagation)

| File | Line | Change |
|---|---|---|
| `distillations/decision-making/openstax-economics-3e-decision-making.md` | 16 | Same glyph fix as deep 27: split into two exact spans around `time-` |
| `distillations/stakeholder-engagement/openstax-economics-3e-stakeholder-engagement.md` | 38 | Same fix as deep 478: paraphrase plus the exact section title under `[V]` |
| `references/openstax-economics-3e.md` (light ref) | 91 | Quoted "an indirect subsidy from consumers to producers." replaced with paraphrase plus the exact Ch 34.1 section title |

Grepped the light ref and all three distillations for the other corrected wordings ("must accept the prevailing", "value of their marginal", "assistance programs", "riskier behaviour", "convey information about conditions", "upper or the under", "efficient mechanism for information", "co-developed"): no other occurrences. The stakeholder-engagement distillation already quotes "riskier behavior" correctly.

Claims a derived artefact may carry that changed in the deep: the price-taker definition (141), the market-as-information passage (101; now cited to 4.3's own wording), the Table 5.2 framing (109; "substitutable items" dropped), the EITC figures (227), the Friedman citation (now Ch 26.2), the Chamberlin entry. The light ref line 25 still says "substitutable goods (restaurant meals, premium cable) are elastic" as unquoted paraphrase; the source's framing is "items that are not necessities". Not a quotation, left for the parent's re-derivation.

## Left as is

- **Deep 147, interrupted:** "the price level in a perfectly competitive market will move toward the zero-profit point" matches the Ch 8.3 summary (src 12374) except for the running header `**210 8 • Self-Check Questions**` between "zero-profit" and "point" (page break). Conversion noise, not a defect.
- **Initial (deep 57, 71, 89, 113; decision-making 22; software-business 140) and apostrophe (deep 91):** need no fix by the checker's rules.
- **Triage cross-check:** all 15 triage rows (101, 141, 203, 227, 245, 539, 540, 542, 552, 555, 556, 557, 561, 567, 569) are fixed as listed above; line numbers matched the current file.

## Open

- Deep 125 cites the loss-aversion quote to Ch 6.3; the same wording appears in 6.3 (src 9036) and 16.1 (src 22732). Correct as cited.
- The deep's frontmatter stamp is unchanged per quotations mode. The derived tier was edited only for the quotations above; it was not re-derived or stamped.

## Derived tier, settled by the parent

- Light reference line 25: "substitutable goods (restaurant meals, premium cable) are elastic" now reads "items that are not necessities (restaurant meals, premium cable) are more price-sensitive", following the source's own sentence in Ch 5.3. The other changed claims (price taker, 4.3 information passage, EITC figures, Friedman, Chamberlin, Follett) appear in no derived artefact: the light reference's Friedman and Chamberlin lines carry no chapter number or "co-developed" wording. Light reference and distillations restamped against the edited deep.
