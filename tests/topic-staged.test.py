#!/usr/bin/env python3
"""Staged topic pass tests: the mechanics between the linker's three stages.

A corpus too large for one topic-linker agent is filed in stages: one agent
proposes the topic list (`topics.skeleton.json`), several file one payload
chunk each (`topics.chunk-NN.json`), and one consolidates. The scripts do the
mechanics in between, so these cases lock in:

- `check_topics --skeleton-only` passes a well-formed topic list and stops one
  with concepts filed, a one-sided debate or a broader link to nothing;
- `check_topics --chunk NN` judges one chunk against its payload, with the
  chunk's proposed topics counted as topics;
- `merge_topic_chunks merge` folds chunk filings into the skeleton by key and
  debate side by label, pools proposals by key across chunks, and stops on a
  filing against a topic or side the skeleton lacks;
- `merge_topic_chunks apply` accepts, redirects, splits, moves, drops, edits
  and flags duplicates, and stops on an operation that names a missing topic;
- a full check fails while proposals remain unconsolidated, and passes once
  they are settled.

No test framework, matching tests/mechanical-headings.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/topic-staged.test.py
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes.check_topics import check, check_skeleton, chunk_doc  # noqa: E402
from scripts.build_indexes.merge_topic_chunks import apply, merge  # noqa: E402


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def row(concept: str, aliases: list[str] | None = None) -> dict:
    return {"concept": concept, "name": concept.replace("-", " ").title(), "aliases": aliases or [],
            "sources": [], "contexts": {}, "filed": False}


CHUNK_1 = [row("hindsight-bias", ["knowledge-of-outcome bias"]), row("high-reliability-organizations"),
           row("challenger"), row("blameless-review")]
CHUNK_2 = [row("normal-accident-theory", ["NAT"]), row("outcome-bias"), row("subject-index"),
           row("psychological-safety")]

SKELETON = {
    "schema_version": 1,
    "grain_rule": "a topic is a subject a practitioner would look up",
    "topics": [
        {"key": "cognitive-biases", "name": "Cognitive biases", "kind": "subject", "synonyms": [],
         "boundary": "", "scope_note": "", "broader": ""},
        {"key": "hindsight-bias", "name": "Hindsight bias", "kind": "subject", "synonyms": [],
         "boundary": "not outcome bias", "scope_note": "", "broader": "cognitive-biases"},
        {"key": "accident-models", "name": "Accident models", "kind": "subject", "synonyms": [],
         "boundary": "", "scope_note": "", "broader": ""},
        {"key": "nat-vs-hro", "name": "Normal accidents vs high reliability", "kind": "debate", "synonyms": [],
         "boundary": "", "scope_note": "", "broader": "",
         "positions": [{"label": "accidents are inevitable"}, {"label": "reliability can be organised"}]},
    ],
}

FILED_1 = {
    "chunk": "01",
    "topics": [
        {"key": "hindsight-bias", "concepts": ["hindsight-bias"], "examples": ["challenger"]},
        {"key": "cognitive-biases", "concepts": ["hindsight-bias"]},
        {"key": "accident-models", "concepts": ["high-reliability-organizations"]},
        {"key": "nat-vs-hro", "positions": [{"label": "reliability can be organised",
                                             "concepts": ["high-reliability-organizations"]}]},
    ],
    "proposed_topics": [
        {"key": "blameless-culture", "name": "Blameless culture", "kind": "subject", "synonyms": [],
         "boundary": "", "scope_note": "", "broader": "", "concepts": ["blameless-review"], "examples": [],
         "why": "no skeleton topic covers how teams respond to failure"},
    ],
    "unplaced": [],
    "synonyms": {"hindsight-bias": ["knowledge-of-outcome bias"]},
    "merge_candidates": [],
}

FILED_2 = {
    "chunk": "02",
    "topics": [
        {"key": "cognitive-biases", "concepts": ["outcome-bias"]},
        {"key": "accident-models", "concepts": ["normal-accident-theory"]},
        {"key": "nat-vs-hro", "positions": [{"label": "accidents are inevitable",
                                             "concepts": ["normal-accident-theory"]}]},
    ],
    "proposed_topics": [
        {"key": "blameless-culture", "name": "Blameless culture", "kind": "subject", "synonyms": [],
         "boundary": "", "scope_note": "", "broader": "", "concepts": ["psychological-safety"], "examples": [],
         "why": "safety to speak up belongs with blameless practice"},
    ],
    "unplaced": [{"concept": "subject-index", "reason": "noise"}],
    "synonyms": {"normal-accident-theory": ["NAT"]},
    "merge_candidates": [],
}


def labels(problems) -> set[str]:
    return {label for label, _ in problems}


def case_skeleton_check_passes_a_topic_list() -> None:
    problems, counts = check_skeleton(SKELETON)
    assert_(not problems, f"a well-formed skeleton must pass: {problems}")
    assert_(counts == {"topics": 4, "debates": 1}, f"counts: {counts}")


def case_skeleton_check_reports_problems() -> None:
    bad = copy.deepcopy(SKELETON)
    bad["topics"][0]["concepts"] = ["outcome-bias"]
    bad["topics"][1]["broader"] = "no-such-topic"
    bad["topics"][3]["positions"] = [{"label": "accidents are inevitable"}]
    found = labels(check_skeleton(bad)[0])
    for expected in ("concepts filed in the skeleton (filing is stage 2)", "broader names no topic",
                     "debate with fewer than two labelled sides"):
        assert_(expected in found, f"expected '{expected}' among {found}")


def case_chunk_check_counts_proposals_as_topics() -> None:
    doc, unknown = chunk_doc(SKELETON, FILED_1)
    assert_(not unknown, f"chunk 1 files only against skeleton topics: {unknown}")
    problems, _ = check(CHUNK_1, doc)
    assert_(not problems, f"a complete chunk must pass, its proposals counted as topics: {problems}")


def case_chunk_check_reports_unknown_topics_and_gaps() -> None:
    filed = copy.deepcopy(FILED_1)
    filed["topics"].append({"key": "no-such-topic", "concepts": ["challenger"]})
    filed["topics"][3]["positions"][0]["label"] = "a side nobody wrote"
    filed["proposed_topics"] = []                      # blameless-review now placed nowhere
    doc, unknown = chunk_doc(SKELETON, filed)
    assert_("no-such-topic" in unknown, f"an unknown key must be reported: {unknown}")
    assert_(any("a side nobody wrote" in u for u in unknown), f"an unknown side must be reported: {unknown}")
    assert_("not placed" in labels(check(CHUNK_1, doc)[0]), "an unfiled concept in the chunk must be reported")


def case_merge_folds_chunks_and_pools_proposals() -> None:
    doc = merge(SKELETON, [FILED_1, FILED_2])
    topics = {t["key"]: t for t in doc["topics"]}
    assert_(topics["cognitive-biases"]["concepts"] == ["hindsight-bias", "outcome-bias"],
            f"filings from both chunks must land on the skeleton topic: {topics['cognitive-biases']}")
    sides = {p["label"]: p["concepts"] for p in topics["nat-vs-hro"]["positions"]}
    assert_(sides == {"accidents are inevitable": ["normal-accident-theory"],
                      "reliability can be organised": ["high-reliability-organizations"]},
            f"debate sides must be matched by label: {sides}")
    assert_(len(doc["proposed_topics"]) == 1, f"one key proposed twice pools into one: {doc['proposed_topics']}")
    pooled = doc["proposed_topics"][0]
    assert_(pooled["concepts"] == ["blameless-review", "psychological-safety"] and pooled["from_chunks"] == ["01", "02"],
            f"pooled proposal: {pooled}")
    assert_(doc["synonyms"] == {"hindsight-bias": ["knowledge-of-outcome bias"], "normal-accident-theory": ["NAT"]},
            f"synonyms from every chunk: {doc['synonyms']}")
    assert_("proposed topics not yet consolidated" in labels(check(CHUNK_1 + CHUNK_2, doc)[0]),
            "a merged file with open proposals must fail the full check")


def case_merge_stops_on_unknown_topics() -> None:
    filed = copy.deepcopy(FILED_2)
    filed["topics"].append({"key": "no-such-topic", "concepts": ["outcome-bias"]})
    try:
        merge(SKELETON, [FILED_1, filed])
    except SystemExit as e:
        assert_("no-such-topic" in str(e), f"the error must name the unknown topic: {e}")
        return
    raise AssertionError("a chunk filing against a topic the skeleton lacks must stop the merge")


def case_apply_accepts_then_the_file_passes() -> None:
    doc = apply(merge(SKELETON, [FILED_1, FILED_2]),
                {"accept": [{"key": "blameless-culture", "boundary": "responses to failure, not blame"}]})
    assert_("proposed_topics" not in doc, "an empty proposal list must be dropped")
    accepted = {t["key"]: t for t in doc["topics"]}["blameless-culture"]
    assert_("from_chunks" not in accepted and "why" not in accepted, f"working fields must go: {accepted}")
    assert_(accepted["boundary"] == "responses to failure, not blame", "accept may change fields")
    problems, _ = check(CHUNK_1 + CHUNK_2, doc)
    assert_(not problems, f"a consolidated file must pass the full check: {problems}")


def case_apply_redirects_splits_and_edits() -> None:
    merged = merge(SKELETON, [FILED_1, FILED_2])
    merged["topics"][2]["examples"] = ["challenger"]
    doc = apply(merged, {
        "redirect": {"blameless-culture": "cognitive-biases", "hindsight-bias": "cognitive-biases"},
        "split": {"accident-models": [{"key": "normal-accidents", "name": "Normal accidents",
                                       "concepts": ["normal-accident-theory"], "examples": ["challenger"]}]},
        "edit": {"cognitive-biases": {"name": "Cognitive biases in review", "concepts": ["ignored"]}},
    })
    topics = {t["key"]: t for t in doc["topics"]}
    assert_("hindsight-bias" not in topics, "a redirected topic must be removed")
    biases = topics["cognitive-biases"]
    assert_(set(biases["concepts"]) == {"hindsight-bias", "outcome-bias", "blameless-review", "psychological-safety"},
            f"redirect must move every member: {biases['concepts']}")
    assert_(biases["examples"] == ["challenger"], f"redirect must move examples: {biases['examples']}")
    assert_(biases["name"] == "Cognitive biases in review", "edit must change the name")
    assert_(biases["concepts"] != ["ignored"], "edit must not touch filings")
    child = topics["normal-accidents"]
    assert_(child["broader"] == "accident-models", f"a split child's broader is its parent: {child}")
    parent = topics["accident-models"]
    assert_("normal-accident-theory" not in parent["concepts"] and parent["examples"] == [],
            f"split members must leave the parent: {parent}")


def case_apply_repoints_broader_links_on_redirect() -> None:
    merged = merge(SKELETON, [FILED_1, FILED_2])
    doc = apply(merged, {"accept": [{"key": "blameless-culture"}], "redirect": {"cognitive-biases": "accident-models"}})
    hindsight = {t["key"]: t for t in doc["topics"]}["hindsight-bias"]
    assert_(hindsight["broader"] == "accident-models", f"a child of a redirected topic follows it: {hindsight}")


def case_apply_moves_concepts_and_flags_duplicates() -> None:
    merged = merge(SKELETON, [FILED_1, FILED_2])
    doc = apply(merged, {
        "accept": [{"key": "blameless-culture"}],
        "move": [{"concept": "challenger", "from": "hindsight-bias", "to": "accident-models"},
                 {"concept": "normal-accident-theory", "from": "nat-vs-hro", "to": ""},
                 {"concept": "outcome-bias", "from": "", "to": "hindsight-bias"}],
        "merge_candidates": [{"concepts": ["blameless-review", "psychological-safety"], "note": "fixture"}],
    })
    topics = {t["key"]: t for t in doc["topics"]}
    assert_(topics["accident-models"]["examples"] == ["challenger"] and topics["hindsight-bias"]["examples"] == [],
            "an example moves as an example")
    sides = {p["label"]: p["concepts"] for p in topics["nat-vs-hro"]["positions"]}
    assert_(sides["accidents are inevitable"] == [], f"an empty 'to' removes the placement: {sides}")
    assert_("outcome-bias" in topics["hindsight-bias"]["concepts"], "an empty 'from' adds a placement")
    assert_(doc["merge_candidates"] == [{"concepts": ["blameless-review", "psychological-safety"], "note": "fixture"}],
            f"flags are added: {doc['merge_candidates']}")
    try:
        apply(merged, {"move": [{"concept": "outcome-bias", "from": "hindsight-bias", "to": "accident-models"}]})
    except SystemExit as e:
        assert_("not in 'hindsight-bias'" in str(e), f"the error must say where the concept isn't: {e}")
        return
    raise AssertionError("moving a concept out of a topic that doesn't hold it must stop")


def case_apply_drops_a_debate_without_moving_its_sides() -> None:
    merged = merge(SKELETON, [FILED_1, FILED_2])
    doc = apply(merged, {"accept": [{"key": "blameless-culture"}], "drop": ["nat-vs-hro", "cognitive-biases"]})
    topics = {t["key"]: t for t in doc["topics"]}
    assert_("nat-vs-hro" not in topics, "a dropped debate must be removed")
    assert_(topics["accident-models"]["concepts"] == ["high-reliability-organizations", "normal-accident-theory"],
            f"a drop must not move the debate's sides anywhere: {topics['accident-models']}")
    assert_(topics["hindsight-bias"]["broader"] == "", f"a child moves up to the dropped topic's broader: {topics['hindsight-bias']}")
    assert_("not placed" in labels(check(CHUNK_1 + CHUNK_2, doc)[0]),
            "dropping a subject topic that alone held a concept must fail the check")


def case_apply_stops_on_missing_topics() -> None:
    merged = merge(SKELETON, [FILED_1, FILED_2])
    for ops in ({"accept": [{"key": "no-such-proposal"}]}, {"redirect": {"blameless-culture": "no-such-topic"}},
                {"split": {"no-such-topic": []}}, {"edit": {"no-such-topic": {"name": "x"}}},
                {"drop": ["no-such-topic"]}):
        try:
            apply(merged, ops)
        except SystemExit as e:
            assert_("no-such" in str(e), f"the error must name what is missing: {e}")
            continue
        raise AssertionError(f"ops naming a missing topic must stop: {ops}")


CASES = [
    case_skeleton_check_passes_a_topic_list,
    case_skeleton_check_reports_problems,
    case_chunk_check_counts_proposals_as_topics,
    case_chunk_check_reports_unknown_topics_and_gaps,
    case_merge_folds_chunks_and_pools_proposals,
    case_merge_stops_on_unknown_topics,
    case_apply_accepts_then_the_file_passes,
    case_apply_redirects_splits_and_edits,
    case_apply_repoints_broader_links_on_redirect,
    case_apply_moves_concepts_and_flags_duplicates,
    case_apply_drops_a_debate_without_moving_its_sides,
    case_apply_stops_on_missing_topics,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        try:
            case()
            print(f"  ok   {case.__name__}")
        except (Exception, SystemExit) as e:  # noqa: BLE001 — the scripts stop with SystemExit; report it as a failure
            failures.append(f"{case.__name__}: {e}")
            print(f"  FAIL {case.__name__}: {e}")

    print()
    if failures:
        print(f"topic-staged: {len(failures)} of {len(CASES)} cases FAILED")
        return 1
    print(f"topic-staged: all {len(CASES)} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
