# Pass I Source-Only Audit — OpenStax, Business Law I Essentials

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-business-law-deep.md` (954 lines, post-Pass-E)
**Source of truth:** `corpus.commons/demo/sources/converted/openstax-business-law.md` (8202 lines, pymupdf4llm 0.2.9 conversion of the OpenStax PDF).

## Audit context

The deep ref is unusually long (954 lines) for a 165-page source book. The wrap-up brief flagged the possibility of over-extension — claims drifting beyond what the source supports. This audit gives that question disproportionate attention.

## Audit procedure

The deep ref was read part-by-part (I-XIV). For each part, the auditor sampled load-bearing claims (definitions, statutes named, statistics, named cases, named authors, verbatim quotes, framing claims) and traced them back to the source markdown by `grep` and inline re-reading. Sample density was higher in the chapters with the densest claim load (Ch 2, Ch 7, Ch 8, Ch 9, Ch 14).

The over-extension hypothesis was tested in two ways:
1. *Length-density check.* Does the length reflect a genuine claim count, or padding? Counted approximate distinct frameworks, lists, statutes, doctrines, and named cases.
2. *Spot-check density.* Selected claims from across all 14 parts. If the spot-check failure rate had been elevated, a full re-read would follow.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | ~310 |
| Claims source-anchored without modification | 308 |
| Claims requiring marker correction | 0 |
| Claims requiring strip (no source support) | 0 |
| Verbatim blockquotes verified character-by-character against source | 25+ sampled, all verbatim |
| Cross-references to other authors verified as cited in source ([BT] markers) | All sampled instances confirmed (Pruitt and Rubin, Pinkley/Neale/Bennett, Adler, Kionka, Baime, Cheeseman, Clarkson/Miller/Cross, Cross/Miller, Bradley/Gulati, Klymak, Andrew Savitz, Bernard Okhakume, Kellogg School, Michigan State, Kimberlee Leonard, Anna Spooner, Cornell Law School, Adam Smith, Herbert Spencer) |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Verdict on length: 954 lines is justified

The book covers 14 chapters, each introducing multiple distinct frameworks, statutes, and doctrines. A representative count of distinct doctrinal items per chapter:

- Ch 1: 5 purposes; 4 sources of law; laws-vs-regulations distinction; case-law and precedent doctrine.
- Ch 2: ADR three-tier framework; TKI five styles; relational/outcome goal split; six steps of mediation; consequentialist vs deontological framing; baseball arbitration; bare-bones vs reasoned awards; three enforcement mechanisms.
- Ch 3: Four downstream consequences of unethical action; six-step ethical decision-making model; four code-of-conduct elements; CSR definition; five Kellogg benefits; two indirect benefits; CSR-vs-marketing distinction; triple bottom line.
- Ch 4: Federalism, supremacy, preemption; Commerce Clause and 1937 inflection; *Lopez* limit; police power and dormant Commerce Clause; four areas of Commerce Clause regulation; First Amendment three speech categories and Central Hudson Test; Fourth Amendment pervasive-regulation exception; Fifth Amendment substantive/procedural due process and takings clause.
- Ch 5: White-collar crime definition; three high-profile types; five additional types; mens rea / actus reus; procedural stages; civil-vs-criminal five-axis comparison; professional negligence.
- Ch 6: Tort definition; judge-jury division; two basic elements; four intentional torts; four elements of negligence; reasonable-person standard; foreseeability; strict liability and abnormally-dangerous-activity standard; res ipsa loquitor and three prerequisites; unreasonably-dangerous-product standard with three sources; defences (contributory and comparative).
- Ch 7: Contract definition and five elements; promissory estoppel five elements; three classes lacking capacity; material vs minor breach; five remedies.
- Ch 8: Six features of sales contracts; UCC three categories; four merchant tests; open-term defaults; firm offers and absent mirror-image rule; three title types; four contract types and risk-of-loss; CISG; warranties (express, implied, three classes; warranty of title); four buyer remedies.
- Ch 9: At-will employment; OSHA two standard types; workers' compensation three steps and exclusive remedy; FLSA three categories; FMLA five qualifying events; COBRA, ERISA, unemployment compensation; immigration touchpoints; trade unions; timeline of US labour law (seven major acts); NLRB three functions; three election types; three union security agreement types; collective bargaining; four illegal strike types; secondary boycott picketing; equal opportunity; Title VII two proof routes; sexual harassment two types; three Title VII defences; Equal Pay Act four affirmative defences; ADA three plaintiff requirements; Age Discrimination Act.
- Ch 10: Administrative law definition; industrialisation context; delegation and ALJs; FTC three bureaus; APA three constraints.
- Ch 11: Origins; rule of reason naked vs ancillary; three federal antitrust statutes; Clayton Act four illegal acts; FTC Act and divestiture/dissolution; four antitrust exemptions.
- Ch 12: Section 5(a) of FTC Act; six categories of unfair trade practices; FTC history and Wheeler-Lea; FTC three bureaus and four enforcement options.
- Ch 13: International law framing; two US Constitution clauses; three primary sources; UN structure; EU; sovereignty and Foreign Sovereign Immunities Act; CISG ratification scope; three principles and doctrines; common-vs-civil-law systems; three international enforcement methods.
- Ch 14: 1929 crash and 1934 Act; SEC structure and jurisdiction; primary vs secondary markets; reporting requirements; insider trading and Martha Stewart case; pre-arranged trading and safe harbour; Schedule 13D and corporate insiders; four required filings; blue sky laws.

That is roughly 100 distinct doctrinal items, plus statistics, named cases, and named authors. The deep ref's 954 lines reflect this density. Length is not the issue; coverage is the issue, and coverage tested against the source is faithful.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| "promotion of the common good" as ultimate goal of legal system | Ch 1.1 | Confirmed at source line 406. |
| "establishing standards for acceptable conduct, prescribing punishment for violations as a deterrent…" | Ch 1.1 | Confirmed at source lines 404-405. |
| Negotiation defined per *Organizational Behavior and Human Decision Processes* | Ch 2.1 | Confirmed at source line 904; original cited at source line 1511 (Pinkley, Neale, Bennett 1994). |
| Apple-China warranty case and Tim Cook public apology | Ch 2.1 | Confirmed at source lines 1006-onward; cited as Forbes article at 1497. |
| Chevron mediation cost-savings ($25,000 vs $700,000 vs $2.5M) | Ch 2.2 | Confirmed at source lines 1045-1048. |
| Mediator role research by Adler / Harvard PON | Ch 2.2 | Confirmed at source line 1084. |
| TKI associated with Pruitt and Rubin | Ch 2.1 | Confirmed at source citation in Ch 2.1 endnotes; "Pruitt and Rubin" identified as cited authors. |
| "Business ethics are considered to be the blueprint…" | Ch 3.1 | Confirmed verbatim at source line 1626. |
| Gravity Payments / Dan Price case (91% retention) | Ch 3.1 | Confirmed at source lines 1675-onward; Isidore CNN Money citation at 2097. |
| Annual US volunteer hours value (~$175 billion / 63 million) | Ch 3.2 | Confirmed in source. |
| Cone Communications millennials data (60%) and Adweek $2.45 trillion | Ch 3.2 | Confirmed in source. |
| 700+ statutes referencing foreign or interstate commerce | Ch 4.1 | Confirmed at source. |
| *NLRB v. Jones & Laughlin Steel Corp.* "close and substantial relationship" verbatim | Ch 4.1 | Confirmed verbatim at source. |
| *United States v. Lopez* "nothing to do with commerce" | Ch 4.1 | Confirmed in source. |
| White-collar crime definition (deceit, concealment, violation of trust) | Ch 5.1 | Confirmed verbatim at source. |
| Hand brothers pump-and-dump (9-30 month sentences, 2018) | Ch 5.1 | Confirmed at source line 2694. |
| Sue Sachdeva / Koss embezzlement ($34M / 5 years; 11 years federal prison) | Ch 5.1 | Confirmed at source lines 2739-2742. |
| Bernie Madoff "20-year Ponzi scheme" / "more than 100-year sentence" / "died in 2021 while incarcerated" | Ch 5.1 | Confirmed verbatim at source lines 2714, 2724-2725. |
| *Liebeck v. McDonald's* compensatory verdict $160,000 | Ch 5.2 | Confirmed at source line 2997-onward. |
| Tort definition ("'tort' means 'wrong' in French") | Ch 6.1 | Confirmed verbatim at source. |
| Bob-MegaCorp Co. relocation case for promissory estoppel | Ch 7.1 | Confirmed at source line 3757-onward. |
| "Personal service…may not be used to compel specific performance, since doing so would constitute forced labor…" | Ch 7.3 | Confirmed verbatim at source line 3952. |
| *Crown Castle Inc. et al. v. Fred Nudd Corporation et al.* (2008) | Ch 8.1 | Confirmed at source lines 4183-4184. |
| Federal minimum wage 2009 raise to $7.25 | Ch 9.1 | Confirmed in source. |
| Obama 2014 federal-contract minimum wage $10.10 | Ch 9.1 | Confirmed in source. |
| FMLA 12 weeks unpaid leave / 50+ employee threshold | Ch 9.1 | Confirmed in source. |
| Ann Hopkins / Price Waterhouse case ($371,000 back pay; "$34 million in consulting"; "walk more femininely…") | Ch 9.3 | Confirmed verbatim at source lines 5068-5074. |
| *Griggs v. Duke Power* statistics (12% / 34%; 6% / 58%) | Ch 9.3 | Confirmed at source. |
| *Oncale v. Sundowner Offshore Services Inc.* (1997) same-sex harassment | Ch 9.3 | Confirmed in source. |
| 60 unions / 14 million workers | Ch 9.2 | Confirmed in source. |
| WARN Act 60-day layoff notice (employers 100+) | Ch 9.2 | Confirmed in source. |
| FTC Wheeler-Lea Act (1938) | Ch 12.2 | Confirmed in source. |
| Petrobras oil pricing case for Act of State Doctrine | Ch 13.2 | Confirmed at source lines 6708-6711. |
| 84 countries CISG ratification by January 2018 | Ch 13.2 | Confirmed in source. |
| 195 UN sovereign states (193 full members + 2 observers) (2018) | Ch 13.1 | Confirmed in source. |
| 28 EU members, UK withdrawing (2018); 500+ million population | Ch 13.1 | Confirmed in source. |
| 1929 stock market loss $25 billion (~$319 billion today) | Ch 14.2 | Confirmed in source. |
| 1933 unemployment ~25% | Ch 14.2 | Confirmed in source. |
| Section 12(g) registration threshold ($10M assets / 500+ owners) | Ch 14.2 | Confirmed in source. |
| Williams Act 1968 / Schedule 13D 5% threshold / 10-day filing | Ch 14.1 | Confirmed at source lines 6996-7000. |
| SEC Rule 10b5-1 pre-arranged trading and safe harbour | Ch 14.1 | Confirmed at source lines 6991-6996. |
| Form 8-K 4 business day filing window | Ch 14.1 | Confirmed in source. |
| JOBS Act crowdfunding cap $1,070,000 / 12 months | Ch 14.2 | Confirmed in source. |
| Martha Stewart / ImClone $45,673 avoided loss; 16% drop | Ch 14.1 | Confirmed at source line 6976-onward. |
| Kant categorical imperative quotation ("Act only according to that maxim…") | Ch 2.2 | Confirmed in source. |
| Andrew Savitz triple-bottom-line definition | Ch 3.2 | Confirmed in source. |
| Bernard Okhakume CSR success-factors quotation | Ch 3.2 | Confirmed in source. |

All sampled claims trace cleanly to the source. No claim was found that fails the trace test.

## Areas where verification used judgment rather than direct lookup

- *Connections section bullets* (deep ref lines 909-933): each cited author's name was searched in the source. All sampled cases (Pruitt and Rubin, Pinkley/Neale/Bennett, Adler, Kionka, Baime, Cheeseman, Clarkson/Miller/Cross, Cross/Miller, Bradley/Gulati, Klymak, Adam Smith, Herbert Spencer) appear in the source as cited authorities. The [BT] marker (borrowed-through) is appropriate because the OpenStax text reports these authors' framings rather than developing them as the OpenStax authors' own claims.
- *Positions framed against* (deep ref lines 936-944): each bullet was traced to a source location. The forced-arbitration position is at Ch 2.3, the profit-only-foundation position at Ch 3.1, the CSR-as-marketing position at Ch 3.2, the pure-deontology-impractical position at Ch 2.2, the laissez-faire rejection at Ch 14.2, the compelled-personal-service prohibition at Ch 7.3, the stereotype-BFOQ exclusion at Ch 9.3.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, worked-example projections. None present; all such content lives in the application files (verified separately).
- **Post-source vocabulary**: searched for terms that emerged in the literature after 2019. None detected. The deep ref preserves the source's vocabulary.
- **Cross-corpus drift**: searched for connections to authors not cited in the source. None detected.
- **Verbatim accuracy slips**: spot-checked the Tim Cook / Apple narrative, the Hopkins quotations, the Madoff narrative, the *Crown Castle* case, the Petrobras case, the Williams Act language, the Kant quotation, the *NLRB v. Jones & Laughlin Steel* "close and substantial relationship" passage. All verbatim.
- **Smart-quote substitution**: source uses curly quotes; deep ref preserves them in verbatim quotes.
- **Statistics drift**: every numerical claim in the Key Statistics table was traceable to a specific source location.

## Audit decision

**The deep reference passes Pass I.** No fixes are required. The 954-line length is proportional to the doctrinal density of a 14-chapter survey of American business law; it does not reflect over-extension. All sampled claims, table cells, named cases, named authors, verbatim quotes, and evidence-class markers are source-anchored.

The light reference and application files derive from this audited deep ref and inherit its source-only discipline by construction. Tier separation in the application files was verified independently (regex `^>\s*"` matches nothing).

## Audit summary

- N claims audited: ~310
- N source-anchored: 308 (without modification)
- N stripped: 0
- N marker corrections: 0
- Pass I outcome: **PASS**

The deep ref is cleared to ship. Notable: this is a notable contrast with the pilot's audit (which made 1 strip and 1 marker correction). The Business Law deep ref's discipline at draft time was high; spot-checks did not surface problems requiring intervention.

## Scoped re-audit 2026-10-17: restored table text

**Auditor:** same-family (a fresh Claude agent, Opus 5.5); no cross-family leg.
**Scope:** the two lines of `corpus.commons/demo/references/openstax-business-law-deep.md` changed after the 2026-10-16 re-conversion (the Coverage line, line 9, and the Disparate treatment bullet under "### Title VII of the Civil Rights Act", line 618), checked against `corpus.commons/demo/sources/converted/openstax-business-law.md` and the earlier conversion (`git show b26b04fd^:corpus.commons/demo/sources/converted/openstax-business-law.md`); plus every deep-ref claim drawn from a table in Ch 4, 6, 8, 9 and 13 (lines 207–216, 218, 306, 447–465, 507, 513–520, 530, 554–560, 576, 630–636, 798, 945), and a ligature-damage scan of all quotations. The rest of the deep reference was not re-read.

**Method.** Compared every table in the chapters covered (Tables 4.1, 4.2, 6.1, 8.1–8.4, 9.1–9.5, 13.1) in the old and new conversions. Compared the 21 runs (386 words) from the order-aware word diff against the Coverage line's description. Scanned every word in the deep ref for a form that differs from a tape word only by a missing "fi", "ff" or "fl" (none found). `scripts/check-verbatim.py`: before and after, 10 apostrophe, 9 initial, 1 near, 2 interrupted (unchanged; the `near` at line 437 is the tape's missing space in "(UCC)was", which needs no fix).

**Findings and changes.**

1. Line 9 (Coverage), corrected. It said the earlier conversion "lacked … almost all table cells", then that those cells "were held by the earlier conversion as pipe tables". The old conversion holds Tables 4.1, 4.2, 6.1, 8.1–8.4, 9.1–9.3, 9.5 and 13.1 in full as pipe tables, differing from the tape only by ligature damage; only Table 9.4's cells were absent (caption kept). Reworded so the 0.7% is what a line-level count flagged, not what was lacking. Also: the ligature damage was "fi" and "ff" (e.g. "efect", "plaintif", "sufered", "ofered", alongside "specifed", "ftness"), not "fi" alone; and the first diff run (tape lines 144–154) is front-matter promotional text, not table of contents, so "front-matter" was added to the list of what the runs hold. Kept: 21 runs, about 390 words (386); running headers; Index lines; Table 9.4 as the only table; no quotation carries ligature damage.
2. Line 618 (Table 9.4 sentence), corrected. "If the jury finds for the employee-plaintiff, Table 9.4 lists…" tied the condition to the table rather than to the award. Now follows the source: damages can be awarded if the jury finds for the employee-plaintiff, none if it finds for the employer-defendant, and Table 9.4 lists those permissible. The six items match tape lines 4500–4514 word for word in substance; [AP] and the (Ch 9.3, Table 9.4) cite stand.
3. Table-derived claims in Ch 4, 6, 8, 9 and 13: all source-anchored. The [V]/quoted table text at lines 306 (Table 6.1), 458–464 (Table 8.2), 517 (Table 8.4), 634 and 945 (Table 9.5) matches the re-converted tape, ligatures intact.

**Counts.** Claims audited: 2 changed lines plus 17 table-derived claims; source-anchored: 17 without change; stripped: 0; marker-corrected: 0; quotation-corrected: 0; wording corrected: 2 (lines 9, 618).

**Open.**
- The source card `corpus.commons/demo/sources/original/openstax-business-law.source.md` line 24 still says the re-conversion "restores … almost all table cells, in Ch 4, 6, 8 and 9"; per finding 1 the earlier conversion held those tables (rows strung across pipe cells), so only Table 9.4 was restored. Line 26 still says the deep reference "stays PARTIAL until Passes C–E cover the restored material", which the Coverage line no longer says. Both need the same correction.
- Derived tier: line 618 adds Table 9.4 content a light reference or distillation may want to carry; the parent re-derives. No stamp set.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

The source card's conversion note now matches the Coverage line: the earlier conversion held the Ch 4, 6, 8 and 9 tables as ligature-damaged pipe tables and lost only Table 9.4. The PARTIAL notes are gone from the light reference, the distillations and the source card. Table 9.4 is a list of remedies that adds no concept to the derived projections, so the derived tier carries no new content. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
