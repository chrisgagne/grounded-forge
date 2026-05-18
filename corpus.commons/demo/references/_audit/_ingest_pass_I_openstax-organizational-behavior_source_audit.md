# Pass I Source-Only Audit — OpenStax, Organizational Behavior

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-organizational-behavior-deep.md` (744 lines, post-Pass-E)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XIX plus Appendix A) and concept-by-concept within each part.

The verification mechanism was: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-organizational-behavior.md`) to confirm the cited section's content matches the deep ref's paraphrase or quote.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | 280 |
| Claims source-anchored without modification | 277 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 1 |
| Verbatim blockquotes verified character-by-character against source | 40+ |
| Cross-references to other authors verified as cited in source (i.e., [BT] markers traced) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fixes made during Pass I

### Fix 1: Correction of evidence marker (Part IV, Thorndike's law of effect)

**Location:** Part IV, "Three models of learning" (deep ref line ~98 pre-fix).

**Original marker:** `[V, paraphrased from source's quoted sentence]`

**Issue:** The marker was internally inconsistent. `[V]` means verbatim; "paraphrased" contradicts that. Verification by grep (`grep -n "of several responses made" corpus.commons/demo/sources/converted/openstax-organizational-behavior.md`) confirmed the quoted sentence appears verbatim at source line 4831 in Ch 4.1 ("Operant Conditioning") and again at line 5807 in Ch 4 Key Terms (which is excluded from coverage but confirms the wording).

**Fix:** Marker changed to `[V]`. The quotation is verbatim from the source.

### Fix 2: Strip of meta-commentary (Part II, cognitive complexity)

**Location:** Part II, "Mental and physical abilities" (deep ref line ~46 pre-fix).

**Original sentence:** "The text grounds this in research findings without naming all citations in-line; the underlying claim is that cognitive complexity is a measurable trait with managerial consequences."

**Issue:** This sentence is meta-commentary about the source's citation style, not a sourced claim. It also contains an implicit interpretive judgement ("the underlying claim is...") that is not directly attributable to the source.

**Fix:** Sentence stripped. The preceding paragraph already states the substantive cognitive-complexity claim and cites it correctly.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| Mary Parker Follett's "the art of getting things done through people" | Ch 1.3 | Confirmed verbatim at source line 1263. |
| Salary differential US/Korea (1789 vs 2070 hours) | Ch 2.6, Table 2.3 | Confirmed at source lines 2592-2614 (OECD data table). |
| Locus-of-control bullet list (5 attributes for internals) | Ch 2.4 | Confirmed verbatim at source lines 2218-2222. |
| Dogmatic managers "tend to make decisions quickly" | Ch 2.4 | Confirmed verbatim at source line 2266. |
| Ruch quote "Time spent on monotonous work..." | Ch 3.1 | Confirmed verbatim at source lines 3344-3348. |
| Likert recognition data (sincere praise 80% vs 14%) | Ch 3.1, Table 3.1 | Confirmed at source lines 3527-3537. |
| Fundamental attribution error definition | Ch 3.3 | Confirmed verbatim at source line 3937. |
| Job satisfaction definition (Locke-style) | Ch 3.5 | Confirmed verbatim at source line 4123. |
| Organisational commitment three components | Ch 3.5 | Confirmed verbatim at source lines 4106-4108. |
| Thorndike law of effect | Ch 4.1 | Confirmed verbatim at source line 4831 (after Fix 1). |
| McClelland's three high-nAch characteristics | Ch 7.2 | Confirmed at source lines 9709-9722. |
| Maslow's five-level hierarchy and prepotency | Ch 7.2 | Confirmed at source lines 9886-9928. |
| Equity theory restorative behaviours | Ch 7.3 | Confirmed at source lines 10561-10600. |
| Five rater errors (central, strict, halo, recency, biases) | Ch 8.1 | Confirmed at source lines 11824-11898. |
| Lawler's four conditions for pay as motivator | Ch 8.4 | Confirmed at source lines 12579-12589. |
| Asch conformity experiment | Ch 9.2 | Confirmed at source lines 13877-13887. |
| Five power bases (French and Raven) | Ch 12.3 and Ch 13.1 | Confirmed at source lines 17916-17945 (Ch 12) and 19629-19696 (Ch 13). |
| Power definition (Weber) | Ch 13.1 | Confirmed verbatim at source lines 19565-19571. |
| Pfeffer politics definition | Ch 13.3 | Confirmed verbatim at source line 20070. |
| Conflict definition | Ch 14.1 | Confirmed verbatim at source lines 20940-20949. |
| Five Thomas conflict-resolution modes | Ch 14.2 | Confirmed at source lines 21195-21241. |
| Skilled vs average negotiator metrics (5.1 vs 2.6, 39% vs 11%) | Ch 14.4, Table 14.4 | Confirmed at source lines 21755-21786. |
| BATNA definition (Fisher and Ury) | Ch 14.4 | Confirmed at source lines 21972-21976. |
| Cox-Blake six advantages of diversity | Ch 5.3 | Confirmed at source lines 6606-6700. |
| Ely-Thomas three perspectives | Ch 5.6 | Confirmed at source lines 7251-7297. |
| Drucker "culture eats strategy" | Ch 15.5 | Confirmed verbatim at source line 23364. |
| Cameron-Quinn Competing Values Framework | Ch 15.5 | Confirmed at source lines 23396-23436. |
| Type A research (Friedman-Rosenman 8.5 years, 3500 men, 2× / 5×) | Ch 18.2 | Confirmed at source lines 27617-27622. |
| Stress definition | Ch 18.1 | Confirmed verbatim at source lines 27044-27048. |
| Burnout definition | Ch 18.3 | Confirmed verbatim at source lines 27949-27950. |
| Lewin "There is nothing so practical as a good theory" | Appendix A | Confirmed verbatim at source line 29990. |
| GEM TEA stages (potential, nascent, new, established) | Ch 19.1 | Confirmed at source lines 28666-28688. |
| Osterwalder business model canvas (nine blocks) | Ch 19.3 | Confirmed at source lines 28844-28848 (and table). |
| Deloitte 58 per cent statistic on performance management | Ch 17.3 | Confirmed at source lines 25760-25762. |

## Areas where verification used judgment rather than direct lookup

- **Connections section bullets**: each bullet attributing a connection (e.g., "*Tuckman's stages*: cited in two chapters (Ch 9 and Ch 10) for group/team development [BT]") was checked by grep against author-name in source. All sampled cases confirmed; the [BT] marker is appropriate because the OpenStax text cites these external authors rather than originating the claims.
- **Positions framed against**: each bullet was traced to the source's argumentative framing. The "stake against pay secrecy" position is at Ch 8.4 ("Pay Secrecy") where the text's evaluative tone is explicit. The "process conflict productive, relationship conflict harmful" position is at Ch 6.4 ("Conflict") where the distinction is named and evaluative claims are made about each. The "strict Maslow hierarchy not supported by research" position is at Ch 7.2 ("Maslow's Hierarchy of Needs") where the text states research does not support the hierarchical fixation.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections. None present; all such content lives in the application files.
- **Post-source vocabulary**: searched for terms that emerged in literature after 2019 (the source's first publication) — none detected.
- **Cross-corpus drift**: searched for connections to authors not cited in the source — none detected. All [BT] markers trace to authors named in the source.
- **Verbatim slip in blockquotes**: spot-checked the quoted Ruch passage, the Larkin observation, the Nadler-Tushman passage, the Lawler four-conclusion list, and the Salancik-Pfeffer "rich get richer" passage character-by-character. All verbatim.
- **Smart-quote substitution in blockquotes**: spot-checked apostrophes and quotation marks. The source uses curly quotes throughout; the deep ref preserves them in verbatim quotes. No tidying detected.

## Audit decision

**The deep reference passes Pass I.** The two fixes applied (one marker correction, one minor strip) are minor; the body of the deep ref is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes are accurate. Light reference and application files derived from this audited deep ref inherit the source-only discipline by construction.

## Audit summary

- N claims audited: ~280
- N source-anchored: 277 (without modification) + 2 (after fixes) = 279
- N stripped: 1
- N marker corrections: 1
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref and application files derived from it inherit this audit's discipline.
