# Screening, 11 Oct 2026: cross-family leg for mcdp1-warfighting

Screened in the aarbuddy corpus as one of its most-routed deeps with no Pass I stamp, after a defect sample there found a high rate; this demo copy of the deep is the same file. GPT-5.6 Sol audited a frozen copy blind (sha256
`da84bf336a8f08fcb719a09669cb84b68829fa7df489a74a57ef60dccf246692`); a fresh Claude Opus 5.5 subagent checked each finding against the tape and applied the ones
that held (`projects/defect-sample-2026-10/apply-brief.md`); the parent reviewed the apply report.

**Deep after this leg:** sha256 `6cec9ab752a6f34aec2455ba3b92dea5759a5c6d3c43b43b476da7f56f6a6248` (including the stamp line).

**Parent's note:** Parent checked the deep's sha256 against the report and two fixes against the tape: the imprint's '© 1997 United States Government as represented by the Secretary of the Navy. All rights reserved.' (tape 61), and the levels of war 'may compress' (891). Both hold. Scope kept 'open': the official PDF's cover carries Distribution Statement A, "Approved for public release; distribution is unlimited".

**Derived tier:** the light reference and distillations are re-derived from this deep and stamped with
`check_derived_provenance --stamp --slug mcdp1-warfighting`.

## Apply report

# Apply report: mcdp1-warfighting

Deep: `corpus.local/aarbuddy/references/mcdp1-warfighting-deep.md`. Before editing it matched `frozen-deep.sha256` (`da84bf33…f246692`) byte for byte. Card: `corpus.local/aarbuddy/sources/original/mcdp1-warfighting.source.md`, identical to the packet's `source-card.md`. Line numbers are frozen-deep lines unless marked "now". This source was screened (one of the most-routed deeps), not drawn in the random sample. Per this leg's brief, `[V]`-for-`[BT]` tagging, OCR repair and pandoc markup are not defects.

## What I read

- In full: `apply-brief.md`, `sol-blind-findings.md`, `sol-brief.md`, `pass-i-spec.md`, `source-card.md`, the frozen deep (244 lines), and `tape.md` lines 1–3041 (Foreword, Preface, contents, all four chapters with epigraphs, all Notes, GPO line).
- The original `source.pdf`: metadata (115 pages), the text layer of pages 1–8 and 114, and page images of 1 (cover), 4 (Krulak's signature and the imprint), 7 (Gray's signature), 38 and 40 (Figures 1 and 2) and 65 (Professionalism heading). The cover and both signatures are images only; the tape has no text from them.
- In part: the sample `REPORT.md` (bucket definitions and the apply-step section, lines 42–58 and 136–163).
- Not read: `fixtures/`, `sol-blind-log.txt`.
- Checks: `scripts/check-verbatim.py` against the tape, on the frozen deep and on the edited deep. On the edited deep every flag is OCR repair (*uncertainly*, *f eliminated*, *ajid*, glued note numbers), a page header inside a quote, a permitted ellipsis or capital, or line 236 (now), the cover's Distribution Statement A, which exists only as an image and was read from the original. Edits were made by `apply-mcdp1-warfighting/apply.py` (each old string matched exactly once and started on the cited frozen line), dry-run to `deep.new.md`/`card.new.md`, then written; the result is byte-identical to the dry run.

## Sol's findings

1. **Applied, own wording** (PDF pp. 4, 7: "C. C. KRULAK, General, U.S. Marine Corps, Commandant of the Marine Corps"; "A. M. GRAY, General, U.S. Marine Corps (Ret.), 29th Commandant of the Marine Corps"). Deep line 5 now reads "U.S. Marine Corps, … 1997; Foreword signed by General C. C. Krulak, Commandant of the Marine Corps." Card `author: "U.S. Marine Corps"`; "Charles C.", "Alfred M." and "31st Commandant" are gone from the card body (line 19). **Light.**
2. **Applied, own wording; scope change not applied.** Cover (PDF p. 1): "DISTRIBUTION STATEMENT A: Approved for public release; distribution is unlimited"; imprint (tape 61): "© 1997 United States Government as represented by the Secretary of the Navy. All rights reserved." Deep line 5 ends "Licence: unverified (…both notices…)". Line 230 (now 236) quotes both notices and says the source doesn't itself establish public-domain status or a right to republish derivative work; the 17 U.S.C. §105 analysis, "legally vestigial", "freely re-publishable" and "can travel into compiled applications" are gone. The old line also cut "All rights reserved." from the imprint it quoted. Card `licence: unverified`, body line 21 rewritten the same way. I did not set Scope to `copyrighted`, as Sol recommended: your brief gives the scope as `open`, Distribution Statement A supports public release, and scope is an operator call that also governs the commons copy (see Flags). The deep and card now say `Scope: open` rests on the distribution statement. **Light.**
3. **Applied** (`shasum`: `source.pdf` = `51008277…f35097c0`, `tape.md` = `c36d3f3f…b7d62182`; the ingest skill defines `checksum_sha256` as the input file's hash). Card frontmatter now carries the PDF hash. I didn't add a `converted_checksum_sha256` field, which no other card uses; the converted hash moved into the card's provenance prose (line 25) and is still in the deep (line 226, now 232). **Light.**
4. **Applied, own wording** (tape 7–20, 35–36, 41, 69–72, 83–85). Card line 19 no longer says Gray "made the doctrinal pivot from attrition warfare to maneuver warfare". It quotes the Foreword ("the authoritative basis…"), Gray's stated intent ("to describe my philosophy on warfighting"), "refines and expands" (Preface), and gives Krulak's "retaining the spirit, style, and essential message" as his stated intent, not as an outcome. Sol's version turned that intent into "says it retains". **Invented** (card only).
5. **Applied, own wording** (tape 2899–2915, 2995–2997, 3034–3036; no Wyly or Wilson anywhere). Card line 23 now lists what the Notes credit: Boyd (OODA loop, Notes 18 of Ch 2; implicit communication, Notes 5 of Ch 4), Lind (Notes 11 of Ch 4), Clausewitz in 15 notes, and *On War* and *The Art of War* as essential reading. "Uncredited in the document; well-established historically", Wyly and Wilson are gone. **Invented** (card only).
6. **Not applied.** Line 20: the quoted sentences are MCDP 1's own words too; they open Ch 1, "The evolution of war" (tape 558–559), and the deep says so. Line 216: "Resolute and self-reliant in their decisions … energetic and insistent in execution" is MCDP 1's own unquoted sentence (tape 1576–1577; PDF p. 65 prints "self-reliant" across a line break); Note 5 cites FM 100-5 as its source. Either way this is `[V]`-for-`[BT]` tagging. **Not a defect.**
7. **Applied, own wording** (tape 745–759, read in full). New paragraph after "War as an act of policy" (now 81), quoting the section's three key statements. Sol's paraphrase dropped the source's "for example" before the four kinds of power. **Invented** (missing section).
8. **Applied, own wording** (tape 1879–1891, read in full). New "Conclusion" paragraph after "Equipping" (now 127), quoting the whole five-sentence section. **Invented** (missing section).
9. **Applied, own wording.** Line 224 (now 230) states coverage against the `pdftotext` conversion and says the cover, the two signatures and the figures are images read from the original. The 4,478-line OCR, "no chunks dropped" and "three reads" are gone. Sol's "full for this audit" and "supplied 3,041-record" wording was process framing, so I left it out. **Light.**
10. **Applied, own wording** (tape 3017–3020: "The Day Soft-/ware Puts the Universe in a Shoebox"). Line 228 (now 234): no *after-action* or *retrospective*; *software* only in Gelernter's subtitle, which is now quoted; no software work; *critique* is the review term. **Light.**
11. **Applied as written** (strip; tape 178–194). The `[AR]` that closes the thesis item stays. **Invented** (a causal link the source doesn't draw).
12. **Applied, own wording** (tape 499–517). "The passage on fear is the chapter's most direct treatment of the moral dimension:" became "On fear:". "Unit cohesion is the operational mechanism against fear" is stripped, and the sentence the quote had cut ("Leaders should develop unit cohesion and esprit and the self-confidence of individuals within the unit. In this environment,") is restored inside the `[V]` quote. Sol's replacement said peers' trust "can help overcome" fear, but the source says "can overcome", and it repeated the quote. **Distorted** (one mechanism given where the source names leadership, experience, training and cohesion).
13. **Applied as written** (strip "The chapter's load-bearing section."). **Light.**
14. **Applied, own wording** (tape 1592–1614). The label became "On boldness and initiative:". The sentence calling the leniency/severity pairing "the institutional discipline that supports the mission-tactics philosophy of Ch 4" is stripped, not replaced: Sol's replacement only restated the quote just before it. **Invented** (a causal link the section doesn't draw).

## Sweep: further defects of the same kinds (applied)

- S1. Line 13: "refines and expands … while retaining the spirit, style, and essential message" asserted an outcome; the Foreword says "It is my intent to do this while retaining…" (tape 35–36). Now "Krulak's stated intent was to do so while…". **Distorted** (dropped hedge).
- S2. Line 17: label "deliberately compact, deliberately philosophical" stripped. **Light.**
- S3. Line 25: Notes described as "bibliographic references … effectively a curated reading list". They also carry Joint Pub 1-02 definitions and commentary, including the only account of the OODA loop (tape 2680–3036). Rewritten to say so. **Light.**
- S4. Lines 49, 77, 103, 125: glosses on what the epigraphs do ("triangulate the chapter's claims"; "set the chapter's three structural commitments … a dialectic of attack and defence"; "frame preparation as the disciplined development of will + intellect"; "the synthesis of everything that came before") stripped. The epigraphs are now just described, with Churchill's line quoted at 77 (tape 658–660). **Light.**
- S5. Lines 81, 83, 181, 232: the acronym "MOOTW", which the source never uses, replaced with its own term. The vocabulary entry (181, now 187) now quotes its definition (tape 765–766) where "low-intensity end" had paraphrased it. **Light.**
- S6. Line 81: "A military trained for one is not automatically equipped for the other" made a one-way, hedged statement symmetric and unhedged. It now quotes "may find itself ill-prepared for a 'small' war against a lightly equipped guerrilla force" (tape 811–819). **Distorted.**
- S7. Line 83: "levels collapse" for the source's "the levels of war may compress so that there is significant overlap" (tape 887–894). Rewritten in the source's terms and order. **Distorted.**
- S8. Lines 99 and 155: "The chapter's closing move" and "closes the chapter's argument". Both chapters end with a Conclusion section after these. Labels stripped or replaced ("The section's MAGTF-level example", tape 2637). **Light.**
- S9. Ch 2 "Conclusion" (tape 1422–1441, read in full) was missing. Added after "Creating and exploiting opportunity" (now 103). **Invented** (missing section).
- S10. Line 105: `[V]` closed a paraphrase that broadened "all force planning" to "all planning". Now *"concept-based"* `[V]`, followed by an `[AP]` paraphrase in the source's terms (tape 1489–1492). **Light.**
- S11. Line 113: "loyal compliance after". The source condemns "ready compliance" and asks juniors to "support it as if it were their own" (tape 1629–1634). Now "loyal support". **Light.**
- S12. Line 115: "Exercises must introduce friction". The source says "should" (tape 1691–1699). **Distorted.**
- S13. Line 187: "The whole document is a redirection away from attrition" stripped. No passage says the Corps' doctrine had been attrition-based, and the source holds that all warfare mixes both (tape 1133–1138). **Invented.**
- S14. Line 188: "The Ch 4 statement is even sharper:" became "Ch 4:". **Light.**
- S15. Line 195: Notes 8 of Ch 1 is attached to "the violent essence of war will never change" (tape 485–486), not to the anti-romanticising sentence it was said to "reinforce". Now says so. **Light.**
- S16. Line 220: "the book gives the document the word it needs" stripped. *Topsight* is now quoted from the note (tape 3026–3029). **Light.**
- S17. Line 232: "The figure captions and their textual referents are reproduced verbatim in Ch 2" is not true of the deep's Ch 2. Now: the captions and the passage that refers to the figures are in the converted text (Ch 2, "Levels of war"; tape 824, 845, 887–898). Sol's check of the figures holds (PDF pp. 38, 40). **Light.**

Checked and left: the 15 Clausewitz notes; every Notes locator in "Connections"; Joint Pub 1-02's definitions list; all historical example lists; "Personnel management … picked up in Ch 4" (Ch 4 ties implicit communication to familiarity and shared experience, tape 2155–2162, 2251–2253); and the small-caps headings claim (PDF p. 65).

## Coverage additions

- **Means in war** (now 81), from tape 745–759. The section is 11 lines and was read in full.
- **Ch 2 Conclusion** (now 103), from tape 1422–1441, read in full.
- **Ch 3 Conclusion** (now 127), from tape 1879–1891, read in full.

Every TOC section of all four chapters (tape 96–140) now has a paragraph or a quotation cited to it. Ch 1's Conclusion was already quoted in Thesis 1, and Ch 4's in "Closing".

## Source-card changes

`author: "U.S. Marine Corps"`; `licence: unverified`; `checksum_sha256` set to the PDF hash. Body line 19 rewritten (F1, F4) and line 21 rewritten (F2). Line 23 rewritten (F5). Line 25 gains the converted-text hash. `scope: open` unchanged. I left line 25's note about the earlier OCR and the 2026-10-02 quotation re-check, which is card provenance, and line 31's Coram companion-volume pointer, which Sol also passed.

## Breadcrumbs stripped (deep)

- 224 "…in the 4,478-line plain-text OCR of this edition that the deep reference was written from. No sections skipped; no chunks dropped. … tractable in three reads." (with F9)
- 226 "The converted source is now…" (now "is"); "where either conversion garbles it" (now "the conversion"); "Every quotation was re-checked against this conversion with `scripts/check-verbatim.py` on 2026-10-02; … `_audit/_pass_I_quotations_…_2026-10-02.md`." (stripped)
- 232 "Declared `text-only` at pre-flight." (now "Text-only.")

## Flags for you

- **The commons copy is now stale.** `corpus.commons/demo/references/mcdp1-warfighting-deep.md` and its card are byte-identical to the frozen versions (sha `da84bf33…`), so the public-tier corpus still carries every defect above, including the public-domain claim. The local card's line 29 ("Both corpora hold the same … deep reference") is false until the two are synced. Per the brief I touched neither.
- **Scope.** Sol's rule (licence unverified → `copyrighted`) would pull this source out of `open` profiles. I kept `open` on the strength of Distribution Statement A; the call is yours.
- The light reference and distillations were derived from the old deep and were not touched.

## Buckets

| | Sol | Sweep |
|---|---:|---:|
| Invented | 6 (4, 5, 7, 8, 11, 14) | 2 (S9, S13) |
| Distorted | 1 (12) | 4 (S1, S6, S7, S12) |
| Light | 6 (1, 2, 3, 9, 10, 13) | 11 (S2–S5, S8, S10, S11, S14–S17) |
| Not a defect | 1 (6) | — |
| **Total** | **14** | **17** |

Sol's claim-unit count: **297** (239 marker-closed units, 38 unmarked deep units, 20 card units). Sol's invented and distorted findings come to 7, or 2.4 per 100 units. Findings 4 and 5 are card-only.

Deep sha256 after edits: `6dd4e264371be281877bcb9d52a82af8dc749134adfc258448391f6b453eaf8d` (250 lines). Card sha256: `985c583f32999f8594d7731d4b80880f1259ebf885fb21ddb90e358e949fa549`.

## Sol blind findings

## 1. What I read

Read in full:

- `sol-brief.md`
- All three calibration fixtures
- `pass-i-spec.md`
- `frozen-deep.md`
- `tape.md`, numbered lines 1–3041. `wc -l` reports 3040 because the final form-feed is not newline-terminated.
- `source-card.md`
- The governing repository, architecture, source-integrity and Pass I instructions.

Read in part:

- `source.pdf` metadata and the pages needed for provenance, OCR and figure verification: PDF pages 1, 2, 4, 6, 7, 38, 40, 54, 55, 67, 69, 70, 87 and 114.

The complete textual source was read through `tape.md`; no part of the tape was skipped.

## 2. Findings

Gate: **FAIL pending 14 fixes.**

1. **Locations:** `frozen-deep.md:5`; `source-card.md:3,19`  
   **Class:** `provenance`  
   **Evidence:** The original identifies the signatories only as C. C. Krulak and A. M. Gray; it identifies Gray as the 29th Commandant but does not supply either man’s expanded first name or identify Krulak as the 31st Commandant (PDF pp. 4, 7; tape 88–91).  
   **Exact fix:** In the deep reference and card author field, use `U.S. Marine Corps` as the institutional author. Where signatories are discussed, use `General C. C. Krulak, Commandant of the Marine Corps` and `General A. M. Gray, 29th Commandant`; strip `Charles C.`, `Alfred M.` and `31st Commandant`.

2. **Locations:** `frozen-deep.md:5–6,230`; `source-card.md:9–10,21`  
   **Class:** `provenance`  
   **Evidence:** The cover says, “DISTRIBUTION STATEMENT A: Approved for public release; distribution is unlimited,” while the imprint says, “© 1997 United States Government as represented by the Secretary of the Navy. All rights reserved” (PDF pp. 1, 4; tape 59–65). The source does not state that it is public domain, that the notice is legally vestigial, or that derivative republication is unrestricted.  
   **Exact fix:** Replace the legal conclusions with:

   > **Scope determination.** The cover states, “DISTRIBUTION STATEMENT A: Approved for public release; distribution is unlimited.” [V] The imprint states, “© 1997 United States Government as represented by the Secretary of the Navy. All rights reserved.” [V] The source itself does not establish public-domain or derivative-republication rights.

   Set the card licence to `unverified` and, under the repository’s unverified-rights rule, Scope to `copyrighted` pending an external rights determination. Strip `public-domain`, the 17 U.S.C. §105 analysis, `legally vestigial`, and `freely re-publishable`.

3. **Location:** `source-card.md:14`  
   **Class:** `provenance`  
   **Evidence:** The stated checksum, `c36d…b62182`, is the SHA-256 of `tape.md`, not the binary input. `source.pdf` hashes to `51008277a48f89dc4f302715764461086a5e616d520a41b71bdbd3f8f35097c0`; the card itself gives that correct original hash at line 25.  
   **Exact fix:** Replace line 14 with:

   `checksum_sha256: 51008277a48f89dc4f302715764461086a5e616d520a41b71bdbd3f8f35097c0`

   If the converted checksum is retained, add a separately named `converted_checksum_sha256` field containing `c36d…b62182`.

4. **Location:** `source-card.md:19`  
   **Class:** `external-framing`  
   **Evidence:** The Foreword says FMFM 1 changed Marine thinking and that current doctrine rests on its manoeuvre-warfare tenets; the Preface calls the first edition Gray’s philosophy (tape 7–20, 69–87). It does not say Gray personally “made the doctrinal pivot from attrition warfare to maneuver warfare.”  
   **Exact fix:** Replace the paragraph with:

   > The publication presents the U.S. Marine Corps’ warfighting philosophy. It has approximately 100 numbered pages plus front matter, a Foreword, a Preface, four chapters and Notes. It supersedes the 1989 *FMFM 1: Warfighting*. General A. M. Gray, 29th Commandant, says the first edition described “my philosophy on warfighting”; the 1997 revision signed by General C. C. Krulak says it retains the original’s spirit, style and essential message.

5. **Location:** `source-card.md:23`  
   **Class:** `cross-reference`  
   **Evidence:** The source cites Boyd and Lind at Notes 18 of Ch 2 and Notes 5 and 11 of Ch 4 (tape 2899–2915, 2995–2997, 3034–3036). It contains no Mike Wyly or G. I. Wilson citation or attribution.  
   **Exact fix:** Replace the paragraph with:

   > Named citations relevant to the manoeuvre vocabulary include John Boyd, William S. Lind, Clausewitz and Sun Tzu.

   Strip the “uncredited … well-established historically” framing and the Wyly and Wilson references.

6. **Locations:** `frozen-deep.md:20,216`  
   **Class:** `marker`  
   **Evidence:** Line 20 explicitly takes its words from the earlier FMFM 1 (tape 80–81). Line 216 identifies its quoted language as coming through *Field Manual 100-5* (tape 1571–1577, 2953–2955). These are named quoted-through sources, not MCDP 1’s unattributed original words.  
   **Exact fix:** Change `[V]` to `[BT]` at both locations. Alternatively, line 20 may retain `[V]` if it cites the identical occurrence in Ch 1, “The evolution of war,” instead of the Preface’s quotation of FMFM 1.

7. **Locations:** `frozen-deep.md:22,75–99,224`  
   **Class:** `coverage`  
   **Evidence:** Ch 2’s “Means in War” section says war can employ economic, diplomatic, military and psychological power; military force must not be considered in isolation; and its forms range from deployment as a demonstration of resolve through truce enforcement to general warfare (tape 745–759). The structure list names the section, but the synthesis omits it.  
   **Exact fix:** Add after “War as an act of policy”:

   > **Means in war.** At the highest level, war brings economic, diplomatic, military and psychological forces to bear. Although the pamphlet focuses on military force, it says military force must not be considered in isolation from the other elements of national power. Its forms range from deployment as a demonstration of resolve through enforcement of a negotiated truce to general warfare. [AP] (Ch 2, “Means in War”)

8. **Locations:** `frozen-deep.md:101–121,224`  
   **Class:** `coverage`  
   **Evidence:** Ch 3’s Conclusion says the two basic military functions are waging and preparing for war, that other activity is justified only by preparedness, and that conduct and preparation cannot be separated because failure in preparation causes battlefield disaster (tape 1879–1891). This section is absent.  
   **Exact fix:** Add after “Equipping”:

   > **Conclusion.** The chapter names two basic military functions—waging war and preparing for war—and says activities not contributing to a present war are justified only when they contribute to preparedness for a future one. Conduct and preparation cannot be separated; failure in preparation leads to disaster on the battlefield. [AP] (Ch 3, “Conclusion”)

9. **Location:** `frozen-deep.md:224`  
   **Class:** `coverage`  
   **Evidence:** The supplied audit tape has 3,041 numbered records, not the claimed 4,478-line artefact. The alleged earlier OCR and “three reads” are not supplied independently, and the reference’s substantive coverage omits the two sections identified above.  
   **Exact fix:** After adding Findings 7–8, replace the paragraph with:

   > **Coverage: full for this audit.** Foreword, Preface, all four chapters and the Notes were read end-to-end in the supplied 3,041-record `pdftotext` conversion. Provenance and visual claims were checked against the original PDF.

10. **Location:** `frozen-deep.md:228`  
    **Class:** `quantity-qualifier`  
    **Evidence:** The original contains one occurrence of *Software*, in Gelernter’s cited subtitle *The Day Software Puts the Universe in a Shoebox* (PDF p. 114). Conversion splits it as `Soft-` / `ware` at tape 3017–3020. The work does not discuss software practice, but the claimed zero occurrence is wrong once the line-break hyphen is repaired.  
    **Exact fix:** Replace the first sentence with:

    > The source contains no occurrence of *after-action* or *retrospective*. Its sole occurrence of *software* is in the subtitle of Gelernter’s cited book; it does not address software work. Its term for reviewing a completed training event is *critique* (Ch 3, “Training”).

11. **Location:** `frozen-deep.md:37`  
    **Class:** `external-framing`  
    **Evidence:** Ch 1 supports war as an interactive social process between opposing wills (tape 178–194). No passage says this particular proposition is the foundation for “every later move” toward tempo, mission tactics and the OODA loop.  
    **Exact fix:** Strip the final sentence beginning `This claim — that war is a social process…`.

12. **Location:** `frozen-deep.md:67`  
    **Class:** `external-framing`  
    **Evidence:** The source discusses fear, courage, leadership, cohesion, esprit and peer trust (tape 476–517). It does not rank this as the chapter’s “most direct treatment” or call cohesion an “operational mechanism.”  
    **Exact fix:** Replace `The passage on fear is the chapter's most direct treatment of the moral dimension:` with `The section states:`. Replace the final sentence with:

    > The section directs leaders to develop unit cohesion, esprit and individual self-confidence, and says respect and trust among peers can help overcome personal fear. [AP]

13. **Location:** `frozen-deep.md:87`  
    **Class:** `external-framing`  
    **Evidence:** The source contrasts attrition and manoeuvre at length (tape 1032–1138), but does not rank the section as “load-bearing.”  
    **Exact fix:** Strip `The chapter's load-bearing section.`

14. **Location:** `frozen-deep.md:111`  
    **Class:** `external-framing`  
    **Evidence:** The source pairs leniency for mistakes from overboldness with severity for inaction or timidity (tape 1592–1614). It does not call the passage “load-bearing” or explicitly state that this pairing is the institutional mechanism supporting Ch 4’s mission-tactics philosophy.  
    **Exact fix:** Replace `The trust-and-initiative passage is the chapter's load-bearing section:` with `The section states:`. Replace the final sentence with:

    > The text pairs leniency for errors stemming from overboldness with severity for errors of inaction or timidity. [AP]

## 3. Count

**Claims checked: 297 claim units.**

Counting rule:

- Each evidence-marked statement or quotation cluster closed by one marker counted as one unit: 239 total (`204 [V]`, `3 [AP]`, `8 [AR]`, `1 [AE]`, `23 [BT]`).
- Each remaining unmarked claim-bearing paragraph, list row or metadata field in the deep reference counted as one unit: 38.
- Each source-card frontmatter field or claim-bearing body paragraph counted as one unit: 20.
- Headings and blank lines were excluded. Coordinated subclaims inside a unit were all traced even though the unit counted once.

| Class | Defects |
|---|---:|
| unsupported | 0 |
| marker | 1 |
| quote | 0 |
| quantity-qualifier | 1 |
| overbroad | 0 |
| coverage | 3 |
| cross-reference | 1 |
| task-guidance | 0 |
| post-source-vocabulary | 0 |
| external-framing | 5 |
| provenance | 3 |
| **Total** | **14** |

**Key-statistics table:** none exists. That is appropriate for this doctrinal source. The Napoleon “three to one” maxim is quoted-through material, not an empirical key statistic, and matches tape 2755–2757.

**Author-stated limitations:** there is no standalone limitations list. The deep accurately preserves the source’s principal bounds and qualifications: no specific techniques or procedures; doctrine is authoritative but not prescriptive; manoeuvre and attrition always occur in some mixture; speed is not always the limiting factor; and technology cannot eliminate the human dimension. No limitations-list defect was counted.

## 4. Over-flag guard

- The automated verbatim check reported 29 candidates, but none warranted a `quote` finding. Most were page headers inside otherwise contiguous passages, permitted ellipses, omitted footnote markers, open/closed dash typography or OCR damage.
- `uncertainty` at deep line 41, `if eliminated` at line 97, the “yes-men” punctuation at line 113 and `and discuss them` at line 115 were checked visually against the original. The deep repairs the OCR correctly.
- The initial-capitalisation difference in “the truly decisive element…” at line 85 is the permitted mid-sentence quotation case.
- The count of 15 Clausewitz notes was verified: five in Ch 1, nine in Ch 2 and one in Ch 3.
- The two figure descriptions at deep line 232 match the rendered originals: Figure 1 shows limited overlap among the three levels; Figure 2 shows the levels compressed with substantial overlap.
- `~100 pages` was not flagged: the PDF has 115 physical pages, including front matter, while the publication’s printed pagination reaches 106.
- Source-card line 29 was not treated as grounded evidence; it is an internal corpus-state note. Line 31 was considered for `cross-reference` but not counted because it is explicitly labelled a corpus companion-volume pointer rather than a claim that MCDP 1 cites Coram.
- The acquisition date, Wayback note, conversion version and quotation-check date were treated as operational provenance metadata. The available page count, hashes and installed `pdftotext` version were consistent except for the generic checksum field reported in Finding 3.

## Sol brief

# Cross-family Pass I (blind leg): MCDP 1: Warfighting deep reference

You are the cross-family auditor for a deep reference written by another model. This audit is one of ten in a random sample, run to measure how often the library's older deep references carry defects. Nothing else is being audited alongside it. Audit blind.

## Files (all in this folder)

- `frozen-deep.md`: the deep reference under audit, frozen before any edits (sha256 in `frozen-deep.sha256`).
- `tape.md`: the full converted source. Converted text on disk, 3041 lines; read all of it.
- `source.pdf`: the original, for provenance checks (title, authors, date, version) and for any table, figure or chart whose values the tape can't carry cleanly.

- `source-card.md` (if present): the ingesting agent's sidecar. Audit its provenance claims too.
- `pass-i-spec.md`: the audit standard, including the fail conditions and the source-external framing list.
- `fixtures/`: three calibration exemplars. Read these before the deep reference.

## Task

Read the three fixtures, then `pass-i-spec.md`, then `frozen-deep.md` cold. Trace every claim (prose, table cell, evidence marker, blockquote, cross-reference, thesis paragraph, statistics row, "positions the author frames against", source-integrity notes) to a passage in `tape.md` or the original.

Report every defect, labelled with one of these classes:
- `unsupported`: a claim with no source passage;
- `marker`: a wrong evidence marker (`[V]` without exact verbatim text, `[AP]` without author content, and so on);
- `quote`: a blockquote or quoted string that doesn't match the tape character for character, other than smart-quote normalisation (say which);
- `quantity-qualifier`: a changed quantity, sample size, sign or significance level, or a dropped hedge or qualifier (for an empirical source, check every number in the deep reference against the tape);
- `overbroad`: a finding stated more broadly than the source's setting or identification supports;
- `coverage`: a section of the source missing from the coverage, or a coverage statement that overstates what was read;
- `cross-reference`: a cross-reference to an author or work the source doesn't cite;
- `task-guidance`: task-application guidance in the deep tier;
- `post-source-vocabulary`: vocabulary the source doesn't use, presented as the source's;
- `external-framing`: source-external analytical framing (evaluative labels, plausibility judgements, methodological verdicts, invented oppositions, causal explanation the source doesn't give);
- `provenance`: a wrong title, author, edition, date, licence or other card fact.

The test is "which passage says it?", not "is it true?".

Three things are not defects, so don't count them:
- **OCR repair.** Where the tape has OCR damage ("jour" for "your", "leam" for "learn", "tw^o", a broken word) and the deep quotes the word the original actually prints, the deep is right. Check the original when in doubt; flag only where the deep changes a word the original prints.
- **Conversion markup.** Pandoc writes an em dash as `---` and an en dash as `--`, and adds anchors like `[]{#id}`; a deep that renders the dash or drops the anchor matches the source.
- **Quoted-through material marked `[V]`.** If the deep marks a saying the author quotes from someone else (Dogen, a sutra, another writer) as `[V]` while naming that speaker, report it once as a single `marker` finding listing the lines, not as one finding per line.

Also say whether the deep reference's key-statistics table (if any) matches the tape, and whether its list of the source's limitations matches what the authors themselves state.

## Output

1. What you read in full and in part. If you could not read the tape in full, say exactly which parts you read.
2. Findings, numbered. For each: the deep reference line, the class, the evidence (tape line or page), and the exact fix: the replacement text, or "strip".
3. A count: claims checked (say what you counted as one claim), and defects by class.
4. Over-flag guard: list anything you considered flagging but judged clean, with the reason. Over-flagging is as costly as missing a defect.

Don't edit any file.

## Re-derivation (2026-10-12)

Deep: two quotations extended during re-derivation, each a verbatim match to the source: mission tactics *"benefits the senior commander by freeing time to focus on higher-level concerns rather than the details of subordinate execution"*; the main-effort passage's *"It becomes clear to all other units in the command that they must support that unit in the accomplishment of its mission."* The coverage header now agrees with the coverage note (the cover, signatures and figures were read from the original PDF).

Derived tier re-derived and stamped: the light reference (author as printed; Gray's and Krulak's statements as intents; licence unverified, quoting Distribution Statement A and the imprint; the three added sections); the five demo distillations (aar, decision-making, retro, software-business, stakeholder-engagement): licence claims replaced by both notices, Boyd's decision-cycle argument attributed to Boyd, ranking and "load-bearing" labels removed, and evidence notes corrected to the current conversion's line numbers and OCR repairs. Every MCDP 1 `[V]` quotation in the five files was checked against the converted source. Each axis index's per-source entry follows. `LICENSE-CONTENT` quotes both notices in place of the public-domain claim.

**Deep after these fixes:** sha256 `2bedae6bcf6897403031342bddadd2fb0e71e3941082928e0d00f4b78ec25b12`.
