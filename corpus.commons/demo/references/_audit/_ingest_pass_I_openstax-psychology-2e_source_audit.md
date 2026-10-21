# Pass I Source-Only Audit — OpenStax, Psychology 2e

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-psychology-2e-deep.md` (505 lines, post-Pass-E; this audit produced 2 Pass-I fixes that are now in the deep ref).

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I–XV plus the Key Statistics, Connections, Positions Framed Against, and Citation/Source-Integrity Notes sections) and concept-by-concept within each part.

The verification mechanism was: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-psychology-2e.md`) to confirm the cited section's content matches the deep ref's paraphrase or quote.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | 190 |
| Claims source-anchored without modification | 188 |
| Claims requiring marker correction | 1 |
| Claims requiring strip / rewrite (no source support / corruption) | 1 |
| Verbatim claims (inline `[V]` markers, no `> "..."` blockquote format) verified by grep | 25+ |
| Cross-references to other authors verified as cited in source ([BT] markers traced) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fixes made during Pass I

### Fix 1: Correction of corrupted Key-statistics row (Buss 1989)

**Location:** Key statistics table (deep ref line 437 pre-fix).

**Original row:**

```
| Number of monkeys' first words across 37 cultures (Buss 1989) | women valued earning potential, men valued youth and attractiveness across all 37 | [BT] (Ch 1.3) |
```

**Issue:** The metric column ("Number of monkeys' first words across 37 cultures") is a corruption — there is no claim about monkeys' first words anywhere in *Psychology 2e*. The actual content (women valued earning potential, men valued youth and attractiveness across 37 cultures, citing Buss 1989) is supported by the source at line 1569 ("spanned 37 cultures, Buss (1989) found that women valued earning potential factors greater than men..."). The row label is unsalvageable as written; the value column content is correct.

**Fix:**

```
| Buss (1989) cross-cultural mate-preference study | Across 37 cultures, women valued earning potential more than men; men valued youth and physical attractiveness more than women | [BT] (Ch 1.3) |
```

**Verification:** grep confirmed the substantive claim at source line 1569; Buss (1989) reference confirmed at source line 35781 ("Buss, D. M. (1989). Sex differences in human mate preferences: Evolutionary hypotheses tested in 37 cultures."). [BT] (borrowed-through) marker is correct because OpenStax is citing Buss rather than originating the claim.

### Fix 2: Marker correction for object-permanence row

**Location:** Key statistics table (deep ref line 438 pre-fix; line 438 post-Fix-1).

**Original row:**

```
| Children with object permanence | develops between 5 and 8 months | [V] (Ch 9.2) |
```

**Issue:** The [V] marker indicates verbatim. The source at line 16540 says "Between 5 and 8 months old, the child develops object permanence" — close but not identical to the deep ref's "develops between 5 and 8 months". The deep ref's wording is a structurally rephrased paraphrase, not verbatim. Also, the row label "Children with object permanence" is awkward (it suggests a percentage rather than an age range).

**Fix:**

```
| Object permanence development | develops between 5 and 8 months | [AP] (Ch 9.2) |
```

**Verification:** grep confirmed the source claim at line 16540 in Ch 9.2 ("Stage theories"). [AP] (author paraphrase) marker is now correct.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| Asch 76% conformity | Ch 12.4 | Confirmed at source line 23557–23558. |
| Milgram 65% maximum-voltage | Ch 12.4 | Confirmed at source lines 23685–23710 area; standard citation in Ch 12.4 narrative. |
| Buss (1989) 37 cultures | Ch 1.3 | Confirmed at source line 1569; reference at 35781. |
| Chandola 68% job-strain heart-disease risk for under-50s | Ch 14.2 | Confirmed at source lines 28130–28131. |
| Holt-Lunstad 50% greater survival likelihood | Ch 14.4 | Source supports the claim (sample-confirmed in surrounding text on social-support meta-analysis); deep ref's framing is consistent. |
| Kahneman-Deaton happiness plateau ~$75,000 | Ch 14.5 | Source confirms in Ch 14.5 happiness narrative. |
| Obesity ~40% US adults, ~75% overweight (CDC 2018) | Ch 10.2 | Confirmed at source line 18972. |
| Forgetting curve ~50% / 20 min, ~70% / 24 hr (Ebbinghaus) | Ch 8.3 | Source confirms Ebbinghaus 1885 forgetting-curve content in Ch 8.3 errors-and-distortions section. |
| Working memory 7±2 (Miller); 4±1 (Cowan revision) | Ch 8.1 | Source confirms in Ch 8.1 short-term memory section. |
| Schizophrenia ~1% lifetime prevalence | Ch 15.8 | Source confirms (claim is in the Ch 15 disorders content, which is in the deep ref despite being excluded from application projection). |
| IQ mean 100, SD 15; 68% within ±1 SD; 2.2% below 70 | Ch 7.5 | Source confirms in Ch 7.5 IQ-measurement section. |
| Pavlov "lock-and-key relationship" | Ch 3.2 | Verbatim phrase confirmed by grep against source (neurotransmitter binding section). |
| Maslow criticism: "subjective nature and... inability to account for phenomena" | Ch 10.1 | Source confirms the critical framing in Ch 10.1 motivation section. |
| Fundamental attribution error: "much more common in individualistic cultures" | Ch 12.1 | Source confirms the cultural-comparative claim in Ch 12.1. |
| Tienari et al. (2004) adoption study of schizophrenia | Ch 3.1 | Source cites Tienari in genetics-environment-interaction section. |
| Loftus & Palmer (1974) misinformation effect "smashed" vs "contacted" | Ch 8.3 | Source confirms classic study in Ch 8.3. |
| Ross, Amabile, Steinmetz (1977) quizmaster study | Ch 12.1 | Source confirms in Ch 12.1 attribution section. |
| Ekman universal facial expressions in pre-literate New Guinea | Ch 10.4 | Source confirms in Ch 10.4 emotion-and-culture section. |
| Hawthorne effect verbatim definition | Ch 13.1 | Source line confirmed; deep ref's verbatim quote is exact. |
| Lillian Gilbreth "the mother of modern management" | Ch 13.1 | Source confirms phrase in Ch 13.1 history section. |
| Six historical schools of psychology | Ch 1.2 | Source confirms structuralism, functionalism, psychoanalytic, Gestalt, behaviourism, humanism in Ch 1.2. |

## Areas where verification used judgment rather than direct lookup

- **"Connections the authors make in the text" bullets**: Each bullet attributing a borrowed-through connection (e.g., "Pavlov, Watson, Skinner, Bandura — the behaviorist-to-social-cognitive lineage shapes Ch 6 (learning) and Ch 11.4 (personality) [BT]") was checked by grep against author names in source. All sampled cases confirmed; the [BT] marker is appropriate because the OpenStax text cites these external authors rather than originating the claims.
- **"Positions framed against" bullets**: Each bullet was traced to source's argumentative framing. The "punishment" position is at Ch 6.3, "FAE" at Ch 12.1, "Maslow critique" at Ch 10.1, "Freud psychosexual" at Ch 9.2, "Theory X" at Ch 13.3, "vaccines and autism" at Ch 15.10, "conversion therapy" at Ch 10.3, "BMI as clinical measure" at Ch 10.2, "polygraph" at Ch 10.4. Sampled positions confirmed.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections. None present; all such content lives in the application files (Pass G output).
- **Post-source vocabulary**: the source was first-edition published in 2014, second edition in 2020. Searched for terms that emerged after the second edition (post-2020 frameworks for evolved-cognition, post-2020 DSM revisions). None detected.
- **Cross-corpus drift**: searched for connections to authors not cited in the source. None detected. All [BT] markers trace to authors named in the source.
- **Verbatim slip in inline `[V]` quotes**: spot-checked the Pavlov "lock-and-key", Asch 76%, Maslow criticism, Hawthorne effect definition, and Cohen et al. cold-susceptibility framing. All confirmed verbatim where [V] is marked. (One [V] was downgraded to [AP] in Fix 2 above where the wording was structurally rephrased even though substantive words overlapped.)
- **Smart-quote substitution in inline quotes**: spot-checked apostrophes and quotation marks. Source uses straight ASCII quotes throughout; deep ref preserves them in verbatim quotes. No tidying detected.
- **No `> "..."` blockquote format**: this deep ref's verbatim citations are inline rather than blockquoted. This is an acceptable format choice consistent with Pass D's "Direct quotation appears in standard quotation marks at this stage" framing in the protocol; the [V] marker travels with each.

## Audit decision

**The deep reference passes Pass I.** The two fixes applied (one row-label correction, one marker correction) are minor; the body of the deep ref is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes (inline) are accurate. Light reference and application files derived from this audited deep ref inherit the source-only discipline by construction.

## Audit summary

- N claims audited: ~190
- N source-anchored without modification: 188
- N source-anchored after fix: 188 + 2 = 190
- N stripped: 0
- N rewritten / corrected: 2 (1 row-label correction in Key Statistics; 1 marker downgrade [V] → [AP])
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref and application files derived from it inherit this audit's discipline.

## Note on Application-projection scope

The deep ref describes content from Chapters 15 (Psychological Disorders) and 16 (Therapy and Treatment). Pass I confirms that this content is **source-anchored** — the deep ref's coverage of these chapters is faithful to the source. However, per the spawn-prompt directive and the deep ref's Application-projection note, this content is **not projected** into the decision-making or stakeholder-engagement application files. The audit verified that:

- The application files (Pass G output) contain no clinical-disorder framings.
- The application files contain no therapist-client framings.
- The application files name the scope constraint explicitly in their relevance section.

The exclusion of clinical content from application projection is a deliberate scope choice (stated in the spawn prompt and in the deep ref), not a Pass-I source-integrity finding. The clinical content remains in the deep ref because Pass C's coverage rule is "read in full"; the constraint is on which Pass G axes the content gets projected into, not on which content the deep ref covers.

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** same-family (a fresh Claude agent, cold context). No cross-family leg was run, so this scope is audited-but-unverified.

**Scope.** Only the text the 2026-10-16 re-conversion restored (2,288 words in 40 runs, `sources/converted/openstax-psychology-2e.md`) and the deep-reference text written for it on 2026-10-17: lines 9, 59, 67 (added clauses only), 101, 121, 150, 186, 254, 357, 405, 417, 441, 445 and 522 of `references/openstax-psychology-2e-deep.md`. Each new paragraph's whole box was read in the tape, including the parts the old conversion already held (Medical Marijuana and Prader-Willi continuations, the Learned Helplessness reformulation paragraphs). Box labels were confirmed from the PDF's text layer (no page renders used): every paragraph's Dig Deeper / Everyday Connection label matches the PDF. The Learned Helplessness reformulation paragraphs (Peterson & Seligman) sit inside the box's shaded frame on PDF p. 526, so the paragraph's attribution of them to the box is correct. The Henner box's "Everyday Connection" label is in the PDF but absent from the tape.

**Verbatim check.** `scripts/check-verbatim.py` before and after: 11 apostrophe, 10 initial, 1 interrupted (baseline, unchanged). All nine new `[V]` quotations match the tape.

**Counts.** Claims audited: 52. Source-anchored without change: 43. Corrected: 9 (6 claim wording, 2 marker, 1 Coverage line). Stripped: 0. Quotation-corrected: 0. No text was added beyond the corrections below.

**Changes (line: reason).**

1. Line 9, Coverage: said restored "body and table text" was folded into existing paragraphs and listed "equation numbers and figure credits" as excluded scaffolding. The 40 runs are eleven feature boxes, Table 15.3 (given its own paragraph), and otherwise box labels, running headers, the front-matter promotion and index page headers; no body text, equations or figure credits. Rewritten to say so.
2. Line 59, vaccine-autism box: "the retraction followed a significant conflict of interest" weakened the tape's causal "the retraction was made because of"; now matches.
3. Line 121, behaviour modification box: "with the caregiver calm throughout" overstated "remain calm when directing your child to time-out"; corrected.
4. Line 150, Solving Puzzles box: "'Puzzling Scales' logic puzzle by puzzle master Sam Loyd" asserted authorship the tape only implies by juxtaposition (it introduces the puzzle, then says Loyd "created and refined countless puzzles", cited to Cyclopedia of Puzzles). Rewritten to report the juxtaposition, with `[BT, Cyclopedia of Puzzles]` added.
5. Line 357, federal job satisfaction box: bare `[BT]` on the 2013 study; the tape cites no source for it. Marker changed to `[AP]`.
6. Line 405, social status box: "lower status brings stress and poor health through lack of control … and resource inequality" turned the tape's "Some factors … include" into a complete account; corrected to "include".
7. Line 417, learned helplessness box: "dogs … later failed even to try" dropped the tape's "most"; restored.
8. Line 441, Dancing Mania box: spider venom and ergot poisoning are cited in the tape to ("Dancing Mania," 2011), not Waller; marker now `[BT, Waller; "Dancing Mania," 2011]`.
9. Line 445, Table 15.3: "more likely in one sex than the other" replaced the table's gender framing ("Gender Differences", men / women); reworded in the table's terms.

**Known item: the two retraction accounts.** The book gives two reasons for the vaccine-autism retraction. Ch 2.3's Dig Deeper box: "the retraction was made because of a significant conflict of interest in which the leading researcher had a financial interest in establishing a link" (Offit, 2008). Ch 15.10, "Child Vaccinations and Autism Spectrum Disorder": the article "was retracted by the journal that had published it after evidence surfaced indicating fraud and unethical practices on the part of the lead researcher". Both deep-ref lines report their own passage correctly (line 59 for Ch 2.3; line 443 for Ch 15.10), so neither was changed. The tension is the book's own, and the deep reference doesn't currently point it out.

**Checks with no finding.** Placement: every paragraph sits in the Part and section its box belongs to (Ch 2.3, 2.4, 4.5, 6.3, 7.3, 8.1, 10.2, 13.3, 14.3, 14.4, 15.3, 15.11), with section-name citations. No outside facts or added framing found beyond the items above. Line 522 (integrity note on the word-diff method) matches the run list.

**Open.**

- Part XIV heading (line 427) reads "overview only; spawn-prompt directive excludes clinical content from distillation projection". The two Ch 15 additions are consistent with that note's projection exclusion and with the Coverage line (every chapter read). The Table 15.3 paragraph, though, lists all sixteen behaviours, which is item-level detail under an "overview only" heading. Not a fidelity defect; the parent may want to shorten it to keep Part XIV's depth even.
- Line 67 keeps "profound ethical failure" from the pre-existing sentence (outside this scope's added clauses). The tape's box says only that the guidelines "were not always applied in the past" and asks "Why is this study unethical?". This is an evaluative label for the full audit to weigh.
- Line 67: the 1972 press discovery is cited in the tape to (Tuskegee University, n.d.); the deep ref carries no `[BT]` for it. Left as is, since the sentence's load is the `[V]` quotation.

**Derived tier.** Changes 2–9 alter wording the light reference or a distillation may carry, if they quote these paragraphs (most likely the learned helplessness, social status and job satisfaction paragraphs, which fall in Ch 13–14 projection scope). The parent re-derives. Not stamped.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

The PARTIAL notes are gone from the light reference, the distillations and the source card, replaced by a coverage statement that names the single-family audit. The light reference's job-satisfaction summary predates this pass and carries none of the corrected wording; no distillation carries the restored boxes, so no re-derivation is needed. The Table 15.3 paragraph stays as written: it summarises a restored table in a Part the Coverage line covers, and Part XIV's "overview only" note concerns projection into distillations. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
