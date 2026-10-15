# Pass I (quotations mode): mcdp1-warfighting, 2026-10-15

**Deep reference:** `corpus.commons/demo/references/mcdp1-warfighting-deep.md` (251 lines)
**Distillations:** aar, decision-making, retro, software-business, stakeholder-engagement
**Source:** `corpus.commons/demo/sources/converted/mcdp1-warfighting.md`, rebuilt from the PDF (3,555 lines; SHA256 `dabeb5c0f06ce72238c3b427deb29bd3ea7587b73e863afa38ca57c08fe7163a`)
**Trigger:** `scripts/check-verbatim.py` on the files synced in PR #9 reported 2 initial, 5 near, 1 ligature, 17 interrupted, 1 wrong-source and 7 missing in the deep reference, and further lines in the distillations. The 2026-10-02 quotations pass had kept the book's wording in 13 quotations where the conversion was garbled, so those quotations differed from the conversion. This pass makes the conversion carry the page's words instead. The `Pass I applied` stamp is left as it is.

## The conversion

Two causes sat behind the garbled readings, and each is fixed in the conversion, not in the quotations.

- **Lost compound hyphens.** pdftotext's default `-remove-hyphens all` deletes every line-end hyphen, so a compound split across a line lost its hyphen (*selfreliant*, *nowin*, *missiontype*, *everincreasing*). The PDF's text layer keeps the hyphen. Re-converted with `pdftotext -remove-hyphens soft`, which keeps it; `check-verbatim.py` rejoins a split word and keeps a true compound.
- **Publisher OCR slips.** Five slips fall in quoted passages. Each was read again by tesseract from a 300-dpi render and checked against the page image, then corrected in the conversion. The source card lists them: `firepower. it` (p45), `f eliminated` (p55), `of"yes-men"-—-will` (p67), `ajid` (p70), `certainly` (p87).
- **The cover.** Page 1 is an image with no text layer, so Distribution Statement A was in no converted text (the checker found the same boilerplate in DOE Vol. 1 and reported `wrong-source`). The cover's text is now tesseract OCR before the first page break, with one tesseract slip in the emblem corrected (`EMPER FIDELIS,` → `SEMPER FIDELIS`). The other text-empty pages (5, 11, 31, 59, 61, 79) are blank; tesseract finds nothing on them.

## Quotations changed

| File | Line | Change | Reason |
|---|---|---|---|
| deep | 237 | `"DISTRIBUTION STATEMENT A: Approved for public release; distribution is unlimited."` → `"DISTRIBUTION STATEMENT A:Approved for public release; distribution is unlimited"` | The cover sets no space after the colon and no closing period (page image). |

No other quotation needed a change: each now matches the conversion.

## Prose changed

- Deep reference, source-integrity notes: the coverage note says the cover's text is in the conversion; the source-acquisition note describes the new conversion and its SHA256 and says quotations match it, omitting glued footnote numbers and running headers; the evidence-markers note drops "OCR garbles restored".
- aar, retro, software-business, stakeholder-engagement: the "Evidence-marker continuity" notes drop the sentences about OCR repairs. aar's source line numbers follow the new conversion (critique 1983-1998, zero defects 1859-1866, intent 2900-2903, burden of understanding 2954-2966).
- The light reference and the five distillations are restamped to the deep's new hash; none carries the notes that changed.

## Checker findings left, none of them a defect

Deep reference, after the fix: 2 initial, 5 near.

| Kind | Lines | What it is |
|---|---|---|
| initial | 88, 96 | A quotation that starts mid-sentence in the source; not failing. |
| near | 42, 96, 114, 116, 156 | The quotation omits a footnote reference number glued to a word: `accomplished.8`, `quickly.'8` (footnote 18), `conduct.4`, `learning.6`, `it.°` (footnote 10 on the page). |

Running headers and page numbers between two pages of a quoted passage, and a quotation holding both a word split across a line (`situa-` / `tion`) and a compound split across a line (`ever-` / `increasing`), are conversion noise the checker sets aside (PR #15).

Distillations, after the fix: aar 1 initial (13); decision-making none; retro 15 cross-source (below); software-business none; stakeholder-engagement 1 initial (138).

## Cross-source quotations in the retro distillation

The retro distillation's integration table (lines 163-170) quotes seven other sources, each named on its line. `cross-source` means the checker found the quotation in another converted source that the line names; it does not fail. Each was checked against its named source's conversion directly: all are word for word. *"It's better to have one or two improvement items . . ."* starts mid-sentence in the Field Guide (`it's`, an `initial` difference), and Letaw's fist-of-five sentence differs only in apostrophe style. The checker lists some quotations more than once because one table row is one segment for each `[V]` marker in it.

## Private corpus

`corpus.local/aarbuddy` holds the same converted source, deep reference and source card; the same changes are applied there and committed in its local repository.
