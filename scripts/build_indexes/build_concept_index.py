"""Assemble ``concept-index.json`` from per-source extracted artefacts plus
a Sonnet cross-link pass that decides aliasing/merging.

Pipeline (Phase 3):

  1. Python aggregates raw concept candidates from
     ``_planning/extracted/{corpus}/*.json``: every ``book_index_entries``
     concept text and every ``enumerated_methods`` name across every source.
     This is the candidate vocabulary, large and redundant by design.

  2. Python writes the merged candidate list to
     ``_planning/staging/{corpus}/concepts/candidates.json``. This artefact
     is the *input* to the Sonnet cross-link pass.

  3. A Sonnet sub-agent reads the candidates, makes alias / merge / novel
     decisions, and writes
     ``_planning/staging/{corpus}/concepts/decisions.json``. The spec calls
     out (§"Anti-patterns to avoid") that this step MUST be the LLM; regex
     cannot adjudicate aliases, vocabulary variation, related-but-distinct.

  4. Python reads the decisions, applies them to the candidate vocabulary,
     resolves slug → ID, and writes ``concept-index.json``.

Steps 1, 2, 4 are mechanical and live in this script. Step 3 is the human
(or orchestrator) running the Sonnet pass with the staging artefacts.

Usage:

    # Step 1+2 (aggregation): emit candidates for the Sonnet pass.
    python -m scripts.build_indexes.build_concept_index --corpus demo \\
        --emit-candidates

    # Step 4 (after Sonnet decisions land): assemble final index.
    python -m scripts.build_indexes.build_concept_index --corpus demo \\
        --assemble

Decision-file schema (written by the Sonnet pass):

    {
      "schema_version": 1,
      "decisions": [
        {
          "canonical": "agile-theatre",
          "name": "Agile Theatre / Aping the Lingo",
          "aliases": ["agile theatre", "aping the lingo"],
          "sources": [
            {"slug": "meyer-...", "lines": [100, 200], "context": "..."}
          ]
        },
        ...
      ]
    }

The decision-file is the LLM's *output*; the script trusts it and emits
``concept-index.json`` mechanically from it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from .common import (
    corpus_root,
    extracted_path,
    index_output_dir,
    load_slug_table,
    repo_root,
    slug_to_id,
    staging_dir,
)


_KEBAB_SPLIT = re.compile(r"[-_]+")


def _kebab_to_phrase(name: str) -> str:
    """`five-core-properties` → `five core properties`."""
    return _KEBAB_SPLIT.sub(" ", name).strip().lower()


def _section_for_line(headings: list[dict], target_line: int) -> str | None:
    """Find the most recent heading whose ``line`` is <= target_line.

    The heading tree is flat with ``{level, title, line}`` entries; the
    section containing a given line is the most-recent heading before it.
    Returns the cleaned title (without markdown emphasis markers) and
    filters generic front/back-matter headings like ``**CONTENTS**`` that
    don't name a body section.
    """
    if not headings or target_line is None:
        return None
    best: dict | None = None
    for h in headings:
        line = h.get("line")
        if line is None or line > target_line:
            break
        best = h
    if not best:
        return None
    title = _clean_heading_title(best.get("title", ""))
    if not title or _is_blocked_heading(title):
        return None
    return title


def _build_extracted_lookup(corpus: str, slug_id: dict[str, str]) -> dict[str, dict]:
    """For each source, build a lookup over two body-anchored surfaces:

    - ``methods``: ``{normalised_method: {line, section}}`` from
      ``enumerated_methods`` entries with a resolved ``located_line``.
      These are author-curated method names, hand-located by the
      discovery scan → highest-confidence body anchor.
    - ``headings``: the source's full heading tree
      (``[{level, title, line}]``). Used at assembly time to do a
      substring match between concept names and heading titles: the
      runtime-routing surface most operators expect.

    ``book_index_entries`` are intentionally excluded. They live in the
    back-matter index region and resolving them to ``section=**A**``
    or ``Index`` tells the runtime nothing useful; it just reports
    that the source has an index. Page-marker resolution to body lines
    is also skipped here; ~17 demo sources have empty page-marker maps,
    and the partial coverage would mislead more than it helps.
    """
    extracted_dir = repo_root() / "_planning" / "extracted" / corpus
    if not extracted_dir.is_dir():
        return {}

    lookup: dict[str, dict] = {}
    for path in sorted(extracted_dir.glob("*.json")):
        with path.open("r", encoding="utf-8") as f:
            record = json.load(f)
        raw_slug = record.get("slug") or path.stem
        slug = raw_slug.removesuffix(".md") if isinstance(raw_slug, str) else raw_slug
        rid = slug_id.get(slug)
        if rid is None:
            continue
        headings = record.get("headings", [])
        methods: dict[str, dict] = {}

        for e in record.get("enumerated_methods", []):
            name = e.get("method_description") or e.get("name")
            if not name:
                continue
            key = _normalise(name)
            if not key or key in methods:
                continue
            line = e.get("located_line")
            if not line:
                continue  # no body line to anchor
            section = _section_for_line(headings, line)
            methods[key] = {"line": line, "section": section}

        lookup[rid] = {
            "methods": methods,
            "headings": headings,
        }
    return lookup


_HEADING_NOISE_CHARS = re.compile(r"[*_`#]")
_HEADING_BLOCKLIST = {
    "contents",
    "table of contents",
    "index",
    "references",
    "bibliography",
    "glossary",
    "acknowledgements",
    "acknowledgments",
    "preface",
    "foreword",
}


def _clean_heading_title(title: str | None) -> str:
    if not title:
        return ""
    return _HEADING_NOISE_CHARS.sub("", title).strip()


def _is_blocked_heading(title: str) -> bool:
    """Front-matter / back-matter heading names that aren't body sections.

    A heading whose entire cleaned title is one of the blocked names
    (e.g. ``**CONTENTS**`` → ``contents``) anchors at the front-matter
    TOC or back-matter glossary, not a body discussion of the concept.
    Substring match against these reliably mis-resolves.
    """
    return title.strip().lower() in _HEADING_BLOCKLIST


_LEADING_NUMBERING = re.compile(r"^\s*(?:ch(?:apter)?\s*)?\d+(?:\.\d+)*\.?\s*", re.IGNORECASE)


def _strip_section_numbering(title: str) -> str:
    """Strip leading numbering like ``12.1`` or ``Chapter 1`` from a heading.

    Used so the substring match treats ``12.1 The Nature of Leadership``
    as matching ``the nature of leadership`` cleanly.
    """
    return _LEADING_NUMBERING.sub("", title).strip()


def _heading_match(headings: list[dict], phrases: list[str]) -> dict | None:
    """Find the heading whose title most naturally names one of the
    given concept phrases.

    Scoring prefers (in order):

    1. Exact match between the heading's stripped title and the phrase.
    2. Title that *starts with* the phrase (modulo numbering).
    3. Title where the phrase is a substring.

    Tie-breaker: shallower headings (numbered chapter sections like
    ``12.1 The Nature of Leadership``) win over deeper leaf headings
    (``Visible Leadership`` buried elsewhere), because the chapter
    section names the concept's primary treatment.

    Phrases shorter than 4 characters are ignored (avoids matching
    generic single letters / digits).
    """
    if not headings or not phrases:
        return None
    norm_phrases = [p.lower() for p in phrases if p and len(p) >= 4]
    if not norm_phrases:
        return None

    best: dict | None = None
    best_score = -1
    for h in headings:
        title = _clean_heading_title(h.get("title", ""))
        if not title or _is_blocked_heading(title):
            continue
        stripped = _strip_section_numbering(title).lower()
        norm_title = title.lower()
        for phrase in norm_phrases:
            if not phrase:
                continue
            match_quality = 0
            if stripped == phrase:
                match_quality = 1000
            elif stripped.startswith(phrase + " ") or stripped.endswith(" " + phrase):
                match_quality = 500
            elif phrase in stripped:
                match_quality = 250
            elif phrase in norm_title:
                match_quality = 100
            else:
                continue

            # Shallower headings win on the level tiebreaker.
            level = h.get("level") or 6
            level_bonus = max(0, 10 - level)  # level 1 → +9, level 5 → +5
            # Shorter titles win on the length tiebreaker (fewer extra words).
            length_penalty = min(len(title), 200) // 10
            score = match_quality + level_bonus - length_penalty
            if score > best_score:
                best_score = score
                best = {
                    "title": title,
                    "line": h.get("line"),
                }
            break
    return best


def _section_pointer(
    extracted_lookup: dict[str, dict],
    rid: str,
    canonical: str,
    aliases: list[str],
    name: str | None,
) -> dict | None:
    """Resolve a concept to a body section + line in a specific source.

    Two-tier matching:

    1. **Enumerated methods** (highest confidence). If the source's
       discovery scan named this concept and the preprocessor located
       it on a body line, return that line + its enclosing heading.
    2. **Heading-tree substring match**. Look for a body heading whose
       title contains the canonical / alias / display name as a
       substring. Used when no enumerated-method match exists but the
       concept names a section directly (e.g., concept "leadership"
       matches heading "12.1 The Nature of Leadership").

    Returns ``None`` when no body anchor can be resolved; the runtime
    can still locate the source via the slug-ID alone.
    """
    source_lookup = extracted_lookup.get(rid)
    if not source_lookup:
        return None

    # Variant set for matching.
    phrase_variants: list[str] = []
    for c in [canonical] + list(aliases or []):
        if not c:
            continue
        phrase_variants.append(c.lower())
        phrase_variants.append(_kebab_to_phrase(c))
    if name:
        phrase_variants.append(name.strip().lower())
    # De-dupe preserving order.
    seen: set[str] = set()
    phrase_variants = [
        p for p in phrase_variants if not (p in seen or seen.add(p))
    ]

    # Tier 1: enumerated_methods.
    methods = source_lookup.get("methods", {})
    for key in phrase_variants:
        hit = methods.get(key)
        if hit:
            return {
                "section": hit.get("section"),
                "md_line": hit.get("line"),
                "via": "enumerated_method",
            }

    # Tier 2: heading-tree substring match.
    heading_hit = _heading_match(
        source_lookup.get("headings", []), phrase_variants
    )
    if heading_hit:
        return {
            "section": heading_hit.get("title"),
            "md_line": heading_hit.get("line"),
            "via": "heading_match",
        }

    return None


_WHITESPACE = re.compile(r"\s+")
_TRAILING_PAGE_NUMBERS = re.compile(r"(?:[\s,]+\d{1,4}){1,}\s*$")
_MD_HEADER_NOISE = re.compile(r"^#+\s|^\*\*[A-Z]\*\*$|^\*\*Symbols\*\*$", re.IGNORECASE)


def _strip_trailing_locators(text: str) -> str:
    """Strip the trailing `, page-number, page-number, ...` from a flattened-
    plaintext index entry surface form. ``Access discrimination 130`` →
    ``Access discrimination``; ``360 assessment 503`` → ``360 assessment``.

    Mechanical only. The first numeric run inside the concept name (e.g. the
    leading ``360`` in ``360 assessment``) is preserved.
    """
    return _TRAILING_PAGE_NUMBERS.sub("", text).strip()


def _is_structural_noise(text: str) -> bool:
    """Reject obviously non-concept lines that survived the index region
    cut: section headers like ``##### **A**``, ``## **Index**``, the
    ``**Symbols**`` divider, and pure-numeric strings.
    """
    stripped = text.strip()
    if not stripped:
        return True
    if _MD_HEADER_NOISE.search(stripped):
        return True
    # bare letter dividers (single letter inside asterisks/hash markers)
    if re.fullmatch(r"#+\s*\*{0,2}[A-Z]\*{0,2}", stripped):
        return True
    # pure numeric (just a page number that escaped the index region)
    if re.fullmatch(r"\d+", stripped):
        return True
    return False


def _normalise(text: str) -> str:
    """Light text normalisation for de-duplication only. NOT a semantic merge.

    Strip trailing locators (page numbers), lowercase, collapse whitespace,
    strip surrounding punctuation. Used to bucket textual duplicates inside
    the candidate vocabulary so the Sonnet pass sees one entry per *distinct
    surface form*, not seven copies of the same string from a multi-page
    index.
    """
    t = _strip_trailing_locators(text)
    t = t.strip().lower()
    t = _WHITESPACE.sub(" ", t)
    t = t.strip(".,;:—–-•· ")
    return t


def _collect_candidates(corpus: str, slug_id: dict[str, str]) -> dict:
    """Walk every extracted artefact for the corpus and aggregate raw
    concept candidates by normalised surface form.
    """
    extracted_dir = repo_root() / "_planning" / "extracted" / corpus
    if not extracted_dir.is_dir():
        raise SystemExit(f"ERROR: extracted dir not found: {extracted_dir}")

    candidates: dict[str, dict] = defaultdict(
        lambda: {"surface_forms": [], "sources": []}
    )

    for path in sorted(extracted_dir.glob("*.json")):
        with path.open("r", encoding="utf-8") as f:
            record = json.load(f)
        raw_slug = record.get("slug") or path.stem
        # Preprocessor stores slug as <name>.md (carried through from
        # the discovery JSON which uses filename-as-slug). Strip the
        # extension so it matches the slug-table.
        slug = raw_slug.removesuffix(".md") if isinstance(raw_slug, str) else raw_slug
        rid = slug_id.get(slug)
        if rid is None:
            continue  # source not in slug-table

        for entry in record.get("book_index_entries", []):
            text = entry.get("concept_text")
            if not text or _is_structural_noise(text):
                continue
            key = _normalise(text)
            if not key:
                continue
            surface = _strip_trailing_locators(text)
            cand = candidates[key]
            if surface not in cand["surface_forms"]:
                cand["surface_forms"].append(surface)
            cand["sources"].append(
                {
                    "slug": slug,
                    "id": rid,
                    "origin": "book_index",
                    "kind": entry.get("kind"),
                    "page_locators": entry.get("locators"),
                    "line": entry.get("line"),
                    "parent": entry.get("parent"),
                }
            )

        for entry in record.get("enumerated_methods", []):
            name = entry.get("method_description") or entry.get("name")
            if not name:
                continue
            key = _normalise(name)
            if not key:
                continue
            cand = candidates[key]
            if name not in cand["surface_forms"]:
                cand["surface_forms"].append(name)
            cand["sources"].append(
                {
                    "slug": slug,
                    "id": rid,
                    "origin": "enumerated_method",
                    "located_line": entry.get("located_line"),
                    "located": entry.get("located"),
                }
            )

    return {
        "schema_version": 1,
        "corpus": corpus,
        "candidate_count": len(candidates),
        "candidates": {key: candidates[key] for key in sorted(candidates)},
    }


def _emit_candidates(corpus: str) -> Path:
    """Aggregate per-source extractions into a Sonnet-ready candidate list.

    Two-layer construction:

    - **Curated layer**: every ``concept_tag`` in ``reference-index.json``.
      These are the operator-validated (via Sonnet pass 1) routing tags;
      they form the spine of the concept-index.
    - **Mechanical layer**: enumerated-method names (author-curated) plus
      back-matter book-index entries that appear in *at least two distinct
      source slugs*. Single-source book-index entries are excluded from
      the first build: they bloat the candidate set with verbose textbook
      back-matter without adding cross-source routing capability. Phase 5
      re-runs can promote them as needed.

    The decision file the Sonnet pass writes back must cover both layers.
    """
    slug_table = load_slug_table(corpus)
    slug_id = slug_to_id(slug_table)
    bundle = _collect_candidates(corpus, slug_id)

    # Filter mechanical candidates to high-signal entries only.
    filtered: dict[str, dict] = {}
    for key, cand in bundle["candidates"].items():
        slugs = {s["slug"] for s in cand["sources"]}
        origins = {s.get("origin") for s in cand["sources"]}
        if "enumerated_method" in origins or len(slugs) >= 2:
            filtered[key] = cand

    bundle["candidates"] = filtered
    bundle["candidate_count"] = len(filtered)
    bundle["filter_rule"] = (
        "enumerated_method OR book_index in >=2 distinct source slugs"
    )

    # Curated layer: reference-index concept_tags.
    ref_index_path = corpus_root(corpus) / "reference-index.json"
    if ref_index_path.is_file():
        with ref_index_path.open("r", encoding="utf-8") as f:
            ref_index = json.load(f)
        tag_index: dict[str, list[str]] = {}
        for rid, rec in ref_index["refs"].items():
            for tag in rec.get("concept_tags", []):
                tag_index.setdefault(tag, []).append(rid)
        bundle["curated_tags"] = {
            tag: sorted(ids) for tag, ids in sorted(tag_index.items())
        }
        bundle["curated_tag_count"] = len(tag_index)
    else:
        bundle["curated_tags"] = {}
        bundle["curated_tag_count"] = 0
        bundle["warning"] = (
            f"reference-index.json not found at {ref_index_path}; "
            "build reference-index first to seed curated tags"
        )

    # Slim payload for the Sonnet pass — drop per-source locator metadata
    # the cross-link decision doesn't need. The full extracted artefacts
    # remain available at _planning/extracted/{corpus}/*.json if a decision
    # needs to drill into line ranges.
    slim_candidates: dict[str, dict] = {}
    for key, cand in bundle["candidates"].items():
        slugs_ordered: list[str] = []
        ids_ordered: list[str] = []
        for s in cand["sources"]:
            sid = s.get("id")
            if sid and sid not in ids_ordered:
                ids_ordered.append(sid)
                slugs_ordered.append(s.get("slug"))
        slim_candidates[key] = {
            "surface_forms": cand["surface_forms"][:3],
            "ids": ids_ordered,
            "slugs": slugs_ordered,
            "origins": sorted(
                {s.get("origin") for s in cand["sources"] if s.get("origin")}
            ),
        }

    bundle["candidates"] = slim_candidates

    out_dir = staging_dir(corpus, "concepts")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "candidates.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(
        f"wrote {out_path}: {bundle['candidate_count']} mechanical candidates "
        f"+ {bundle['curated_tag_count']} curated tags across "
        f"{len(slug_table['slugs'])} sources ({out_path.stat().st_size} bytes)"
    )
    return out_path


def _assemble(corpus: str) -> Path:
    slug_table = load_slug_table(corpus)
    slug_id = slug_to_id(slug_table)

    decisions_path = staging_dir(corpus, "concepts") / "decisions.json"
    if not decisions_path.is_file():
        raise SystemExit(
            f"ERROR: decisions file not found at {decisions_path}.\n"
            "Run the Sonnet cross-link pass against candidates.json before --assemble."
        )

    with decisions_path.open("r", encoding="utf-8") as f:
        decisions = json.load(f)

    id_to_slug = {rid: slug for slug, rid in slug_id.items()}
    valid_ids = set(slug_id.values())

    extracted_lookup = _build_extracted_lookup(corpus, slug_id)

    concepts: dict[str, dict] = {}
    drift_log: list[dict] = []
    section_hits = 0
    source_count = 0

    for entry in decisions.get("decisions", []):
        canonical = entry.get("canonical")
        if not canonical:
            continue
        aliases = entry.get("aliases", []) or []
        name = entry.get("name", canonical)
        sources_out = []
        seen_ids: set[str] = set()

        for src in entry.get("sources", []):
            slug = src.get("slug")
            rid = src.get("id")

            # Reconcile slug/id against the slug-table (mechanical source-of-truth).
            # Prefer the ID when it's valid; the cross-link pass occasionally
            # types a slug wrong (LLM mis-spell) but the ID is from the
            # candidates payload we generated mechanically.
            if rid and rid in valid_ids:
                resolved_slug = id_to_slug[rid]
                if slug and slug != resolved_slug:
                    drift_log.append(
                        {
                            "concept": canonical,
                            "decision_slug": slug,
                            "decision_id": rid,
                            "resolved_slug": resolved_slug,
                            "policy": "trusted-id-over-slug",
                        }
                    )
                resolved_id = rid
            elif slug and slug in slug_id:
                resolved_id = slug_id[slug]
                if rid:
                    drift_log.append(
                        {
                            "concept": canonical,
                            "decision_slug": slug,
                            "decision_id": rid,
                            "resolved_id": resolved_id,
                            "policy": "trusted-slug-over-id",
                        }
                    )
            else:
                drift_log.append(
                    {
                        "concept": canonical,
                        "decision_slug": slug,
                        "decision_id": rid,
                        "policy": "dropped-no-resolution",
                    }
                )
                continue

            if resolved_id in seen_ids:
                continue  # de-dupe within a concept
            seen_ids.add(resolved_id)

            rec: dict = {"id": resolved_id}
            if "context" in src and src["context"]:
                rec["context"] = src["context"]
            if "deep" in src:
                rec["deep"] = src["deep"]

            # Attach section + line pointer when the canonical name (or
            # an alias) matches an extracted entry in this source. The
            # `line` is the line in the *converted markdown*, not the
            # original source — pymupdf4llm conversion ate page anchors
            # for most demo sources, so section name is the authoritative
            # in-source navigation marker. Mechanical, opt-in per match.
            pointer = _section_pointer(
                extracted_lookup, resolved_id, canonical, aliases, name
            )
            if pointer:
                if pointer.get("section"):
                    rec["section"] = pointer["section"]
                if pointer.get("md_line"):
                    rec["md_line"] = pointer["md_line"]
                section_hits += 1

            sources_out.append(rec)
            source_count += 1

        concepts[canonical] = {
            "name": name,
            "aliases": aliases,
            "sources": sources_out,
        }

    if drift_log:
        drift_path = staging_dir(corpus, "concepts") / "drift.json"
        with drift_path.open("w", encoding="utf-8") as f:
            json.dump(
                {"corpus": corpus, "drift_entries": drift_log}, f, indent=2
            )
        print(
            f"  reconciled {len(drift_log)} slug/id drift entries; log: {drift_path}"
        )

    out = {
        "schema_version": 1,
        "corpus": corpus,
        "generated_from": "extracted+sonnet-cross-link",
        "concepts": concepts,
    }

    out_path = index_output_dir(corpus) / "concept-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    size = out_path.stat().st_size
    coverage = (section_hits / source_count * 100) if source_count else 0
    print(
        f"wrote {out_path} ({len(concepts)} concepts, {size} bytes); "
        f"section pointers attached to {section_hits}/{source_count} source mentions "
        f"({coverage:.0f}%)"
    )
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build concept-index.json")
    parser.add_argument("--corpus", required=True)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--emit-candidates", action="store_true")
    g.add_argument("--assemble", action="store_true")
    args = parser.parse_args(argv)

    if args.emit_candidates:
        _emit_candidates(args.corpus)
    else:
        _assemble(args.corpus)
    return 0


if __name__ == "__main__":
    sys.exit(main())
