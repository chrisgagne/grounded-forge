# Verbatim-mode report contract

The model step of `generate.py` writes one file, `report.json`, in the report folder. This is its exact shape. `resolve.py` places every span from it; `render.py` draws the page. The model never types a quotation: wherever it wants an author's words it writes a placeholder, and the resolver puts the source's own sentence there or marks the span as not placed.

## The rules that matter

**The joins carry no quotation.** A join is the model's own prose between spans. It never puts a source's words in quotation marks. Every word of an author's that reaches the page reaches it through a placeholder.

**The joins carry no credit either.** Any sentence that says what a source says, holds, found or recommends ("MCDP 1 ranks purpose above task", "The textbook stays contingent", "Both sources link uncertainty to decentralisation") is a placeholder, so it carries a pointer to the passage it rests on. Where you want the author's words, that is a quotation placeholder. Where your own sentence says it better, it is a *pointed paraphrase*: a placeholder with `"show": "paraphrase"`, whose `paraphrase` is your sentence and whose anchor places the passage it rests on. A sentence comparing two sources is two pointed paraphrases, one per source, joined by your own words. A join may name an author only in the lead-in that runs straight into the placeholder after it ("Dörner observes:"). Your own reasoning about the question ("For a 300-person company, this means…") names no source and needs no pointer. `generate.py` checks every join sentence for a credit and repairs or stops on any it finds.

## Top level

```json
{
  "question": "the question exactly as asked",
  "mode": {"verbatim": 1.0, "context": "paras:1", "protocol": "Synthesis", "lens": "none", "corpora": ["aarbuddy"], "joins": "essay"},
  "coverage_note": "…",
  "subclaims": [ … ],
  "rank": [ … ],
  "sections": [ … ],
  "charts": [ … ],
  "trace": "Trace [Synthesis, lens: none, mode: project, corpus: aarbuddy, …]: …",
  "sources": { … }
}
```

| Field | Type | What it holds |
|---|---|---|
| `question` | string | The question, word for word as given. |
| `mode.protocol` | `Named` \| `Diagnostic` \| `Synthesis` | The answer-from-corpus protocol the model ran. |
| `mode.lens` | string | `none`, or the lens slug(s) applied. |
| `mode.corpora` | list of bare corpus names | The corpora the run was allowed to read. |
| `mode.verbatim`, `mode.context`, `mode.joins` | | Leave at `1.0`, `"paras:1"`, `"essay"`. The renderer's flags override them. |
| `coverage_note` | string | One short paragraph, the model's words: what the corpora lack for this question, said plainly, and two or three named ingestion candidates (authors or works) that would let the corpus answer it directly. Ingestion candidates are named, never cited. |
| `subclaims` | list | The answer's moves: `{"id": "c1", "label": "Act on early evidence", "spans": ["span-id", …]}`. Every span appears in at least one subclaim. Labels are short (under 45 characters). |
| `rank` | list of span IDs | Every quotation placeholder exactly once, most load-bearing first; pointed paraphrases are left out. `--verbatim R` keeps the first `ceil(R × n)` as the author's words and shows the rest as their paraphrase. |
| `sections` | list | The answer, below. |
| `charts` | list, optional | Charts drawn from numbers a span states, below. Omit or leave empty when no span states numbers worth drawing. |
| `trace` | string | The answer-from-corpus trace footer, one line, mode `project`. |
| `sources` | object | Every source a span cites, below. |

## Sections

```json
{
  "heading": "Keep the memory alive between events",
  "joins": [
    "Model prose. ",
    {"span": "caib-invisible-deviance", "source": "00u",
     "anchor": "invite the normalization of deviance, they may be the most risky of all",
     "sentences": 1,
     "paraphrase": "The Columbia board warns that the less visible problems, because they invite the normalisation of deviance, may be the riskiest."},
    " More model prose."
  ],
  "joins_min": [
    {"span": "caib-invisible-deviance"},
    " A lapse nobody notices until it matters."
  ]
}
```

`joins` is the essay form: strings of model prose and placeholder objects, in reading order. Strings carry their own leading and trailing spaces. Each section opens with a string and holds as many placeholders as its argument needs: quotations where the author's words carry the point, and a pointed paraphrase for every other sentence that credits a source. The number of sections and placeholders follows from the question, not from a target.

`joins_min` is the terse form of the same section: the same placeholders, by `span` ID only, in the same order, with the shortest strings that still make the argument. No lead-ins ("As Edmondson puts it:", "Dörner observes"): the span's source mark names the source. A string may be empty or absent between two spans.

### A placeholder

| Field | Rule |
|---|---|
| `span` | A unique ID across the report, kebab-case, `{author}-{gist}`: `caib-invisible-deviance`. |
| `source` | The source's short ID in its corpus's `references/slug-table.json` (`"00u"`), not the slug. |
| `anchor` | **8 to 12 consecutive words copied character for character from the converted text** (`{corpus}/sources/converted/…`), never from a reference, a distillation, or memory. Copy them from a line you read with Read or Grep in this run. Pick words that occur once in the source. Leave out Markdown and Pandoc noise (`*`, `[`, `]{.class}`); the resolver ignores case, curly versus straight quotes, and dash styles. |
| `sentences` | 1 to 4. How many sentences, counted from the one that holds the anchor's last word, the span should run to. The resolver expands the hit backward to the start of the anchor's sentence and forward through this many sentence ends. |
| `paraphrase` | The model's own sentence saying what the span says, attributed ("The Columbia board warns…"). It renders whenever the span is not shown as the author's words: always for a pointed paraphrase, below the `--verbatim` share, under the shipping gate for a copyrighted source, or when the anchor is not found. It must not quote the source. |
| `show` | Optional. `"quote"` (the default) shows the author's words; `"paraphrase"` makes the placeholder a pointed paraphrase: the page always shows `paraphrase`, tagged as a paraphrase of a passage, and a click opens the passage the anchor places. A pointed paraphrase is not in `rank`. |
| `figure` | Optional. When the passage names a figure in the source (`Fig. 23`, `Figure 4.2`): `{"name": "Fig. 23", "image": "sources/converted/…/img-0038.jpg", "via": "how the image was matched"}` with `image` from `sources/converted/IMAGE-INDEX.yaml`; or `{"name": "Fig. 23"}` to let the resolver look it up. |

## Charts

```json
{"span": "dorner-doubling", "kind": "growth",
 "title": "What a longer doubling time does to a count",
 "caption": "Two doubling times the passage states, 8 months (1984) and 13.5 months (1988), each applied to 100 cases for four years.",
 "x_label": "months", "x_max": 48, "base": 100,
 "series": [{"label": "1984", "value": 8}, {"label": "1988", "value": 13.5}],
 "figure_spans": ["dorner-deceleration"]}
```

A chart is drawn right after its `span` and only from numbers that span states. The resolver checks every series `value`, and every number in a series `label`, against the placed text of the span; a chart with any number the passage does not state is withdrawn, and the page says so. `kind` is `growth` (each `value` a doubling time; the curve is computed from it) or `bars` (each `value` drawn as a bar, optional `unit`). `figure_spans` names spans whose `figure` the chart should show beside it.

## Sources

```json
"00u": {"slug": "caib-report-vol1", "corpus": "demo",
        "converted": "sources/converted/caib-report-vol1.md",
        "short": "CAIB"}
```

| Field | Rule |
|---|---|
| key | The short ID, as in `slug-table.json`. |
| `slug` | The slug that ID maps to. The resolver checks the pair against the slug table. |
| `corpus` | The bare corpus name. |
| `converted` | The converted file's path from the corpus root, the file the anchors were copied from. |
| `short` | A two- or three-word name for the source mark: author surname, or a short institution name. |
| `original`, `title`, `author`, `year`, `scope` | Optional. The resolver fills them from the source's sidecar and `sources/original/`. |

## What the resolver does with it

For each placeholder: open the converted file, find the anchor (exact, then a loose level that drops punctuation and rejoins words split by a line-end hyphen), expand to whole sentences inside the paragraph, and record the placed text, line, locator, printed page if the converter kept one, the paragraph around it, and the deep-reference, light-reference and distillation lines that carry the claim. Converter markup (Pandoc fences and blockquote markers, table bars and rules) and a heading the conversion ran into the paragraph are left out of the placed text. An anchor it cannot find is `not-found`: the page shows the paraphrase, hatched, and the trace footer counts it. A not-found span is never shown as a quotation.

The renderer then checks each placed quotation word for word against the page it finds it on in the original. A word the conversion split that the page has whole is set as the page has it; any other difference is recorded on the span and shown beside it. The check reads the original's text layer, so an OCR slip that the PDF's own text shares goes uncaught.
