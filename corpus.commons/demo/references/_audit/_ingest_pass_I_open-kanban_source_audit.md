# Pass I Audit Log — open-kanban

**Audit target:** `corpus.commons/demo/references/open-kanban-deep.md`
**Source:** Hurtado, J. (with Annita Yegorova Hurtado), AgileLion Institute. *Open Kanban — Open Source Initiative to create a Kanban core that is Agile, Lean and Free*. Release 1.00 Rev A. CC BY 3.0 Unported. https://github.com/agilelion/Open-Kanban.
**Source converted markdown:** `corpus.commons/demo/sources/converted/open-kanban.md` (210 lines, repository-as-source ingest — combines top-level README.md plus translations call-for-contributors as Appendix A plus diagrams manifest as Appendix B plus excluded-files note as Appendix C).
**Auditor:** claude-opus-4-7[1m], xhigh effort, 9-pass protocol.
**Date:** 2026-05-13.

## Calibration

Read prior to cold-read:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case — biographical claim the source does not make).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical correction case — [V] marker on a paraphrase).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean negative control — over-flagging is as costly as missing real violations).

## Audit summary

| Bucket | Count |
|---|---|
| Total non-trivial claims audited | ~65 |
| Source-anchored, no fix needed | 62 |
| Claims stripped | 0 |
| Claims rewritten in place | 1 (Beck book-title precision) |
| Section retitled / reframed to flag operator context | 1 (Corpus-role caveat — see correction 2 below) |
| Markers corrected in-place | 0 |
| Cross-corpus drift detected | 0 (after the corpus-role-caveat section was reframed) |
| Training-data leakage detected | 0 (the Beck book-title over-precision was a borderline case, corrected) |
| Post-source vocabulary detected | 0 |
| Task-application guidance smuggled into deep | 0 |
| Verbatim accuracy slips in blockquotes | 0 |

The deep reference is short by corpus norms (~180 lines body) because the source itself is short (~3,200 words of methodology text). Most paragraphs in the deep ref are direct quotations with `[V]` markers; the audit confirmed every quoted passage character-for-character against the converted markdown. Two corrections were applied; no full strips were needed.

## Corrections

### Correction 1 — Kent Beck book-title over-precision

**Where:** the deep ref's Part I.2 (Courage) section and the "Connections the author makes in the text" list entry for Kent Beck.

**Issue:** the deep ref originally read "with an Amazon link to *Extreme Programming Explained: Embrace Change*" and "*Kent Beck, Extreme Programming Explained: Embrace Change*, cited for the Courage value." The source text actually says "like [Kent Beck]" with the bracketed link going to an Amazon book page whose URL fragment is `Extreme-Programming-Explained-Embrace-Edition`. The source itself does *not* name the book title in prose; only the URL hints at it (and the URL is ambiguous between "Embrace Change" — the standard subtitle of *XP Explained, 2nd Ed.* — and "Embrace Edition" as a literal reading of the fragment).

**Fix applied in place:** changed the deep ref to "*Kent Beck*, cited by name for the *Courage* value (the source hyperlinks Beck's name to a book on *Extreme Programming Explained*) [BT]" and the body-section reference to "with an Amazon hyperlink on Beck's name pointing at the *Extreme Programming Explained* edition page". The marker remains [BT] (Borrowed-through, the author cites someone else for the claim); the borrowed-through stance is correct, and the precision of what title is being borrowed-through is now correctly hedged.

**Why it matters for the audit:** stating a book title the source does not state in prose is a borderline training-data leak — the title is in the wider literature but not in the source. The correction preserves the borrowed-through claim while honestly representing what the source actually surfaces.

### Correction 2 — Corpus-role caveat section reframed as operator context

**Where:** deep ref §"Authoritativeness and corpus role (provenance caveat)" and light ref §"Authoritativeness Note".

**Issue:** the original section named other Kanban authors (David J. Anderson, Donald G. Reinertsen, Mike Burrows, the Mauvius Group's Klipp/Andersen-Carmichael materials) with publication-year claims as part of justifying why Open Kanban is the only clean-CC Kanban specification in the corpus. None of these authors or works is cited by the source itself; Hurtado names Shalloway, Ladas, and Scotland as fellow-traveller methodologists, but not Anderson, Burrows, Reinertsen as Kanban authors, and not the Lean Kanban University tradition. Reinertsen *is* cited by Hurtado, but only for batch-size reduction's flow argument; not as a Kanban-authority reference. The caveat section as originally written introduced cross-corpus knowledge the source does not state.

**Fix applied in place:** the section was retitled "Corpus-role caveat (operator-supplied, not from source)" and reframed with an opening paragraph in italics that explicitly states: *"The following provenance note is the operator's gap-triage framing for this corpus, not a claim derived from the source. The source itself makes no statements about its author's standing in the Kanban field or about its position relative to other Kanban primary sources. The caveat is recorded here, in a section explicitly flagged as operator context, because it shapes how downstream consumers should weight the reference."* The specific year-citations of Anderson / Reinertsen / Burrows / Klipp publications were removed; the caveat now refers generically to "Other widely-recognised Kanban primary sources" being under non-redistributable licences. The light ref's parallel section was reframed identically.

**Why it matters for the audit:** without this reframing, the deep ref smuggled non-source claims into what reads as source-grounded text. With the reframing, the boundary is explicit: the rest of the deep ref is source-grounded; this clearly-labelled section is operator context that the operator (per the ingest prompt) explicitly asked be included. This is the pattern used elsewhere in the corpus when an operator-provided caveat must travel with a source-grounded reference — flag the boundary, do not blur it.

**Note on the distillations:** the decision-making distillation's *What this distillation does not cover* section still names Anderson, Burrows, and Reinertsen in the context of "this distillation does not cover X; for X, look at Y." This is permitted at the distillation tier (which the protocol defines as the place for library-level synthesis and cross-reference integration); the boundary it enforces is that the deep ref does not make such claims. The distillation is doing the right job: telling a downstream reader where to look for what Open Kanban does not address.

## Cross-claim verifications spot-checked against the source

All quotations below verified character-for-character against the converted markdown at `corpus.commons/demo/sources/converted/open-kanban.md`.

| Claim | Verified against converted markdown line(s) |
|---|---|
| "Open Kanban is a movement to make the core values and principles of Kanban available to all" | 35 |
| "those four freedoms, but now in the context of shared knowledge" | 37 |
| "This freedom shows our commitment to communication, collaboration and continuous improvement" | 41 |
| "with growth also came a push to align Kanban..." | 46 |
| "Open Kanban actually corresponds to what most people familiar with the Agile movement think of when they refer to Kanban itself" | 48 |
| "Open Kanban is an Agile and Lean ultra light method..." | 56 |
| "Open Kanban is not a full or complete Agile or Lean method, instead it is the heart of that method..." | 58 |
| "the kernel of an open source operating system" | 58 |
| "A set of values that align it with the Agile and Lean Movements..." | 61 |
| "Extensions on top of Open Kanban constitute Agile and Lean Methods..." | 67 |
| "Open Kanban is the heart of all those Kanban methods. Our license allows them to be free or commercial" | 67 |
| "All Open Kanban Methods share in common the following characteristics" | 69 |
| "We extend an open invitation to them" / Shalloway / Ladas / Scotland naming | 78 |
| "Open Kanban practices are rooted in values that are Lean and Agile..." | 84 |
| "At the core of Lean and TPS is respecting people" | 87 |
| "Respect for people allows for delegation and the demand-pull..." | 88 |
| "Respect for people also aligns with sustainable pace in Agile, or Muri 無理 in Lean" | 89 |
| "An exhausted developer, manager or team are the perfect recipe for disaster" | 89 |
| "Respect for people is not enough; like Kent Beck noticed..." | 91 |
| "When a manager, VP, or person in authority makes a mistake..." | 91 |
| "Courage combined with respect for people enable effective delegation, proper demand-pull and continuous improvement" | 92 |
| "One of the key purposes of Kanban is the creation of value" | 94 |
| "Value implies customer satisfaction, and that is the purpose of our efforts" | 94 |
| "Value is at the center of Lean and TPS... eliminate waste or 'Muda' in Japanese Muda 無駄..." | 95 |
| "Communication, and collaboration are at the center of teamwork..." | 97 |
| "One value does not work without the other..." | 97 |
| "Without teamwork Kanban fails..." | 98 |
| "Deming's System of Profound Knowledge and Goldratt's Theory of Constraints reminds us..." | 100 |
| "the key part of the system is people, not just as resources, but also as full rounded individuals who make the system work" | 100 |
| "Kanban agrees with this vision and aims to drive improvement where it counts" | 101 |
| "Open Kanban values translate into action by following four key practices" | 104 |
| "the output of your effort is much smaller than the effort involved, and the bulk of that effort cannot be easily seen" | 107 |
| "Kanban deals with this challenge by using Kanban boards..." | 108 |
| "This Kanban practice makes it easier to collaborate in a team setting..." | 109 |
| "Visualizing the workflow is not limited to Kanban boards..." | 110 |
| "Unless your organization is composed of just one person..." | 112 |
| "Although Kanban starts where you are, and does not need to modify any titles or roles in an organization..." | 113 |
| "Teams and team leadership are crucial to deliver value... No need for new roles or titles, but we do have a need for working teams, with leaders in them!" | 114 |
| "Research in the way the mind works..." (multi-source citation incl. Lean, ToC, Kanban) | 116 |
| "Multitasking does not work" | 116 |
| "Limiting how many things you do at any given time..." | 117 |
| "one of the best explanations of this fact has been given by Donald G. Reinertsen" | 117 |
| "Limiting WIP is a consequence of reducing the batch size of your efforts..." | 118 |
| "Open Kanban does not ask you to limit WIP, but it does request that you 'Reduce the Batch Size of your Efforts'" | 118 |
| "Reduce the complexity and the quantity of things you do at any stage of the value chain" | 119 |
| "reduce the number of large stories (epics) you create" | 119 |
| "The four previous practices ensure you are doing things better than before..." | 122 |
| "Retrospectives, Strategy Meetings or even Kaizen Groups" | 123 |
| "Learning is the key concept before continuous improvement can ever happen!" | 124 |
| "Open Kanban further supports learning by listening to the community and updating itself" | 125 |
| "Our search for a suitable open source license..." (LGPL v3, MIT, CC) | 129 |
| "Although the first two licenses are appropriate, both are designed for sharing of computer source code..." | 131 |
| "Creative Commons on the other hand is appropriate for knowledge work that deals with writing, and media creation" | 131 |
| "We selected the Creative Commons Attribution 3.0 Unported license" | 133 |
| "We only ask you that you: Give us credit; Contribute your best ideas back to Open Kanban root repository" | 137 |
| "Kanban Ace Coach - An Open Kanban Method" (closing signature) | 162 |
| カンバン (Kamban) Japanese term | 48 |
| Author / contributor / sponsor metadata (Hurtado / Yegorova Hurtado / AgileLion Institute) | 7–9 |
| Release "1.00 Rev A" | 12 |

All quotations verified. The italicised emphasis ("Reduce the Batch Size of your Efforts") and the Japanese characters (Muri 無理, Muda 無駄, カンバン / Kamban) are preserved in the deep reference exactly as they appear in the source.

## Cross-checks for the failure-mode catalogue

- **Training-data leakage.** No claims about Joseph Hurtado's biography, career beyond the AgileLion Institute / Kanban Ace Coach role the source signs as, or post-2014 activity. The Kent Beck book-title over-precision was corrected (Correction 1). The Anderson / Burrows / Reinertsen-as-Kanban-authority paragraph was reframed as explicitly operator context (Correction 2). **Pass.**
- **Post-source vocabulary.** No introduction of concepts from later Hurtado works, later AgileLion materials, or later Kanban methodology releases. The deep ref stays faithful to Release 1.00 Rev A's vocabulary. **Pass.**
- **Cross-corpus drift.** The deep ref's *Connections the author makes in the text* section lists only sources Hurtado cites (Kent Beck, Deming, Goldratt, Cockburn, Reinertsen, TPS, Agile Manifesto, Lean, VersionOne, Shalloway, Ladas, Scotland, Free Software Foundation, Linux kernel, Kaizen Groups). The deep ref's "does not cite Anderson" framing observation is an *absence* claim about the source, not a connection — and absence claims are permitted when the absence is part of the methodology's positioning. The corpus-role caveat section is now explicitly flagged as operator context. **Pass.**
- **Task-application guidance smuggled into the deep.** No diagnostic questions, no decision rules, no practitioner checklists in the deep tier. All such material is in the distillations (`open-kanban-decision-making.md`, `open-kanban-stakeholder-engagement.md`). **Pass.**
- **Verbatim accuracy slips.** Blockquotes spot-checked character-by-character: the *Muda* passage with the Japanese characters preserved; the WIP-as-consequence passage with the embedded quoted phrase "Reduce the Batch Size of your Efforts" preserved. Italicisation, capitalisation, punctuation match the source. **Pass.**
- **Silent partial coverage.** Both the canonical README and the bundled stable copy were read end to end; their textual identity (modulo the one typo "submisssions" / "submissions") was verified. The six language-translation directories were skipped *by design* (translation content, not methodological content); this is documented in the converted markdown's Appendix C and is not a partial-coverage caveat in the source-integrity-rule sense — the methodological coverage of the English source is complete. **Pass.**
- **Repository-as-source pattern integrity.** The SHA-256 checksum recorded in the sidecar is computed over the concatenated converted markdown (since the source is a repository, not a single binary file). The original repository tree is preserved at `corpus.commons/demo/sources/original/open-kanban-repo/` for any later work that needs the diagrams, the translations, or the Illustrator-source PDFs. The repository-as-source ingest pattern is documented in the converted markdown's leading HTML comment and in the source sidecar's body. **Pass.**

## Gate decision

The deep reference passes Pass I and is cleared to ship. The light reference (`open-kanban.md`) and the two distillations (`open-kanban-decision-making.md`, `open-kanban-stakeholder-engagement.md`) derive from the audited deep and inherit the discipline by construction. The light ref's Authoritativeness section was reframed in parallel with the deep ref's Corpus-role-caveat section so the operator-context flagging propagates.

The Hurtado deep reference is short by corpus norms (~180 lines body), reflecting the source's own brevity (~3,200 words of methodology text). The audit-claim-to-line ratio is high; this matches the source's citation density (the document is unusually citation-dense for a methodology specification, with explicit external references to Beck, Deming, Goldratt, Cockburn, Reinertsen, TPS, Lean, Agile Manifesto, Free Software Foundation, the Linux kernel, Wikipedia entries on Kaizen and Information Radiators, and VersionOne 2013).
