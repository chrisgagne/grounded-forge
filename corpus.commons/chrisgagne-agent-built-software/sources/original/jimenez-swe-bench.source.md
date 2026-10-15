---
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
author: Carlos E. Jimenez; John Yang; Alexander Wettig; Shunyu Yao; Kexin Pei; Ofir Press; Karthik Narasimhan
publisher: ICLR 2024 (conference paper); arXiv preprint
publish_year: 2024
version: arXiv:2310.06770v3 [cs.CL], 11 Nov 2024 (v1 10 Oct 2023; v2 5 Apr 2024)
url: https://arxiv.org/abs/2310.06770
doi: 10.48550/arXiv.2310.06770
scope: open
licence: CC BY 4.0
ingested: 2026-10-01
original_format: pdf
converted_via: "pdftotext (poppler 26.08.0), run one page at a time with a {page-N} marker inserted before each page; N is the PDF page index, which equals the printed page number on all 52 pages. markitdown 0.1.5 was tried first and set aside because it dropped the spaces between words."
checksum_sha256: f7e8e1df64129742b8199a21a042734519a823a1dafd6f48f8f3ddcfb48ee296
image_scope: text-only (no figure visually inspected; ten figures in the PDF)
---

# Source: SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (Jimenez et al.)

The ICLR 2024 paper as posted to arXiv in version 3 (11 Nov 2024), 52 pages including Appendices A–F, supplied as a PDF, now `sources/original/jimenez-swe-bench.pdf`. The licence, CC BY 4.0, comes from the arXiv listing, which links http://creativecommons.org/licenses/by/4.0/; the PDF itself states none. arXiv subjects: cs.CL, cs.AI, cs.SE.

Converted deterministically with pdftotext, page by page. The tape runs to 4,441 lines and 22,194 words (22,142 text words plus 52 page markers), all 52 pages, ending on the last case table's discussion and printed page 52. markitdown ran to 18,331 words because it dropped the spaces between words through much of the text (on a whitespace split, 1,401 tokens of 25 or more characters against 283 in pdftotext's output; 1,138 against 33 leaving out tokens with a slash or underscore), so it was not used. The paper is single-column; pdftotext sets table cells out one per line, so table figures in the deep reference were read against `pdftotext -layout` output of the same page. pdftotext joins words split at a line-end hyphen, occasionally dropping a real hyphen ("state-ofthe-art", p. 1). Two gaps are in the PDF itself: a sentence in §2.4 points to a missing location, and Appendix A.7 stops mid-sentence.

Converted text: [`../converted/jimenez-swe-bench.md`](../converted/jimenez-swe-bench.md). Deep reference: [`../../references/jimenez-swe-bench-deep.md`](../../references/jimenez-swe-bench-deep.md). Light reference: [`../../references/jimenez-swe-bench.md`](../../references/jimenez-swe-bench.md).
