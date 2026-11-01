# Judge brief

You are judging two answers to the same question, labelled A and B. You do not know what produced either, and it does not matter: judge each claim on the page as written.

Question: {question}

- Answer A: `{a_path}`
- Answer B: `{b_path}`
- The sources both answers draw on: `{originals_dir}` (PDFs and EPUBs) and, for a source with no original file, its converted text: {converted_only}.

Read both answers in full first. Then, for each answer, go claim by claim. A claim is a sentence, or a clause with its own citation, that says something a source supports: a quotation, a paraphrase attributed to an author, or a statement carrying a citation marker. Joining prose that cites nothing and attributes nothing is not a claim; skip it.

For each claim, try to verify it against the sources using only what the answer gives you: its citation markers, the passages it shows for them, its pointers (file, page, line, page image), and then, if those fail, your own search of the source files (`grep -n`, `pdftotext`, or a PyMuPDF text dump through `uv run --python 3.12 --with pymupdf python`). Open EPUBs with the same tools.

Score each claim on two things.

1. **Support**: `yes` (the cited source says this; for a quotation, word for word), `partly` (the source says something close but narrower, broader, or worded differently while in quotation marks), or `no` (the source does not say it, or the cited passage is about something else). Name the passage you found: file and page or line, and its first few words.
2. **Verification effort**: which pointer got you there (the shown passage, the page image, the page number, the converted line, a citation marker's popup text, your own search) and how many steps it took, counting each file opened, each search run and each page turned as one step. A claim you could not verify at all scores the steps you spent before giving up.

Write one table per answer:

| # | Claim (first 8 words) | Quote or paraphrase | Support | Passage found | Pointer used | Steps |
|---|---|---|---|---|---|---|

Then, per answer: claims scored, the count of yes, partly and no, the mean steps for the claims you verified, and two or three sentences on what made verification easy or hard. End with one paragraph comparing the two answers on support and on verification effort, and say which you would rather hand to a reader who must check every claim.

Write your result to `{out_path}`. Quote no more than a few words from any source in your result; give file and page or line instead. Keep to the files named here.
