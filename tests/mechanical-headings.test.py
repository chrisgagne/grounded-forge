#!/usr/bin/env python3
"""Heading-extraction regression tests — the journal-article class.

Locks in the behaviour of `scripts/mechanical_index/handlers/headings.py` and
the tier it drives in `scripts/mechanical_index/dispatch.py`.

The regression it exists to prevent: journal PDFs converted by markitdown /
pymupdf4llm emit their section spine as plain body lines (`3.11. Others`,
`2.1. Polysaccharides and dietary fibers`), with no markdown `#`. The extractor
recognised only book-shaped conventions, so a paper produced an empty heading
tree, fell through to tier `inference-only`, and `concept-index.json` got no
in-source section pointers for it. Two ingestion agents hit this independently
on a private corpus made up almost entirely of journal articles.

The hard half is precision, not recall. Reference-list entries, numbered
procedure steps, restarting enumerations and measurement table rows all open
with the same shape, and a section pointer aimed at the wrong passage is worse
than no pointer at all. So half the cases below are false-positive controls,
and one is the book-shaped path — the currently-working convention, which
matters more than the new one.

No test framework, matching tests/derived-provenance.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/mechanical-headings.test.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.mechanical_index.dispatch import run  # noqa: E402
from scripts.mechanical_index.handlers import headings  # noqa: E402

FILLER = "and the sampled cones were then weighed before oven drying overnight.\n"


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def build_doc(entries: list[tuple[int, str]], total: int = 400) -> list[str]:
    """Place ``(line_number, text)`` pairs into a document of filler prose.

    Filler matters: the corroboration gates are document-relative, so a
    fixture that is only its own headings would pass tests the real thing
    would fail.
    """
    lines = [FILLER] * total
    for lineno, text in entries:
        assert_(1 <= lineno <= total, f"fixture line {lineno} outside the document")
        lines[lineno - 1] = text + "\n"
    return lines


def numbered(lines: list[str]) -> list[dict]:
    return [h for h in headings.extract(lines) if h["kind"] == "numbered-plaintext"]


def titles(records: list[dict]) -> list[str]:
    return [r["title"] for r in records]


# ─── the shape we are trying to recognise ─────────────────────────────────────

# Modelled on a converted two-column review article, which has zero `#`.
JOURNAL_SPINE = [
    (20, "1. Introduction"),
    (55, "1.1. Distribution, consumption, and economic potential of the material"),
    (90, "2. Chemical composition"),
    (125, "2.1. Polysaccharides and dietary fibers"),
    (160, "2.2. Proteins, peptides, and amino acids"),
    (195, "3. Health effects"),
    (230, "3.11. Others"),
    (265, "4. Processing and storage"),
    (300, "5.1.1. Beverages"),
    (340, "6. Conclusions and perspectives"),
]


def case_journal_spine_is_extracted() -> None:
    found = numbered(build_doc(JOURNAL_SPINE))
    assert_(
        len(found) == len(JOURNAL_SPINE),
        f"expected the whole spine; got {titles(found)}",
    )
    assert_(
        titles(found) == [t for _, t in JOURNAL_SPINE],
        f"titles should survive verbatim, in line order; got {titles(found)}",
    )
    assert_(
        [f["line"] for f in found] == [n for n, _ in JOURNAL_SPINE],
        "line numbers should be 1-based positions in the source",
    )


def case_level_comes_from_number_depth() -> None:
    by_title = {h["title"]: h["level"] for h in numbered(build_doc(JOURNAL_SPINE))}
    assert_(by_title["1. Introduction"] == 1, "``1.`` is a level-1 section")
    assert_(by_title["3.11. Others"] == 2, "``3.11.`` is a level-2 section, not level 11")
    assert_(by_title["5.1.1. Beverages"] == 3, "``5.1.1.`` is a level-3 section")


def case_column_interleaving_is_tolerated() -> None:
    """Two-column PDFs deliver a real spine partly out of order.

    One two-column review emits ``3.3``, ``3.4``, ``3.1``, ``3.5``, ``3.2`` in that
    reading order, and ``4.`` before ``3.8``. A strict monotonic gate would
    throw the whole paper away.
    """
    scrambled = [
        (20, "1. Introduction"),
        (55, "2. Chemical composition"),
        (90, "3. Health effects"),
        (125, "3.3. Immunomodulatory activity"),
        (160, "3.4. Anti-inflammatory activity"),
        (195, "3.1. Allergenicity"),
        (230, "3.5. Glucose and lipid metabolism regulatory activity"),
        (265, "3.2. Antioxidant activity"),
        (300, "4. Processing and storage"),
        (330, "3.8. Hepatoprotective activity"),
        (360, "5. Applications in the food industry"),
    ]
    found = numbered(build_doc(scrambled))
    assert_(len(found) == len(scrambled), f"interleaved spine should survive; got {titles(found)}")


def case_no_subsections_still_works() -> None:
    """A flat IMRaD spine is legitimate; it just has to be longer to earn trust."""
    flat = [
        (20, "1. Introduction"),
        (90, "2. Materials and methods"),
        (170, "3. Results"),
        (250, "4. Discussion"),
        (330, "5. Conclusions"),
    ]
    found = numbered(build_doc(flat))
    assert_(len(found) == len(flat), f"flat spine should be recognised; got {titles(found)}")


# ─── false-positive controls ──────────────────────────────────────────────────


def case_reference_list_is_not_a_spine() -> None:
    """The canonical look-alike: `12. Smith, J. (2019)...` shares the shape."""
    refs = [
        (200, "References"),
        (210, "1. Addison S, Armstrong C, Wigley K. What matters most? Environ Microbiome. 2023;18(1):45."),
        (215, "2. Agarwal VK, Sinclair JB. Principles of seed pathology. 2nd ed. Boca Raton: CRC Press; 1997."),
        (220, "3. Anderson MJ. A new method for non-parametric multivariate analysis of variance."),
        (225, "4. Burdon R, Libby W, Brown A. Domestication of forest trees. Cham: Springer; 2017."),
        (230, "5. Callahan BJ, McMurdie PJ, Rosen MJ. DADA2: high-resolution sample inference."),
        (380, "32. Association of Official Seed Analysts, Michigan, United States. 88 p."),
    ]
    found = numbered(build_doc(refs))
    assert_(not found, f"reference entries must not become headings; got {titles(found)}")


def case_body_spine_survives_a_trailing_reference_list() -> None:
    """The realistic file: a real spine, then a reference list under it."""
    doc = build_doc(
        JOURNAL_SPINE
        + [
            (355, "References"),
            (360, "1. Chen Y, Wang Z, Quan W. A review of chemical composition."),
            (365, "2. Li Q, Shan X, Zhao Y. Structural characterisation of a polysaccharide."),
            (370, "3. Shan X, Wang T, Qu T. Antioxidant activity of plant extracts."),
            (375, "4. Wang T, Xue C, Qu T. Wall disruption improves bioaccessibility."),
        ]
    )
    found = numbered(doc)
    assert_(
        titles(found) == [t for _, t in JOURNAL_SPINE],
        f"the body spine should be kept and the reference list dropped; got {titles(found)}",
    )


def case_numbered_procedure_steps_are_not_a_spine() -> None:
    """Steps inside Methods cluster locally; a section spine does not."""
    steps = [
        (100, "1. Weigh the cone sample"),
        (104, "2. Oven dry for four hours"),
        (108, "3. Separate the fertile scales"),
        (112, "4. Record the filled seed count"),
        (116, "5. Repeat for the second collection"),
        (120, "6. Report the mean and standard deviation"),
    ]
    found = numbered(build_doc(steps))
    assert_(not found, f"a local procedure list is not a section spine; got {titles(found)}")


def case_restarting_enumerations_are_not_a_spine() -> None:
    """bramlett-etal-1977: three numbered lists, each restarting at 1.

    Spread across the document and individually heading-shaped, so only the
    repeated numbering distinguishes them from a real spine.
    """
    enumerations = [
        (40, "1. Seed potential"),
        (60, "2. Total developed seeds"),
        (80, "3. Percent developed seeds"),
        (100, "4. Percent filled seeds"),
        (180, "1. First-year aborted ovules"),
        (200, "2. Second-year aborted ovules"),
        (220, "3. Percent filled seeds"),
        (240, "4. Insect-damaged seeds"),
        (300, "1. Filled"),
        (320, "2. Partially filled"),
        (340, "3. Empty"),
    ]
    found = numbered(build_doc(enumerations))
    assert_(not found, f"restarting enumerations are not a spine; got {titles(found)}")


def case_table_rows_and_measurements_are_not_headings() -> None:
    """Measurement rows, running page headers and affiliations all lead with
    digits. None of them survive the per-line shape test, so the set never
    reaches corroboration."""
    noise = [
        (20, "6.41 ± 0.07"),
        (60, "1054.9 ± 12.0"),
        (100, "0.5 mL/100 g b.w./24 h p.o."),
        (140, "3.52 mg/g (Chen et al., 2021; Li et al., 2015; Shan et al., 2019). The"),
        (180, "1440 G. Gastaminza et al"),
        (220, "2 of 16"),
        (260, "1 Department of Orthopedics and Traumatology, Provincial Specialist Hospital"),
        (300, "20 cones terminating the second cycle were observed from clones 55, 89, and 274"),
        (340, "1985 CONES"),
    ]
    found = numbered(build_doc(noise))
    assert_(not found, f"numeric body lines must not become headings; got {titles(found)}")


def case_prose_enumeration_with_sequence_adverb_is_rejected() -> None:
    """A real spine plus one body enumeration item that reuses a number.

    ``10. Second, the matrix invites empirical validation...`` appears in
    sorensen-innovators-dilemma-agents.md. It is heading-length and starts
    with a capital; the sequence adverb is what gives it away.
    """
    doc = build_doc(JOURNAL_SPINE + [(360, "10. Second, the trust-context matrix invites empirical validation")])
    found = numbered(doc)
    assert_(
        titles(found) == [t for _, t in JOURNAL_SPINE],
        f"the prose enumeration item should be dropped; got {titles(found)}",
    )


# ─── the currently-working path must not move ────────────────────────────────


def case_book_shaped_source_is_unchanged() -> None:
    """Markdown headings plus the bolded numbered questions that fill the
    openstax / flo sources. Convention 4 must add nothing here."""
    doc = build_doc(
        [
            (10, "# Organizational Behavior"),
            (40, "## 12.1 The Nature of Leadership"),
            (70, "### Managerial Leadership"),
            (100, "**1. How do I feel about the session? Reflect on the strategies you used**"),
            (110, "**2. What do I like about what I did? Think about the aspects you felt good**"),
            (120, "**3. What do I want to improve or do differently? Consider what you would**"),
            (130, "**4. What were the key points about the feedback I received?**"),
            (200, "## 12.2 Early Approaches to the Study of Leadership"),
            (300, "## Chapter Review Questions"),
        ]
    )
    found = headings.extract(doc)
    kinds = {h["kind"] for h in found}
    assert_(kinds == {"markdown"}, f"only markdown headings should be found; got {kinds}")
    assert_(len(found) == 5, f"expected the 5 markdown headings; got {titles(found)}")


def case_allcaps_and_anchor_conventions_still_fire() -> None:
    doc = build_doc(
        [
            (19, ""),
            (20, "INTRODUCTION"),
            (21, ""),
            (59, ""),
            (60, "MATERIALS AND METHODS"),
            (61, ""),
            (100, "[]{#page_12}"),
        ]
    )
    found = headings.extract(doc)
    kinds = sorted(h["kind"] for h in found)
    assert_(
        kinds == ["allcaps", "allcaps", "anchor-only"],
        f"the three original conventions must be untouched; got {kinds}",
    )


def case_one_line_is_claimed_once() -> None:
    """A numbered ALL-CAPS label must not be emitted by two conventions."""
    doc = build_doc(
        [
            (20, ""),
            (21, "1. INTRODUCTION"),
            (22, ""),
            (90, "2. MATERIALS AND METHODS"),
            (170, "3. RESULTS AND DISCUSSION"),
            (250, "4. CONCLUSIONS"),
            (330, "5. ACKNOWLEDGEMENTS"),
        ]
    )
    found = headings.extract(doc)
    lines_seen = [h["line"] for h in found]
    assert_(
        len(lines_seen) == len(set(lines_seen)),
        f"no line should produce two heading records; got {sorted(lines_seen)}",
    )


# ─── the tier the dispatcher derives from it ─────────────────────────────────


def case_dispatch_derives_numbered_sections_tier() -> None:
    record = run(build_doc(JOURNAL_SPINE), {"slug": "fixture-journal"})
    assert_(
        "numbered-sections" in record["derived_tier"],
        f"a paper with a section spine should carry its own tier; got {record['derived_tier']}",
    )
    assert_(
        "inference-only" not in record["derived_tier"],
        f"a spine is a mechanical artefact, not an inference; got {record['derived_tier']}",
    )
    assert_(
        len(record["headings"]) == len(JOURNAL_SPINE),
        "the spine should reach the extraction record",
    )


def case_dispatch_still_falls_through_to_inference_only() -> None:
    """The fallback must survive: a source with no extractable artefact at all."""
    record = run(build_doc([(20, "# A Book"), (100, "## A Chapter")]), {"slug": "fixture-book"})
    assert_(
        record["derived_tier"] == ["inference-only"],
        f"markdown headings alone are still inference-only; got {record['derived_tier']}",
    )


# ─── on-disk corroboration (skipped when the corpus is absent) ───────────────

# The spot-check list names private sources, so it lives beside them in
# gitignored corpus.local as {"corpus.local/.../slug.md": min_sections}.
LOCAL_SOURCES_FILE = REPO_ROOT / "corpus.local" / "mechanical-headings-sources.json"


def real_sources() -> dict[str, int]:
    if not LOCAL_SOURCES_FILE.is_file():
        return {}
    return json.loads(LOCAL_SOURCES_FILE.read_text(encoding="utf-8"))


def case_real_journal_articles_on_disk() -> None:
    """Spot-check against converted sources when they are present locally.

    corpus.local is gitignored, so this is advisory: absent files skip.
    """
    checked = 0
    for rel, minimum in real_sources().items():
        path = REPO_ROOT / rel
        if not path.is_file():
            continue
        found = numbered(path.read_text(encoding="utf-8").splitlines(keepends=True))
        assert_(
            len(found) >= minimum,
            f"{rel}: expected at least {minimum} numbered sections, got {len(found)}",
        )
        checked += 1
    if not checked:
        print("       (no on-disk journal sources present — skipped)")


CASES = [
    case_journal_spine_is_extracted,
    case_level_comes_from_number_depth,
    case_column_interleaving_is_tolerated,
    case_no_subsections_still_works,
    case_reference_list_is_not_a_spine,
    case_body_spine_survives_a_trailing_reference_list,
    case_numbered_procedure_steps_are_not_a_spine,
    case_restarting_enumerations_are_not_a_spine,
    case_table_rows_and_measurements_are_not_headings,
    case_prose_enumeration_with_sequence_adverb_is_rejected,
    case_book_shaped_source_is_unchanged,
    case_allcaps_and_anchor_conventions_still_fire,
    case_one_line_is_claimed_once,
    case_dispatch_derives_numbered_sections_tier,
    case_dispatch_still_falls_through_to_inference_only,
    case_real_journal_articles_on_disk,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        try:
            case()
            print(f"  ok   {case.__name__}")
        except Exception as e:  # noqa: BLE001 — test runner reports any failure
            failures.append(f"{case.__name__}: {e}")
            print(f"  FAIL {case.__name__}: {e}")

    print()
    if failures:
        print(f"mechanical-headings: {len(failures)} of {len(CASES)} cases FAILED")
        return 1
    print(f"mechanical-headings: all {len(CASES)} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
