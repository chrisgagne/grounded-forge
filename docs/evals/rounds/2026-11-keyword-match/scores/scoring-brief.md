# Scoring brief: keyword-match round

You are scoring answers for a pre-registered eval. Read these first, in full:

- `docs/evals/rounds/2026-11-keyword-match/DESIGN.md` (the "Scoring" section is binding)
- `docs/evals/rounds/2026-11-keyword-match/targets.json` (each target's slug, section line range, `key_elements`, `alt_sources`)

Each packet is one answer to one question. The question ID's first three characters (K01…K10) name the target.

## What to decide per answer

1. **Key sentence.** The first sentence in the answer that states the answer key, meaning *all* of the target's `key_elements` are present in that sentence or in the sentence plus the one immediately after it (a definition is often split over two sentences; if you use two, say so). Copy it verbatim (trim to 300 characters). If no sentence states all key elements, the key sentence is `null`.
2. **Score 4, answer-key hit (yes/no):** every key element appears somewhere in the answer, whatever is cited.
3. **Score 2, key claim on target source (yes/no):** the key sentence credits the target source.
   - Gemini packets: the sentence's `[n:VERDICT:source]` markers. Yes if any marker on that sentence (or the two-sentence span) has the target's slug as source (verdict IN or OUT).
   - grounded-forge packets: the sentence credits the target source by its author, title or organisation (e.g. "the Columbia Accident Investigation Board", "the Scrum Guide", "OpenStax *Psychology*", "the DOE handbook", "MCDP 1"). A credit given in the immediately preceding lead-in sentence of the same paragraph that the key sentence plainly continues counts.
4. **Score 1, key citation on target (yes/no/source-only):**
   - Gemini: yes if any marker on the key sentence has verdict IN. No otherwise.
   - grounded-forge: yes if the key claim's credit comes with a quotation that the packet's "Quotation locations" list marks IN-SECTION, or with a locator (chapter, section, page, heading) that falls inside the target section as `targets.json` names it. If the claim is credited to the target source with no quotation or locator, score `source-only`. If the quotation/locator given for it is elsewhere in the source, score `no`. Look at quotations in the key sentence and the sentences immediately supporting it in the same paragraph.
5. **Score 3, wrong-book citations on the key claim:** the number of distinct sources credited on the key sentence that are neither the target nor in its `alt_sources`. For Gemini count distinct `OTHER` sources among its markers; for grounded-forge count distinct other works credited in it.

6. **Score 5 inputs, quotation exactness.** The packet's "Quotation locations" list was extracted mechanically and over-collects. For every line marked `MISSING`, decide whether it is an **author quotation** (the answer presents it as a source's own words) or **not** (the answer's own suggested wording or script, a heading or row name, a trace-footer path, the user's words, or a fragment produced by mis-pairing quote marks). For each author quotation marked MISSING, check by eye whether the converted source carries it with only a page header, footnote number or line-break hyphen in between (open `corpus.commons/demo/sources/converted/{slug}.md` around the nearest match; Grep a shorter fragment). Count: `quotes_exact` = lines marked found or IN-SECTION, plus MISSING author quotations that are exact apart from such page furniture; `quotes_inexact` = MISSING author quotations whose words differ from the source (list each in `note`, with what the source says). Ignore lines that are not author quotations.

7. **Lenient reading (post-hoc, reported beside the strict scores).** The strict two-sentence rule penalises long, structured answers that spread a definition over a passage. So also score:
   - `s2_lenient`: the **key passage** is where the answer first explains the target concept (the paragraph, list or section that together states the key elements; a heading, lead-in sentence or the sentence right after counts as part of it). Yes if that passage credits the target source.
   - `s1_lenient`: yes if that passage's credit carries a citation that lands inside the target section (Gemini: any `IN` marker in the passage; grounded-forge: an IN-SECTION quotation in the passage, or a locator in it that falls inside the section). `source-only` if credited with no quotation or locator; `no` otherwise.
   Use the same conventions for both arms: "the guide/handbook/textbook/chapter" counts as a credit when it plainly means the source named earlier; a lead-in that names the source carries to its list items.

If the key sentence is null, scores 1, 2 are `no` and 3 is 0, and still score 4 from the whole answer.

Be strict and literal. When unsure, grade down and say why in `note`.

## Output

Write one JSON array to the output path you're given, one object per packet:

```json
{"id": "K01B-1", "key_sentence": "...", "s1": "yes|no|source-only", "s2": "yes|no", "s3": 0, "s4": "yes|no", "quotes_exact": 0, "quotes_inexact": 0, "s2_lenient": "yes|no", "s1_lenient": "yes|no|source-only", "note": "one or two lines"}
```

Then reply with a five-line summary: counts of s1=yes by A and by B, and anything odd.
