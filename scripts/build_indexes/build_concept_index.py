"""Assemble ``concept-index.json`` from per-source extracted artefacts plus
an LLM cross-link pass that decides aliasing/merging.

Pipeline (Phase 3):

  1. Python aggregates raw concept candidates from
     ``_planning/extracted/{corpus}/*.json``: every ``book_index_entries``
     concept text and every ``enumerated_methods`` name across every source.
     This is the candidate vocabulary, large and redundant by design.

  2. Python writes the merged candidate list to
     ``_planning/staging/{corpus}/concepts/candidates.json``. This artefact
     is the *input* to the cross-link pass.

  3. The ``ingest-concept-linker`` agent reads the candidates, makes alias / merge / novel
     decisions, and writes
     ``_planning/staging/{corpus}/concepts/decisions.json``. The spec calls
     out (§"Anti-patterns to avoid") that this step MUST be the LLM; regex
     cannot adjudicate aliases, vocabulary variation, related-but-distinct.

  4. The ``ingest-topic-linker`` agent files the concepts under topics and
     writes ``_planning/staging/{corpus}/concepts/topics.json``.

  5. Python reads the decisions, applies them to the candidate vocabulary,
     resolves slug → ID, and writes two variants: ``concept-index.json``
     (runtime) and ``concept-index-deep.json`` (adds section/md_line body
     pointers; the operator/audit surface). With a topics file the runtime
     index is schema 3: a topics block a model reads whole, then one concept
     row per line, found by topic ID. Without one it is schema 2: one row per
     concept, read whole.

Steps 1, 2, 5 are mechanical and live in this script. Steps 3 and 4 are the
orchestrator running the agents with the staging artefacts.

Usage:

    # Step 1+2 (aggregation): emit candidates for the cross-link pass.
    python -m scripts.build_indexes.build_concept_index --corpus demo \\
        --emit-candidates

    # Step 5 (after the cross-link and topic decisions land): assemble final index.
    python -m scripts.build_indexes.build_concept_index --corpus demo \\
        --assemble

Decision-file schema (written by the cross-link pass):

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
_LEADING_BULLET = re.compile(r"^\s*[-–—•*·]+\s+")

# Words that, at the edge of an entry, usually mean a dangling book-index
# sub-entry fragment ("characteristics of, 247") rather than a concept.
# Regex cannot adjudicate this — real concepts end in function words too
# ("genius of the and", "i intend to") — so suspects are *flagged* for the
# cross-link LLM pass to keep or drop, never auto-dropped.
_FRAGMENT_EDGE_WORDS = {
    "of", "and", "the", "to", "in", "for", "on", "vs", "with", "as", "at",
    "by", "from", "or",
}


def _strip_bullet(text: str) -> str:
    """Strip a leading markdown list bullet from a scraped index line.

    EPUB back-matter indexes converted to markdown arrive as bullet lists
    ("- abandonment"); the bullet is conversion furniture, not part of the
    concept name.
    """
    return _LEADING_BULLET.sub("", text)


def _is_fragment_suspect(key: str) -> bool:
    words = key.split()
    if not words:
        return False
    return words[0] in _FRAGMENT_EDGE_WORDS or words[-1] in _FRAGMENT_EDGE_WORDS


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
    the candidate vocabulary so the cross-link pass sees one entry per *distinct
    surface form*, not seven copies of the same string from a multi-page
    index.
    """
    t = _strip_bullet(text)
    t = _strip_trailing_locators(t)
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
            if not text:
                continue
            text = _strip_bullet(text)
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
    """Aggregate per-source extractions into a candidate list for the cross-link pass.

    Two-layer construction:

    - **Curated layer**: every ``concept_tag`` in ``reference-index.json``.
      These are the operator-validated (via the refs pass) routing tags;
      they form the spine of the concept-index.
    - **Mechanical layer**: enumerated-method names (author-curated) plus
      back-matter book-index entries that appear in *at least two distinct
      source slugs*. Single-source book-index entries are excluded from
      the first build: they bloat the candidate set with verbose textbook
      back-matter without adding cross-source routing capability. Phase 5
      re-runs can promote them as needed.

    The decision file the cross-link pass writes back must cover both layers.
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

    # Slim payload for the cross-link pass — drop per-source locator metadata
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
        if _is_fragment_suspect(key):
            slim_candidates[key]["fragment_suspect"] = True

    bundle["candidates"] = slim_candidates
    bundle["fragment_rule"] = (
        "candidates flagged fragment_suspect start or end with a dangling "
        "function word; the cross-link pass must explicitly keep (real "
        "concept) or drop (book-index sub-entry fragment) each one — "
        "never include them silently"
    )

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


def _clean_aliases(name: str, canonical: str, aliases: list[str]) -> list[str]:
    """Mechanical alias hygiene at assembly time.

    Strips scraped bullet markers, collapses whitespace, and de-dupes
    case-insensitively (also against the display name and the canonical
    slug, both of which already resolve). Purely lossless: every surviving
    string still resolves to the same entry.
    """
    seen = {name.strip().lower(), canonical.strip().lower()}
    out: list[str] = []
    for alias in aliases:
        if not alias:
            continue
        cleaned = _WHITESPACE.sub(" ", _strip_bullet(alias)).strip()
        if not cleaned:
            continue
        key = cleaned.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(cleaned)
    return out


def _previous_pointers(deep_path: Path) -> dict[tuple[str, str], dict]:
    """Section pointers from the last deep index, keyed by (concept, source ID).

    Extracted artefacts live in the untracked ``_planning/`` tree, so a machine
    or clone without them would re-assemble every pointer away. For a source
    with no artefact here, assembly keeps its last known pointer instead.
    """
    if not deep_path.is_file():
        return {}
    with deep_path.open("r", encoding="utf-8") as f:
        deep = json.load(f)
    out: dict[tuple[str, str], dict] = {}
    for canonical, rec in deep.get("concepts", {}).items():
        for src in rec.get("sources", []):
            ptr = {k: src[k] for k in ("section", "md_line") if src.get(k)}
            if ptr:
                out[(canonical, src["id"])] = ptr
    return out


_TOPIC_ID = re.compile(r"t(\d{3})")

_TOPIC_FORMAT = ["id", "name", "synonyms", "boundary", "kind", "broader", "concepts", "sources", "positions?"]
_ROW_FORMAT = ["name", "kind", "synonyms", "source_ids", "topics", "contexts?"]


def _load_topics(corpus: str) -> tuple[Path, dict | None]:
    """The topic linker's decisions, if this corpus has any."""
    path = staging_dir(corpus, "concepts") / "topics.json"
    if not path.is_file():
        return path, None
    with path.open("r", encoding="utf-8") as f:
        return path, json.load(f)


def _published_topic_ids(runtime_path: Path) -> set[str]:
    """Topic IDs already shipped in a schema-3 runtime index."""
    if not runtime_path.is_file():
        return set()
    with runtime_path.open("r", encoding="utf-8") as f:
        index = json.load(f)
    if index.get("schema_version") != 3:
        return set()
    return {t[0] for t in index.get("topics", [])}


def _retire_topic_ids(topics_doc: dict, published: set[str]) -> bool:
    """Record shipped topic IDs that topics.json no longer holds; True if the list changed.

    ``retired_ids`` in topics.json keeps them out of circulation for good, even
    once the runtime file that carried them has been overwritten.
    """
    current = {t["id"] for t in topics_doc["topics"] if t.get("id")}
    before = set(topics_doc.get("retired_ids", []))
    after = before | (published - current)
    if after == before:
        return False
    topics_doc["retired_ids"] = sorted(after)
    return True


def _assign_topic_ids(topics_doc: dict, published: set[str]) -> bool:
    """Give each topic without an ``id`` the next free one; True if any were assigned.

    IDs are append-only: never reassigned and never reused, even after a topic
    is retired (``published`` carries the IDs already shipped). They are
    fixed-width, t001 to t999, because retrieval finds a topic's rows by the
    prefix ``"t031``, which would also match ``"t0310`` if widths varied.
    """
    taken = {t["id"] for t in topics_doc["topics"] if t.get("id")} | published
    numbers = [int(m.group(1)) for i in taken if (m := _TOPIC_ID.fullmatch(i))]
    following = max(numbers, default=0) + 1
    assigned = False
    for topic in topics_doc["topics"]:
        if topic.get("id"):
            continue
        if following > 999:
            raise SystemExit("topic IDs would pass t999; widen the ID format before adding topics")
        topic["id"] = f"t{following:03d}"
        following += 1
        assigned = True
    return assigned


def _write_schema3(out_path: Path, corpus: str, concepts: dict[str, dict], topics_doc: dict) -> dict:
    """Write the schema-3 runtime index and check it; return counts for the build log.

    A topics block comes first, one topic per line, with ``topic_lines`` giving
    its line range so a model reads exactly the block. Concept rows follow, one
    per line. A row lists its topic IDs, and a debate side as ``t031.1``, so
    ``grep -F '"t031'`` returns every row under topic t031, sides included.
    Rows carry no slug: the pipeline keys concepts by slug in ``decisions.json``
    and the deep variant.
    """
    dump = lambda value: json.dumps(value, ensure_ascii=False, separators=(",", ":"))  # noqa: E731
    topics = sorted(topics_doc["topics"], key=lambda t: t["id"])
    key_to_id = {t["key"]: t["id"] for t in topics}
    refs: dict[str, set[str]] = {c: set() for c in concepts}
    members: dict[str, set[str]] = {t["id"]: set() for t in topics}
    filed_as_concept: set[str] = set()
    unknown: list[str] = []

    def attach(topic_id: str, ref: str, canonical: str, as_concept: bool) -> None:
        if canonical not in refs:
            unknown.append(f"{topic_id} -> {canonical}")
            return
        refs[canonical].add(ref)
        members[topic_id].add(canonical)
        if as_concept:
            filed_as_concept.add(canonical)

    for topic in topics:
        topic_id = topic["id"]
        for canonical in topic.get("concepts", []):
            attach(topic_id, topic_id, canonical, True)
        for canonical in topic.get("examples", []):
            attach(topic_id, topic_id, canonical, False)
        for side, position in enumerate(topic.get("positions", []), 1):
            for canonical in position.get("concepts", []):
                attach(topic_id, f"{topic_id}.{side}", canonical, True)
    bad_broader = [t["key"] for t in topics if t.get("broader") and t["broader"] not in key_to_id]
    if unknown or bad_broader:
        raise SystemExit(
            "topics.json doesn't match the concept vocabulary:\n"
            + "".join(f"  unknown concept {u}\n" for u in unknown[:20])
            + "".join(f"  unknown broader topic on {k}\n" for k in bad_broader)
        )

    synonyms = topics_doc.get("synonyms", {})
    unplaced = {u["concept"] for u in topics_doc.get("unplaced", [])}
    dropped_synonyms = 0

    def topic_line(topic: dict) -> str:
        topic_id = topic["id"]
        source_ids = {s["id"] for c in members[topic_id] for s in concepts[c]["sources"]}
        line = [topic_id, topic["name"], topic.get("synonyms", []), topic.get("boundary", ""),
                topic.get("kind", "subject"), key_to_id.get(topic.get("broader") or "", ""),
                len(members[topic_id]), len(source_ids)]
        if topic.get("kind") == "debate":
            line.append([p["label"] for p in topic.get("positions", [])])
        return dump(line)

    def concept_line(canonical: str) -> str:
        nonlocal dropped_synonyms
        rec = concepts[canonical]
        if canonical in synonyms:
            kept = [a for a in synonyms[canonical] if a in rec["aliases"]]
            dropped_synonyms += len(synonyms[canonical]) - len(kept)
        else:
            kept = rec["aliases"]  # not yet reviewed by the topic linker
        kind = "example" if refs[canonical] and canonical not in filed_as_concept else "concept"
        row = [rec["name"], kind, kept, [s["id"] for s in rec["sources"]], sorted(refs[canonical])]
        contexts = {s["id"]: s["context"] for s in rec["sources"] if "context" in s}
        if contexts:
            row.append(contexts)
        return dump(row)

    topic_lines = [topic_line(t) for t in topics]
    order = sorted(concepts, key=lambda c: (concepts[c]["name"].casefold(), c))
    head = [
        "{",
        '"schema_version": 3,',
        f'"corpus": {dump(corpus)},',
        '"generated_from": "extracted+cross-link+topics",',
    ]
    first = len(head) + 5  # after topic_lines, topic_format, row_format and '"topics": ['
    head += [
        f'"topic_lines": [{first}, {first + len(topic_lines) - 1}],',
        f'"topic_format": {dump(_TOPIC_FORMAT)},',
        f'"row_format": {dump(_ROW_FORMAT)},',
        '"topics": [',
    ]
    text = ("\n".join(head) + "\n" + ",\n".join(topic_lines) + "\n],\n" + '"concepts": [\n'
            + ",\n".join(concept_line(c) for c in order) + "\n]}\n")

    # The contract retrieval relies on: the file parses, topic_lines brackets
    # the block, and each topic's prefix grep returns exactly its rows.
    parsed = json.loads(text)
    lines = text.splitlines()
    start, end = parsed["topic_lines"]
    if not all(lines[k - 1].startswith('["t') for k in range(start, end + 1)) or lines[end].startswith('["t'):
        raise SystemExit("schema 3: topic_lines doesn't bracket the topics block")
    rows = lines[end:]
    for topic in topics:
        hits = sum(1 for line in rows if f'"{topic["id"]}' in line)
        if hits != len(members[topic["id"]]):
            raise SystemExit(f"schema 3: grep for {topic['id']} finds {hits} rows, expected {len(members[topic['id']])}")

    out_path.write_text(text, encoding="utf-8")
    return {
        "topics": len(topics),
        "debates": sum(1 for t in topics if t.get("kind") == "debate"),
        "rows": len(order),
        "block_bytes": sum(len(lines[k - 1]) + 1 for k in range(start, end + 1)),
        "unfiled": sorted(c for c in concepts if not refs[c] and c not in unplaced),
        "unreviewed": sum(1 for c in concepts
                          if c not in synonyms and c not in unplaced and concepts[c]["aliases"]),
        "dropped_synonyms": dropped_synonyms,
    }


def _assemble(corpus: str) -> Path:
    slug_table = load_slug_table(corpus)
    slug_id = slug_to_id(slug_table)

    decisions_path = staging_dir(corpus, "concepts") / "decisions.json"
    if not decisions_path.is_file():
        raise SystemExit(
            f"ERROR: decisions file not found at {decisions_path}.\n"
            "Run the cross-link pass against candidates.json before --assemble."
        )

    with decisions_path.open("r", encoding="utf-8") as f:
        decisions = json.load(f)

    id_to_slug = {rid: slug for slug, rid in slug_id.items()}
    valid_ids = set(slug_id.values())

    extracted_lookup = _build_extracted_lookup(corpus, slug_id)
    out_dir = index_output_dir(corpus)
    previous_pointers = _previous_pointers(out_dir / "concept-index-deep.json")

    concepts: dict[str, dict] = {}
    drift_log: list[dict] = []
    section_hits = 0
    source_count = 0
    carried = 0

    for entry in decisions.get("decisions", []):
        canonical = entry.get("canonical")
        if not canonical:
            continue
        name = _WHITESPACE.sub(" ", _strip_bullet(entry.get("name", canonical))).strip()
        aliases = _clean_aliases(name, canonical, entry.get("aliases", []) or [])
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
            if not pointer and resolved_id not in extracted_lookup:
                pointer = previous_pointers.get((canonical, resolved_id))
                carried += bool(pointer)
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

    # Dual emission. The deep variant keeps the rich dict shape with
    # section/md_line body pointers; it is the operator/audit surface and
    # stays at corpus level (apps never ship it — build.js ships the runtime
    # file). The runtime file is schema 3 when the topic linker has filed this
    # corpus (see _write_schema3), otherwise compact v2: one row per concept,
    # sorted by slug, one line each. Row: [slug, name, aliases, source_ids]
    # with an optional 5th element {id: context} when any source carries a
    # context string.
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "concept-index.json"
    topics_path, topics_doc = _load_topics(corpus)
    topic_stats = None
    if topics_doc is not None:
        published = _published_topic_ids(out_path)
        retired_changed = _retire_topic_ids(topics_doc, published)
        if retired_changed:
            with topics_path.open("w", encoding="utf-8") as f:
                json.dump(topics_doc, f, indent=2, ensure_ascii=False)
                f.write("\n")
        if _assign_topic_ids(topics_doc, published | set(topics_doc.get("retired_ids", []))):
            with topics_path.open("w", encoding="utf-8") as f:
                json.dump(topics_doc, f, indent=2, ensure_ascii=False)
                f.write("\n")
        topic_stats = _write_schema3(out_path, corpus, concepts, topics_doc)

    rows = []
    for canonical in sorted(concepts):
        rec = concepts[canonical]
        row: list = [
            canonical,
            rec["name"],
            rec["aliases"],
            [src["id"] for src in rec["sources"]],
        ]
        contexts = {
            src["id"]: src["context"] for src in rec["sources"] if "context" in src
        }
        if contexts:
            row.append(contexts)
        rows.append(row)

    header = {
        "schema_version": 2,
        "corpus": corpus,
        "generated_from": "extracted+cross-link",
        "row_format": ["slug", "name", "aliases", "source_ids", "contexts?"],
    }
    if topic_stats is None:
        with out_path.open("w", encoding="utf-8") as f:
            f.write("{\n")
            for key, value in header.items():
                f.write(f"{json.dumps(key)}: {json.dumps(value, ensure_ascii=False)},\n")
            f.write('"concepts": [\n')
            f.write(
                ",\n".join(
                    json.dumps(row, ensure_ascii=False, separators=(",", ":"))
                    for row in rows
                )
            )
            f.write("\n]}\n")

    deep_path = out_dir / "concept-index-deep.json"
    with deep_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "schema_version": 1,
                "corpus": corpus,
                "generated_from": "extracted+cross-link",
                "variant": "deep",
                "concepts": concepts,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    size = out_path.stat().st_size
    deep_size = deep_path.stat().st_size
    coverage = (section_hits / source_count * 100) if source_count else 0
    runtime = "runtime v2" if topic_stats is None else "runtime schema 3"
    print(
        f"wrote {out_path} ({len(rows)} concepts, {size} bytes {runtime}; "
        f"{deep_size} bytes deep at {deep_path.name}); "
        f"section pointers attached to {section_hits}/{source_count} source mentions "
        f"({coverage:.0f}%)"
        + (f", {carried} kept from the previous deep index for sources with no extracted artefact"
           if carried else "")
    )
    if topic_stats is not None:
        s = topic_stats
        print(
            f"  topics: {s['topics']} ({s['debates']} debate), topics block {s['block_bytes']} bytes; "
            f"{len(s['unfiled'])} concepts not yet filed under a topic; "
            f"{s['unreviewed']} with aliases whose synonyms the topic linker hasn't reviewed"
            + (f"; {s['dropped_synonyms']} kept synonyms no longer among their concept's aliases"
               if s["dropped_synonyms"] else "")
        )
        if s["unfiled"]:
            print(f"  not yet filed: {', '.join(s['unfiled'][:10])}{' …' if len(s['unfiled']) > 10 else ''}")
    return out_path


def _emit_topic_payload(corpus: str) -> Path:
    """Write the topic linker's input: the assembled vocabulary, one concept per line.

    Built from the deep index, so run --assemble first. Each line is
    ``{"concept", "name", "aliases", "sources", "contexts", "filed"}`` with
    sources as slugs; ``filed`` is true when topics.json already places the
    concept (under a topic or as noise), which is what the linker's per-source
    mode skips. One line per concept lets the linker read the whole vocabulary
    in order rather than slices of a large JSON object.
    """
    deep_path = index_output_dir(corpus) / "concept-index-deep.json"
    if not deep_path.is_file():
        raise SystemExit(f"no deep index at {deep_path}; run --assemble first")
    with deep_path.open("r", encoding="utf-8") as f:
        deep = json.load(f)
    id_to_slug = {rid: slug for slug, rid in slug_to_id(load_slug_table(corpus)).items()}

    _, topics_doc = _load_topics(corpus)
    filed: set[str] = set()
    for topic in (topics_doc or {}).get("topics", []):
        filed.update(topic.get("concepts", []), topic.get("examples", []))
        for position in topic.get("positions", []):
            filed.update(position.get("concepts", []))
    filed.update(u["concept"] for u in (topics_doc or {}).get("unplaced", []))

    concepts = deep["concepts"]
    out_path = staging_dir(corpus, "concepts") / "topic-payload.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    order = sorted(concepts, key=lambda c: (concepts[c]["name"].casefold(), c))
    with out_path.open("w", encoding="utf-8") as f:
        for canonical in order:
            rec = concepts[canonical]
            line = {
                "concept": canonical,
                "name": rec["name"],
                "aliases": rec.get("aliases", []),
                "sources": [id_to_slug.get(s["id"], s["id"]) for s in rec["sources"]],
                "contexts": {id_to_slug.get(s["id"], s["id"]): s["context"]
                             for s in rec["sources"] if s.get("context")},
                "filed": canonical in filed,
            }
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    unfiled = sum(1 for c in order if c not in filed)
    print(f"wrote {out_path} ({len(order)} concepts, {unfiled} not yet filed under a topic)")
    return out_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build concept-index.json")
    parser.add_argument("--corpus", required=True)
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--emit-candidates", action="store_true")
    g.add_argument("--assemble", action="store_true")
    g.add_argument(
        "--emit-topic-payload",
        action="store_true",
        help="write the topic linker's input from the assembled deep index",
    )
    args = parser.parse_args(argv)

    if args.emit_candidates:
        _emit_candidates(args.corpus)
    elif args.emit_topic_payload:
        _emit_topic_payload(args.corpus)
    else:
        _assemble(args.corpus)
    return 0


if __name__ == "__main__":
    sys.exit(main())
