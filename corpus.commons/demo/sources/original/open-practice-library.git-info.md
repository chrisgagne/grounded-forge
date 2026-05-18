# Open Practice Library — Git clone provenance

**Source repository:** https://github.com/openpracticelibrary/openpracticelibrary
**Cloned commit:** `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e`
**Commit date (upstream):** 2026-04-28 14:53:11 +1000
**Clone date (this corpus):** 2026-05-13
**Site:** https://openpracticelibrary.com/

## What was ingested

Only the **content layer** of the upstream repository was promoted into this corpus:

- `src/pages/practice/*.md` — the 266 practice pages — preserved at `open-practice-library-practices/` and concatenated into `../converted/open-practice-library.md`.

## What was NOT ingested

The upstream repository's other contents (React/Gatsby application code under `src/components/`, `src/pages/{about.js, learn.js, index.js, ...}`, `gatsby-config.js`, `gatsby-node.js`, `package*.json`, `netlify*`, `cypress/`, `static/`, image assets in `static/images/`, blog posts under `src/pages/blog/`) total **716MB** and were not copied. They are licensed Apache 2.0 (application code) and the substantive content for this ingestion is the practice catalogue only.

## Re-fetch instructions

To reconstruct the exact source state used for this ingestion:

```bash
git clone https://github.com/openpracticelibrary/openpracticelibrary
cd openpracticelibrary
git checkout 8bfa450e75dfba1e2a3c68ac0e514e587f6f116e
ls src/pages/practice/*.md | wc -l   # should report 266
```

## Practice count by Mobius phase

(Counted from `mobiusTag` frontmatter values across the 266 files at the cloned commit.)

- **Foundation:** 111
- **Discovery:** 86
- **Options:** 32
- **Delivery:** 37
- **Unclassified (no `mobiusTag`):** 0

Total: 266.

## Licence

- **Content** (the 266 practice pages): **CC BY 4.0** (declared at site footer of openpracticelibrary.com).
- **Application code** (not ingested here): Apache 2.0.

Derivative artefacts produced from this ingestion (deep reference, light reference, task distillations) inherit the CC BY 4.0 attribution requirement for the content.
