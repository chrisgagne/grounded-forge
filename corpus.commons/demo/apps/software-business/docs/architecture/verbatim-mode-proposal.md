# Verbatim mode (proposal)

A third output shape for `answer-from-corpus`, beside the prose answer and the trace footer: a report whose source-grounded words are placed deterministically from the converted sources, and whose joining prose is visibly the model's. The reader can tell, on sight, which words the author wrote and which the model wrote, click any source span to see it in its surrounding context, and click again to walk the provenance stack: original, converted text, deep reference, light reference, the distillations that carry the claim, and the source's own figure where one exists.

Status: a working generator in [`scripts/verbatim/`](../../scripts/verbatim/), outside the skill and the build. Nothing is wired into `answer-from-corpus` or the app build. Reports that quote copyrighted sources live in gitignored corpus folders under `corpus.local/`.

## Usage

```bash
python3 scripts/verbatim/generate.py \
  --question "How can NZ better prepare itself for the next pandemic?" \
  --corpora aarbuddy,demo --out corpus.local/aarbuddy/projects/verbatim-reports/nz-pandemic
```

1. **Model step.** One headless `claude -p` run (Opus by default, `--model` to change) from the repo root, with `--add-dir` for each corpus. It runs `answer-from-corpus` in project mode and writes `report.json` under the contract in [`scripts/verbatim/contract.md`](../../scripts/verbatim/contract.md): joins in the model's words, and a placeholder wherever the author's words go. `--joins both` (the default) asks for the essay form and the terse form.
2. **Resolve.** [`resolve.py`](../../scripts/verbatim/resolve.py) finds each anchor in `sources/converted/`, expands it to whole sentences, and writes `bundle.json`. No model.
3. **Repair, once.** Spans not found go back to one more `claude -p` run with only their converted files; it supplies new anchors copied from the text, and the resolver runs again. A span still missing renders as its paraphrase, hatched.
4. **Credits, once.** Every join sentence that credits a source ("the textbook stays contingent", "both sources…") must be a placeholder, so it carries a pointer: a quotation, or a *pointed paraphrase*, the model's own sentence with an anchor to the passage it rests on. Any credit the check finds in the joins goes to one more `claude -p` run, which turns it into a pointed paraphrase or cuts it. A credit still without a pointer stops the run.
5. **Render.** [`render.py`](../../scripts/verbatim/render.py) writes `preview.html` and copies in what the page opens (D3, the originals, the converted text, figures, and the hit page with two either side pre-rendered as PNGs, the passage highlighted on the hit page). It also writes `answer.md`, the same report as plain prose with every pointer ([`flatten.py`](../../scripts/verbatim/flatten.py)), from the same bundle as the page. Each quotation is checked word for word against its page in the original. A word the conversion split ("bet ter") that the page prints whole is set as printed; any other difference is shown beside the quotation. The folder works zipped and from `file://`. Page images need an arm64 PyMuPDF; `generate.py` runs the renderer through `uv run --python 3.12 --with pymupdf`.

The render-time flags (`--verbatim`, `--context`, `--ship`) and the page's own controls need no model call: they change what is shown, never what was placed. `--render-only` resolves and renders an existing `report.json` with no model call. Corpora are named bare and found under `corpus.commons/{name}` (ceiling open-nc) or `corpus.local/{name}` (ceiling copyrighted). `summary.json` in the report folder records spans placed and missing, the cost of the model steps, and the share of the page's words that are the authors' own.

## Why

Today an answer carries `[V]` markers in-band and a trace footer, and `check_quotes.py` catches a quote that is not the author's words. All of that is after the fact and lives in the markdown. The reader of the finished answer still sees one colour of prose. The join between what the corpus says and what the model inferred is the one thing the architecture exists to keep honest, and it is invisible at the point of reading.

The fix is to move the quote out of the model's hands. The model names the span; a deterministic step places it.

## The flags

```
--verbatim R          R in 0..1. The share of load-bearing claims carried as the
                      author's own words. 1: every placed span is verbatim where the
                      licence allows. 0: every span is paraphrased with attribution,
                      and the reader still gets the provenance click-through.
                      Default 1 for the operator's own use; the build profile's
                      max_visibility ceiling clamps copyrighted sources to paraphrase
                      in anything that ships.
--context UNIT[:N]    How much surrounding source text a click reveals.
                      chars:600, words:120, paras:1 (default), pages:1.
                      The unit is a window on the converted file; pages resolve
                      through the page markers the converter kept.
```

## Placeholder grammar

The model writes the report as joins and placeholders. It never types a quotation. For each claim it wants in the author's words it emits a placeholder that names the source and an anchor: eight to twelve words it expects to find in the converted text.

```json
{
  "joins": [
    "The quiet years are where readiness is lost. ",
    {"span": "caib-invisible-deviance", "source": "00u", "anchor": "invite the normalization of deviance, they may be the most risky of all",
     "paraphrase": "The Columbia board warns that the less visible problems, because they invite the normalisation of deviance, may be the riskiest."},
    " A stockpile left to expire is that kind of problem."
  ]
}
```

The `paraphrase` is the model's fallback. It renders when `--verbatim` leaves the span out, when the licence gate forces it, or when resolution fails. It is always labelled as the model's words.

## Deterministic resolution

A resolver walks the placeholders:

1. Look up the source by short ID in `references/slug-table.json`; open `sources/converted/{slug}.md`.
2. Find the anchor in two levels: exact (case, whitespace, curly quotes, dash styles, ligatures and Pandoc span noise folded), then loose (punctuation dropped too, and a word split by a line-end hyphen rejoined). The loose level needs six words or more, so a short anchor can't land on a chance match.
3. Expand the hit to sentence boundaries. The expanded text is the span. The model's anchor is discarded.
4. Record the line number, the nearest heading above it as the locator, the printed page if the converter kept one, and the context window for every unit, so the renderer can switch units without reopening the source.
5. Attach the provenance layers: the deep-reference line that carries the claim and its evidence marker, the light-reference line, every distillation line that carries it, the original file if redistributed, and the figure entry from the image index if the passage names a figure.
6. Write `bundle.json`: resolved spans, sources, and a result per span: `exact`, `loose`, or `not-found`. A missing span never renders as a quote. It renders as the model's paraphrase with a visible mark, and the trace footer counts it.

Resolution runs in the corpus (project mode) against `sources/converted/`. In an app, which ships no sources, the resolver's output is what ships: the app carries `report.json` already resolved, or resolves against the `[V]` lines of its distillations and says so.

## The rendered report

The preview renders `report.json` as a page in the G design system, with Tufte's sidenotes doing the work a footnote list would otherwise do.

- Model prose is ink. A placed span carries a hairline underline in its corpus's colour and a superscript source mark. A paraphrase-forced span has a dashed underline. A missing span is hatched, which in G means waiting.
- Click a span: its sidenote shows the span inside its context window at the current `--context` unit, with the locator and page. The unit can be changed on the page.
- Click "more": the sidenote expands to the provenance stack, one row per layer, each row the actual line from that file, with the evidence marker the deep reference gives it.
- Charts are bound to numbers the source states, not to numbers the model remembers. Each chart names the passage it is drawn from and, where the source has its own figure, shows that figure beside the redraw with its caption and page.
- Three figures stand above the prose: where in each source the report's spans sit (a strip per source, chapter ticks, one mark per span), the share of the page's words that are the authors' own, and the coverage of the question's sub-claims by source.
- The trace footer is the one the skill writes today, plus `spans: N placed, M paraphrased by licence, K missing`.

## What this does not change

The retrieval protocols, the matrix, the distillation tier, the trace footer. Verbatim mode is a renderer and a resolver over an answer the existing skill produced. The one change to the skill is that, in this mode, the model writes placeholders where it would have written quotes.

## Open questions

- Whether the anchor should be the model's or the resolver's: the model could instead name a claim and let a retriever choose the sentence, at the cost of the model no longer choosing the words it builds the join around.
- Whether `--context pages` is worth the converter work for sources whose page markers were not kept.
- How the OKF bundle should carry a resolved report, if at all.
- What `--verbatim` should order by when it drops spans: the model's own ranking, the deep reference's marker (keep `[V]` spans first), or position in the argument.
