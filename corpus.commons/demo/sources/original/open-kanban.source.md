---
title: "Open Kanban — Open Source Initiative to create a Kanban core that is Agile, Lean and Free"
author: Joseph Hurtado (with Annita Yegorova Hurtado, contributor)
publisher: AgileLion Institute
publish_year: 2014
url: https://github.com/agilelion/Open-Kanban
scope: open
licence: CC BY 3.0 Unported
ingested: 2026-05-13
original_format: git_repository
converted_via: manual (concatenation of repository's English-language markdown files; the source is markdown-native)
checksum_sha256: ba846e451dc029caad144bd37f64a4f3eb4daa6a67eb6f0e6a4ce36c9a71a641
---

# Source: Open Kanban (Hurtado, AgileLion Institute), Release 1.00 Rev A

The canonical-state-as-of-ingest of the *Open Kanban* methodology specification published by Joseph Hurtado (with contributor Annita Yegorova Hurtado) of the AgileLion Institute on GitHub. Release 1.00 Rev A. CC BY 3.0 Unported. Acquired via `git clone https://github.com/agilelion/Open-Kanban`. Deep reference at `../../references/open-kanban-deep.md`; light reference at `../../references/open-kanban.md`; converted markdown at `../converted/open-kanban.md`.

**Repository-as-source ingest (a new pattern for this corpus).** The source is a GitHub repository containing multiple markdown files rather than a single document. The canonical methodology specification lives in two parallel forms inside the repository: the top-level `README.md` (the GitHub-facing canonical view) and a substantively identical "stable copy" at `Open Kanban Support Documents/Open Kanban Main v1_RevA.md` that translators are explicitly asked to use as their source. Those two files are textually identical apart from a single typo difference ("submisssions" with three s's in the support-doc copy versus "submissions" in the README); the converted markdown uses the README's spelling. The converted markdown also appends the translations call-for-contributors README as Appendix A, a diagrams manifest (filenames only; the binaries are not visually inspected in this text-only ingest) as Appendix B, and an excluded-files note as Appendix C.

**SHA-256 checksum** is computed over the concatenated converted markdown (`sources/converted/open-kanban.md`), not over a single binary source file; there is no single binary source. The full repository tree is preserved at `corpus.commons/demo/sources/original/open-kanban-repo/` for any later work that needs the diagrams, the translations, or the Illustrator-source PDFs.

**Constituent files included in the converted markdown:**

- `README.md` (top-level; canonical methodology specification; ~140 lines of markdown).
- `Open Kanban Support Documents/Open Kanban Main v1_RevA.md` (read for cross-comparison; substantively identical to the README, modulo one typo; not separately concatenated since it would duplicate the canonical text).
- `Open Kanban Translations/README.md` (call for translators; appended as Appendix A).
- `Open Kanban Diagrams/` filenames (listed in Appendix B; binary images not inlined or visually inspected in this run).

**Constituent files excluded:**

- `Open Kanban Translations/Open-Kanban-French/`, `.../Open-Kanban-Italian/`, `.../Open-Kanban-Portuguese/`, `.../Open-Kanban-Russian/`, `.../Open-Kanban-Spanish/`, `.../Open-Kanban-Ukrainian/`. Translation directories reproducing the same methodology in other languages. Excluded by design: the methodology content is identical to the English source, and shipping all six translations would inflate the corpus without adding methodological content. Available in the preserved original repo tree for any later translation-specific work.
- The binary diagram files (PDFs and PNGs) in `Open Kanban Diagrams/`. Listed in the converted markdown's Appendix B as references but not visually inspected in this text-only ingest. The diagrams may be added to `docs/images/IMAGE-INDEX.yaml` via a later `ingesting-images` run.

**Licence and distribution note.** This source is released under CC BY 3.0 Unported. CC BY 3.0 has no Share-Alike (copyleft) provision: derivative works (including this corpus's deep reference, light reference, and distillations) inherit only the attribution obligation, not a propagating copyleft obligation. This is materially different from the Jones (CC BY-SA 4.0) and Scrum Guide (CC BY-SA 4.0) co-mixed in this corpus: those carry SA propagation; Open Kanban does not. Build profiles incorporating Open-Kanban-derived content are obliged to give credit to Joseph Hurtado and the AgileLion Institute but are not obliged to release derivative work under any specific licence.

**Provenance.** The Open Kanban GitHub repository was started circa 2014; this `Release 1.00 Rev A` is the initial public release explicitly framed (in the README's *Open Kanban Components* section) as expecting "future contributions and revisions" via GitHub pull requests. The author signs the closing of the methodology document as "Joseph Hurtado, Founder AgileLion Institute, Kanban Ace Coach - An Open Kanban Method".

**Version-pin caveat.** "Release 1.00 Rev A" is the upstream's self-naming in the README body, not a git tag; the upstream repository carries no release tags at the time of ingest, and this source-card does not pin a `git_commit_sha`. The SHA-256 checksum above is over the concatenated converted markdown, not over a stable repository identifier. Re-ingesting against the same repository at a later date and getting the same checksum is the practical verifier that the upstream has not shifted. Future re-ingestions should record the head commit SHA at fetch time even when no upstream tag exists.

**Role in corpus.** The redistributable Kanban-methodology slot. Open Kanban is the only clean-CC Kanban methodology specification this corpus's gap-triage identified at ingest; other widely-recognised Kanban primary sources are under non-redistributable licences. The deep reference carries the corpus-role caveat explicitly in a section flagged as operator context. The reference projects onto both of the demo's task axes (`decision-making` strong fire; `stakeholder-engagement` moderate fire). A dedicated retrospective or flow-of-work axis added later would be a strong fit for Open Kanban as well.
