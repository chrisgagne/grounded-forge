# Pass I Source-Only Audit — Letaw, Handbook of Software Engineering Methods

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-13
**Subject:** `corpus.commons/demo/references/letaw-handbook-sweng-methods-deep.md` (post-Pass-E)

## Audit procedure

The deep reference was read cold against the converted markdown at `corpus.commons/demo/sources/ingest/letaw-sweng-methods.md` (5,159 lines, pre-promotion). For every body claim, table row, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" Where direct quotations appear, the auditor verified them character-by-character via `grep`. Where paraphrases appear, the auditor located the source passage and confirmed the paraphrase faithfully represents it.

Before reading the deep reference, three calibration fixtures were read to anchor the audit:
- `tests/audit-fixtures/01-training-leakage.md` (canonical strip case).
- `tests/audit-fixtures/07-marker-mismatch-V-without-verbatim.md` (canonical marker-correction case).
- `tests/audit-fixtures/12-clean-negative-control.md` (clean snippet that must not be flagged).

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | ~180 |
| Claims source-anchored without modification | ~172 |
| Marker corrections applied ([V] → [AP] where prose was paraphrase) | 4 |
| Verbatim quotes corrected to match source wording exactly | 4 |
| Citation tightening (Glossary citation removed where wording matches body only) | 2 |
| Verbatim blockquotes verified character-by-character against source | 40+ |
| Cross-references to other authors verified as cited in source ([BT] markers traced) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary or training-data leakage detected | 0 |

## Specific fixes made during Pass I

### Fix 1: ISO definition quote — source-faithful wording

**Location:** Author's thesis section.

**Original quote:** `"the systematic application of scientific and technological knowledge, methods, and experience to the design, implementation, testing, and documentation of software"`

**Issue:** Source's Glossary entry (line 4632) reads "**Systematic** application of scientific and technological knowledge..." — sentence-leading capital, no "the". My deep ref added "the" and lowercased "Systematic", breaking verbatim-fidelity for a `[V]`-marked quote.

**Fix:** Replaced with the exact Glossary wording in quotation marks; clarified that the Introduction announces the ISO definition while the Glossary carries the full definition body. Citation tightened to `(Glossary, "software engineering")`. Also added the verbatim Introduction sentence noting which standards bodies agreed the definition.

### Fix 2: Sustainable/extensible quote — restore "it's"

**Location:** Author's thesis section.

**Original quote:** `"feasible for the program to grow, exist, and be maintained" and "feasible to add more features"`

**Issue:** Source (Introduction, "What's the Purpose of Software Engineering?") says "Sustainable means it's feasible for the program to grow, exist, and be maintained. Extensible means it's feasible to add more features." My deep ref dropped the "it's" prefix from both quoted segments.

**Fix:** Restored verbatim wording: `"Sustainable means it's feasible for the program to grow, exist, and be maintained"` and `"Extensible means it's feasible to add more features"`.

### Fix 3: Risk-reduction quote at Chapter 2 head

**Location:** Author's thesis section, third load-bearing claim paragraph.

**Original prose (pre-fix):** `defining and tracking the project, communicating with the team, researching the implications of decisions, developing backup plans, selecting suitable tools` followed by `[V]`.

**Issue:** Source (Ch 2, opening) says "**defining and keeping track of your project, communicating** with your project team, **researching the implications** of decisions, **developing backup plans**, and selecting **suitable tools**." My deep ref paraphrased ("tracking" instead of "keeping track of", drops "your", drops "and") but kept `[V]`.

**Fix:** Replaced paraphrase with verbatim quote: `"defining and keeping track of your project, communicating with your project team, researching the implications of decisions, developing backup plans, and selecting suitable tools"`. Kept `[V]`.

### Fix 4: Fist-of-five risk-reduction quote — restore "can"

**Location:** Part II, "Interpersonal skills" subsection.

**Original quote:** `"reduces risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment"`

**Issue:** Source (Ch 2.4.3) says "can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment." My deep ref dropped "can" and converted "reduce" to "reduces".

**Fix:** Restored verbatim: `"can reduce risk by (1) bringing problems to light and (2) increasing team motivation, ownership, and investment"`.

### Fix 5: SDLC five-stage list — marker correction

**Location:** Part I, "The SDLC and software process models" subsection.

**Original marker:** `[V]` covering both the quoted opening phrase and the parenthetical paraphrases of the five stages.

**Issue:** The opening phrase `"the progression of a software project through five SDLC stages"` is verbatim, but the parenthetical descriptions of the five stages (Requirements, Design, Implementation, Testing, Maintenance) are paraphrases of the source's bullet content (lowercased, parenthesised), not verbatim.

**Fix:** Split the marker: `[V]` follows the opening quoted phrase; `[AP]` follows the parenthetical paraphrase list.

### Fix 6: Gray-area sentence — marker correction

**Location:** Author's thesis section, second paragraph (organising claim).

**Original marker:** `[V]` at end of a sentence containing multiple verbatim quoted phrases connected by paraphrased prose.

**Issue:** The sentence is a hybrid: verbatim phrases (`"a gray area of computer science"`, `"Is this algorithm correct?"`, etc.) embedded in paraphrased connective tissue. Pure `[V]` mis-represents the structure.

**Fix:** Changed to `[AP] [V]` to flag both the dominant paraphrase and the embedded verbatim phrases.

### Fix 7: WinGui Gateway quote — restore source phrasing

**Location:** Part V, "Case study: ODOT TOCS migration" subsection.

**Original quote:** `"prepares data from the services"`

**Issue:** Source (Ch 5.5) says "The WinGui Gateway application is responsible for preparing data from the services so it can be used by the New Home Screen UI." My deep ref's `"prepares"` was not in the source.

**Fix:** Replaced with the full source phrase in quotes: `"responsible for preparing data from the services so it can be used by the New Home Screen UI"`.

### Fix 8: Function with Many Parameters — restore "As appropriate,"

**Location:** Part VIII, "Code smells about functions" subsection.

**Original quote:** `"Pass an object that combines the parameters, make calls within the function to get the parameter data, break into multiple functions, or find another way of reducing the number of parameters."`

**Issue:** Source (Ch 8.4.1) says "As appropriate, pass an object..." with capitalised "As" leading the sentence. My deep ref dropped the leading phrase and capitalised "Pass".

**Fix:** Restored full source wording in the quote.

### Fix 9: Heuristic #3 quote — restore gerund form

**Location:** Part VII, "The eight heuristics" subsection.

**Original quote:** `"diligently gather and thoroughly review relevant information before acting"`

**Issue:** Source (Ch 7.3.3) says "Abi and Pat **approach decision-making** by **diligently gathering and thoroughly reviewing** relevant information before acting." My deep ref converted "gathering"/"reviewing" (gerunds) to "gather"/"review".

**Fix:** Restored source's gerund form: `"approach decision-making by diligently gathering and thoroughly reviewing relevant information before acting"`.

### Fix 10: RACI quote — preserve source typo

**Location:** Part II, "Interpersonal skills: team communication" subsection.

**Original quote:** `"that can increase the probability of negative events and outcomes"`

**Issue:** Source (Ch 2.4.2) actually contains a typo: "that can increase the probability of **a** negative events and outcomes". My deep ref silently corrected the typo by dropping "a".

**Fix:** Per Pass D rule, verbatim means verbatim — restored "a negative events and outcomes" with the source's "a" intact.

### Fix 11: "Three example formats" sentence — marker correction

**Location:** Part III, "Functional requirements: three formats and user stories" subsection.

**Original marker:** `[V]` after the lead-in sentence, which is paraphrase (the verbatim quotes follow in parenthetical examples).

**Fix:** Changed lead-in marker to `[AP]`; trailing `[V]` for the given-when-then explanation is unchanged.

### Fix 12: Waterfall-as-default position-against — fix bracketed insertion

**Location:** "Positions the author explicitly frames against" section.

**Original quote:** `"often associate[d] . . . with an article that describes Waterfall's major flaws"`

**Issue:** Source (Ch 1.1) says "Ironically, people often **associate** Waterfall with an article that describes Waterfall's major flaws." The bracketed `[d]` in my deep ref changed the source's present-tense verb to past-tense, misrepresenting the source.

**Fix:** Replaced with verbatim: `"Ironically, people often associate Waterfall with an article that describes Waterfall's major flaws"`.

### Fix 13: Three reasons to learn project management — marker correction

**Location:** Part II, "Project management and the triple constraint" subsection.

**Original marker:** `[V]` at end of a sentence with no quoted phrases — all paraphrase.

**Fix:** Changed to `[AP]`.

### Fix 14: Tuckman five stages — marker correction

**Location:** Part II, "Interpersonal skills: team communication" subsection.

**Original marker:** `[V] [BT]` at end of paragraph paraphrasing each Tuckman stage in parentheticals without quotation marks.

**Fix:** Changed to `[AP] [BT]` — the stages are named verbatim by Letaw (and so by my ref), but the stage *descriptions* in my ref are paraphrases, not quotes.

### Fix 15: Managerial Skill Mix definitions — restore verbatim

**Location:** Part II, "Managerial skill mix (MSM)" subsection.

**Original prose:** parenthetical descriptions of Interpersonal/Technical/Administrative-and-conceptual without quotation marks despite carrying `[V]` marker.

**Fix:** Wrapped each category's definition in quotation marks with the source's exact wording (including "your" instead of "the", "e.g.", "etc.").

### Fix 16: Requirements elicitation definition — quote it

**Location:** Part III, "Requirements elicitation" subsection.

**Original:** `*Requirements elicitation* is the process of gathering requirements (Ch 3.4; Glossary) [V].`

**Issue:** Carried `[V]` without quotation marks on "the process of gathering requirements"; that phrase is verbatim from Ch 3.4 ("The process of gathering requirements is called requirements elicitation") so the fix is to quote it.

**Fix:** `*Requirements elicitation* is "the process of gathering requirements" (Ch 3.4, "Requirements Elicitation"; Glossary, "requirements elicitation") [V].`

### Fix 17: Software-requirement definition — citation tightening

**Location:** Part III, "Two main types" subsection.

**Original citation:** `(Ch 3, opening; Glossary)` for the quoted definition.

**Issue:** The Ch 3 opening phrasing differs from the Glossary phrasing. The quote matches Ch 3 opening exactly, not Glossary.

**Fix:** Removed the `; Glossary` part of the citation; left `(Ch 3, opening)`.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| ISO/IEC/IEEE software engineering definition | Glossary, "software engineering" | Confirmed verbatim at source line 4631-4634. |
| "this book is geared toward Agile software development" | Introduction, "Agile Isn't Perfect" | Confirmed verbatim at source line 351. |
| HP 2017 software-process-model distribution (51/24/16/7/2) | Ch 1.2, citing Hewlett Packard Enterprise, 2017 | Confirmed at source lines 639-655. |
| HP 2017 Agile-adoption benefits (54/52/49/43/42) | Ch 1.2 | Confirmed at source lines 658-671. |
| CHAOS Report failure rate 17–22% of 25,000+ projects | Ch 1.1, citing Standish CHAOS Report 2015 | Confirmed at source lines 613-620. |
| Scrum Master accountabilities | Ch 1.2.2 | Confirmed verbatim at source line 693. |
| Product Owner accountabilities | Ch 1.2.2 | Confirmed verbatim at source lines 695-697. |
| Developers definition | Ch 1.2.2 | Confirmed verbatim at source lines 699-701. |
| Sprint definition (one month or less...) | Ch 1.2.2 | Confirmed at source lines 715-717. |
| Daily Scrum 15-minute event | Ch 1.2.2 | Confirmed verbatim at source line 721. |
| Spike definition | Ch 1.2.3 | Confirmed verbatim at source lines 776-778; Glossary line 4651. |
| Triple constraint definition | Ch 2.2 | Confirmed verbatim at source line 844. |
| Risk definition | Ch 2, opening | Confirmed verbatim at source line 849. |
| Managerial Skill Mix three categories (Badawy, 1995) | Ch 2.3 | Confirmed verbatim at source lines 962-974. |
| Fist of five definition | Ch 2.4.3 | Confirmed verbatim at source line 1190. |
| Fist of five encoding (None–Five) | Ch 2.4.3 | Confirmed verbatim at source lines 1200-1210. |
| Project priority matrix (Constrain/Enhance/Accept) | Ch 2.5.2 | Confirmed verbatim at source lines 1255-1259. |
| Eisenhower matrix (Do/Decide/Delegate/Delete) | Ch 2.5.3 | Confirmed verbatim at source lines 1322-1341. |
| Story points and ideal days definitions | Ch 2.5.5, citing Cohn 2006 | Confirmed at source lines 1427-1437. |
| Planning poker process | Ch 2.5.5, citing Cohn 2006 and Mahnič & Hovelja 2012 | Confirmed at source lines 1449-1457. |
| Project network diagram definition | Ch 2.5.6 | Confirmed verbatim at source lines 1465-1469. |
| Activity-on-Node attribution to Larson & Gray 2018 | Ch 2.5.6 | Confirmed at source line 1476. |
| Functional / nonfunctional requirements definitions | Ch 3.1, citing Wiegers & Beatty 2013 | Confirmed verbatim at source lines 1664-1672. |
| "Requirements should be" eight-attribute list | Ch 3.3, citing Texas DIR 2008 | Confirmed verbatim at source lines 1741-1755. |
| Quality attributes catalogue | Ch 3.5.1 | Confirmed verbatim at source lines 1875-1897. |
| INVEST acronym | Ch 3.6.1, citing Wake 2003 | Confirmed verbatim at source lines 2021-2097. |
| Definition of Done | Ch 3.6.1 | Confirmed at source lines 2104-2107. |
| Use case required and additional parts | Ch 3.6.2 | Confirmed verbatim at source lines 2159-2202. |
| UML history (1994, 1997, 2005, v2) | Ch 4.3 | Confirmed verbatim at source lines 2387-2392. |
| Class diagram definition (Fowler 2004) | Ch 4.6 | Confirmed verbatim at source lines 2459-2462. |
| Class-diagram notation conventions | Ch 4.6.1 | Confirmed verbatim at source lines 2491-2550. |
| Sequence diagram definition | Ch 4.7 | Confirmed verbatim at source lines 2583-2585. |
| Sequence-diagram notation conventions | Ch 4.7.1 | Confirmed verbatim at source lines 2614-2664. |
| "UML diagrams are for communicating with humans — not computers" | Ch 4.8 | Confirmed verbatim at source line 2693. |
| Monolith definition | Ch 5.1 | Confirmed verbatim at source lines 2794-2795. |
| Microservices definition | Ch 5.2 | Confirmed verbatim at source lines 2809-2811. |
| Lewis & Fowler component definition | Ch 5.2.2 | Confirmed verbatim at source line 2828. |
| Michell (2011) business capability definition | Ch 5.2.3 | Confirmed verbatim at source lines 2876-2878. |
| Eventual consistency description | Ch 5.2.4 | Confirmed verbatim at source lines 2913-2915. |
| ODOT/CASS TOCS case study facts (.NET 4.8 deprecation, AMQP, JSON for Profile Service) | Ch 5.5 | Confirmed at source lines 3023-3079. |
| Three fidelity levels of UI prototypes | Ch 6, opening, citing Snyder 2011 | Confirmed verbatim at source lines 3133-3173. |
| Paper prototype definition | Ch 6, opening | Confirmed verbatim at source lines 3184-3187. |
| Inclusivity Heuristics definition and inclusive-design citation (Microsoft) | Ch 7, opening | Confirmed verbatim at source lines 3246-3250. |
| Five cognitive facets (Burnett et al., 2016) | Ch 7, opening | Confirmed verbatim at source lines 3253-3265. |
| Heuristic evaluation (Nielsen & Molich, 1990) | Ch 7.1 | Confirmed verbatim at source lines 3290-3294. |
| Eight Inclusivity Heuristics with persona reactions | Ch 7.3.1–7.3.8 | Each verbatim quote confirmed against the source (lines 3317-3514). |
| Code smell self-diagnostic thoughts list (six items) | Ch 8, opening | Confirmed verbatim at source lines 3614-3626. |
| Refactoring definition | Ch 8.2; Glossary | Confirmed verbatim at source line 3673 and Glossary line 4543. |
| Four code smells about comments | Ch 8.3.2 | Confirmed verbatim at source lines 3722-3762. |
| Three code smells about functions | Ch 8.4.1 | Confirmed verbatim at source lines 3805-3845. |
| Four code smells about code in general | Ch 8.5.1 | Confirmed verbatim at source lines 3875-3972. |
| Chapter 8 closing claim | Ch 8.6 | Confirmed verbatim at source lines 3994-3995. |

## Areas where verification used judgement rather than direct lookup

- **Connections section bullets:** each bullet attributing a connection (e.g., *Agile Manifesto* citation as grounding document) was checked by grep against the author name in the source. All sampled cases confirmed; `[BT]` markers are appropriate because Letaw cites these external authors rather than originating the claims herself. The relationship characterisations (approving, critical/ironic, neutral) were judged against the source's framing rather than against any single quote — Letaw's neutral attribution of Larson & Gray's AON format vs her critical-ironic framing of Royce's article being two examples.
- **Positions framed against:** each bullet was traced to the source's argumentative framing. Letaw's anti-Waterfall framing is in Ch 1.1 (the Royce-irony observation). Her anti-over-commenting framing is in Ch 8.3 ("Drawbacks of Having Many Comments"). Her framing against rigid UML correctness is in Ch 4.4 (drawback 2) and Ch 4.7 ("What's most important... is not following the rules or conventions but communicating with your audience"). Her framing against ground-rules-as-performative-compliance is in Ch 2.4.1's warning sentence.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref:** searched for diagnostic-question lists, anti-pattern lists, and worked-example projections (Pass G territory). None present; the worked examples (e.g., NIH pain-management software, ODOT TOCS, the wholesaler user story) are the author's own examples and appropriately marked `[AE]`, not task-application projections.
- **Post-source vocabulary:** searched for terms not in Letaw's vocabulary. None detected. The deep ref uses Letaw's own naming throughout (e.g., "Inclusivity Heuristics" rather than the older "Cognitive Style Heuristics" except where the source explicitly names both).
- **Cross-corpus drift:** searched for connections to authors not cited in the source — none detected. All `[BT]` markers trace to authors named in the source's chapter or end-of-book References.
- **Training-data leakage about author career:** the deep ref does not state biographical facts about Letaw beyond what the source's front matter provides (Oregon State University, OSU OER Unit, contact email, 2nd-edition acknowledgements).
- **Em-dash typography normalisation:** the source uses em-dashes without surrounding spaces (`a—b`); my deep ref uses spaced em-dashes (`a — b`) per the project's prose convention. This is permitted typography drift, not a meaning change.
- **Curly-vs-straight quote normalisation:** the source uses Unicode curly quotes (`"`, `'`); my deep ref uses ASCII straight quotes (`"`, `'`) per the corpus's other deep-reference convention. Permitted normalisation.

## Audit decision

**The deep reference passes Pass I.** Seventeen fixes were applied (six marker corrections converting `[V]` to `[AP]` or splitting markers; eight verbatim-quote corrections to restore source wording exactly; two citation tightenings; one bracketed-insertion fix that had altered tense). The body of the deep ref is well-anchored to source material; the corrections were typography- and quote-fidelity issues rather than substantive content errors. No training-data leakage, post-source vocabulary, cross-corpus drift, or task-application smuggling was detected.

## Audit summary

- N claims audited: ~180
- N source-anchored: ~172 (without modification) + ~8 (after fixes) = ~180
- N stripped: 0
- N marker corrections: 6
- N verbatim-quote corrections: 8
- N citation tightenings: 2
- N bracketed-insertion fixes: 1
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref and distillations derived from it inherit this audit's discipline.

## Scoped re-audit 2026-10-16: restored callouts

**Scope.** Only the callout and example-box text restored by the 2026-10-16 re-conversion (PyMuPDF text blocks, sort=False) and the deep-reference text written for it (`git diff origin/main`). Everything else was audited earlier and is unchanged. Out of scope, so not re-audited: the body-text "17%–22%" CHAOS row.

**Read.** Every tape range in the dispatch, in full: 244–266, 482–516, 528–560, 656–676, 744–766, 846–870, 892–912, 987–1011, 1216–1240, 1362–1386, 1576–1596, 1665–1773, 1831–1877, 1947–1971, 2056–2076, 2132–2156, 2246–2270, 2360–2380, 2440–2470, 2791–2811, 2828–2848, 2868–3075, 3129–3153, 3205–3229, 3245–3269, 3296–3334, 3363–3383, 3454–3503, 3532–3552, 3761–3782, 4328–4348, 4449–4469. Grep checks: Standish/CHAOS mentions (lines 492–525, 703, 4459), the RACI example (912–935). Deep reference: every added or changed line in the diff (lines 9, 33–35, 39, 61, 75, 79, 91, 121, 129, 138–144, 148, 152, 158, 172, 189, 217, 219, 284–291, 293, 299, 320, 324, 341, 360, 409), read in full. One page render (PDF p. 47, Figure 3.3), to check the "project cards" description: three boxed cards, confirmed.

**Verbatim check.** `check-verbatim.py` before and after: 67 apostrophe, 23 initial, nothing that needs a fix. Every restored `[V]` quotation matches the tape, including the eight heuristic design recommendations, the three Figure 3.4 criteria, the Manifesto, the CHAOS figures and the Ch 8 callouts.

**Counts.**
- Claims audited: 49
- Source-anchored as written: 44
- Stripped: 1
- Marker or wording corrected: 2
- Coverage-line completions: 2
- Quotations corrected: 0

**Changes.**
1. Line 35 (CHAOS subsection): stripped "The callout reports the figures without discussing how the report defines failure." No passage says this. It is the ingester's methodological caveat, which invites doubt the source doesn't raise.
2. Line 39 (Agile and the Manifesto): "The Manifesto is quoted in full" became "The source quotes the Manifesto". Whether the quotation is the *full* Manifesto can't be checked against this source; that would take outside knowledge. The quotation itself is verbatim.
3. Line 129 (user stories): "to a satirical Twitter feed" became "to a Twitter feed". "Satirical" is an evaluative label the source doesn't use (the callout says "comically bad user stories").
4. Line 9 (Coverage): the list of what was added left out several in-scope additions. Added "the quality-attributes and user-story callouts" (Part III), "the two GenderMag pointers" (Part VII) and "further-resources" (Part VIII), so the list matches the body.

**Checked and left as written.**
- CHAOS "citing Standish Group 2015" (line 35, and the line 360 row): the callout itself names only "The 2015 CHAOS report". The same section's body bullet credits "CHAOS Report from the Standish Group International, Inc. (2015)" (tape 519–521), and Ch 1's references list it (703). The attribution holds.
- Gesture callout: "is an insult" paraphrases "it means 'up yours!'". [AP] [BT] fits.
- Use-case citation "(Ch 3.6, Figure 3.2)": Figure 3.2 comes before the 3.6.1 heading (tape 1669–1693), so the citation is correct.
- Figure 3.3 quotation: "spread of disinformation" is Figure 3.3's wording. Figure 3.4 reads "the spread of disinformation", and the deep reference quotes 3.3 correctly.
- Integrity paragraph (line 409): its comparison remark ("wrapped reference entries, a wrapped code line and the ISO definition's citation") is conversion provenance. The tape agrees as far as it goes (the reference ranges, and the ISO citation on its own line at 250–254), but the comparison itself wasn't re-run.
- Restored boxes left out of the deep reference (the RACI example list at 902–935; "If any links are broken, try the Wayback Machine"): leaving them out is a selection choice. The Coverage line doesn't claim every box was added.

**Derived tier.**
- Light reference: the "Manifesto's four values are quoted in full" sentence is accurate as worded (all four values are quoted), so the deep-reference change in item 2 doesn't make it stale. The CHAOS sentence and row, the requirements worked examples (use case, US-023, the Definition of Done's 10 ms criterion, the SDD/SRS quotation) and the heuristic-recommendations sentence all trace to the tape. None of the light reference's additions carries the stripped caveat or "satirical".
- Software-business concept 16's Definition-of-Done sentence: the quotation "The message appears within 10 milliseconds" is verbatim (tape 1861–1863). Tying it to INVEST's "Testable" is task application, which belongs at distillation tier, and it's supported by the source's own link between acceptance criteria and "done" (1835–1840).
- Source card coverage sentence: accurate.
- The PARTIAL notes removed from the five distillations: the deep reference now covers the restored text. But only software-business gained content from it. The other four (aar, decision-making, retro, stakeholder-engagement) weren't re-projected. Retro's and decision-making's fist-of-five and requirements material may be worth checking against the new gesture caution, user-story and Definition-of-Done content. Taking the notes out is honest only if the parent judges that content immaterial to those tasks. All six derived files carry `derived-from-deep` stamps, which this re-audit's edits make stale. Re-stamp after the parent's re-derivation decision.
- Claims the derived tier might carry that changed here: none of the four changes alters a claim found in the light reference or any distillation.

**Open.** The deep reference is not stamped here; the driver stamps once the cross-family leg is done. The "Pass I has not run." lines are untouched.

### Apply leg (sort reconciliation and derived tier)

**Sort result.** 21 findings sorted: 15 confirmed and fixed, 0 confirmed with a wrong or incomplete fix, 0 missed by the fix-in-place audit, 0 over-flagged by the blind auditor, 2 over-flagged by the fixer, 4 disputed; 0 new defects; gate PASS. Remaining edits: none.

**Disputed findings, settled against the tape.**
- S1 (CHAOS caveat stripped, line 35): the callout (tape 492–506) is a heading sentence and six figures; it says nothing about how failure is defined. The removed sentence described an absence, not a source passage. Left stripped.
- S3 ("satirical", line 129): the callout says "comically bad user stories" (1763); "satirical" isn't in it. Left as "a Twitter feed" [AP].
- H6 (marker scope, line 15; outside this re-audit's scope): every quoted fragment matches tape 278–281, and the unquoted "the field keeps changing" traces to "Software engineering as a field also keeps changing" (279). No defect; left as written.
- H12 (Waterfall quotation, line 400; outside scope): matches tape 480 exactly (apostrophe notice only). Left as written.
- S2 (over-flagged): "The source quotes the Manifesto" is accurate and stays.

**Verbatim check.** `check-verbatim.py` on the deep reference: 67 apostrophe, 23 initial, no mismatches.

**Derived tier.** The deep reference's changed claims since the earlier audit are the fixer's three (S1 strip, "quoted in full", "satirical") plus the Coverage and integrity notes. Read in full: the light reference and all five distillations. Only one derived claim echoed a changed one: the light reference's "The Agile Manifesto's four values are quoted in full" became "The source quotes the Agile Manifesto's four values", matching the deep reference's wording (tape 535–550). Software-business concept 16's added sentence checks out: "The message appears within 10 milliseconds" matches tape 1861–1863, and the deep reference lines 138–144 back it. No distillation index row carries a changed claim. No provisional or PARTIAL header text remains. `check-verbatim.py`: light reference clean; software-business 4 apostrophe, 3 initial, no mismatches.

### Gate settlement (2026-10-16, orchestrator)

The apply leg passed the gate with one open item: whether the aar, decision-making, retro and stakeholder-engagement distillations should carry restored callouts. Settled as Pass G would: the fist-of-five concept in all four now carries the hand-gesture caution ([V], Ch 2.4.3), labelled where it turns into advice; stakeholder-engagement's Definition-of-Done concept carries Figure 3.4's US-023 example ([V], Ch 3.6.1); and its cross-cultural limits note cites Ch 2.4.3. The fidelity check covers these additions.


## Second leg

**Auditor:** gpt-6.1-sol via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `cada55f2d15253dbec22e1c6da61d7a48d2fc7984d261899c6a0706eca620d01`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `c5b45850b3847151fe9048058ac4f7ba86a341017ee4c8ea5d37d523a4ef57a3`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_letaw-handbook-sweng-methods_crossfamily_blind.md`, `_ingest_pass_I_letaw-handbook-sweng-methods_crossfamily_sort.md`, `_ingest_pass_I_letaw-handbook-sweng-methods_crossfamily_prompts.md`.

**Sort result:** 21 findings sorted: 15 confirmed and fixed, 0 confirmed with a wrong or incomplete fix, 0 missed by the fixer, 0 over-flagged by the blind auditor, 2 over-flagged by the fixer, 4 disputed, 0 new defects; gate verdict PASS.

**Remaining edits applied (2026-10-16):** The sort listed no remaining edits, so 0 were applied as written, 0 applied with changed wording and 0 declined; the four disputed findings (S1, S3, H6, H12) were settled against the tape in favour of the current deep-reference wording.

**Gate:** accepted by operator. Deep reference sha256 `091e513ad1ffc3231136d5b99748053baa55b8c8289b88e6da0d16208c57e83d`, stamp included.

## Derived-tier fidelity check (2026-10-16)

Fidelity check of the derived tier for the restored callouts (2026-10-16). I checked 37 claims against the audited deep reference: 16 light-reference additions, 3 each in the aar, decision-making and retro distillations (the fist-of-five caution and its labelled application, plus the PARTIAL-note removal), 4 in software-business and 7 in stakeholder-engagement, and the source card's coverage sentence. The 91 index rows were unchanged and carry no restored-text claim, and their structure checked clean. Fixed 4. Two restored a dropped qualifier or scope: the light reference's heuristic-6 recommendation now says Tim and Pat bypass steps and tutorials they don't need, not the whole path, and stakeholder-engagement's cross-cultural note now says single-finger gestures. One re-anchored a quotation to the wording the deep reference carries: stakeholder-engagement concept 10 now quotes US-023's story as in Figure 3.3, not Figure 3.4's "the spread" variant. One labelled an application as the distillation's own: software-business concept 16's link between Figure 3.4 and INVEST's "Testable". check-verbatim on each edited file shows only apostrophe and initial flags, none in edited lines. One anchor defect in the deep reference is recorded in `fidelity-deep-defects.json`: the GenderMag facets pointer is anchored Ch 7.1 but sits in the Chapter 7 opening (tape L2801). No derived file carries it.

### Post-stamp anchor fix (2026-10-16, orchestrator)

The fidelity check recorded one deep-reference defect: the GenderMag facets pointer was anchored (Ch 7.1), but the callout sits in the Chapter 7 opening (tape L2801), before the 7.1 heading. Re-anchored to (Ch 7, opening); derived tier restamped.
