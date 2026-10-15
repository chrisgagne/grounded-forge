# Pass I quotations audit: nhs-just-culture-guide (2026-10-15)

**Mode:** quotations. Deep reference read in full (184 of 184 lines). Source: `corpus.commons/demo/sources/converted/nhs-just-culture-guide.md`, read in full (122 of 122 lines). Scope open (OGL v3.0, per the sidecar), so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of four deep-ref rows.

## Counts

- Actionable checker lines worked: 6 (2 near, 4 no-quote).
- Quotation-corrected: 2 in the deep ref (slash spacing).
- Quotation marks added (marker kept `[V]`): 4 in the deep ref.
- Marker-corrected: 0.
- Stripped: 0.
- Derived-tier changes: 0.
- Left as is (conversion noise): none.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 27 | no-quote: source words given unquoted under `[V]`; the line had also swapped the source's full stop for a semicolon | The guide "is not a replacement for an investigation of a patient safety incident. Only a full investigation can identify the underlying causes that need to be acted on to reduce the risk of future incidents" [V] | src 11 |
| 29 | no-quote: source words unquoted under `[V]` | The guide "does not replace HR advice and should be used in conjunction with organisational policy" [V] | src 13 |
| 30 | no-quote: source words unquoted under `[V]` | Both sentences now in quotation marks, from "The guide can only be used…" to "…considered separately"; `[V]` and the trailing `[AR]` kept | src 14 |
| 34 | no-quote: source words unquoted under `[V]`; the source opens "This guide", the line "The guide" | The guide "supports a conversation between managers … to work safely" [V] [AR], with the subject outside the quote | src 20 |
| 66 | near: quote closed up the slashes ("protocols/accepted", "action/omission"); the source spaces them | Now "protocols / accepted practice" and "action / omission" | src 69 |
| 67 | near: same slash spacing | Now "protocols / accepted practice" | src 71 |

On 66–67: the checker's display drops trailing punctuation, which made it look as if the source lacked the question marks. The converted text carries "?" on both questions (src 69, 71), and the source has only one copy of each. So the question marks stay. Only the slash spacing was wrong.

## Changes, derived tier

- None needed. I grepped the light ref and all five distillations for each corrected wording ("not a replacement for an investigation", "does not replace HR", "in conjunction with organisational", "one action (or failure", "considered separately", "supports a conversation between managers", "protocols /", "action / omission"). Where a distillation quotes these passages under `[V]` (aar 28; decision-making 36; software-business 36, 153; stakeholder-engagement 18, 107, 162), the quote already matches the source. Every other mention is unquoted paraphrase with no `[V]`: light ref 13, 21, 53–56; decision-making 38, 54, 79–80; software-business 28, 58, 83, 129, 193, 199; stakeholder-engagement 38, 83, 139, 163–164. The 3a/3b rows in decision-making (79–80) already use the source's spaced slashes.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the parent needs to re-stamp derived provenance.

## Left as is (conversion noise)

- None. The remaining checker lines are all non-failing. There are 14 `initial` lines: a quote starting mid-sentence in lower case where the source has a capital ("action singling out…", src 20; "an important part…", src 24; "only a full investigation…", src 11), or the reverse ("The appropriate response…", src 24; "supporting consistent…", src 3). There are 3 `cross-source` lines (retro 109, software-business 189, stakeholder-engagement 153), each quoting tc-25-20-army-aar and naming it.

## Triage cross-check

All four triage rows are fixed, and each keeps `[V]`. In each case the line's wording was already the source's, so I added quotation marks rather than changing the marker to `[AP]`.

- **Deep 27:** quoted. The source's full stop between the two sentences replaces the line's semicolon, and the subject "The guide" sits outside the quote (the source's subject is "**A just culture guide**").
- **Deep 29:** quoted. The subject sits outside the quote for the same reason.
- **Deep 30:** quoted whole, including "The guide", which is the source's own subject on this bullet (src 14). The distillations already quote it the same way.
- **Deep 34:** quoted, with "The guide" outside the quote because the source reads "This guide".

## Checker counts

- Before: 14 initial, 3 cross-source, 2 near, 4 no-quote (6 failing).
- After: 14 initial, 3 cross-source (0 failing).

## Open

- Pass I stamp left as is (quotations mode). No commit made, no build run.
- **Key statistics table (deep 156–159):** four rows mark structural counts `[V]`: 5 tests, 11 sub-questions, 7 end-states, 4 caveats. The counts are correct against src 9–114. But "11 (1+3+3+3+1)" and "7 (A through G)" are counts the ingester derived, not quoted text, so `[AP]` fits better. The checker reports these rows as "figure claims not checked". This is outside a quotations pass; a full Pass I should decide.
- **Conversion-path note (deep 176):** says pymupdf4llm produced "a 156-line markdown rendering". The converted file is 122 lines.
- **Converted text carries ingester-authored structure.** The deep ref (line 8) says the A–G recommendation labels were "introduced in the converted markdown". The converted file also has text a pymupdf extraction would not produce: the description line (src 5), the tree-mechanics paragraph (src 30, "The five tests are applied in order…"), the "If Yes → / If No →" routing bullets, and the recommendation headings. The deep ref cites some of this as the source's own content. For example, line 13's "only one action … is taken through the tree at a time" is closest to src 30's wording, though it also cites bullet 4 (src 14), which says the same thing in the source's words. A full Pass I should check the converted file against the PDF. It should also mark which converted lines are editorial before any of them are quoted under `[V]`.
