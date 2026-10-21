## Scoped re-audit 2026-10-16: restored callouts

**Result: no confirmed defects in the scoped additions.** No replacements or strips are required. This conclusion covers the restored callouts and specified derived changes; it does not recertify the unchanged reference.

**1. What I read**

Read in full:

- `blind-brief.md`, the three calibration fixtures and `pass-i-spec.md`.
- Every tape range specified in the brief, including the restored examples, callouts, heuristic recommendations and surrounding context.
- Every added or changed passage in `frozen-deep.md`, identified against `origin/main`.
- The specified light-reference additions, software-business concept 16’s added sentence, the source card’s coverage sentence and the five removed PARTIAL notices.

The frozen deep reference’s SHA-256 matches `frozen-deep.sha256`: `cada55f2d15253dbec22e1c6da61d7a48d2fc7984d261899c6a0706eca620d01`.

I did not read the whole tape or whole deep reference. Unchanged prose appearing on a changed line was treated as context. I did not consult the parallel auditor’s findings or earlier audit log.

The deterministic verbatim checker ran against the frozen deep and supplied tape. It returned no failing mismatches or source-lookup errors. Its notices were apostrophe/quotation typography and initial capitalisation; unchanged passages were not reopened as audit findings.

**2. Findings**

None confirmed.

The following trace ledger records the substantive checks:

| Scoped deep-reference passage | Frozen-deep lines | Tape evidence | Result |
|---|---:|---:|---|
| CHAOS aggregate and six failure rates | 35 | 492–506 | Figures, project-size categories and attribution match. |
| Manifesto preamble, four values and concluding qualification | 39 | 535–550 | Complete displayed passage retained. |
| Quality included in scope | 61 | 754–763 | Matches the callout. |
| Existing standards as ground rules | 75 | 856–860 | IEEE Code of Ethics and Manifesto are source-named. |
| Cultural meanings of hand gestures | 79 | 997–1001 | Locations and meanings match. |
| Story-point scales and spacing rationale | 91 | 1226–1230 | Matches. |
| Wikipedia quality-attribute pointer | 121 | 1586–1588 | Source-supported cross-reference. |
| User-story format, project cards and humorous-example pointer | 129 | 1709–1765 | Template, fields, identifier, priority and quoted story match. |
| US-023’s three acceptance criteria | 138–142 | 1835–1869 | All three criteria retained; 10 milliseconds is correct. |
| Glossary’s given-when-then definition | 144 | 3770–3780 | Definition and Agile Alliance attribution match. |
| Clinician use-case example | 148 | 1675–1701 | Title, actor, ten steps and quoted endpoints match. |
| SRS/SDD distinction | 152 | 1957–1961 | Includes the source’s overlap qualification. |
| UML epigraph | 158 | 2066 | Wording and Fowler attribution match. |
| IDE-generated diagrams | 172 | 2142–2148 | Regeneration benefit and excessive-detail qualification retained. |
| Diagram audience | 189 | 2256–2260 | Matches. |
| Dumb pipes; library versus service | 217, 219 | 2450–2465 | Both distinctions are explicit in the source. |
| Eight heuristic recommendations | 284–291 | 2878–2884; 2903–2907; 2928–2932; 2959–2963; 2982–2988; 3008–3014; 3038–3042; 3061–3065 | All eight match, including persona assignments and stated purposes. |
| GenderMag pointers | 293 | 2801; 2838–2840 | Both pointers are source-supported. |
| Further coding resources | 299 | 3139–3143 | Names and wording match. |
| Comment callouts | 320 | 3215–3219; 3255–3259 | Both match. |
| Function callouts | 324 | 3306–3308; 3324; 3373 | All three match. |
| General-code callouts | 341 | 3464–3470; 3489–3493; 3542 | Qualifications and wording retained. |
| New CHAOS statistics row | 360 | 496–506 | All six values and pairings match. |

The light-reference additions and software-business Definition-of-Done sentence preserve the same source content. The removal of the five PARTIAL notices is consistent with completion of the restored-callout coverage described in the brief.

**Statistics:** the new CHAOS row matches the tape: Agile versus Waterfall failure rates are 9% versus 29% overall, 23% versus 42% for large projects, and 4% versus 11% for small projects. The unchanged statistics rows, including 17%–22%, remain outside scope.

**Author-stated limitations:** the unchanged limitations list was not re-audited. The new text preserves the restored callouts’ qualifications. The sentence observing that the CHAOS callout does not define failure accurately describes that passage’s contents; it does not attribute an explicit methodological limitation to Letaw.

**3. Counts**

Counting a complete quotation or coherent paraphrase as one claim unit, with independently listed statistics counted separately:

| Check | Count |
|---|---:|
| Deep-reference source-content claim units checked | 64 |
| Derived-tier source-content claim units checked | 9 |
| **Total source-content claim units checked and anchored** | **73** |
| Additional coverage/provenance checks | 8 |

The eight additional checks comprise the deep Coverage line, first integrity-note paragraph, source-card coverage sentence and five PARTIAL-notice removals. Historical statements about when ingestion occurred are supported by the supplied audit context, rather than by the textbook.

| Defect class | Count |
|---|---:|
| Unsupported claim or cross-reference | 0 |
| Evidence-marker mismatch | 0 |
| Verbatim mismatch requiring correction | 0 |
| Changed quantity or dropped qualifier | 0 |
| Overgeneralisation | 0 |
| Missing restored-source coverage | 0 |
| Task guidance introduced by the reference | 0 |
| Post-source vocabulary or source-external analytical framing | 0 |
| **Total confirmed defects** | **0** |

**4. Over-flag guard**

- **Prescriptive heuristic recommendations:** clean. These are the source’s own recommendations, quoted and attributed, rather than newly introduced task guidance.
- **“Arbitrary” coding thresholds:** clean. The author explicitly uses that description at tape lines 3464–3470.
- **Three-to-four-line functions and zero parameters:** clean. Both emphatic statements occur in the source; their strength is not an ingester embellishment.
- **Ten-millisecond acceptance criterion:** clean. The quantity appears explicitly at tape lines 1861–1863. Its practical plausibility is outside this audit.
- **User “logged in as a user” in an admin story:** clean. That wording is in Figure 3.4; correcting it would change the source.
- **“Satirical Twitter feed”:** not flagged. The source introduces the named feed as examples of “comically bad user stories”; the paraphrase preserves that humorous-example context.
- **“Alternating” clinician and software actions:** not flagged. Read as a summary of the interaction, it describes the flow’s movement between actor and system without claiming strict step-by-step alternation.
- **Quotation typography, wrapping and soft hyphens:** clean after conversion-noise and smart-quote normalisation. No changed substantive wording was found in the scoped quotations.
- **Complete-coverage statements:** accepted for this scoped restoration, relying on the brief’s earlier-audit boundary. This audit independently checked the restored passages, not the previously audited remainder.

No files were modified. The filesystem is read-only, so this report could not be appended to the audit log on disk.