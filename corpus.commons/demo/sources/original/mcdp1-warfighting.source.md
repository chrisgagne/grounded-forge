---
title: "MCDP 1: Warfighting"
author: "U.S. Marine Corps"
publisher: "Headquarters United States Marine Corps, Department of the Navy"
publish_year: 1997
publication_id: "PCN 142 000006 00"
supersedes: "FMFM 1 Warfighting (1989)"
url: "https://www.marines.mil/Portals/1/Publications/MCDP%201%20Warfighting.pdf"
scope: open
licence: unverified
ingested: 2026-05-21
original_format: pdf
converted_via: "pdftotext -remove-hyphens soft (poppler 26.08.0); cover page by tesseract 5.5.3 OCR of a 300-dpi greyscale pdftoppm render; six OCR corrections, each checked against the page image (listed below)"
checksum_sha256: 51008277a48f89dc4f302715764461086a5e616d520a41b71bdbd3f8f35097c0
---

# Source: MCDP 1 Warfighting (US Marine Corps, 1997)

The U.S. Marine Corps' warfighting philosophy; the Foreword calls the publication "the authoritative basis for how we fight and how we prepare to fight." About 100 pages (printed pagination runs to 106); Foreword + Preface + 4 chapters + Notes. Supersedes FMFM 1 (Fleet Marine Force Manual 1), *Warfighting*, first published in 1989, whose intent, in the words of General A. M. Gray, 29th Commandant of the Marine Corps, was "to describe my philosophy on warfighting." MCDP 1 "refines and expands" that philosophy; General C. C. Krulak, Commandant of the Marine Corps, states in the Foreword his intent to revise it "while retaining the spirit, style, and essential message of the original."

Licence unverified. The cover carries Distribution Statement A, "Approved for public release; distribution is unlimited" (PCN 142 000006 00); the imprint reads "© 1997 United States Government as represented by the Secretary of the Navy. All rights reserved." The source states no other licence; scope `open` rests on the distribution statement.

Cited thinkers: the Notes credit John Boyd with the OODA loop (his lecture "The Patterns of Conflict", Notes 18 of Ch 2) and with implicit communication as a command tool (Notes 5 of Ch 4), and cite William S. Lind's 1985 *Maneuver Warfare Handbook* for *reconnaissance pull* and *command push* (Notes 11 of Ch 4). Clausewitz's *On War* is cited in 15 notes, more than any other work; the Notes call it and Sun Tzu's *The Art of War* essential reading for Marine officers.

The original is the official PDF at the canonical URL above, fetched from its 2026-03-22 Wayback capture because the live marines.mil host 403s automated clients (`mcdp1-warfighting.pdf`, 115 pages, SHA256 `51008277a48f89dc4f302715764461086a5e616d520a41b71bdbd3f8f35097c0`; PCN 142 000006 00, foreword dated 20 June 1997). Its text layer is publisher OCR. Converted with pdftotext rather than markitdown, which reorders lines on this PDF. `-remove-hyphens soft` keeps the line-end hyphens pdftotext's default deletes, so a true compound split across a line (*self-reliant*, *no-win*, *mission-type*, *ever-increasing*) keeps its hyphen; a word split across a line reads as `un-` / `certainty`, which `scripts/check-verbatim.py` rejoins. The cover (page 1) is an image with no text layer, so its text is tesseract OCR, placed before the first page break. Footnote reference numbers are glued to the words they follow, and the text layer garbles some of them (`'8` for 18, `°` for 10); they are left as the text layer has them. Converted text SHA256 `dabeb5c0f06ce72238c3b427deb29bd3ea7587b73e863afa38ca57c08fe7163a`. The deep reference was written from an earlier plain-text OCR of the same edition with heavier character errors; its quotations were re-checked against this conversion with `scripts/check-verbatim.py` on 2026-10-15.

**OCR corrections.** Each was checked against the page image. The five in the text layer were also read again by tesseract from a 300-dpi render of the page, and tesseract agrees with the page. Each OCR string occurs once in the conversion, so the replacements are exact.

| PDF page | OCR text | Page reads |
|---|---|---|
| 1 (cover, tesseract) | `EMPER FIDELIS,` | `SEMPER FIDELIS` (the emblem's ribbon) |
| 45 | `firepower. it is a direct` | `firepower. It is a direct` |
| 55 | `Which, f eliminated,` | `Which, if eliminated,` |
| 67 | `the behavior of"yes-men"-—-will` | `the behavior of "yes-men"—will` |
| 70 | `admit mistakes ajid discuss` | `admit mistakes and discuss` |
| 87 | `un-` / `certainly, disorder` | `un-` / `certainty, disorder` |

Deep reference: [`corpus.local/aarbuddy/references/mcdp1-warfighting-deep.md`](../../references/mcdp1-warfighting-deep.md). Light reference: [`corpus.local/aarbuddy/references/mcdp1-warfighting.md`](../../references/mcdp1-warfighting.md). Pass I audit: [`corpus.local/aarbuddy/references/_audit/_ingest_pass_I_mcdp1-warfighting_source_audit.md`](../../references/_audit/_ingest_pass_I_mcdp1-warfighting_source_audit.md).

**Cross-corpus note.** The same edition is ingested in the public-tier `corpus.commons/demo/` corpus under slug-id `00q`. Both corpora hold the same converted source, deep reference and light reference; the audits in `corpus.commons/demo/references/_audit/` cover both.

**Companion volume in the corpus.** Coram's *Boyd: The Fighter Pilot Who Changed the Art of War* (slug 081) — the biographical / intellectual source of the OODA-loop / maneuver-warfare framework MCDP-1 codifies.
