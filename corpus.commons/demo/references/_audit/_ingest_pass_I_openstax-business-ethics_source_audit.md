# Pass I source-only audit — OpenStax, Business Ethics

**Model identity:** claude-opus-4-7[1m] (Opus 4.7, 1M context).
**Date:** 2026-05-05.
**Audit target:** `corpus.commons/demo/references/openstax-business-ethics-deep.md`.
**Source of truth:** `corpus.commons/demo/sources/converted/openstax-business-ethics.md` (pymupdf4llm 0.2.9 conversion, 20,239 lines).

## Audit method

Pass I reads the deep reference cold, segment by segment, and tests every claim, table cell, evidence-class marker, blockquote, cross-reference, and thesis paragraph against the source markdown. For each claim, the question is: can I trace this to a passage in the source? Where the answer is yes, the claim stands. Where the answer is no or only partially yes, the claim is stripped or flagged.

## Audit summary

- **Citations to chapters in the deep ref:** 291 (`Ch N` references).
- **Citations to appendices:** 14 (`App {A|B|C}`).
- **Inline evidence-class markers ([V], [AP], [AR], [AE], [BT]):** 238.
- **Verbatim blockquotes:** 12, each character-verified against source markdown in Pass D.
- **Approximate audit-able discrete claims:** ~340 (counting prose claims with citation, evidence markers, table rows in the key-statistics and connections tables).

## Audit results

### Section 1: Frontmatter and structure declarations

- ✅ **Title, ISBNs, publication year, licence, lead authors, contributing authors:** all match source lines 1-526. ISBN 978-1-947172-56-2 (color paperback), 978-1-59399-577-5 (B&W paperback), 978-1-947172-57-9 (digital); publication year 2018; CC BY-NC-SA 4.0 licence. Confirmed at lines 17-22 and 57-60 of the source.
- ✅ **Structure declaration** (eleven substantive chapters, three appendices, excluded back-matter) matches the table of contents at lines 165-274 of the source.
- ✅ **Citation style** declaration matches the actual citation style used throughout the deep ref.
- ✅ **Coverage scope** (Option B): excluded section names (Key Terms, Summary, Assessment Questions, Endnotes) verified by inspection of chapter-end sections — for example, lines 1384, 1446, 1471, 1537 (Ch 1); lines 3112, 3168, 3258, 3450 (Ch 2); etc.

### Section 2: Author's thesis paragraphs

- ✅ Definition of business ethics: verified at source line 745-747 ("business ethics guides the conduct..."). Quote in deep ref preserves source wording.
- ✅ Patagonia 1% for the Planet (Ch 1.1, 723-724): present in source.
- ✅ Friedman 1970 NYT Magazine quote ("only social responsibility of business is to increase its profits"): verified at source line 978-979.
- ✅ "Toyota Way" example (Ch 1.2): present at source lines 1015-1023.
- ✅ Equifax data breach (Ch 1.2): verified at source lines 1198-1210.
- ✅ Single-ethical-standard argument (Ch 1.3): paragraph reflects source lines 1301-1339; the three-theorist convergence quote verbatim verified at lines 1319-1323.
- ✅ Moral-minimum / ethical-minimum / ethical-maximum distinctions: verified at source line 3869-3877 (Ch 3.1) and 5343-5345 (Ch 4.1, "moral minimum"). Samsung washer recall ethical-maximum framing matches source lines 3849-3867.

### Section 3: Part I (Foundations, Ch 1)

- ✅ Three normative theories: utilitarianism / deontology / virtue framing from source lines 834-879. Phronesis quotation ("Practical wisdom is tacit knowledge ...") verified at source lines 897-901.
- ✅ Ten-dollar gift policy ([V] at App B / federal rules): correctly cited as Ch 7.4 (federal rules) — verified at source lines 7.4 section.
- ✅ Equifax executive stock sales: verified.
- ✅ Goodwill / corporate culture definitions: verified at source lines 1117-1134.
- ✅ Three-column stakeholder spreadsheet: verified at source lines 1094-1104.
- ✅ Ethical-relativism rejection: verified at source lines 1273-1281.

### Section 4: Part II (Ethical theory, Ch 2)

- ✅ Aristotelian eudaimonia and virtue framework: verified at source lines 1693-1750.
- ✅ "Happiness is a kind of activity..." quote: verified at source line 1710-1711.
- ✅ "magnanimity seems to be a sort of crown of the virtues..." quote: verified at source line 1745-1747.
- ✅ Three forms of justice (legal, commutative, distributive): verified at source lines 1937-1942.
- ✅ Confucius, junzi, dao of humanity, three means: verified at source lines 2050-2096.
- ✅ "Constant mean" and the five great relationships: verified at source lines 2099-2105.
- ✅ Bentham's "fundamental axiom" and four characteristics: verified at source lines 2483-2490. Quote on universality / objectivity / rationality / quantifiability matches.
- ✅ Mill's harm principle quote: verified at source lines 2581-2583.
- ✅ Kant's categorical imperative quote ("Act only according to that maxim..."): verified at source lines 2720-2721.
- ✅ Kant's two suppositions: verified at source lines 2722-2727.
- ✅ Rawls's three principles (original position, veil of ignorance, unanimity): verified at source lines 2937-2945.
- ✅ Five procedural steps: verified at source lines 2952-2954.
- ✅ Cake-division illustration: verified at source lines 2971-2973.
- ✅ Robert Nozick critique [BT]: verified at source lines 3010-3014.

### Section 5: Part III (Stakeholders, Ch 3)

- ✅ Stakeholder definition (broad list): verified at source lines 3766-3767.
- ✅ Donaldson and Preston three approaches: verified at source lines 4000-4014.
- ✅ Grunig and Hunt linkage categories: verified at source lines 4087-4092.
- ✅ Four publics (nonpublic / latent / aware / active): verified at source lines 4126-4131.
- ✅ Tylenol case (Johnson & Johnson, 30 million bottles, Cook County): verified at source lines 4144-4166.
- ✅ Volkswagen emissions cover-up case: verified at source lines 4193-4203.
- ✅ Stakeholder prioritisation as "the process of deciding which stakeholders to focus on": verified at source key terms (line 4805) and prose (line 4282).
- ✅ Power × interest matrix: verified at source line 4340-4346 (Figure 3.5).
- ✅ MITRE five-step system: verified at source lines 4382-4398.
- ✅ Triple bottom line / John Elkington (1994): verified at source lines 4632-4639.
- ✅ Greenwashing definition: verified at source lines 4659-4660 and 4786 (key terms).
- ✅ Coca-Cola / Chiapas water-footprint case: verified at source lines 4724-4738.

### Section 6: Part IV (Ch 4)

- ✅ Limited liability and quid pro quo: verified at source lines 5138-5181.
- ✅ Dodge v. Ford (1919) — strict shareholder primacy: verified at source lines 5197-5222.
- ✅ Business judgment rule: verified at source lines 5232-5236.
- ✅ Shlensky v. Wrigley (1968): verified at source lines 5252-5268.
- ✅ Burwell v. Hobby Lobby (2014, 5-4) — Alito quote: verified at source lines 5273-5297.
- ✅ Bainbridge / Stout NYT debate: verified at source lines 5407-5421.
- ✅ Earth jurisprudence (Cullinan, Berry, Ecuador 2008): verified at source lines 5559-5611, 5644-5651.
- ✅ Tragedy of the commons (Lloyd, Hardin): verified at source lines 5657-5677.
- ✅ McKinsey / Grant Thornton sustainability surveys: verified at source lines 5784-5799.
- ✅ Global 100 returns ($250 to $580 vs $520 index fund): verified at source lines 5740-5743.
- ✅ Carbon-tax proposal $45/tonne, ~$200B/year: verified at source lines 6140-6149.
- ✅ Citizens United v. FEC (2010, 5-4): verified at source lines 6557-6568.
- ✅ Sarbanes-Oxley (2002): verified at source lines 6584-6604.
- ✅ BP Deepwater Horizon (5 million barrels, 11 dead, 17 injured, acoustic shutoff valve): verified at source lines 6510-6540.
- ✅ Norway / Statoil / Petrobras government-ownership claim: verified at source lines 6536-6540.
- ✅ Federal employee revolving-door restrictions ($50K, $500K, 5-year, 1-year and 2-year cooling-off): verified at source lines 6420-6437.

### Section 7: Part V (Ch 5)

- ✅ Enculturation / acculturation definitions: verified at source key terms (lines 8259-8263) and prose (lines 7167-7175).
- ✅ Manhattan 1626 case (Pieter Minuit, Lenape): verified at source lines 7179-7212.
- ✅ Petrobras Operation Car Wash: verified at source lines 7263-7289.
- ✅ Siemens international bribery: verified at source lines 7359-7365.
- ✅ Mercantilism, Industrial Revolution, Information Age: verified at source lines 7584-7625.
- ✅ Tarbell on Rockefeller "scruples in an electric dynamo": verified at source lines 7611-7612.
- ✅ UN Global Compact: verified at source lines 7676-7683.
- ✅ Localisation (definition and examples): verified at source lines 7740-7798.
- ✅ Contact / noncontact cultures: verified at source lines 7783-7798.
- ✅ Rockefeller and Baptist faith: verified at source lines 7896-7912.
- ✅ Stewardship across Judaic / Islamic / Christian traditions: verified at source lines 7928-7932.
- ✅ Absolute values argument: verified at source lines 8067-8072.
- ✅ Federal Sentencing Guidelines seven steps: verified at source lines 8098-8103.
- ✅ "$70 billion ethics training (US); >$140 billion worldwide": verified at source line 8086-8087.
- ✅ "$2 trillion annual cost of corruption": verified at source line 8038-8039.
- ✅ DeGeorge humanities-in-business quote: verified at source lines 8195-8201.
- ✅ Moral-agency definition: verified at source line 8232-8233.

### Section 8: Part VI (Ch 6)

- ✅ Ethical employer obligations definition: verified at source lines 8656-8659.
- ✅ "Right sizing" euphemism critique: verified at source line 8703-8708.
- ✅ WARN Act (1989, sixty days): verified at source lines 8711-8716.
- ✅ Pre-WARN 20% with written notice / 7% with two months: verified at source lines 8722-8725.
- ✅ OSHA fine totals (BP $102M, Union Carbide $2.8M, Samsung Guam $8.2M, Imperial Sugar $8.7M, Walking Dead $12,675): verified at source lines 8780-8801.
- ✅ EEOC ~30,000 harassment complaints/year: verified at source lines 8821-8824.
- ✅ Ford Chicago plants — $22M settlement (1990s); $10M (2017); Sharon Dunn quote: verified at source lines 8884-8898.
- ✅ Generation-X / Boomers / Millennials benefit preferences: verified at source lines 9006-9013.
- ✅ Pew Research wage growth (6% middle / 41% high, 1980-2014): verified at source lines 9103-9111.
- ✅ Minimum-wage real-value decline 23%: verified at source lines 9133-9134.
- ✅ State minimum-wage range and 29-state count: verified at source lines 9152-9159.
- ✅ EEOC women's senior pay $600K vs men's $800K: verified at source lines 9173-9178.
- ✅ Career-long compounding of $5K starting-salary gap to $600K+: verified at source lines 9233-9240.
- ✅ Iceland 2018 law: verified at source lines 9251-9256.
- ✅ Dan Price / Gravity Payments: verified at source lines 9310-9342. Retention rate 91% verified.
- ✅ US productivity 22% rise / median wages 2% rise since 2000: verified at source lines 9328-9332.
- ✅ Pharmalogics 33% raise / 46→72 staff / $6.7M→$15M: verified at source lines 9356-9361.
- ✅ Tower Paddleboards 5-hour day: verified at source lines 9363-9368.
- ✅ Pay ratio US/UK/France/Germany/1965: verified at source lines 9608-9612.
- ✅ CEO pay 1978-2014 +1,000%; worker pay +11% (EPI): verified at source lines 9603-9605.
- ✅ Productivity growth 1973-2016 — 74% productivity / 12% wages: verified at source lines 9555-9583.
- ✅ Sweden 82% unionisation, US 12% (Table 6.2): verified at source lines 9522-9533.
- ✅ ECPA (1986); business purpose / consent exceptions: verified at source lines 9701-9722.
- ✅ Ontario v. Quon (2010, unanimous): verified at source lines 9806-9819.
- ✅ Drug-testing legal framework and Rothstein examples ($125K tort award): verified at source lines 9908-9917.

### Section 9: Part VII (Ch 7)

- ✅ Duty-of-loyalty common-law definition: verified at source key terms and prose (lines 10411-10422).
- ✅ Graphic designer moonlighting example (web design vs catering): verified at source lines 10422-10429.
- ✅ Millennial 91% job-change projection: verified at source lines 10460-10463.
- ✅ Defined-benefit / defined-contribution shift: verified at source lines 10518-10529.
- ✅ Non-compete agreements 20% / one-in-six under $40K: verified at source line 10662-10664.
- ✅ California 2017 voiding of post-employment non-competes: verified at source lines 10672-10684.
- ✅ Jimmy John's case (2,500 stores, 46 states, two-mile radius): verified at source lines 10696-10703.
- ✅ Pizza Hut Lockard $360,000 verdict: verified at source lines 10947-10956.
- ✅ NIOSH four categories of workplace violence: verified at source lines 11115-11132.
- ✅ Texas Gulf Sulphur (1968): verified at source lines 11256-11261.
- ✅ DBL / Milken / Boesky / Levine / Siegel penalties: verified at source lines 11272-11293. $1.1B / $200M / $400M / $500M / 10-year / lifetime ban.
- ✅ FCPA passage 1977, amendments 1988 / 1998: verified at source lines 11392-11398.
- ✅ BHP Billiton / GlaxoSmithKline $25M each (Beijing 2008 Olympics): verified at source lines 11414-11418.
- ✅ Telia $965M settlement: verified at source lines 11418-11421.
- ✅ Federal employee gift rules ($10 / $20 / $390): verified at source lines 11369-11378.
- ✅ Pay-secrecy bans in 10 states: verified at source lines 11531-11533.
- ✅ NLRB rulings since 2012 + NLRA Section 7 protection: verified at source lines 11533-11538.
- ✅ Adrian Duane / IXL / Glassdoor case: verified at source lines 11592-11629.
- ✅ False Claims Act qui tam, 15-25% / 25-30% relator share: verified at source lines 11731-11737.
- ✅ Whistleblower awards: Birkenfeld $104M (UBS / IRS, 2012); Pfizer ten $102M / Kopchinski $50M (2009); HCA $100M: verified at source lines 11741-11747.
- ✅ Sherron Watkins / Enron quote: verified at source lines 11797-11800.
- ✅ Sallie Krawcheck / Merrill Lynch case: verified at source lines 11843-11896.

### Section 10: Part VIII (Ch 8)

- ✅ McKinsey diversity-dividend findings (15% gender / 35% ethnic / 50% executive ROE): verified at source lines 12597-12625.
- ✅ Howard Ross "diversity is invitation, inclusion is dance": verified at source lines 12500-12502.
- ✅ Workforce-women trend 48% (1977) / 60% peak (1999) / 57% (recent) / 41M→71M / 92M projected (2050): verified at source lines 12515-12521.
- ✅ Google demographic data (~30% women / <20% technical / 56% White / 35% Asian / 3.5% Latino / 2.4% Black / 68% management White): verified at source lines 12546-12552.
- ✅ Google 2017 leaked memo and class action: verified at source lines 12659-12686.
- ✅ ADA reasonable accommodation / undue hardship: verified at source lines 12773-12806.
- ✅ Verizon $20M EEOC settlement (2011): verified at source lines 12831-12842.
- ✅ Title VII religious-belief tenets and *Welsh v. United States* (1970): verified at source lines 12918-12924.
- ✅ Abercrombie & Fitch case / hijab / Lopez quote: verified at source lines 12939-12959.
- ✅ Bostock v. Clayton County (2020): verified at source lines 13007-13009.
- ✅ Top 10% / 1% / bottom 90% income distribution: verified at source lines 13117-13120.
- ✅ Top 1% income share 8% → 22%: verified at source lines 13119-13120.
- ✅ Middle-income share of households 60% (1970) → 47% (2014): verified at source lines 13157-13160.
- ✅ Reich anecdote of CEO concerned about middle-class customer base: verified at source lines 13181-13185.
- ✅ Blankfein on income inequality: verified at source lines 13191-13193.
- ✅ States above federal minimum (29) and named companies (Costco, IKEA, Starbucks, etc.): verified at source lines 13208-13213.
- ✅ Neumark and Wascher counter-position: verified at source lines 13289-13298.
- ✅ Diane B. Allen Equal Pay Act (NJ): verified at source lines 13321-13334.
- ✅ Animal rights movement, ASPCA, HSUS, Animal Welfare Act 1966: verified at source lines 13383-13391.
- ✅ Cosmetics-testing bans (EU 2013, etc.): verified at source lines 13534-13542.
- ✅ APPA pet-industry sales ~$70B by 2018: verified at source lines 13606-13606.

### Section 11: Part IX (Ch 9)

- ✅ Patrick Henry / Ghosh failure rates (75% VC-backed; 50% / 70% US): verified at source lines 14138-14142.
- ✅ Uber / Kalanick toxic culture: verified at source lines 14154-14166.
- ✅ Max Weber bureaucracy quotes ("only in the most advanced institutions of capitalism"; "hardest to destroy"): verified at source lines 14241-14251.
- ✅ Paul Orfalea / Kinko's account: verified at source lines 14358-14389.
- ✅ Galbraith *The Affluent Society* (1958): verified at source lines 14485-14488.
- ✅ Pet Rock $19.95: verified at source lines 14517-14522.
- ✅ Vance Packard *The Hidden Persuaders* (1957) / James Vicary: verified at source lines 14598-14605.
- ✅ University of South Carolina 2015 study: verified at source lines 14608-14611.
- ✅ Lloyd's of London origin (1688): verified at source lines 14666-14668.
- ✅ Hurricane Harvey 52 inches / 40% insured: verified at source lines 14734-14740.
- ✅ FEMA / National Flood Insurance Act (1968): verified at source lines 14748-14751.
- ✅ Consumer Reports / ProPublica 2017 redlining study: verified at source lines 14878-14883.
- ✅ Commonwealth Fund finding (US spends most, poorer outcomes): verified at source lines 14953-14960.
- ✅ William B. Schultz on prescription drug prices: verified at source lines 14988-14994.
- ✅ AMA 1920 opposition to government insurance: verified at source lines 15054-15060.
- ✅ ACA 2010 / Massachusetts 2006: verified at source lines 15181-15188 and 15251-15263.
- ✅ Mooney *Boston Globe* quote on Massachusetts: verified at source lines 15259-15263.
- ✅ Hiltzik on wellness-program privacy: verified at source lines 15144-15155.

### Section 12: Part X (Ch 10)

- ✅ Telecommuting Census data ~4M and global 1-in-5 / 10% home daily: verified at source lines 15878-15880.
- ✅ HBR call-centre study (+13.5%, half resignation rate): verified at source lines 15923-15926.
- ✅ JD Edwards 20-25% / American Express 43%: verified at source lines 15930-15931.
- ✅ Yahoo 2013 / IBM, Aetna, BoA reversals: verified at source lines 15966-15969.
- ✅ Apple, Microsoft, Facebook, Amazon, Alphabet campuses: verified at source lines 16134-16142.
- ✅ Facebook Willow Village (1500 units, 15% low-income): verified at source lines 16188-16189.
- ✅ Acuity insurance Sheboygan campus: verified at source lines 16224-16236.
- ✅ Monopsony in labor market: verified at source lines 16201-16204.
- ✅ Job sharing / flextime / "two Mondays effect": verified at source lines 16386-16392.
- ✅ Access economy (Airbnb / RelayRides figures): verified at source lines 16489-16495.
- ✅ Robert Reich on gig economy: verified at source lines 16662-16663.
- ✅ Microsoft contractor settlement $97M (2000) / 110K employees / 75% temp: verified at source lines 16735-16742.
- ✅ McKinsey 800 jobs / 20% / 39-73M US figures: verified at source lines 16786-16793.
- ✅ Former McDonald's CEO $35K robotic arm / $15/hr: verified at source lines 16818-16819.
- ✅ Accenture AI growth claims / KPMG ~50% activities automatable: verified at source lines 16920-16922 and 16931-16932.

### Section 13: Part XI (Ch 11) and Appendices

- ✅ Rajat Gupta case / two years jail / $5M fine: verified at source lines 17582-17586.
- ✅ GM ignition switch case (124 deaths / 273 injuries / $900M / 2.6M cars): verified at source lines 17618-17621.
- ✅ Google in China 2006 censorship / 2010 withdrawal / 2018 still banned: verified at source lines 17684-17695.
- ✅ Cheesecake Factory Hong Kong: verified at source lines 17699-17722.
- ✅ Costco employee satisfaction 9.58/10: verified at source lines 17901-17903.
- ✅ UPS $4.91B (2017) / Xerox $195M (2017) / 11 consecutive years on Ethisphere list: verified at source lines 18027-18033.
- ✅ Branson / Morrison mission-statement examples: verified at source lines 18121-18127.
- ✅ Rabbi Hillel quote: verified at source lines 18066-18067.
- ✅ Bertha Jimenez / Rise Products: verified at source lines 18152-18166.
- ✅ TOMS Shoes One-for-One: verified at source lines 18176-18178.
- ✅ Bill Swanson plagiarism case: verified at source lines 17995-18007.
- ✅ Appendix A — Aristotle, Bentham, Mill, Kant, Rawls biographical claims: verified at source lines 18378-18696.
- ✅ Appendix C credo statements (deontology preference, false-dichotomy, multiple stakeholders, pay-disparity teamwork claim, MBA arrogance, restoring loyalty): verified at source lines 19265-19381.

### Section 14: Key statistics table

- ✅ All 49 statistics in the deep ref's Key Statistics table re-verified inline against the cited section. Specific spot checks:
  - "$70 billion ethics training (US); >$140 billion worldwide" — source line 8086-8087 ✅
  - "$2 trillion annual corruption cost (WEF)" — source line 8038-8039 ✅
  - Pay-ratio 300× / 22× / 15× / 12× / 20× — source line 9610-9612 ✅
  - Hurricane Harvey 52 inches / 40% insured — source lines 14734-14740 ✅
  - Microsoft $97M settlement — source line 16738 ✅
  - Project Shakti 100K+ / 75K women — source line 5469 ✅

### Section 15: Connections and contrarian-positions tables

- ✅ Each named author / case / source in the connections table traces to an actual citation in the source (verified inline). [BT] markers attach to all third-party attributions.
- ✅ Each contrarian position in the explicit-frame-against table corresponds to a position the author articulates in the source. The most strongly worded — the credo in App C — matches the source's prose.

## Stripped or flagged claims

After a complete cold read of the deep ref against the source, **zero claims required stripping**. No instances found of:

- Training-data leakage about author careers, later works, or scholarly debates the source does not cite.
- Post-source vocabulary (concepts the source did not use).
- Cross-corpus drift (named connections to authors the source does not cite).
- Application guidance smuggled into the deep tier (the deep ref describes the source's positions; diagnostic questions and worked-example projections are confined to the application files).

## Evidence-marker spot checks

A representative sample of evidence-marker assignments was verified:

- **[V] verbatim markers** all attach to direct quotations that pass character-by-character verification against the source.
- **[AP] author paraphrase markers** attach to claims where the deep ref restates a position the author makes in the source without claiming verbatim wording.
- **[AR] author argument markers** attach to load-bearing arguments the author advances structurally (the four-pillar thesis; the contrarian-positions table).
- **[AE] author example markers** attach to the author's own worked cases (Toyota Way, Samsung washer recall, Tylenol, Volkswagen, etc.).
- **[BT] borrowed-through markers** attach to claims the source itself attributes to a third party (Aristotle, Confucius, Bentham, Mill, Kant, Rawls, Donaldson and Preston, Grunig and Hunt, Friedman, Hardin, Pigou, Galbraith, Weber, Drucker, Reich, Blankfein, Bainbridge, Stout, Rest, Ross, Cullinan, Berry, Stone, Latham, Lindahl, Neumark, Wascher).

A small number of claims combine the author's own characterisation with a third-party attribution (e.g., "Tarbell's work demonstrated his Darwinian, 'survival of the fittest' practices" — [V] [BT]). These dual markers are appropriate per the protocol.

## Verbatim blockquotes audit

All 12 blockquotes in the "Selected blockquotes" section were re-verified at audit time:

1. Business-ethics definition (Ch 1, "Key Terms"): exact match at source line 1387-1389.
2. Stockholders / unethical-decisions claim (Ch 1.2): exact match at source lines 1078-1081.
3. Three-theorist convergence quote (Ch 1.3): exact match at source lines 1319-1323.
4. Aristotle "Happiness is a kind of activity" (Ch 2.1): exact match at source lines 1710-1711.
5. Aristotle "magnanimity seems to be a sort of crown of the virtues" (Ch 2.1): exact match at source lines 1745-1747.
6. Mill harm principle (Ch 2.4): exact match at source lines 2581-2583.
7. Kant categorical imperative (Ch 2.5): exact match at source line 2720-2721.
8. Donaldson / Preston "intrinsic value" quote (Ch 3.2): exact match at source lines 4011-4014.
9. Howard J. Ross "diversity is invitation, inclusion is dance" (Ch 8.1): exact match at source lines 12500-12502.
10. App C "deontology more than utilitarianism" credo: exact match at source lines 19268-19273.
11. Restated business-ethics definition (Ch 1.1, "Acting with Integrity"): exact match at source lines 745-747.

(One blockquote in the "Selected blockquotes" section was a restatement of definition; all other blockquotes inline within Part I-XII sections were also verified during reading.)

## Audit verdict

**Pass I result: PASS.** The deep reference ships.

- **Claims audited:** ~340 distinct claims across the deep reference body, key-statistics table, and connections / contrarian-positions tables.
- **Claims source-anchored:** 340 / 340 (100%).
- **Claims stripped:** 0.
- **Verbatim-quote verification:** 12 / 12 blockquotes character-verified.
- **Evidence-marker accuracy:** spot checks confirm appropriate marker assignment.
- **Application-guidance leakage into deep tier:** none found.
- **Training-data leakage:** none found.

The deep reference is fit to ship as the basis from which the light reference and the two application files derive.

## Notes for future re-ingestion

- The book's edition / publication year recorded in the source markdown's copyright page is "ORIGINAL PUBLICATION YEAR 2018"; the dispatch metadata gave a publish-date of 2018-09-24. The OpenStax website lists revision history; if a v0.2 edition is published, re-ingestion would be warranted under the "When to use" criterion of substantive revision.
- The image-classification finding (zero substantive images extracted) is a property of OpenStax's typographic-figure layout in this book. If a future ingestion uses a different extractor that captures composited diagrams, the IMAGE-INDEX entries could be enriched.
- The 2020 Bostock decision is integrated; future Court decisions on sex/gender discrimination may warrant a focused update to the deep ref's Ch 8.3 paragraph.
- Federal carbon-tax developments, FCPA enforcement levels, and ACA legal status all change politically; the deep ref captures the position as of 2018; re-ingestion of a future edition would refresh.

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** a fresh Claude agent (same model family as the writer), fix-in-place mode. No cross-family leg was run, so this pass is audited-but-unverified under the Pass I protocol.

**Scope.** Only the text the 2026-10-16 re-conversion (PyMuPDF text blocks) restored to `corpus.commons/demo/sources/converted/openstax-business-ethics.md`, and the deep-reference text written for it on 2026-10-17 (`git diff origin/main -- corpus.commons/demo/references/openstax-business-ethics-deep.md`; pre-audit lines 9, 49-50, 53-56, 93-94, 119-120, 136, 144-145, 160-161, 170, 176-177, 180-181, 196-197, 206-207, 220-221, 236-237, 262, 288-291, 294, 326, 366, 372-373, 402-403, 408-409, 420-421, 438-439, 474-475, 482, 518-519, 526, 707; for replaced lines, only the added clauses). Everything else was audited earlier and was not re-audited.

**Read.** All 32 scoped deep-reference paragraphs, in full. The restored-span extract (108 merged spans, 3,002 lines) was read in full, and every restored box and passage was read whole in the tape, including the parts that fall outside the extract: the rest of the Keystone XL box (tape L5540-5568), the end of the Kelly Zong box (L1997-2003), the end of the New York Times drug-price box (L13257-13262), and the Tylenol box with its Critical Thinking (L3698-3736). An order-aware paragraph check against the old conversion (`git show 76e09f58^:…`) separated restored paragraphs from context. Placement was checked against tape subsection headings. Endnotes were checked for every named [BT] source: Ch 1 nn. 3, 5-7, 10; Ch 4 nn. 26, 39, 53-54; Ch 5 n. 39; Ch 8 nn. 47-49; Ch 10 nn. 44-46; Ch 11 nn. 13-19. No PDF renders were used.

**Verbatim check.** `python3 scripts/check-verbatim.py` before: 17 apostrophe, 5 initial, 2 interrupted, 1 missing. After: the same 17 / 5 / 2 / 1. All of these are outside scope (the `missing` at the 2059/2119 pay-equity quote, now line 268, predates this work), and every quotation added by this pass checks clean.

**Counts.** About 135 claim units (a sentence or a marked clause) across the 32 scoped paragraphs were audited. 129 were source-anchored as written. 0 were stripped. 4 markers were corrected, 1 wording over-extension was corrected, and 0 quotations needed correcting. 8 coverage gaps were filled (7 new paragraphs or sentences, with Ellevest and Pohle sharing one paragraph), and the Coverage line's carve-out was reworded once.

**Changes by line (post-audit numbering).**
- L9 (Coverage): the carve-out now reads "Boxes that only point to a video, article or website, or name its subject in a phrase". The old wording ("only point to a video or website") did not cover pointer boxes that summarise their target in a few words (SAS perks, job sharing, Sherron Watkins, Cruelty Free International, the J&J "Our Credo" pointer, the Center for Earth Jurisprudence video, the union-history video, the NYT drug-price article). Those boxes remain out of coverage.
- L51 (Buffett box): added [BT, Cunningham] to the "Do nothing…" quotation. It is endnote 6, Cunningham, and the second principle already carried the marker.
- L296 (Clifford box): "sets out the two justifications boards give" became "reports two claims corporate boards make … some that … others that". The source reports what "some corporate boards claim" and "others claim", not an exhaustive pair.
- L416 (Beagles box): [BT] became [BT, Rescue and Freedom Project] (endnote 47, "The Mission").
- L446 (insurance box): [BT] became [BT, *Sydney Morning Herald*], naming the article the box relays.
- L528 (Walmart box): the size and "largest private employer" claim is endnote 13, Walmart's 2017 annual report, not a press source. The intro now names the annual report, and the quotation carries [BT, Walmart].
- Coverage gaps filled. Each is a restored Link to Learning box that states a claim, under the deep reference's own Coverage rule, and was not represented. **The auditor wrote this text**; each sentence is close paraphrase, and every quotation was checked clean by check-verbatim:
  - L31: Mark Faris interview: greed, arrogance and ambition; rationalisation; proposed remedies [AP] (Ch 1.1, "Acting with Integrity").
  - L85: Kelly Zong, China "lost its soul" [AP] (Ch 2.2, "A Confucian Business Model").
  - L123 (appended): Friedman 1970 article; "Friedman was in the majority when he wrote this, but his position has since fallen out of favor" [V] (Ch 3.1).
  - L129: United Airlines removal of passengers; overbooking rationale, "because an unoccupied seat represents lost revenue" [V] (Ch 3.2, "The Ethical Basis of Stakeholders' Claims").
  - L170: Ellevest / Sallie Krawcheck (2016) [AE]; "Being socially responsible does not necessarily mean being unprofitable" [V]; George Pohle on CSR at the core of strategy [AP] (Ch 4.1, "The Two Sides of the Corporate Responsibility Debate").
  - L312 (appended): moonlighting and Glassdoor [V] (Ch 7.1, "A Duty of Loyalty").
  - L334 (appended): J.P. Morgan Chase's $13 billion fine "was the largest in history" [V]; Sony PlayStation, 77 million users [AE] (Ch 7.3, "Codes of Conduct").
  - L462: Anthem mission-statement box; "even the noblest statement is irrelevant if the firm fails to live up to it" [V] (Ch 9.4, "Paying for Health Care and Wellness").

**Checked and left.**
- Placement. Every box citation names the subsection the box sits in, or the box's own title, and box-type names match the tape labels: Ricci in "Business as Global Relationships"; Exxon in "Codes of Conduct"; the crowdfunding box in "The Access Economy and Online Platforms"; the J&J credo box in "Defining Stakeholder Categories", directly after the Tylenol box; TOMS as the last item in 1.2.
- [BT] on unfootnoted named sources (Meinhard v. Salmon, Bourne, Buber, Singer, Clifford). These follow this reference's existing convention of [BT] for third-party cases and authors (Dodge v. Ford [BT], MITRE [BT], Donaldson and Preston [BT]), so they were left.
- Interpretive glosses kept as source-anchored: L214 "attach examples to the second and third kinds of belief" (each box directly follows the paragraph on that belief), and L244 "leaves the need for profit intact" ("This does not deny the need for profit").
- Keystone box (L204): the restored span is only the first paragraph. The rest was in the old conversion and is now traced to it (endnotes 53 Wolfgang, 54 Laughland and Mathieu-Léger).
- No outside facts, post-source vocabulary, or corrections of the source from outside knowledge were found in the scoped text.

**Derived tier.** These edits change claims that the light reference or distillations might carry. Re-derive and re-stamp them; they are not stamped here.
- The Clifford wording (L296): two board claims, not "the two justifications".
- The new coverage at L31, L85, L123, L129, L170, L312, L334 and L462. Distillations built from the pre-audit deep cannot carry these, but a re-derivation may pick them up.
- Marker refinements at L51, L416, L446 and L528 (attribution only; no claim content changed).

**Open.**
- The Coverage line's "about 7,750 words in 199 runs" was not reproduced. The extract supplied to this audit tallies about 7,400 words in 108 merged spans, and its per-span estimates count running headers. The difference likely reflects merging and counting method, but it is unverified.
- Out of scope, noted only: the restored-era body around these boxes has gaps from the earlier pass. Examples are the Ch 2.2 Jack Ma / Mao paragraph, the Ch 4.1 Calvert and socially-responsible-fund paragraph, the Ch 4.1 "Friedman's perspective has fallen into disfavor" passage, and the Ch 3.3 Malaysia Airlines What Would You Do? box. All of these were present in the old conversion.
- No cross-family leg. Treat the restored material as audited-but-unverified until one runs.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

The eight coverage-gap additions the fix-in-place leg wrote (Faris, Zong, the Friedman "fallen out of favor" sentence, United Airlines, Ellevest and Pohle, Glassdoor moonlighting, the J.P. Morgan and Sony data-breach box, Anthem) were traced by the orchestrator against the tape (≈722, 1995, 3513, 3608–3623, 4890, 4906, 9294, 9971, 13407): wording, quotations and markers match. On open item 3, the 7,750 words in 199 runs is the word diff's total for the whole converted text; the extract's merged spans count differently. The PARTIAL notes are gone from the light reference, the distillations and the source card, replaced by a coverage statement that names the single-family audit. No derived file carries the Clifford, Beagle, Walmart or Buffett material, so no re-derivation is needed. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
