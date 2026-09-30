"""The mechanical steps of the staged topic pass, for corpora too large to file in one agent.

Staged filing runs in three stages (see the ingest-topic-linker agent):

1. propose: one agent reads ``topic-names.jsonl`` and writes the topic list,
   ``topics.skeleton.json``, with no concepts filed;
2. file: several agents each file one chunk (``topic-payload.chunk-NN.jsonl``)
   against the skeleton, writing ``topics.chunk-NN.json``;
3. consolidate: one agent reviews the merged result and writes
   ``topics.consolidation.json``, a list of operations this script applies.

This script does the mechanics between the stages, so no agent hand-edits a
large JSON file:

    merge    skeleton + chunk files -> topics.json (proposed topics kept apart)
    report   every topic's size and members, then every proposed topic, compactly
    apply    carry out topics.consolidation.json on topics.json, keeping the
             previous state in topics.before-apply.json

Usage:
    python3 -m scripts.build_indexes.merge_topic_chunks merge  --corpus aarbuddy
    python3 -m scripts.build_indexes.merge_topic_chunks report --corpus aarbuddy
    python3 -m scripts.build_indexes.merge_topic_chunks apply  --corpus aarbuddy

``--folder`` points at a staging folder other than
``_planning/staging/{corpus}/concepts/``.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

from .common import staging_dir

OVERSIZED = 40


def _dedupe(items: list) -> list:
    seen, out = set(), []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def merge(skeleton: dict, chunks: list[dict]) -> dict:
    """Fold chunk filings into the skeleton's topics; collect proposals apart.

    A chunk may only file against skeleton topics (by key) and its own
    proposals. Proposals with the same key from different chunks are pooled;
    consolidation decides what becomes of them.
    """
    topics = []
    for t in skeleton["topics"]:
        topic = copy.deepcopy(t)
        topic["concepts"], topic["examples"] = [], []
        if topic.get("kind") == "debate":
            topic["positions"] = [{"label": p["label"], "concepts": []} for p in t.get("positions", [])]
        topics.append(topic)
    by_key = {t["key"]: t for t in topics}
    proposed: dict[str, dict] = {}
    unknown: list[str] = []
    out = {"schema_version": 1, "grain_rule": skeleton.get("grain_rule", ""), "topics": topics,
           "unplaced": [], "synonyms": {}, "merge_candidates": []}

    for chunk in chunks:
        label = chunk.get("chunk", "?")
        for entry in chunk.get("topics", []):
            target = by_key.get(entry.get("key"))
            if target is None:
                unknown.append(f"chunk {label}: {entry.get('key')}")
                continue
            target["concepts"] += entry.get("concepts", [])
            target["examples"] += entry.get("examples", [])
            sides = {p["label"]: p for p in target.get("positions", [])}
            for p in entry.get("positions", []):
                if p.get("label") not in sides:
                    unknown.append(f"chunk {label}: side '{p.get('label')}' of {target['key']}")
                    continue
                sides[p["label"]]["concepts"] += p.get("concepts", [])
        for p in chunk.get("proposed_topics", []):
            pooled = proposed.setdefault(p["key"], {**copy.deepcopy(p), "concepts": [], "examples": [], "from_chunks": []})
            pooled["concepts"] += p.get("concepts", [])
            pooled["examples"] += p.get("examples", [])
            pooled["from_chunks"].append(label)
        out["unplaced"] += chunk.get("unplaced", [])
        out["synonyms"].update(chunk.get("synonyms", {}))
        out["merge_candidates"] += chunk.get("merge_candidates", [])

    if unknown:
        raise SystemExit("chunks file against topics the skeleton doesn't have:\n"
                         + "".join(f"  {u}\n" for u in unknown[:30]))
    for t in topics + list(proposed.values()):
        t["concepts"], t["examples"] = _dedupe(t["concepts"]), _dedupe(t["examples"])
        for p in t.get("positions", []):
            p["concepts"] = _dedupe(p["concepts"])
    out["proposed_topics"] = list(proposed.values())
    return out


def _members(topic: dict) -> list[str]:
    names = list(topic.get("concepts", [])) + list(topic.get("examples", []))
    for p in topic.get("positions", []):
        names += p.get("concepts", [])
    return _dedupe(names)


def report(doc: dict) -> str:
    """Every topic with its size and members, outliers flagged, then every proposed topic.

    Members are concept keys: the consolidator reads the whole report to find
    oversized or near-empty topics, misfiled concepts and duplicates that fell
    into different chunks, and names them in its operations by key.
    """
    lines = [f"{len(doc['topics'])} topics (size = concepts + examples + debate sides):"]
    for t in doc["topics"]:
        n = len(_members(t))
        flag = "  <- oversized" if n > OVERSIZED else ("  <- empty or single" if n < 2 else "")
        broader = f", under {t['broader']}" if t.get("broader") else ""
        lines.append(f"\n{t['key']} ({t['name']}; {t.get('kind', 'subject')}{broader}): {n}{flag}")
        if t.get("concepts"):
            lines.append(f"  concepts: {', '.join(t['concepts'])}")
        if t.get("examples"):
            lines.append(f"  examples: {', '.join(t['examples'])}")
        for p in t.get("positions", []):
            lines.append(f"  side '{p['label']}': {', '.join(p.get('concepts', []))}")
    proposals = doc.get("proposed_topics", [])
    lines.append(f"\n{len(proposals)} proposed topics:")
    for p in proposals:
        lines.append(f"\n{p['key']} ({p.get('name', '')}) from chunks {p.get('from_chunks')}: {p.get('why', '')}")
        lines.append(f"  members: {', '.join(_members(p))}")
    return "\n".join(lines)


def apply(doc: dict, ops: dict) -> dict:
    """Carry out consolidation operations, in this order: accept, redirect, split, move, unplace, drop, edit, flag.

    - ``accept``: [{"key": proposed key, plus any fields to change}] promotes a proposal.
    - ``redirect``: {"from key": "to key"} moves every member of a topic or proposal
      into another topic and removes the source.
    - ``split``: {"key": [{"key", "name", "synonyms", "boundary", "scope_note",
      "concepts", "examples"}]} makes narrower topics under an oversized one; the
      members named move out of the parent, which becomes their broader topic.
    - ``move``: [{"concept", "from", "to"}] refiles one concept: out of topic
      ``from`` (its concepts, examples or a debate side) and into topic ``to``,
      as a concept or as an example, whichever it was. An empty ``from`` adds a
      placement (and takes the concept out of ``unplaced``); an empty ``to``
      removes one.
    - ``unplace``: [{"concept", "reason": "noise"}] removes a concept from every
      topic and records it as noise, so the chunks' noise calls can be evened out.
    - ``drop``: [keys] removes topics without moving their members, for a
      debate that fails the debate test (its concepts already sit under
      subject topics); the checker reports any concept this leaves unplaced.
      Topics under a dropped one move up to its broader topic.
    - ``edit``: {"key": {fields}} changes a topic's name, synonyms, boundary,
      scope_note or broader link.
    - ``merge_candidates``: [{"concepts", "note"}] adds duplicate flags.

    A redirect target is a topic already in the file or a proposal accepted in
    the same operations.
    """
    doc = copy.deepcopy(doc)
    topics = {t["key"]: t for t in doc["topics"]}
    proposals = {p["key"]: p for p in doc.get("proposed_topics", [])}
    problems: list[str] = []

    for acc in ops.get("accept", []):
        p = proposals.pop(acc["key"], None)
        if p is None:
            problems.append(f"accept: no proposal '{acc['key']}'")
            continue
        p.pop("from_chunks", None)
        p.pop("why", None)
        p.update({k: v for k, v in acc.items() if k != "key"})
        p.setdefault("kind", "subject")
        topics[p["key"]] = p

    for source, target in ops.get("redirect", {}).items():
        src = proposals.pop(source, None) or topics.pop(source, None)
        dst = topics.get(target)
        if src is None or dst is None:
            problems.append(f"redirect: '{source}' -> '{target}' names a missing topic")
            if src is not None:
                proposals[source] = src
            continue
        dst["concepts"] = _dedupe(dst.get("concepts", []) + src.get("concepts", [])
                                  + [c for p in src.get("positions", []) for c in p.get("concepts", [])])
        dst["examples"] = _dedupe(dst.get("examples", []) + src.get("examples", []))
        for t in topics.values():
            if t.get("broader") == source:
                t["broader"] = target

    for parent_key, children in ops.get("split", {}).items():
        parent = topics.get(parent_key)
        if parent is None:
            problems.append(f"split: no topic '{parent_key}'")
            continue
        moved: set[str] = set()
        for child in children:
            if child["key"] in topics:
                problems.append(f"split: '{child['key']}' already exists")
                continue
            new = {"kind": "subject", "synonyms": [], "boundary": "", "scope_note": "", **child,
                   "broader": parent_key}
            new["concepts"], new["examples"] = _dedupe(new.get("concepts", [])), _dedupe(new.get("examples", []))
            moved.update(new["concepts"] + new["examples"])
            topics[new["key"]] = new
        parent["concepts"] = [c for c in parent.get("concepts", []) if c not in moved]
        parent["examples"] = [c for c in parent.get("examples", []) if c not in moved]

    for mv in ops.get("move", []):
        concept, source, target = mv.get("concept"), mv.get("from", ""), mv.get("to", "")
        if (source and source not in topics) or (target and target not in topics) or not (source or target):
            problems.append(f"move: {concept} from '{source}' to '{target}' names a missing topic")
            continue
        field = "concepts"
        if source:
            src = topics[source]
            held = [c for p in src.get("positions", []) for c in p.get("concepts", [])]
            if concept not in src.get("concepts", []) + src.get("examples", []) + held:
                problems.append(f"move: {concept} is not in '{source}'")
                continue
            if concept in src.get("examples", []):
                field = "examples"
            src["concepts"] = [c for c in src.get("concepts", []) if c != concept]
            src["examples"] = [c for c in src.get("examples", []) if c != concept]
            for p in src.get("positions", []):
                p["concepts"] = [c for c in p.get("concepts", []) if c != concept]
        if target:
            topics[target][field] = _dedupe(topics[target].get(field, []) + [concept])
            doc["unplaced"] = [u for u in doc.get("unplaced", []) if u.get("concept") != concept]

    for entry in ops.get("unplace", []):
        concept = entry.get("concept")
        for t in topics.values():
            t["concepts"] = [c for c in t.get("concepts", []) if c != concept]
            t["examples"] = [c for c in t.get("examples", []) if c != concept]
            for p in t.get("positions", []):
                p["concepts"] = [c for c in p.get("concepts", []) if c != concept]
        if all(u.get("concept") != concept for u in doc.get("unplaced", [])):
            doc.setdefault("unplaced", []).append({"concept": concept, "reason": entry.get("reason", "noise")})

    for key in ops.get("drop", []):
        dropped = topics.pop(key, None)
        if dropped is None:
            problems.append(f"drop: no topic '{key}'")
            continue
        for t in topics.values():
            if t.get("broader") == key:
                t["broader"] = dropped.get("broader", "")

    for key, fields in ops.get("edit", {}).items():
        target = topics.get(key)
        if target is None:
            problems.append(f"edit: no topic '{key}'")
            continue
        target.update({k: v for k, v in fields.items() if k in
                       ("name", "synonyms", "boundary", "scope_note", "broader")})

    doc.setdefault("merge_candidates", []).extend(ops.get("merge_candidates", []))

    if problems:
        raise SystemExit("consolidation ops don't fit topics.json:\n" + "".join(f"  {p}\n" for p in problems))
    doc["topics"] = list(topics.values())
    doc["proposed_topics"] = list(proposals.values())
    if not doc["proposed_topics"]:
        del doc["proposed_topics"]
    return doc


def _write(path: Path, doc: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["merge", "report", "apply"])
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--folder", help="staging folder (default _planning/staging/{corpus}/concepts)")
    parser.add_argument("--force", action="store_true", help="merge over an existing topics.json")
    args = parser.parse_args(argv)
    folder = Path(args.folder) if args.folder else staging_dir(args.corpus, "concepts")
    topics_path = folder / "topics.json"

    if args.command == "merge":
        if topics_path.exists() and not args.force:
            raise SystemExit(f"{topics_path} exists; back it up and pass --force to merge over it")
        skeleton = json.load(open(folder / "topics.skeleton.json", encoding="utf-8"))
        chunk_paths = sorted(folder.glob("topics.chunk-*.json"))
        payload_chunks = sorted(folder.glob("topic-payload.chunk-*.jsonl"))
        if len(chunk_paths) != len(payload_chunks):
            raise SystemExit(f"{len(payload_chunks)} payload chunks but {len(chunk_paths)} filed chunks")
        doc = merge(skeleton, [json.load(open(p, encoding="utf-8")) for p in chunk_paths])
        _write(topics_path, doc)
        print(f"wrote {topics_path}: {len(doc['topics'])} topics from the skeleton, "
              f"{len(doc['proposed_topics'])} proposed, from {len(chunk_paths)} chunks")
    elif args.command == "report":
        print(report(json.load(open(topics_path, encoding="utf-8"))))
    else:
        doc = json.load(open(topics_path, encoding="utf-8"))
        ops = json.load(open(folder / "topics.consolidation.json", encoding="utf-8"))
        applied = apply(doc, ops)
        _write(folder / "topics.before-apply.json", doc)
        _write(topics_path, applied)
        print(f"applied {folder / 'topics.consolidation.json'} to {topics_path} (previous state in "
              f"topics.before-apply.json); {len(applied.get('proposed_topics', []))} proposals left")
    return 0


if __name__ == "__main__":
    sys.exit(main())
