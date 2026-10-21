---
title: "Why Language Models Hallucinate"
author: Adam Tauman Kalai; Ofir Nachum; Santosh S. Vempala; Edwin Zhang
publisher: arXiv
publish_year: 2025
doi: 10.48550/arXiv.2509.04664
url: https://arxiv.org/abs/2509.04664
scope: open
licence: Creative Commons Attribution 4.0 International (CC BY 4.0)
ingested: 2026-07-15
original_format: official PDF + TeX source archive
converted_via: pandoc 3.9 (official TeX + BBL); cross-checked with pdftotext -layout and markitdown 0.1.5 against the official PDF
original_file: "why-language-models-hallucinate-kalai.pdf"
original_downloaded: 2026-10-15
checksum_sha256: b6a0d4e8de1b3add1044cbf00c59c92e0ca76c7deef5c944d76cb0f16db28950
---

# Source: Why Language Models Hallucinate

Kalai, Nachum, Vempala, and Zhang's two-stage account of language-model
hallucination. The paper reduces generation error in pretrained base models to
an Is-It-Valid binary-classification problem, develops arbitrary-fact and
poor-model lower bounds, and argues that hallucinations persist through
post-training because influential binary evaluations reward guessing while
giving abstention no credit. It proposes explicit confidence targets and
error penalties in mainstream evaluations.

The operator-supplied Markdown in `sources/ingest/` was an explicitly abridged
copy: it omitted the proof appendices and full bibliography. At the operator's
request, ingestion used the complete official arXiv submission instead. The
official 36-page PDF and official TeX source archive were acquired from arXiv.
The PDF (arXiv:2509.04664v1) sits beside this card as
`why-language-models-hallucinate-kalai.pdf`, downloaded from arXiv on
2026-10-15; its sha256 is
`b6a0d4e8de1b3add1044cbf00c59c92e0ca76c7deef5c944d76cb0f16db28950`, the
checksum recorded at ingestion. The TeX source archive is not kept in this
corpus.

The canonical tape at
[`sources/converted/why-language-models-hallucinate-kalai.md`](../converted/why-language-models-hallucinate-kalai.md)
was produced from the official TeX body and BBL bibliography using pandoc 3.9.
The abstract was preserved from the official TeX. The bibliography follows the
appendices in the tape because it was converted from the separate submitted BBL
file. The tape contains all body sections, six appendices, eight
footnotes, and 94 bibliography entries.

Conversion caveat: section coverage and the 94-entry count do not make the
tape citation-complete. Checked against the PDF on 2026-10-15:

- Most in-text citations lost their author names and years in conversion
  ("The most closely related theoretical work is by , which…"), so the tape
  alone cannot say who is cited where.
- Nine bibliography titles are damaged: "GPT4All" (Anand et al. 2023),
  "BBQ" (Parrish et al. 2022) and "MuSR" (Sprague et al. 2024) are dropped,
  leaving titles that start with a colon; "NPHardEval" reads "ardEval" (Fan
  et al. 2024) and "SelfCheckGPT" reads "elfCheckGPT" (Manakul et al. 2023);
  OpenAI 2023a reads "-4 Technical Report" for "GPT-4 Technical Report";
  OpenAI 2025a reads "echnical Report"; McAllester and Schapire 2000 reads
  "GoodTuring" for "Good–Turing"; and Xu, Mai and Liang 2025 ("HELM
  Capabilities: Evaluating LMs Capability by Capability") has no title.
- The PDF has nine numbered footnotes; the tape has eight. Table 1's
  footnote (PDF footnote 3: the access date, route and model version for each
  dissertation-title query, and that none of the models searched the Web) is
  missing, so tape footnotes 3–8 are PDF footnotes 4–9. The author
  affiliations (OpenAI; Georgia Tech) and the two author notes (contact
  emails; Vempala's NSF and Simons support) are also missing.
- Appendix F's pointer to Table 2 reads "(page )" for "(page 14)".

The PDF beside this card resolves all of these.

Completeness was cross-checked against two independent deterministic PDF
conversions: `pdftotext -layout` (36 page breaks, approximately 16,000 words)
and markitdown 0.1.5 (approximately 26,000 words including extraction noise).
The cleaner TeX+BBL tape is approximately 14,900 words and contains the full
section and theorem sequence visible in the PDF.

Full image scope was selected. All three substantive assets in the official
TeX package were visually inspected and retained under
`sources/converted/why-language-models-hallucinate-images/`: Figure 1's IIV
diagram and the pretraining/post-training calibration panels that compose
Figure 2. Their mappings are recorded in `sources/converted/IMAGE-INDEX.yaml`.

Deep reference:
[`references/why-language-models-hallucinate-kalai-deep.md`](../../references/why-language-models-hallucinate-kalai-deep.md).
Light reference:
[`references/why-language-models-hallucinate-kalai.md`](../../references/why-language-models-hallucinate-kalai.md).
Pass I audit:
[`references/_audit/_ingest_pass_I_why-language-models-hallucinate-kalai_source_audit.md`](../../references/_audit/_ingest_pass_I_why-language-models-hallucinate-kalai_source_audit.md).
