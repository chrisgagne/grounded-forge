#!/usr/bin/env python3
"""Re-filing tests: a source's credits, filings, new rows and removals land in decisions.json and topics.json together.

The re-filing agent proposes changes by display name and topic ID;
refile_sources carries them out. These cases lock in:

- a credit adds the source, with its context, and a repeat is skipped;
- a removal takes the source off a row, and a row left with no source goes
  from both files (placements, synonyms, merge candidates);
- a filing adds topics up to three subject topics, skips past that, drops a
  ``replace`` topic only when full, files a debate side under its position and
  an example-only concept under examples;
- a new row gets a key, its synonyms and its topics; the same new row from two
  files becomes one row credited to both; a new row named like an existing one
  merges into it;
- new rows whose names contain one another, and rows an agent names as
  duplicates, are flagged as merge candidates once;
- a proposal that can't apply (unknown row, topic or debate side, a slug the
  table doesn't know, a new row with no topics) is reported by validate.

No test framework, matching tests/mechanical-headings.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/refile.test.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes.refile_sources import apply, validate  # noqa: E402


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


A = {"slug": "source-a", "id": "s01"}
B = {"slug": "source-b", "id": "s02"}
SLUG_IDS = {"source-a": "s01", "source-b": "s02"}


def rec(canonical, name, *sources):
    return {"canonical": canonical, "name": name, "aliases": [], "sources": [dict(s) for s in sources]}


def fixtures():
    decisions = {"schema_version": 1, "decisions": [
        rec("drift", "Drift Into Failure", A),
        rec("etto", "ETTO Principle", A, B),
        rec("goodhart", "Goodhart's Law", B),
        rec("challenger", "Challenger Disaster", A),
        rec("full-row", "Full Row", A),
    ]}
    topics = {"schema_version": 1, "topics": [
        {"key": "drift-topic", "id": "t008", "name": "Drift", "kind": "subject", "concepts": ["drift"], "examples": ["challenger"], "positions": []},
        {"key": "tradeoffs", "id": "t006", "name": "Trade-offs", "kind": "subject", "concepts": ["etto", "full-row"], "examples": [], "positions": []},
        {"key": "metrics", "id": "t044", "name": "Metrics", "kind": "subject", "concepts": ["goodhart", "full-row"], "examples": [], "positions": []},
        {"key": "cases", "id": "t017", "name": "Cases", "kind": "subject", "concepts": ["full-row"], "examples": [], "positions": []},
        {"key": "targets-debate", "id": "t236", "name": "Targets debate", "kind": "debate", "concepts": [], "examples": [],
         "positions": [{"label": "set targets", "concepts": []}, {"label": "improve the system", "concepts": ["goodhart"]}]},
    ], "unplaced": [], "synonyms": {"goodhart": []},
        "merge_candidates": [{"concepts": ["goodhart", "etto"], "note": "x"}]}
    return decisions, topics


def doc(*sources):
    return {"batch": "b1", "sources": [dict(s) for s in sources]}


def src(base, **changes):
    return {**base, **changes}


def by_key(decisions, key):
    return next((d for d in decisions["decisions"] if d["canonical"] == key), None)


def topic(topics, tid):
    return next(t for t in topics["topics"] if t["id"] == tid)


def case_credit_adds_source_with_context_once() -> None:
    d, t = fixtures()
    p = doc(src(B, credits=[{"row": "Drift Into Failure", "context": "drift as small steps", "evidence": "e"},
                            {"row": "ETTO Principle", "evidence": "e"}]))
    d2, _, log = apply(d, t, [p])
    srcs = by_key(d2, "drift")["sources"]
    assert_({"slug": "source-b", "id": "s02", "context": "drift as small steps"} in srcs, f"credit missing: {srcs}")
    assert_(any("already credited" in e["outcome"] for e in log), "repeat credit not skipped")
    assert_(len(by_key(d2, "etto")["sources"]) == 2, "repeat credit added twice")


def case_removal_and_last_source_drops_row() -> None:
    d, t = fixtures()
    p = doc(src(A, removals=[{"row": "ETTO Principle", "evidence": "e"}]),
            src(B, removals=[{"row": "Goodhart's Law", "evidence": "e"}]))
    d2, t2, _ = apply(d, t, [p])
    assert_([s["id"] for s in by_key(d2, "etto")["sources"]] == ["s02"], "removal didn't take source off")
    assert_(by_key(d2, "goodhart") is None, "row with no source left still in decisions")
    assert_("goodhart" not in topic(t2, "t044")["concepts"], "removed row still filed")
    assert_("goodhart" not in topic(t2, "t236")["positions"][1]["concepts"], "removed row still on a debate side")
    assert_("goodhart" not in t2["synonyms"], "removed row's synonyms stay")
    assert_(t2["merge_candidates"] == [], "merge group with one member left stays open")


def case_filing_caps_replaces_sides_and_examples() -> None:
    d, t = fixtures()
    p = doc(src(A, filings=[
        {"row": "Drift Into Failure", "add_topics": ["t006", "t044"], "evidence": "e"},
        {"row": "Full Row", "add_topics": ["t008"], "evidence": "e"},
        {"row": "Full Row", "add_topics": ["t008"], "replace": "t017", "evidence": "e"},
        {"row": "ETTO Principle", "add_topics": ["t236.2"], "remove_topics": ["t006"], "evidence": "e"},
        {"row": "Challenger Disaster", "add_topics": ["t017"], "evidence": "e"},
    ]))
    d2, t2, log = apply(d, t, [p])
    assert_("drift" in topic(t2, "t006")["concepts"] and "drift" in topic(t2, "t044")["concepts"], "filings not added")
    assert_(any("skipped t008" in e["outcome"] for e in log), "over-cap filing not skipped")
    assert_("full-row" in topic(t2, "t008")["concepts"] and "full-row" not in topic(t2, "t017")["concepts"], "replace didn't swap")
    assert_("etto" in topic(t2, "t236")["positions"][1]["concepts"], "debate side not filed")
    assert_("etto" not in topic(t2, "t006")["concepts"], "remove_topics didn't remove")
    assert_("challenger" in topic(t2, "t017")["examples"], "example-only concept not filed as example")
    assert_(t2["synonyms"].get("drift") == [], "first filing of an unreviewed concept left no synonyms decision")


def case_new_rows_create_merge_and_reuse() -> None:
    d, t = fixtures()
    p1 = doc(src(A, new_rows=[{"name": "Objectives and Key Results (OKRs)", "kind": "concept", "synonyms": ["OKRs"],
                               "topics": ["t044", "t236.1"], "context": "OKRs as stretch goals", "evidence": "e"},
                              {"name": "Vision Zero", "kind": "example", "synonyms": [], "topics": ["t017"], "evidence": "e"}]))
    p2 = doc(src(B, new_rows=[{"name": "Objectives and Key Results", "kind": "concept", "synonyms": [],
                               "topics": ["t044"], "evidence": "e"},
                              {"name": "drift into failure", "kind": "concept", "synonyms": [], "topics": ["t008"], "evidence": "e"}]))
    d2, t2, _ = apply(d, t, [p1, p2])
    okr = by_key(d2, "objectives-and-key-results-okrs")
    assert_(okr is not None, f"new row not created: {[x['canonical'] for x in d2['decisions']]}")
    assert_([s["id"] for s in okr["sources"]] == ["s01", "s02"], "same new row from two files not merged")
    assert_(okr["sources"][0].get("context") == "OKRs as stretch goals", "new row context lost")
    assert_(okr["aliases"] == ["OKRs"] and t2["synonyms"]["objectives-and-key-results-okrs"] == ["OKRs"], "synonyms not kept")
    assert_("objectives-and-key-results-okrs" in topic(t2, "t044")["concepts"], "new row not filed")
    assert_("objectives-and-key-results-okrs" in topic(t2, "t236")["positions"][0]["concepts"], "new row debate side missing")
    assert_("vision-zero" in topic(t2, "t017")["examples"], "example new row not under examples")
    assert_([s["id"] for s in by_key(d2, "drift")["sources"]] == ["s01", "s02"], "new row named like an existing one didn't merge")


def case_overlapping_new_rows_are_flagged_for_merge_review() -> None:
    d, t = fixtures()
    p = doc(src(A, new_rows=[{"name": "Flynn Effect", "kind": "concept", "synonyms": [], "topics": ["t044"], "evidence": "e"}]),
            src(B, new_rows=[{"name": "IQ Malleability (Flynn Effect)", "kind": "concept", "synonyms": [], "topics": ["t044"], "evidence": "e"},
                             {"name": "Effect Size", "kind": "concept", "synonyms": [], "topics": ["t044"], "evidence": "e"}]))
    _, t2, _ = apply(d, t, [p])
    flagged = [set(g["concepts"]) for g in t2["merge_candidates"]]
    assert_({"flynn-effect", "iq-malleability-flynn-effect"} in flagged, f"overlap not flagged: {flagged}")
    assert_(not any("effect-size" in g for g in flagged), f"unrelated row flagged: {flagged}")


def case_duplicates_join_merge_candidates_once() -> None:
    d, t = fixtures()
    g = {"rows": ["Drift Into Failure", "ETTO Principle"], "note": "same idea"}
    p = doc(src(A, duplicates=[g]), src(B, duplicates=[g]))
    _, t2, log = apply(d, t, [p])
    flagged = [set(x["concepts"]) for x in t2["merge_candidates"]]
    assert_(flagged.count({"drift", "etto"}) == 1, f"duplicate group not flagged once: {flagged}")
    bad = doc(src(A, duplicates=[{"rows": ["Drift Into Failure"]}]))
    assert_(validate(d, t, [bad], SLUG_IDS), "one-row duplicates group not reported")


def case_validate_reports_what_cannot_apply() -> None:
    d, t = fixtures()
    p = doc(src(A, credits=[{"row": "No Such Row", "evidence": "e"}],
                filings=[{"row": "Drift Into Failure", "add_topics": ["t999", "t044.1"], "evidence": "e"}],
                new_rows=[{"name": "Orphan", "kind": "concept", "synonyms": [], "topics": [], "evidence": "e"}]),
            {"slug": "source-z", "id": "s99"})
    problems = validate(d, t, [p], SLUG_IDS)
    for needle in ("No Such Row", "t999", "t044.1", "Orphan", "source-z"):
        assert_(any(needle in x for x in problems), f"validate missed {needle}: {problems}")
    ok = doc(src(A, credits=[{"row": "Goodhart's Law", "evidence": "e"}]))
    assert_(validate(d, t, [ok], SLUG_IDS) == [], "valid proposal reported")


def main() -> int:
    cases = [v for k, v in sorted(globals().items()) if k.startswith("case_")]
    failures = []
    for case in cases:
        try:
            case()
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{case.__name__}: {exc}")
    print(f"{len(cases) - len(failures)}/{len(cases)} refile cases pass")
    for f in failures:
        print(f"  FAIL {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
