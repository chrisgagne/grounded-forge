# Scoring brief: case-citations round

You are grading citations in answers to three case questions. Read in full first:

- `cases.json` in this folder's parent (the three prompts)
- `keys.json` (expected ideas for C1 and C2, with sources that carry each)

Each packet is one answer. Its name says the arm, the corpus, the case and the run: `gemini-demo-C1-1`, `gf-aarbuddy-C2-2`, and so on. Converted source text is under the path the packet header gives.

## Unit: one citation

- **Gemini packets.** Every `[n:slug]` marker is one citation. The packet's legend gives, per marker, the source and the full text of the chunk the marker opens. The claim is the sentence the marker sits on (markers at the end of a list item cover that item; a marker right after a heading covers the first sentence under it).
- **grounded-forge packets.** Every sentence that credits a source by author, title or organisation, or that quotes one, is one citation. The credited source is the claim's source. A credit in a lead-in sentence carries to the list items under it. Use the packet's quotation-locations list where there is one, and otherwise search the credited source's converted text for the claim (Grep key terms in several phrasings, then read the region).

## Grades per citation

1. **support:** `supports` (the cited chunk, or the credited source's text, carries the claim as stated), `partial` (on the topic, but not the claim as stated: a narrower, broader or differently qualified statement), `none` (the claim isn't there; for grounded-forge, not found after searching). Grade down on doubt and say why.
2. **wrong_book:** `yes` if the sentence names an author, work or organisation and the cited chunk is from a different one; `no` otherwise (including when the sentence names nobody).
3. **quote_exact:** for a citation with a quotation of five words or more, `yes` or `no` from the packet's quotation-locations list (`found` or `IN-SECTION` = yes; `MISSING` = check by eye for page furniture or a line-break hyphen first, then `no`); blank when there is no quotation.

## Per answer

4. **ideas** (C1, C2 only): for each key idea, `present` and `credited_ok` (the answer credits a source that carries it; the key's `demo_sources` list is a guide, not a limit, and a private-corpus source may qualify).
5. **sources_cited:** distinct sources credited or cited.
6. **note:** one or two lines: the kinds of failure you saw, anything odd.

## Output

One JSON file per packet, named as the packet with `.score.json`, in the output folder you're given:

```json
{"id": "gemini-demo-C1-1", "citations": [{"n": "1", "claim": "...", "cited": "slug", "support": "supports|partial|none", "wrong_book": "yes|no", "quote_exact": "yes|no|"}], "ideas": [{"idea": "...", "present": "yes|no", "credited_ok": "yes|no"}], "sources_cited": 0, "note": "..."}
```

For grounded-forge, `n` is a running number and `cited` the credited slug. Copy each `claim` verbatim, trimmed to 200 characters. Read every packet in full; grade every citation, not a sample. Private-corpus packets stay in the scratch folder and are never copied anywhere else.
