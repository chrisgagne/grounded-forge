#!/usr/bin/env python3
"""Schema-3 concept index tests: the one-file topics-and-concepts contract.

Locks in what retrieval relies on when `build_concept_index.py --assemble`
finds a topics file:

- the topics block sits at the top, one topic per line, and `topic_lines`
  brackets exactly that block, so a model can read the block and nothing else;
- `grep -F '"t031'` over the file returns exactly the rows under topic t031,
  including rows on each side of a debate (`t031.1`) and rows tagged with the
  bare debate ID;
- topic IDs are append-only and fixed-width, never reused after a topic retires;
- a topics file that names a concept the vocabulary doesn't have stops the build.

Also covers the carry-forward of section pointers for sources whose extracted
artefacts aren't on this machine.

No test framework, matching tests/mechanical-headings.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/concept-index-schema3.test.py
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes.build_concept_index import (  # noqa: E402
    _assign_topic_ids,
    _previous_pointers,
    _write_schema3,
)


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


CONCEPTS = {
    "hindsight-bias": {"name": "Hindsight Bias", "aliases": ["knowledge-of-outcome bias", "hindsight bias cook"],
                       "sources": [{"id": "02h"}, {"id": "06y", "context": "outcome knowledge distorts judgment"}]},
    "outcome-bias": {"name": "Outcome Bias", "aliases": [], "sources": [{"id": "06y"}]},
    "normal-accident-theory": {"name": "Normal Accident Theory", "aliases": ["NAT"], "sources": [{"id": "05a"}]},
    "high-reliability-organizations": {"name": "High Reliability Organizations", "aliases": ["HRO"],
                                       "sources": [{"id": "05a"}, {"id": "03r"}]},
    "nat-hro-reconciliation": {"name": "NAT/HRO Reconciliation", "aliases": [], "sources": [{"id": "05q"}]},
    "challenger": {"name": "Challenger", "aliases": [], "sources": [{"id": "05l"}]},
    "subject-index": {"name": "SUBJECT INDEX", "aliases": [], "sources": [{"id": "05l"}]},
}

TOPICS = {
    "topics": [
        {"key": "hindsight-bias", "name": "Hindsight bias", "kind": "subject",
         "synonyms": ["knew-it-all-along effect"], "boundary": "not outcome bias",
         "broader": "cognitive-biases", "concepts": ["hindsight-bias"], "examples": ["challenger"]},
        {"key": "cognitive-biases", "name": "Cognitive biases", "kind": "subject", "synonyms": [],
         "boundary": "", "broader": "", "concepts": ["outcome-bias", "hindsight-bias"], "examples": []},
        {"key": "nat-vs-hro", "name": "Normal accidents vs high reliability", "kind": "debate",
         "synonyms": [], "boundary": "", "broader": "", "concepts": ["nat-hro-reconciliation"], "examples": [],
         "positions": [{"label": "accidents are inevitable", "concepts": ["normal-accident-theory"]},
                       {"label": "reliability can be organised", "concepts": ["high-reliability-organizations"]}]},
        {"key": "accident-models", "name": "Accident models", "kind": "subject", "synonyms": [],
         "boundary": "", "broader": "", "examples": [],
         "concepts": ["normal-accident-theory", "high-reliability-organizations", "nat-hro-reconciliation"]},
    ],
    "unplaced": [{"concept": "subject-index", "reason": "noise"}],
    "synonyms": {"hindsight-bias": ["knowledge-of-outcome bias"], "high-reliability-organizations": ["HRO"]},
}


def build(concepts=CONCEPTS, topics=TOPICS, published=frozenset()):
    doc = copy.deepcopy(topics)
    _assign_topic_ids(doc, set(published))
    out = Path(tempfile.mkdtemp()) / "concept-index.json"
    stats = _write_schema3(out, "fixture", concepts, doc)
    return out, doc, stats


def case_ids_are_append_only_and_fixed_width() -> None:
    doc = copy.deepcopy(TOPICS)
    doc["topics"][1]["id"] = "t007"
    assert_(_assign_topic_ids(doc, {"t009"}), "expected new IDs to be assigned")
    ids = [t["id"] for t in doc["topics"]]
    assert_(ids[1] == "t007", f"an existing ID was reassigned: {ids}")
    assert_(sorted(ids) == ["t007", "t010", "t011", "t012"], f"new IDs must follow the highest published: {ids}")
    assert_(not _assign_topic_ids(doc, set()), "a second pass must assign nothing")
    full = {"topics": [{"key": "x"}]}
    try:
        _assign_topic_ids(full, {"t999"})
    except SystemExit:
        return
    raise AssertionError("passing t999 must stop the build")


def case_topic_lines_bracket_the_block() -> None:
    out, doc, _ = build()
    text = out.read_text()
    index = json.loads(text)
    lines = text.splitlines()
    start, end = index["topic_lines"]
    block = lines[start - 1:end]
    assert_(index["schema_version"] == 3, "schema_version must be 3")
    assert_(len(block) == len(doc["topics"]), f"block holds {len(block)} lines, expected {len(doc['topics'])}")
    assert_(all(line.startswith('["t') for line in block), "every block line must be a topic")
    assert_(not lines[end].startswith('["t'), "the line after the block must not be a topic")


def case_prefix_grep_returns_each_topics_rows() -> None:
    out, doc, _ = build()
    text = out.read_text()
    index = json.loads(text)
    rows = text.splitlines()[index["topic_lines"][1]:]
    ids = {t["key"]: t["id"] for t in doc["topics"]}

    def grep(topic_id):
        return sorted(json.loads(line.rstrip(","))[0] for line in rows if f'"{topic_id}' in line)

    assert_(grep(ids["hindsight-bias"]) == ["Challenger", "Hindsight Bias"],
            f"hindsight topic rows: {grep(ids['hindsight-bias'])}")
    assert_(grep(ids["nat-vs-hro"]) == ["High Reliability Organizations", "NAT/HRO Reconciliation",
                                        "Normal Accident Theory"],
            f"debate rows must include both sides and the bare debate ID: {grep(ids['nat-vs-hro'])}")
    by_name = {r[0]: r for r in index["concepts"]}
    debate = ids["nat-vs-hro"]
    assert_(f"{debate}.1" in by_name["Normal Accident Theory"][4], "side 1 must be tagged with a .1 suffix")
    assert_(f"{debate}.2" in by_name["High Reliability Organizations"][4], "side 2 must be tagged with a .2 suffix")


def case_rows_carry_kind_synonyms_and_contexts() -> None:
    out, _, stats = build()
    by_name = {r[0]: r for r in json.loads(out.read_text())["concepts"]}
    assert_(by_name["Challenger"][1] == "example", "a concept filed only as an example is kind example")
    assert_(by_name["Hindsight Bias"][1] == "concept", "a concept filed under concepts is kind concept")
    assert_(by_name["Hindsight Bias"][2] == ["knowledge-of-outcome bias"], "reviewed synonyms replace the aliases")
    assert_(by_name["Normal Accident Theory"][2] == ["NAT"], "unreviewed aliases stay until the linker decides")
    assert_(by_name["Hindsight Bias"][5] == {"06y": "outcome knowledge distorts judgment"}, "contexts must survive")
    assert_(by_name["SUBJECT INDEX"][4] == [], "an unplaced concept keeps its row with no topics")
    assert_(stats["unfiled"] == [], f"unplaced noise must not count as unfiled: {stats['unfiled']}")
    assert_(stats["unreviewed"] == 1, f"only NAT has aliases the linker didn't review: {stats['unreviewed']}")


def case_topic_line_counts_and_links() -> None:
    out, doc, _ = build()
    topics = {t[1]: t for t in json.loads(out.read_text())["topics"]}
    ids = {t["key"]: t["id"] for t in doc["topics"]}
    hb = topics["Hindsight bias"]
    assert_(hb[3] == "not outcome bias", "the boundary is the topic's note")
    assert_(hb[5] == ids["cognitive-biases"], "broader is written as the parent's topic ID")
    assert_(hb[6] == 2 and hb[7] == 3, f"hindsight topic: 2 rows over 3 sources, got {hb[6]} and {hb[7]}")
    debate = topics["Normal accidents vs high reliability"]
    assert_(debate[4] == "debate" and debate[8] == ["accidents are inevitable", "reliability can be organised"],
            f"a debate lists its sides: {debate}")


def case_unknown_concept_stops_the_build() -> None:
    doc = copy.deepcopy(TOPICS)
    doc["topics"][0]["concepts"].append("no-such-concept")
    try:
        build(topics=doc)
    except SystemExit as e:
        assert_("no-such-concept" in str(e), f"the error must name the unknown concept: {e}")
        return
    raise AssertionError("a topics file naming an unknown concept must stop the build")


def case_previous_pointers_are_keyed_by_concept_and_source() -> None:
    deep = {"concepts": {"hindsight-bias": {"sources": [{"id": "02h", "section": "Ch 3", "md_line": 120},
                                                        {"id": "06y"}]}}}
    path = Path(tempfile.mkdtemp()) / "concept-index-deep.json"
    path.write_text(json.dumps(deep))
    pointers = _previous_pointers(path)
    assert_(pointers == {("hindsight-bias", "02h"): {"section": "Ch 3", "md_line": 120}},
            f"only sources with a pointer are carried: {pointers}")
    assert_(_previous_pointers(path.parent / "missing.json") == {}, "a missing deep index carries nothing")


CASES = [
    case_ids_are_append_only_and_fixed_width,
    case_topic_lines_bracket_the_block,
    case_prefix_grep_returns_each_topics_rows,
    case_rows_carry_kind_synonyms_and_contexts,
    case_topic_line_counts_and_links,
    case_unknown_concept_stops_the_build,
    case_previous_pointers_are_keyed_by_concept_and_source,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        try:
            case()
            print(f"  ok   {case.__name__}")
        except (Exception, SystemExit) as e:  # noqa: BLE001 — the builder stops with SystemExit; report it as a failure
            failures.append(f"{case.__name__}: {e}")
            print(f"  FAIL {case.__name__}: {e}")

    print()
    if failures:
        print(f"concept-index-schema3: {len(failures)} of {len(CASES)} cases FAILED")
        return 1
    print(f"concept-index-schema3: all {len(CASES)} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
