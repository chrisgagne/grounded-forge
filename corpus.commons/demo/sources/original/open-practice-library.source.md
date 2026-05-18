---
title: "Open Practice Library"
author: "117+ contributors via Red Hat Open Innovation Labs"
publisher: "Red Hat Open Innovation Labs / Open Practice Library community"
publish_year: 2026
url: https://openpracticelibrary.com/
scope: open
licence: CC BY 4.0
ingested: 2026-05-13
original_format: git_repository_collection
converted_via: manual (concatenation of 266 practice .md files)
checksum_sha256: 2f1ac99414296eeb6d7af64f23fdaf10c1bd85d9325aa88fe8e58dcbecfc1c77
---

# Source: Open Practice Library (Red Hat Open Innovation Labs community, 2016–present)

The Open Practice Library (`openpracticelibrary.com`) is a community-curated catalogue of **266 practices** for teams that "collaborate and deliver iteratively", covering the full DevOps, Agile, design-thinking, product-discovery, and facilitation territory. The library is organised around the **Mobius Loop**, a four-region map of work consisting of *Foundation* (cultural / team practices that span the loop), *Discovery* (why and who; opportunity, problem, customer, alignment), *Options* (what to try; ideas, experiments, prioritisation), and *Delivery* (build and measure; engineering, ops, feedback). Each practice carries YAML frontmatter (`mobiusTag`, `tags`, `authors`, `difficulty`, `time`, `people`, `participants`) and three body fields (`whatIs`, `whyDo`, `howTo`); the site renders each practice as a single page from this markdown source.

**This is a collection-as-source ingest**: the largest in the `corpus.commons/demo` corpus to date. The 266 practice markdown files in `src/pages/practice/` of the upstream Git repository are concatenated into one converted markdown file, grouped by `mobiusTag` (Foundation, then Discovery, then Options, then Delivery) and alphabetised within each phase by source filename. The Mobius-Loop-then-alphabetical ordering was chosen over pure alphabetical because the Mobius framing is itself a load-bearing claim of the source: the curation is organised around it, and a reader of the converted markdown should see the phase structure first.

**Provenance.** Cloned from `https://github.com/openpracticelibrary/openpracticelibrary` at commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` (committed 2026-04-28). The clone manifest is preserved at `open-practice-library.git-info.md` alongside this sidecar. The 266 practice files (only `src/pages/practice/*.md`) are preserved at `open-practice-library-practices/` alongside this sidecar; the rest of the upstream repository (716MB of application code, build configuration, and image assets) is **not** copied; only the substantive content layer of the library is preserved. The application code (React/Gatsby) is licensed Apache 2.0; that licence covers code only, not content.

**Licence.** The content (the practices themselves) is **CC BY 4.0**, declared at the site footer of `openpracticelibrary.com`. Each practice's frontmatter includes a per-practice `authors:` field listing the contributing community members (most by GitHub handle); the umbrella CC BY 4.0 declaration covers the collection. Derivatives of any practice (the deep reference, the light reference, the task distillations produced from this source) inherit the CC BY 4.0 obligation: attribution to the Open Practice Library and to the named per-practice authors where surfaced. The Apache 2.0 application-code licence is irrelevant to the ingested content and is not propagated.

**Practice count.** Exactly **266** practice `.md` files in the upstream repository's `src/pages/practice/` directory at the cloned commit. Distribution across the four Mobius phases: **111 Foundation**, **86 Discovery**, **32 Options**, **37 Delivery**. (Zero unclassified: every practice in the cloned commit carries a `mobiusTag`.) Two of the 266 files are non-English translations of an English original: `event-storming-tormenta-de-eventos.md` (Spanish translation of `event-storming.md`) and `meditacion.md` (Spanish version of `meditation.md`). Both Spanish files are preserved in the converted markdown without translation; the deep reference cites only the English originals.

**Conversion path.** No format conversion was required: the source is already markdown. The 266 files were concatenated by a Python script that parsed each file's YAML frontmatter, rendered the `title`, `subtitle`, metadata block (tags, mobiusTag, authors, area, difficulty, people, time, participants), and the three body fields (`whatIs`, `whyDo`, `howTo`) as a uniform `## {title}` section, separated by `---` rules. Group headers (`# Phase: …`) mark the four Mobius phases. The concatenated file is at `../converted/open-practice-library.md` (sha256 `2f1ac99414296eeb6d7af64f23fdaf10c1bd85d9325aa88fe8e58dcbecfc1c77`, ~22.3k lines, ~148k words, ~970KB).

**Role in corpus.** A *meta-source*: a curated catalogue that the corpus's distillations can route into rather than recapitulate. The collection's value is in its **breadth, taxonomy, and per-practice metadata** (mobiusTag, tags, difficulty, time, participant types); the deep reference's job is to surface those structural properties along with named exemplars from each cluster, not to recapitulate every practice. The distillations route into the OPL cluster appropriate to each task-axis phase (e.g., decision-making routes into prioritisation and consensus practices; stakeholder-engagement routes into stakeholder-mapping and facilitation practices). Future task axes (retrospective work, sprint events, AAR-style learning) will route into other OPL clusters.

Deep reference at `../../references/open-practice-library-deep.md`; light reference at `../../references/open-practice-library.md`; decision-making distillation at `../../distillations/decision-making/open-practice-library-decision-making.md`; stakeholder-engagement distillation at `../../distillations/stakeholder-engagement/open-practice-library-stakeholder-engagement.md`.
