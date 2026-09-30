#!/usr/bin/env python3
"""Concept merge tests: decisions.json and topics.json change together.

The merge review settles the topic linker's duplicate flags; merge_concepts
carries the decisions out. These cases lock in:

- a merge folds names and aliases into the kept concept, keeps every source
  with its context, and renames every placement in topics.json;
- a split hands each of a conflated concept's sources to the concept it means
  and removes the conflated concept everywhere;
- keep_apart closes a flag and nothing else;
- every resolved merge-candidate group is dropped, the rest stay open;
- a merge file that doesn't fit (unknown or doubly claimed concepts, a synonym
  assembly would drop, an unassigned source) stops before anything is written.

No test framework, matching tests/mechanical-headings.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/concept-merges.test.py
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes.merge_concepts import apply_decisions, apply_topics, validate  # noqa: E402


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def rec(canonical, name, aliases, *sources):
    return {"canonical": canonical, "name": name, "aliases": list(aliases),
            "sources": [dict(s) for s in sources]}


SOURCE_A = {"slug": "source-a", "id": "s01"}
SOURCE_B = {"slug": "source-b", "id": "s02", "context": "trade-off in every act"}
SOURCE_C = {"slug": "source-c", "id": "s03"}
SOURCE_D = {"slug": "source-d", "id": "s04"}
SOURCE_E = {"slug": "source-e", "id": "s05"}

DECISIONS = {"schema_version": 1, "decisions": [
    rec("efficiency-thoroughness-trade-off", "Efficiency-Thoroughness Trade-Off", ["efficiency thoroughness tradeoff"], SOURCE_A),
    rec("etto", "ETTO", [], SOURCE_B),
    rec("etto-principle", "ETTO Principle", ["etto principle"], SOURCE_B, SOURCE_A),
    rec("kanban", "Kanban", [], SOURCE_E),
    rec("kanban-method", "Kanban Method", ["kanban"], SOURCE_D),
    rec("rag", "RAG", ["retrieval-augmented generation", "resilience assessment grid"], SOURCE_C, SOURCE_A),
    rec("resilience-assessment-grid", "Resilience Assessment Grid", [], SOURCE_A),
    rec("retrieval-augmented-generation", "Retrieval-Augmented Generation", [], SOURCE_C),
    rec("safety-ii", "Safety-II", [], SOURCE_A),
]}

TOPICS = {
    "schema_version": 1,
    "topics": [
        {"key": "resilience-engineering", "name": "Resilience engineering", "kind": "subject",
         "concepts": ["etto-principle", "etto", "safety-ii", "resilience-assessment-grid", "rag"],
         "examples": ["efficiency-thoroughness-trade-off"]},
        {"key": "how-llms-work", "name": "How LLMs work", "kind": "subject",
         "concepts": ["retrieval-augmented-generation", "rag"], "examples": []},
        {"key": "lean-and-flow", "name": "Lean and flow", "kind": "subject",
         "concepts": ["kanban", "kanban-method"], "examples": []},
    ],
    "unplaced": [{"concept": "efficiency-thoroughness-trade-off", "reason": "noise"}],
    "synonyms": {"efficiency-thoroughness-trade-off": [], "etto-principle": [], "kanban-method": ["kanban"],
                 "rag": ["retrieval-augmented generation"]},
    "merge_candidates": [
        {"concepts": ["etto", "etto-principle", "efficiency-thoroughness-trade-off"], "note": "one ETTO"},
        {"concepts": ["rag", "retrieval-augmented-generation"], "note": "Kalai's sense"},
        {"concepts": ["rag", "resilience-assessment-grid"], "note": "Hollnagel's sense"},
        {"concepts": ["kanban", "kanban-method"], "note": "maybe"},
        {"concepts": ["safety-ii", "resilience-assessment-grid"], "note": "left for later"},
    ],
}

MERGES = {
    "merge": [{"keep": "etto-principle", "fold": ["etto", "efficiency-thoroughness-trade-off"],
               "name": "ETTO Principle", "synonyms": ["ETTO", "Efficiency-Thoroughness Trade-Off"]}],
    "keep_apart": [{"concepts": ["kanban", "kanban-method"], "note": "the TPS card, not Anderson's method"}],
    "split": [{"concept": "rag", "sources": {"source-c": "retrieval-augmented-generation",
                                             "source-a": "resilience-assessment-grid"}}],
}


def by_key(items, field):
    return {i[field]: i for i in items}


def case_a_valid_merge_file_passes() -> None:
    problems = validate(DECISIONS, TOPICS, MERGES)
    assert_(not problems, f"the fixture merge file must fit: {problems}")


def case_merge_folds_names_aliases_and_sources() -> None:
    out = by_key(apply_decisions(DECISIONS, MERGES)["decisions"], "canonical")
    assert_("etto" not in out and "efficiency-thoroughness-trade-off" not in out, "folded records must go")
    kept = out["etto-principle"]
    assert_(kept["name"] == "ETTO Principle", f"name: {kept['name']}")
    for alias in ("etto principle", "ETTO", "Efficiency-Thoroughness Trade-Off", "efficiency thoroughness tradeoff"):
        assert_(alias in kept["aliases"], f"'{alias}' must become an alias: {kept['aliases']}")
    assert_([s["id"] for s in kept["sources"]] == ["s02", "s01"], f"sources are pooled once each: {kept['sources']}")
    assert_(kept["sources"][0].get("context") == "trade-off in every act", "a source keeps its context")
    assert_(DECISIONS["decisions"][2]["aliases"] == ["etto principle"], "apply must not change the doc it was given")


def case_merge_renames_every_placement() -> None:
    out = apply_topics(TOPICS, MERGES)
    topic = by_key(out["topics"], "key")["resilience-engineering"]
    assert_(topic["concepts"].count("etto-principle") == 1 and "etto" not in topic["concepts"],
            f"folded placements become the kept one, once: {topic['concepts']}")
    assert_(topic["examples"] == [], f"an example that is now the same concept as a filed one goes: {topic['examples']}")
    assert_(out["unplaced"] == [], f"a folded noise entry whose concept is placed leaves unplaced: {out['unplaced']}")
    assert_(out["synonyms"]["etto-principle"] == ["ETTO", "Efficiency-Thoroughness Trade-Off"]
            and "efficiency-thoroughness-trade-off" not in out["synonyms"], f"synonyms: {out['synonyms']}")


def case_split_hands_sources_to_the_meant_concepts() -> None:
    decisions = by_key(apply_decisions(DECISIONS, MERGES)["decisions"], "canonical")
    assert_("rag" not in decisions, "a split concept's record goes")
    assert_([s["id"] for s in decisions["retrieval-augmented-generation"]["sources"]] == ["s03"],
            "a source already credited isn't doubled")
    assert_([s["id"] for s in decisions["resilience-assessment-grid"]["sources"]] == ["s01"],
            f"grid: {decisions['resilience-assessment-grid']['sources']}")
    topics = apply_topics(TOPICS, MERGES)
    held = [t["key"] for t in topics["topics"] if "rag" in t["concepts"]]
    assert_(held == [] and "rag" not in topics["synonyms"], f"a split concept leaves topics.json: {held}")


def case_resolved_flags_close_and_the_rest_stay() -> None:
    groups = [g["concepts"] for g in apply_topics(TOPICS, MERGES)["merge_candidates"]]
    assert_(groups == [["safety-ii", "resilience-assessment-grid"]], f"only the unsettled flag stays open: {groups}")


def case_misfit_merge_files_stop() -> None:
    bad = {
        "unknown concept": {"merge": [{"keep": "etto-principle", "fold": ["no-such"], "synonyms": []}]},
        "claimed twice": {"merge": [{"keep": "etto-principle", "fold": ["etto"], "synonyms": []},
                                    {"keep": "etto", "fold": ["efficiency-thoroughness-trade-off"], "synonyms": []}]},
        "no synonyms decision": {"merge": [{"keep": "etto-principle", "fold": ["etto"]}]},
        "synonym assembly drops": {"merge": [{"keep": "etto-principle", "fold": ["etto"], "synonyms": ["etto principle"]}]},
        "name from nowhere": {"merge": [{"keep": "etto-principle", "fold": ["etto"], "name": "Trade-offs", "synonyms": []}]},
        "unassigned source": {"split": [{"concept": "rag", "sources": {"source-c": "retrieval-augmented-generation"}}]},
        "target folded": {"merge": [{"keep": "resilience-assessment-grid", "fold": ["retrieval-augmented-generation"], "synonyms": []}],
                          "split": copy.deepcopy(MERGES["split"])},
    }
    for label, merges in bad.items():
        assert_(validate(DECISIONS, TOPICS, merges), f"'{label}' must stop the merge")


CASES = [
    case_a_valid_merge_file_passes,
    case_merge_folds_names_aliases_and_sources,
    case_merge_renames_every_placement,
    case_split_hands_sources_to_the_meant_concepts,
    case_resolved_flags_close_and_the_rest_stay,
    case_misfit_merge_files_stop,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        try:
            case()
            print(f"  ok   {case.__name__}")
        except (Exception, SystemExit) as e:  # noqa: BLE001 — report every failure the same way
            failures.append(f"{case.__name__}: {e}")
            print(f"  FAIL {case.__name__}: {e}")

    print()
    if failures:
        print(f"concept-merges: {len(failures)} of {len(CASES)} cases FAILED")
        return 1
    print(f"concept-merges: all {len(CASES)} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
