# Judge brief

You are judging one answer to a question, claim by claim. You do not know what produced it, and it does not matter: judge each claim on the page as written.

Question: {question}

- The answer: `{answer_path}`
- Its claims, already split and typed: `{claims_path}`. Score every claim in that list except those typed `framing`, using its numbers. Do not re-split them.
- The sources the answer draws on: `{originals_dir}` (PDFs and EPUBs) and, for a source with no original file, its converted text: {converted_only}. Pointers inside the answer that name other files (converted text, page images, other copies of the originals) count as named here.

## Counting operations

One operation is each file opened, each search run, each page image viewed, and each page turned or extracted. Reading text that is already in the answer costs nothing: a passage it shows, a paragraph it quotes, or a popup it captured. Reading a file you already opened for an earlier claim costs one operation again, because a reader checking one claim would have to open it.

## For each claim

1. **Delivered support.** Use only what the answer gives for this claim: its citation markers, the passages it shows, and its pointers (file, page, line, page image). Follow them, spending at most 3 operations. Score what you find:
   - `yes`: the passage says this. For a quotation, word for word.
   - `reworded`: a quotation that differs from the source text.
   - `narrower`: the source says less than the claim, or something more specific.
   - `overstated`: the source says something weaker, more hedged or more general, and the claim firms it up or adds specifics.
   - `absent`: the passage pointed to does not bear on the claim.
   - `contradicted`: the source says the opposite.
   - `unassessable`: you have no copy of the source, and the answer shows no passage to judge from.
2. **Recovered support.** Only if delivered support is not `yes`: search the source files yourself, spending at most 6 operations on this claim in total, steps 1 and 2 together. Score what you find on the same scale, or `not found` if the budget runs out. Recovered support never changes the delivered score.
3. **For an `application`:** does the source it applies say what the answer takes from it (`yes` / `overstated` / `absent`)? Is the step from source to question a reasonable one? Answer in one line.
4. **For an `uncited fact`:** is it common knowledge, or a specific factual claim a reader would need a source for? Answer in one line. Do not search for it.
5. **For an `uncited recommendation`:** no score; it is counted.

Write one table:

| # | Type | Delivered | Ops (delivered) | Recovered | Ops (total) | Passage found (file, page or line, first few words) | Note |
|---|---|---|---|---|---|---|---|

Then report:

- the counts of each delivered score and each recovered score, each with its denominator;
- quotation fidelity: exact quotations out of all quotations;
- operations per claim, separately for claims scored `yes` on delivery, claims recovered, and claims `not found`;
- two or three sentences on what made checking easy or hard;
- last, and only after scoring, one line: your guess at what kind of tool produced this answer, and why. It may be "no idea".

Write your result to `{out_path}`. Quote no more than a few words from any source in your result; give file and page or line instead. Keep to the files named here.
