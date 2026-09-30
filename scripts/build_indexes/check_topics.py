"""Check the topic linker's output against the vocabulary it was given.

Reads ``_planning/staging/{corpus}/concepts/topic-payload.jsonl`` (from
``build_concept_index --emit-topic-payload``) and ``topics.json`` beside it,
and reports every way the topics file breaks the Pass H topic contract:

- every concept in the payload is placed: under at least one subject topic
  (as a concept or an example), or in ``unplaced`` as noise;
- no concept sits under more than three subject topics, and debate sides are
  in addition to a subject topic, not instead of one;
- every concept with aliases has a synonyms decision, and every kept synonym
  is one of that concept's aliases, verbatim;
- names, keys, broader links, IDs, boundaries and merge candidates are well
  formed.

Exits non-zero until the file passes, so the linker can run it until clean.

The staged pass (corpora too large for one agent) checks its stages too:
``--skeleton-only`` checks the stage-1 topic list, ``topics.skeleton.json``;
``--chunk NN`` checks one stage-2 file, ``topics.chunk-NN.json``, against its
payload chunk, with the chunk's proposed topics counted as topics. A full
check fails while ``topics.json`` still holds proposals consolidation hasn't
settled.

Usage:
    python3 -m scripts.build_indexes.check_topics --corpus demo
    python3 -m scripts.build_indexes.check_topics --corpus aarbuddy --skeleton-only
    python3 -m scripts.build_indexes.check_topics --corpus aarbuddy --chunk 03
"""

from __future__ import annotations

import argparse
import collections
import copy
import json
import re
import sys
from pathlib import Path

from .common import staging_dir

_ID = re.compile(r"t\d{3}")
_KEY = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def check(payload: list[dict], doc: dict) -> tuple[list[tuple[str, list]], dict]:
    """Return (problems as (label, items), counts). No problems means the file passes."""
    concepts = {p["concept"]: p for p in payload}
    topics = doc.get("topics", [])
    problems: dict[str, list] = collections.defaultdict(list)

    keys = [t.get("key", "") for t in topics]
    problems["duplicate topic keys"] = sorted(k for k, n in collections.Counter(keys).items() if n > 1)
    problems["malformed topic keys"] = sorted(k for k in keys if not _KEY.fullmatch(k))
    ids = [t["id"] for t in topics if t.get("id")]
    problems["duplicate topic IDs"] = sorted(i for i, n in collections.Counter(ids).items() if n > 1)
    problems["malformed topic IDs"] = sorted(i for i in ids if not _ID.fullmatch(i))
    names = [t.get("name", "") for t in topics]
    problems["duplicate topic names"] = sorted(n for n, k in collections.Counter(names).items() if k > 1)
    known_keys = set(keys)

    subject_count: collections.Counter = collections.Counter()
    placed: set[str] = set()
    for t in topics:
        key = t.get("key", "?")
        if t.get("kind", "subject") not in ("subject", "debate"):
            problems["kind is neither subject nor debate"].append(key)
        if t.get("broader") and t["broader"] not in known_keys:
            problems["broader names no topic"].append(f"{key} -> {t['broader']}")
        if len((t.get("boundary") or "").split()) > 14:
            problems["boundary over about 12 words"].append(key)
        members = list(t.get("concepts", [])) + list(t.get("examples", []))
        if t.get("kind") == "debate":
            if len(t.get("positions", [])) < 2:
                problems["debate with fewer than two sides"].append(key)
            for p in t.get("positions", []):
                members += p.get("concepts", [])
        else:
            if t.get("positions"):
                problems["positions on a subject topic"].append(key)
            subject_count.update(set(t.get("concepts", [])) | set(t.get("examples", [])))
        for c in members:
            if c not in concepts:
                problems["unknown concept"].append(f"{key} -> {c}")
            placed.add(c)

    unplaced = {u.get("concept") for u in doc.get("unplaced", [])}
    problems["unplaced for a reason other than noise"] = sorted(
        u.get("concept") for u in doc.get("unplaced", []) if u.get("reason") != "noise")
    problems["unplaced names an unknown concept"] = sorted(c for c in unplaced if c not in concepts)
    problems["not placed"] = sorted(c for c in concepts if c not in placed and c not in unplaced)
    problems["placed only on a debate side (needs a subject topic)"] = sorted(
        c for c in placed if c in concepts and c not in unplaced and subject_count[c] == 0)
    problems["more than three subject topics"] = sorted(c for c, n in subject_count.items() if n > 3)

    synonyms = doc.get("synonyms", {})
    problems["aliases with no synonyms decision"] = sorted(
        c for c, p in concepts.items() if p["aliases"] and c not in synonyms and c not in unplaced)
    problems["kept synonym not among the concept's aliases"] = sorted(
        f"{c}: {a}" for c, kept in synonyms.items() for a in kept
        if c not in concepts or a not in concepts[c]["aliases"])

    for group in doc.get("merge_candidates", []):
        members = group.get("concepts", [])
        if len(members) < 2 or any(c not in concepts for c in members):
            problems["malformed merge candidate"].append(", ".join(members))

    problems["proposed topics not yet consolidated"] = [p.get("key") for p in doc.get("proposed_topics", [])]

    counts = {
        "topics": len(topics),
        "debates": sum(1 for t in topics if t.get("kind") == "debate"),
        "placed": len(placed & set(concepts)),
        "unplaced": len(unplaced),
        "concepts": len(concepts),
        "kept synonyms": sum(len(v) for v in synonyms.values()),
        "merge candidates": len(doc.get("merge_candidates", [])),
    }
    return [(label, items) for label, items in problems.items() if items], counts


def check_skeleton(skeleton: dict) -> tuple[list[tuple[str, list]], dict]:
    """Stage 1 of the staged pass: the topic list, before any concept is filed."""
    topics = skeleton.get("topics", [])
    problems: dict[str, list] = collections.defaultdict(list)
    keys = [t.get("key", "") for t in topics]
    problems["duplicate topic keys"] = sorted(k for k, n in collections.Counter(keys).items() if n > 1)
    problems["malformed topic keys"] = sorted(k for k in keys if not _KEY.fullmatch(k))
    names = [t.get("name", "") for t in topics]
    problems["duplicate topic names"] = sorted(n for n, k in collections.Counter(names).items() if k > 1)
    for t in topics:
        key = t.get("key", "?")
        if t.get("kind", "subject") not in ("subject", "debate"):
            problems["kind is neither subject nor debate"].append(key)
        if t.get("broader") and t["broader"] not in keys:
            problems["broader names no topic"].append(f"{key} -> {t['broader']}")
        if len((t.get("boundary") or "").split()) > 14:
            problems["boundary over about 12 words"].append(key)
        if t.get("kind") == "debate" and len([p for p in t.get("positions", []) if p.get("label")]) < 2:
            problems["debate with fewer than two labelled sides"].append(key)
        if t.get("concepts") or t.get("examples") or any(p.get("concepts") for p in t.get("positions", [])):
            problems["concepts filed in the skeleton (filing is stage 2)"].append(key)
    counts = {"topics": len(topics), "debates": sum(1 for t in topics if t.get("kind") == "debate")}
    return [(label, items) for label, items in problems.items() if items], counts


def chunk_doc(skeleton: dict, chunk: dict) -> tuple[dict, list[str]]:
    """Stage 2: one chunk's filings over the skeleton, with its proposals as topics.

    Returns the combined topics document ``check`` can judge against the chunk's
    payload, and the chunk's references to topics or sides the skeleton lacks.
    """
    topics = {t["key"]: {**copy.deepcopy(t), "concepts": [], "examples": []} for t in skeleton.get("topics", [])}
    for t in topics.values():
        if t.get("kind") == "debate":
            t["positions"] = [{"label": p["label"], "concepts": []} for p in t.get("positions", [])]
    unknown = []
    for entry in chunk.get("topics", []):
        target = topics.get(entry.get("key"))
        if target is None:
            unknown.append(entry.get("key"))
            continue
        target["concepts"] += entry.get("concepts", [])
        target["examples"] += entry.get("examples", [])
        sides = {p["label"]: p for p in target.get("positions", [])}
        for p in entry.get("positions", []):
            if p.get("label") in sides:
                sides[p["label"]]["concepts"] += p.get("concepts", [])
            else:
                unknown.append(f"{target['key']} side '{p.get('label')}'")
    for p in chunk.get("proposed_topics", []):
        if p.get("key") in topics:
            unknown.append(f"proposal '{p.get('key')}' reuses a skeleton key")
            continue
        topics[p["key"]] = {k: v for k, v in p.items() if k != "why"}
    doc = {"topics": list(topics.values()), "unplaced": chunk.get("unplaced", []),
           "synonyms": chunk.get("synonyms", {}), "merge_candidates": chunk.get("merge_candidates", [])}
    return doc, unknown


def _read_payload(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check topics.json against the topic payload")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--folder", type=Path, help="staging folder (default _planning/staging/{corpus}/concepts)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--skeleton-only", action="store_true", help="check topics.skeleton.json (staged stage 1)")
    mode.add_argument("--chunk", help="check topics.chunk-NN.json against its chunk (staged stage 2)")
    args = parser.parse_args(argv)

    folder = args.folder or staging_dir(args.corpus, "concepts")
    if args.skeleton_only:
        needed = [folder / "topics.skeleton.json"]
    elif args.chunk:
        needed = [folder / f"topic-payload.chunk-{args.chunk}.jsonl", folder / f"topics.chunk-{args.chunk}.json",
                  folder / "topics.skeleton.json"]
    else:
        needed = [folder / "topic-payload.jsonl", folder / "topics.json"]
    for path in needed:
        if not path.is_file():
            print(f"missing {path}")
            return 1

    if args.skeleton_only:
        problems, counts = check_skeleton(json.load(open(needed[0], encoding="utf-8")))
    elif args.chunk:
        doc, unknown = chunk_doc(json.load(open(needed[2], encoding="utf-8")), json.load(open(needed[1], encoding="utf-8")))
        problems, counts = check(_read_payload(needed[0]), doc)
        if unknown:
            problems.append(("files against topics or sides the skeleton lacks", unknown))
    else:
        with needed[1].open(encoding="utf-8") as f:
            doc = json.load(f)
        problems, counts = check(_read_payload(needed[0]), doc)
    print(", ".join(f"{k}: {v}" for k, v in counts.items()))
    for label, items in problems:
        print(f"{label} ({len(items)}): {items[:12]}{' …' if len(items) > 12 else ''}")
    print("PASS" if not problems else f"FAIL: {len(problems)} kinds of problem")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
