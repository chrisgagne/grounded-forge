# Image library for this corpus

Source PDFs and EPUBs typically include diagrams, figures, charts. Image extraction is part of source-grounded ingestion.

## Layout

Images live alongside the converted markdown they belong to:

```
corpus.commons/{corpus}/sources/converted/
├── IMAGE-INDEX.yaml                  # persistent index (one entry per kept image)
├── IMAGES-README.md                  # this file
├── openstax-{slug}.md                # converted source markdown
└── openstax-{slug}-images/           # extracted image files (gitignored)
```

The image *files* are gitignored (regenerable from the source via [`scripts/extract-images.py`](../../../../../scripts/extract-images.py)). The *index* (`IMAGE-INDEX.yaml`) is the persistent record and ships with the corpus.

## SUBSTANTIVE vs DECORATIVE classification

After extraction, images are classified by ingestion-time review:

- **SUBSTANTIVE**: a diagram, chart, model, or figure that carries conceptual content. Indexed in `IMAGE-INDEX.yaml` with a description, tags, suggested-use note, and frameworks the image relates to.
- **DECORATIVE**: cover art, ornamental rules, ad-spaces, blank frames. Deleted from `{prefix}-{slug}-images/` after classification. Not indexed.

If an image is not in `IMAGE-INDEX.yaml`, it is not part of the library.

## Index entry shape

```yaml
- file: {prefix}-{source-slug}-images/{filename}.{ext}
  source_ref: {source-slug}        # matches a reference in ../../references/
  page: {N}                        # PDF page number (null for EPUB items)
  description: |
    Plain-language description of what the image shows. Specific
    enough that a reader who hasn't seen the image can understand
    what it depicts.
  tags:
    - tag-one
    - tag-two
  style: diagram | chart | photo | cartoon | illustration | screenshot
  frameworks:                       # optional; cross-reference to references
    - name: {ref-slug}
      relevance: |
        How this image relates to the cited reference.
  suggested_use: |
    Where this image is most powerful in the operator's task domain.
```

Paths are relative to this directory (`corpus.commons/{corpus}/sources/converted/`).

## How to extract

```bash
python3 scripts/extract-images.py {corpus.commons/{corpus}/sources/original/{slug}.pdf}
```

The script writes images to `corpus.commons/{corpus}/sources/converted/{prefix}-{slug}-images/` and an extraction manifest to `corpus.commons/{corpus}/sources/converted/extraction-manifest.json`. The manifest is a working artefact; classify each image, append SUBSTANTIVE entries to `IMAGE-INDEX.yaml`, delete DECORATIVE files.
