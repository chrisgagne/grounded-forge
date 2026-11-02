# Marine warfighting doctrine and the business textbook, in verbatim mode

An answer from the demo corpus in which every quotation is the author's own sentence, placed from the source by code rather than typed by the model, and every claim credited to a source opens the passage it rests on.

- **Question:** Please draw some interesting parallels between US Marines war-fighting doctrine and modern "textbook" business administration.
- **Corpus:** `demo`, open sources only.
- **Made:** 2 November 2026 by [`scripts/verbatim/generate.py`](../../../scripts/verbatim/generate.py) (one Opus model step, then the resolver and renderer), copied here by [`publish.py`](../../../scripts/verbatim/publish.py).
- **What it holds:** 25 placed spans, 13 quotations and 12 pointed paraphrases. No credit is left without a pointer.
- **Page check:** every quotation is word for word with the converted text. 12 of the 13 also match their printed page. The thirteenth is flagged on its span: there the PDF's own text layer carries an OCR slip.

## How to read it

- **[`preview.html`](preview.html)** is the report itself. Open it on GitHub Pages, or download this folder and open the file. It opens with every claim in the author's words.
- **Click any passage.** The sidenote names the book, section and printed page, says whether the quotation matches the printed page, and shows the passage inside its own paragraph.
- **See the page in the original.** This opens an image of the printed page, with the passage highlighted.
- **Converted text, line N** opens the converted source in this repository at that line.
- **Untick "show pointed paraphrases as the author's passage"** to see the 12 sentences the model wrote in its own words. Each still opens the passage it rests on.
- **[`answer.md`](answer.md)** is the same report as plain prose, every pointer written out, for reading on GitHub.

This copy carries one page image per passage, the highlighted one, and none of the original files. The originals are large, and an NC source's original never ships from this repository. The page's "original" link is therefore greyed out. The sources' own sites are linked below.

The repository's [earlier example](../marines-vs-business-admin-conversation.md) asks the same question through `answer-from-corpus` and shows how the answer is built: query shape, lens check, routing. This one shows what verbatim mode makes of the output.

## Make it again

```bash
python3 scripts/verbatim/generate.py --question 'Please draw some interesting parallels between US Marines war-fighting doctrine and modern "textbook" business administration.' --corpora demo --out <report-folder>
python3 scripts/verbatim/publish.py <report-folder> docs/examples/marines-verbatim --converted-url https://github.com/chrisgagne/grounded-forge/blob/main/corpus.commons/demo --passages
```

The model step varies from run to run. The placement, the page images and the page check don't.

## Sources and licence

- U.S. Marine Corps, *MCDP 1: Warfighting* (1997). A US Government work, in the public domain.
- Columbia Accident Investigation Board, *Report, Volume I* (2003). A US Government work, in the public domain.
- OpenStax (David S. Bright, Anastasia H. Cortes, Donald G. Gardner and others), *Principles of Management* (2019), [openstax.org](https://openstax.org/details/books/principles-management), CC BY-NC-SA 4.0.
- Alexey Krivitsky, Craig Larman and Roland Flemm, *Strategic Org Design: The Primer* (2025), [orgtopologies.com](https://orgtopologies.com), CC BY-NC-SA 4.0.

The quotations and page images from the two CC BY-NC-SA works are adapted excerpts. This folder is therefore released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
