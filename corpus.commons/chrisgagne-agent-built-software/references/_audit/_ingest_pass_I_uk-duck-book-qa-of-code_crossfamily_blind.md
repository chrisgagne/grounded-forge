## 1. Reading and audit scope

Read in full:

- `blind-brief.md`; all three calibration fixtures, before the cold read; `pass-i-spec.md`.
- `frozen-deep.md`, all 508 lines.
- `tape.md`, all 6,656 lines, including code examples, directives, captions, alt text and the machine-learning dropdown.
- Repository `CLAUDE.md` and the verbatim-checker implementation.

No `source.*`, `source-card.md`, acquisition manifest, original TOC or image files were supplied. Original-file provenance and image contents therefore remain unverified. I did not read the parallel auditor’s prompts, logs or findings.

The frozen reference’s SHA-256 matches `frozen-deep.sha256`. The tape’s hash, 49,425-word count and 19 file markers match the reference’s stated values.

**Decision: corrections required; acquisition provenance remains unverified.** No files were edited. This message is the report.

## 2. Numbered findings

### 1. Acquisition claims exceed the supplied evidence

**Deep lines:** 5, 7, 501.  
**Class:** Unsupported provenance claims.

The reference specifies commit `fa39f2089905fe07c08ae4d66671736a1becd3c5`, its date, `_toc.yml` ordering, removal of front matter and MDX imports, byte-for-byte preservation, and agreement with an acquisition manifest.

**Evidence:** Tape lines 1–6 establish the title and institutional producer; lines 51–63 establish the licence and suggested citation. The tape contains 19 file markers, but no acquisition manifest, commit metadata, original `_toc.yml` or originals against which conversion fidelity could be checked. The tape hash is independently correct; “matches the manifest” is unverified.

**Exact fixes:**

- Line 5: **strip** `at commit fa39f2089905fe07c08ae4d66671736a1becd3c5 (2026-06-09)`.
- Line 7: replace with:

  > **Structure:** A root page and 18 chapters, in the order presented in the supplied tape, with a `<!-- file: book/{name}.md -->` marker before each file:

- Line 501: replace with:

  > - **Conversion evidence.** The supplied `tape.md` contains 6,656 lines, 49,425 whitespace-delimited words and 19 file markers; its sha256 is `7126cd8914ce6f28cee79a546a25fe5043e19743fa3e5f2f660d2192de9b0708`. MyST directives and Python and R code examples are present. The acquisition manifest and original repository files were not supplied, so the acquisition commit, date, original TOC order and byte-for-byte conversion fidelity remain unverified.

These are unverified claims, not demonstrated falsehoods.

### 2. Image-acquisition claims lack the manifest they depend on

**Deep lines:** 32, 34, 35, 507.  
**Class:** Unsupported provenance claims.

“Not copied” and the assertion that `gradient_descent.png` is absent from the manifest’s image list cannot be established from this bundle.

**Evidence:** Tape lines 2352–2359, 3292–3300 and 4352–4359 establish three remote figure URLs. Lines 6219–6226 reference `gradient_descent.png`. Lines 6334–6341 and 6587–6594 contain the prompt-image references, captions and alt text. None establishes acquisition-manifest contents.

**Exact fixes:**

- Lines 32, 34 and 35: **strip** each assertion that a remote image was “not copied”; retain the remote-image identification and caption information.
- Line 507: replace with:

  > - **Figures.** Figure captions and alt text are represented in the tape. Three figure directives use remote URLs: the Wikimedia DAG image and two xkcd comics. The tape also references `gradient_descent.png`. Image files and the acquisition manifest were not supplied, so copying status, manifest completeness and image contents remain unverified. The two centaur-example prompts are referenced as images; their wording is not transcribed in the tape.

### 3. Accessibility summary drops “most” and the third-party exclusion

**Deep line:** 60.  
**Class:** Dropped scope qualifiers.

The summary lists keyboard, speech-recognition and screen-reader access without preserving the source’s restriction to **most** of the website. It also omits the statement’s exclusion of referenced third-party content.

**Evidence:** Tape lines 68–79 expressly exclude third-party content and repeat “most of the website” for all three navigation/access methods.

**Exact fix:** Replace the accessibility-list clause with:

> The accessibility statement excludes referenced third-party content and says users should be able to change colours, contrast levels and fonts, zoom up to 300% without text spilling off-screen, navigate most of the website using a keyboard or speech-recognition software, and listen to most of the website using a screen reader [AP] (book/intro.md, "Accessibility statement").

Retain the separately supported management, response-time and enforcement claims.

### 4. Breach definition changes potential access into actual access

**Deep line:** 269.  
**Class:** Changed condition.

“A data breach is unauthorised access” loses the source’s condition that unauthorised individuals **may** access accidentally included sensitive information. Actual access need not have been established under the source’s definition.

**Evidence:** Tape lines 3791–3794.

**Exact fix:** Replace the opening clause with:

> The book calls it a data breach if unauthorised individuals may access sensitive information accidentally included in a remote repository [AP] (book/version_control.md, "Handle data breaches via Git");

Retain the following response steps.

### 5. DBMS capability becomes unconditional

**Deep line:** 287.  
**Class:** Dropped qualifier.

“DBMSs manage access and concurrency” states an unconditional capability where the source says DBMSs **usually** support authorisation and concurrent access.

**Evidence:** Tape lines 4378–4387, particularly line 4381.

**Exact fix:** Replace the opening clause with:

> DBMSs usually support authorisation of database access and concurrent access by multiple users;

Retain the examples and remaining supported claims.

### 6. An invitation to reconsider task breakdown becomes a diagnosis

**Deep line:** 363.  
**Class:** Strengthened inference.

The reference says to treat an unfinished task as “a sign it was not broken down enough”. The source asks readers to **consider whether** it was sufficiently broken down; it does not supply that conclusion.

**Evidence:** Tape lines 5727–5730.

**Exact fix:** Replace that phrase with:

> and, if a task remains unfinished at the end of the day, consider whether it has been sufficiently broken down;

### 7. One `[BT]` marker covers borrowed findings and the book’s own commentary

**Deep line:** 395.  
**Class:** Evidence-marker scope mismatch.

The sentence beginning “A study by Anthropic” ends with `[BT]` after combining cited findings with the chapter’s own organisational implications and uncited environmental and ethical commentary.

**Evidence:** Tape line 6320 links the Anthropic and psychological-wellbeing studies; line 6322 links security-vulnerability material. Line 6324 states environmental and ethical concerns without attributing them to another work. The career-progression and technical-debt implications are the chapter’s commentary following the Anthropic finding.

**Exact fix:** Replace that sentence with:

> A study by Anthropic suggests that LLM adoption, especially when rapid and aggressive, can negatively affect learning on the job [BT]. The chapter identifies potential organisational implications for internal career progression and technical debt [AR]. It also cites measured negative impacts on psychological wellbeing, including increased boredom and decreased motivation, and material on critical security vulnerabilities in LLM-generated code, particularly relevant to web-based platforms and applications [BT]. The chapter additionally raises environmental concerns about electricity and fresh-water consumption, especially during training, and ethical concerns about copyrighted training material, reproduced bias, and offensive or harmful content [AP] (book/generative_ai.md, "Vibe check failed - The risks of vibe coding").

### 8. Two explicit scope exclusions are missing

**Deep lines:** 175 and 379; completeness assertion at 502.  
**Class:** Coverage omission—author-stated boundaries.

The reference covers packaging and transformers but omits the source’s explicit limits on discussing them. These are missing source boundaries, not missing chapters.

**Evidence:** Tape lines 1265–1268 exclude packaging and distribution practices from the packaging section. Line 6269 excludes further transformer-architecture discussion. Line 6271 says the guide cannot offer a discussion of post-training.

**Exact fixes:**

Append to line 175:

> The section does not cover the practices required to package and distribute code; it directs readers to code documentation and language-specific packaging guides [AP] (book/modular_code.md, "Organise and document your modules as packages").

Append to line 379:

> Further discussion of transformer architecture is beyond the guide’s scope, and the chapter says it cannot offer a discussion of post-training [AP] (book/generative_ai.md, "Introduction - Machine learning and Large Language Models").

## 3. Counts and specific checks

**Claims checked:** 248 content-bearing line records, including compound paragraphs, bullets, structure entries, figure descriptions, table rows and blockquotes. Compound records were checked clause by clause; 248 is a reproducible record count, not an asserted count of atomic propositions.

**Evidence markers checked:** 477 occurrences: 245 `[V]`, 161 `[AP]`, 4 `[AR]`, 28 `[AE]`, 39 `[BT]`.

| Primary defect class | Count |
|---|---:|
| Unsupported acquisition/provenance claims | 2 |
| Dropped qualifiers or changed conditions/inferences | 4 |
| Evidence-marker scope mismatch | 1 |
| Omitted author-stated scope boundaries | 1 |
| **Total numbered findings** | **8** |

No changed numerical values, quotation mismatches, uncited-author cross-references, post-source vocabulary or added task-application guidance were confirmed.

**Key-statistics table:** All 17 rows’ values and substantive descriptions match the tape. Checks included 2017; commit cadence; 50/72-character lengths; 79-character width; approximately three naming words; the Rule of Three; 100 coin flips; 3/25 parameterised tests; four Python versions; two maintainers; both productivity-study summaries; 1 class/5 functions/225 lines versus 1 function/46 lines; 300%; five working days; and version 2026.1. The successful-build significance qualifier is preserved.

**Blockquotes:** All eight match their source passages, including the retained emphasis in the proportionality quotation. No smart-quote normalisation was needed to clear a mismatch. The automated verbatim check also reported no findings; its 14 unchecked figure claims were subsequently checked manually.

**Coverage:** All 19 tape files are represented. No missing-chapter failure was found. Original `_toc.yml` completeness cannot be independently verified.

**Author-stated limitations:** The draft banners, removed checklists, TDD training note, data-diagram TODO and AI work-in-progress note match the authors’ statements. Other limits, including non-comprehensive learning coverage and SQL testing being outside scope, are represented. Finding 8 records the omitted packaging and AI-discussion boundaries. No unsupported methodological verdict was found in the limitations material.

## 4. Over-flag guard

- **Strong technical judgements:** “Hallucinations are mathematically inevitable”, lack of a world-model, and TDD being “proven” to produce robust code are statements the source makes—tape lines 6279, 6652 and 5410. Their scientific merits are outside this audit.
- **`__future__` compatibility concern:** Deep line 401 repeats the source’s own assessment at tape line 6581; it is not imported auditor reasoning.
- **Precise-prompt requirements:** Numerical data, pandas DataFrames and thresholding are stated in the prose at tape line 6650. Reading the absent prompt image is unnecessary to support that summary.
- **Numerical `[V]` rows:** The verbatim checker explicitly permits figure claims without quotation marks. Accurate numerical table entries were not flagged merely for being paraphrased.
- **Source-authored questions and instructions:** The manager and reviewer question sets are present in the source. Summarising them in the deep reference is not newly invented task guidance.
- **“Positions framed against”:** The listed oppositions have source support. In particular, the Data Driven Design comparison retains “might”, and the source explicitly cautions about inheritance; these were not treated as invented categorical rejections.
- **YAML, TOML, JSON and XML:** The configuration summary follows the source’s listed formats and its general description of formats “like YAML and TOML” as compact and human-readable. This was not counted as a scope defect.
- **Source spellings and source-code errors:** “Macphereson”, “audibility”, “Artifical” and other preserved spellings are source-faithful. Errors in worked code were not attributed to the reference where it accurately reports the source.
- **Correct tape measurements:** The hash, line count, word count and file count are independently supported. Finding 1 concerns the unavailable acquisition evidence, not these measurements.
- **Absent images:** Caption-derived figure descriptions are supported by the tape. Missing originals limit visual verification; they do not establish that the descriptions are wrong.