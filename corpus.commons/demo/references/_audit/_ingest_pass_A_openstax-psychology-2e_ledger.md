<!-- Pass A ledger | psychology-2e | claude-opus-4-7[1m] | 2026-05-05 -->

# Pass A: Context ledger — OpenStax *Psychology 2e*

## Metadata

- **Title:** Psychology 2e
- **Publisher:** OpenStax / Rice University
- **Original publication year:** 2020
- **Publish date (per spawn prompt):** 2020-04-22
- **Senior contributing authors:** Rose M. Spielman (Content Lead, formerly Quinnipiac University); William J. Jenkins (Mercer University); Marilyn D. Lovett (Spelman College).
- **Contributing authors (10):** Mara Aruguete (Lincoln University); Laura Bryant (Eastern Gateway Community College); Barbara Chappell (Walden University); Kathryn Dumper (Bainbridge State College); Arlene Lacombe (Saint Joseph's University); Julie Lazzara (Paradise Valley Community College); Tammy McClain (West Liberty University); Barbara B. Oswald (Miami University); Marion Perlmutter (University of Michigan); Mark D. Thomas (Albany State University).
- **ISBN-13 (color paperback):** 978-1-975076-45-0
- **ISBN-13 (B&W paperback):** 978-1-975076-44-3
- **ISBN-13 (digital):** 978-1-951693-23-7
- **Licence:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
- **URL:** https://openstax.org/details/books/psychology-2e
- **Source format:** PDF (755 pages) converted to markdown via pymupdf4llm 0.2.9.
- **Source path:** `corpus.commons/demo/sources/converted/openstax-psychology-2e.md` (47,143 lines).

## Structure (16 chapters; no preface chapter; back-matter References + Index excluded)

| Chapter | Title | Source line range | Notes |
|---|---|---|---|
| 1 | Introduction to Psychology | 838–2020 | History, schools, contemporary subdivisions, careers. |
| 2 | Psychological Research | 2394–3854 | Research methods, statistics, ethics. |
| 3 | Biopsychology | 4457–5928 | Genetics, neurons, brain, endocrine. |
| 4 | States of Consciousness | 6489–8012 | Sleep, drugs, hypnosis. |
| 5 | Sensation and Perception | 8592–9867 | Vision, hearing, other senses, Gestalt principles. |
| 6 | Learning | 10467–11848 | Classical, operant, observational. |
| 7 | Thinking and Intelligence | 12223–13729 | Cognition, language, problem-solving, intelligence. |
| 8 | Memory | 14192–15605 | Encoding, storage, retrieval, problems. |
| 9 | Lifespan Development | 15964–18062 | Stages, theories, death. |
| 10 | Emotion and Motivation | 18528–20049 | Drive, hunger, sexuality, emotion. |
| 11 | Personality | 20455–22036 | Freud, neo-Freudians, learning, humanistic, biological, traits, cultural, assessment. |
| 12 | Social Psychology | 22627–24707 | Attribution, self-presentation, attitudes, conformity, prejudice, aggression, prosocial. |
| 13 | Industrial-Organizational Psychology | 25399–27073 | I-O subdiscipline; selection, evaluation, organisational psychology, human factors. |
| 14 | Stress, Lifestyle, and Health | 27414–29648 | Stress, stressors, illness, regulation, happiness. |
| 15 | Psychological Disorders | 30174–33102 | Anxiety, OCD, PTSD, mood, schizophrenia, dissociative, childhood, personality. |
| 16 | Therapy and Treatment | 33831–35278 | Treatment types, modalities, substance disorders, sociocultural. |

## Citation style decision

`(Ch N, "Section name")`. The pymupdf4llm conversion preserves bolded section titles like `**1.1 What Is Psychology?**` but does not preserve PDF page anchors. Section names taken from these inline bold markers; sub-section names are likewise preserved (e.g., `**Wundt and Structuralism**`).

## Coverage scope (Option B — substantive content only)

**Included:** chapter introductions; numbered substantive sections (e.g., 1.1, 1.2, ..., N.M).

**Excluded scaffolding sections per chapter:**
- Key Terms
- Summary
- Review Questions
- Critical Thinking Questions
- Personal Application Questions

**Excluded back-matter:** References (line 35,738+); Index (line 45,857+).

There is no Appendix.

## Source-integrity pre-flight

- Source completeness: Table of contents (Preface 1, Chapters 1–16, References 633, Index 735) matches the 16 chapter markers found in the converted markdown. No truncation or chapter-boundary discontinuities observed in the structural scan.
- Citation-style detection: page anchors lost in conversion. Section-name citations selected.
- Model: `claude-opus-4-7[1m]` (Opus 4.7, 1M context). Confirmed.

## Front-matter framing notes

- This is the second edition of an introductory psychology survey. Preface declares: "210 new research references have been added or updated"; "research replication and validity" coverage was strengthened in response to first-edition feedback; "diversity, representation, and inclusion" reviews drove revisions.
- Ch 1 introduces the discipline's six historical schools (structuralism, functionalism, psychoanalytic, Gestalt, behaviorism, humanism) and its modern subdivisions, framing psychology as an empirical natural-and-social science.
- Lead author Rose Spielman is a licensed clinical psychologist; the book balances research science with applied / clinical content (Ch 13 I-O psychology, Ch 14 health, Ch 15 disorders, Ch 16 therapy).

## Image plan

- 353 images extracted to `docs/images/psychology-2e/`.
- 4 PNGs, 349 JPEGs.
- Of 4 PNGs sampled: 3 decorative (Rice University logo, paper texture, dark frame) and 1 substantive (Punnett square diagram, Ch 3).
- Pilot heuristic (PNG = usually substantive; JPEG = usually decorative) inverts here for PNGs. Will read JPEGs in chapter-relevant batches to identify substantive diagrams (e.g., Maslow's hierarchy, brain diagrams, Stages of Sleep, Gestalt principles, hierarchy of personality, attribution Punnett-style tables). Estimated substantive image rate: ~15–20 per cent given the photo-heavy typography.

## Task-axis pre-considerations

The book covers three pockets of content directly relevant to the corpus task axes:

- **Chapter 13 (Industrial-Organizational Psychology)** is the most concentrated source: selection, performance evaluation, job satisfaction, leadership, group processes, organisational climate.
- **Chapter 12 (Social Psychology)** carries attribution, attitudes/persuasion, conformity/compliance/obedience, prejudice/discrimination, aggression, prosocial behaviour — load-bearing for stakeholder engagement.
- **Chapter 7 (Thinking and Intelligence)** covers cognition, problem-solving heuristics, judgement under uncertainty — load-bearing for decision-making.
- **Chapter 6 (Learning)** carries operant conditioning, reinforcement schedules, modelling — relevant to behaviour change in stakeholder engagement.
- **Chapter 10 (Emotion and Motivation)** carries motivation theory (Maslow, drive, self-efficacy, intrinsic-extrinsic) — relevant to both axes.

Therapy/clinical content (Ch 15, Ch 16) excluded from application projection per spawn-prompt directive (do not drift toward coaching framings). The diagnostic/disorder content in Ch 15 and 16 informs only what NOT to project (i.e., we do not borrow DSM categories or therapist-client framings into decision-making or stakeholder-engagement guidance).
