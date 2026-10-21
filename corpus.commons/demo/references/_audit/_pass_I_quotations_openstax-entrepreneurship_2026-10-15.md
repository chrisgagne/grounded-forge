# Pass I quotations audit: openstax-entrepreneurship (2026-10-15)

**Mode:** quotations. Deep reference read in full (504 of 504 lines). Source: `corpus.commons/demo/sources/converted/openstax-entrepreneurship.md` (36,579 lines; passages read around each hit). Scope open-nc (the source states CC BY-NC-SA 4.0, src 17–18), so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref and the three distillations (decision-making, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 11 (3 near, 4 interrupted, 4 missing).
- Quotation-corrected: 6 quotations on 5 deep-ref lines (45, 65 ×2, 75, 131, 169).
- Scare quotes removed from a label the source does not use: 1 (277).
- Marker-corrected: 0.
- Stripped: 0.
- Left as is (conversion noise, or a quote that matches the cited body text): 5 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 45 | interrupted: the quote mixed two passages. Its verb "displace" and opening came from the Ch 1.3 body text; its ending "or accepted methods" came from the Ch 1 Key Terms gloss, which reads "displaces … accepted methods" | Now quotes the Ch 1.3 body text the line cites: technologies that, "once introduced, displace established patterns, processes, and systems previously accepted as normal or accepted" [V] | body src 1966–1968 (Ch 1.3, "An Entrepreneurial Mindset in Your Discipline or Field", heading src 1924); gloss src 2020–2022 |
| 65a | near: the quote began "the process…", but the source's own quote mark opens after "the" (`the “process of industrial mutation…`) | "the" moved outside: the latter defined as the "process of industrial mutation … creating a new one" [V] | src 3427–3429 |
| 65b | near: source ends `‘belongingness.’”` | Quote now ends `'belongingness.'"` | src 3437–3439 |
| 75 | near: the Moore quotation gave the source's ellipsis as `. …` (period, then ellipsis) | Now `entrepreneur…. But`, the source's own order (ellipsis, then period). The ellipsis is in the printed Moore quotation, not an elision by the deep ref | src 4041–4042 |
| 131 | missing: MVP definition opened with "an", which the source does not have; citation read "(Ch 4.3, glossary; Ch 10)" | Now: is glossed as an "early version or prototype of a product … with potential users" [V] (Ch 4 and Ch 10, Key Terms). Quoted from the Key Terms gloss, which is identical in both chapters. The Ch 4.3 body text ("Elaboration", src 8587–8589) words the idea differently and is not quoted | Ch 4 KT src 9001–9003; Ch 10 KT src 22269–22271 |
| 169 | missing: the ideation quote opened with "the" and carried no citation. Its wording matches the Key Terms gloss ("one's mind … many directions"), not the Ch 4.1 body text ("your mind … all directions") | "the" moved outside; cited as the gloss: is glossed as the "purposeful process of opening up one's mind … from a stated purpose or problem" [V] (Ch 4 and Ch 7, Key Terms). Ch 6 has no ideation gloss; Ch 6.2 defines the "ideate" step in other words (src 11529–11530) | Ch 4 KT src 8986–8988; Ch 7 KT src 14437–14439; Ch 4.1 body src 8040–8041 |
| 277 | missing: "fail forward" was set in quote marks as the source's term; the phrase is not in the source | Rewritten without the label: the quotation "anchors the section's argument that early failure can lead to success later", which is the section's own title. The Jack Ma quotation itself is exact | section header src 20702; quote src 20708–20709 |

## Changes, derived tier

- None needed. Propagation grep of the light ref and all three distillations for each corrected wording ("displace", "industrial mutation", "belongingness", "natural-born", "accidental entrepreneur", "early version or prototype", "polished", "opening up", "trains of thought", "fail forward", "unconventional practices", "younger firms", "Jack Ma", "form of success", "self-reliance", "creative destruction"): no copied quotation found. The light ref's line 17 says disruptive technology "displaces established patterns, processes, and systems" as unquoted paraphrase, which the source supports (gloss src 2020–2022). The Schumpeter mentions in the light ref (21, 110), decision-making (202) and software-business (242) are paraphrase or the two-word term "creative destruction", which is exact.
- No change alters a claim the light ref or a distillation carries. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is

- **Deep 75** (near, after the fix): the converted text runs `entrepreneur….But` with no space after the period (src 4042); the deep ref keeps the space at the sentence break. A dropped space at a sentence break, not the author's words.
- **Deep 109** (interrupted): the creativity definition runs across the running header `**Access for free at openstax.org** **4.2 • Creativity, Innovation, and Invention: How They Differ 137**` (src 7961–7967). The quote matches this Ch 4.2 body passage exactly. The Ch 4 summary (src 9035) adds "artistic", so is not the passage quoted.
- **Deep 209** (missing): the entrepreneurial-marketing definition matches the Ch 8.1 body text, the section the line cites, word for word: "a set of unconventional practices that can help start-ups and" (src 15050) / "younger firms emerge and have an edge in competitive markets" (src 15068). Between the two halves sit footnotes 1–3 and the running header `**8.1 • Entrepreneurial Marketing and the Marketing Mix 267**` (src 15053–15064), too long a gap for the checker, which then matched the Key Terms gloss and the summary (src 17722–17724, 17847–17848), both of which read "survive in competitive markets".
- **Deep 237** (interrupted): the angel-investor definition runs across the running header `**318 9 • Entrepreneurial Finance and Accounting**` (src 18279–18284).
- **Deep 327** (interrupted): the networking definition runs across `**Access for free at openstax.org** **12.1 • Building and Connecting to Networks 443**` (src 25356–25362).
- `software-business:58` (initial, capital T on a sentence-opening quote) and the other apostrophe and initial lines need no fix.

## Triage cross-check

- **Deep 45** (displaces→displace): fixed, but the triage's reading is half right. The deep's "displace" is the Ch 1.3 body text's own word (src 1967); the defect was the ending "or accepted methods", taken from the Key Terms gloss. The quote now follows the body text the line cites, ending "or accepted".
- **Deep 131** (article added): fixed. "an" moved outside the quote; cited to the Key Terms gloss (Ch 4 and Ch 10).
- **Deep 169** (your/all→one's/many): fixed, but the deep's words were not a rewording. They are the Key Terms gloss (Ch 4, Ch 7), which reads "one's … many"; the checker had matched the Ch 4.1 body text, which reads "your … all". The defect was the leading "the" and the missing citation. Both are fixed, and the line now names the gloss.
- **Deep 209** (survive→emerge and have an edge): not a defect, left as is. "emerge and have an edge" is the Ch 8.1 body text the line cites (src 15050, 15068); "survive" is the Key Terms and summary wording. See "Left as is".
- **Deep 277** (fail forward): fixed. The label is gone; the line now uses the section's own title.

## Checker counts

- Before: 6 apostrophe, 10 initial, 3 near, 4 interrupted, 4 missing (11 failing).
- After: 8 apostrophe, 10 initial, 1 near, 3 interrupted, 1 missing (5 failing, all listed under "Left as is"). The apostrophe count rose because the corrected quotes on lines 65 and 169 now match at that non-failing level.

## Open

- Stamp left as is (quotations mode). No commit made.
- Outside the scope of a quotations pass: the Key statistics table (deep 421–459) marks figure rows `[V]` (34 figure claims the checker does not check), and the integrity note at deep 503 says every `[V]` passage was verified character by character in Pass D, which this run shows was not so. A full Pass I should look at both.
