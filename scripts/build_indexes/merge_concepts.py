"""Carry out reviewed concept merges on decisions.json and topics.json together.

The topic linker flags concepts that look like one idea under several keys
(``merge_candidates`` in topics.json). The concept linker's merge review
decides each flag and writes ``concept-merges.json`` beside them:

    {
      "merge": [{"keep": "etto-principle", "fold": ["etto", "etto-efficiency-thoroughness-trade-off"],
                 "name": "ETTO Principle", "synonyms": ["ETTO", "efficiency-thoroughness trade-off"]}],
      "keep_apart": [{"concepts": ["kanban", "kanban-method"], "note": "the TPS card, not the method"}],
      "split": [{"concept": "rag", "sources": {"source-a": "retrieval-augmented-generation",
                                               "source-b": "resilience-assessment-grid"}}]
    }

This script makes the changes, so no agent edits either large file by hand:

- merge: the kept concept takes each folded concept's name and aliases as
  aliases, and its sources with their contexts; the folded records go. An
  optional ``name``, one of the merged names, becomes the display name. In
  topics.json every placement of a folded concept becomes the kept one, and
  ``synonyms`` becomes the merged concept's kept synonyms, each one of its
  aliases after the merge, verbatim.
- keep_apart: closes the flag without changing either file's concepts.
- split: a concept that conflates two ideas hands each of its sources (by
  slug) to the concept that source means; its record and placements go.

Every merge-candidate group a decision resolves is dropped. The concept names
of both files must match, so run it before re-assembling:

    python3 -m scripts.build_indexes.merge_concepts check --corpus aarbuddy
    python3 -m scripts.build_indexes.merge_concepts apply --corpus aarbuddy
    python3 -m scripts.build_indexes.build_concept_index --corpus aarbuddy --assemble

``apply`` keeps the previous states as decisions.before-merges.json and
topics.before-merges.json. ``--folder`` points at a staging folder other than
``_planning/staging/{corpus}/concepts/``.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

from .build_concept_index import _clean_aliases
from .common import staging_dir


def _dedupe(items: list) -> list:
    seen, out = set(), []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def validate(decisions: dict, topics: dict, merges: dict) -> list[str]:
    """Every way the merge file doesn't fit the two files. Empty means it applies."""
    records = {d["canonical"]: d for d in decisions["decisions"]}
    problems: list[str] = []
    claimed: dict[str, str] = {}

    def claim(key: str, role: str) -> None:
        if key not in records:
            problems.append(f"{role}: no concept '{key}' in decisions.json")
        elif key in claimed:
            problems.append(f"{role}: '{key}' is already {claimed[key]}")
        else:
            claimed[key] = role

    for m in merges.get("merge", []):
        claim(m.get("keep", ""), f"kept by the merge into '{m.get('keep')}'")
        folds = m.get("fold", [])
        if not folds:
            problems.append(f"merge into '{m.get('keep')}': nothing to fold")
        if "synonyms" not in m:
            problems.append(f"merge into '{m.get('keep')}': no synonyms decision (an empty list is one)")
        for key in folds:
            claim(key, f"folded into '{m.get('keep')}'")
        if m.get("keep") in records and all(k in records for k in folds):
            names = [records[m["keep"]]["name"]] + merged_aliases(records, m["keep"], folds)
            name = m.get("name", records[m["keep"]]["name"])
            if name not in names:
                problems.append(f"merge into '{m['keep']}': name '{name}' is not a name or alias of the merged concepts")
            aliases = set(_assembled_aliases(records, m))
            for s in m.get("synonyms", []):
                if s not in aliases:
                    problems.append(f"merge into '{m['keep']}': synonym '{s}' is not an alias the merged concept "
                                    "keeps after assembly (a name or alias of the merged concepts, not the "
                                    "display name or a case or spacing variant of it)")
    for s in merges.get("split", []):
        key = s.get("concept", "")
        claim(key, "split")
        if key not in records:
            continue
        slugs = {src["slug"] for src in records[key]["sources"]}
        assigned = s.get("sources", {})
        if missing := sorted(slugs - set(assigned)):
            problems.append(f"split '{key}': sources not assigned: {missing}")
        if extra := sorted(set(assigned) - slugs):
            problems.append(f"split '{key}': '{key}' has no source {extra}")
        for target in set(assigned.values()):
            if target not in records:
                problems.append(f"split '{key}': no target concept '{target}'")
            elif target == key or claimed.get(target, "").startswith(("folded", "split")):
                problems.append(f"split '{key}': target '{target}' is itself folded or split")
    for m in merges.get("merge", []):
        for key in m.get("fold", []):
            for s in merges.get("split", []):
                if key in s.get("sources", {}).values():
                    problems.append(f"split '{s['concept']}': target '{key}' is folded into '{m['keep']}'")
    for group in merges.get("keep_apart", []):
        for key in group.get("concepts", []):
            if key not in records:
                problems.append(f"keep_apart: no concept '{key}' in decisions.json")

    topic_keys = set()
    for t in topics.get("topics", []):
        topic_keys.update(t.get("concepts", []), t.get("examples", []))
        for p in t.get("positions", []):
            topic_keys.update(p.get("concepts", []))
    topic_keys.update(u["concept"] for u in topics.get("unplaced", []))
    if stray := sorted(topic_keys - set(records)):
        problems.append(f"topics.json names concepts decisions.json doesn't have (re-sync first): {stray[:10]}")
    return problems


def merged_aliases(records: dict, keep: str, folds: list[str]) -> list[str]:
    kept = records[keep]
    names = list(kept.get("aliases", []))
    for key in folds:
        names += [records[key]["name"]] + list(records[key].get("aliases", []))
    return [n for n in _dedupe(names) if n != kept["name"]]


def _merged_record(records: dict, m: dict) -> tuple[str, list[str]]:
    """The merged concept's display name and aliases, the kept name joining the aliases if renamed."""
    old = records[m["keep"]]["name"]
    name = m.get("name", old)
    aliases = [old] + merged_aliases(records, m["keep"], m["fold"])
    return name, [a for a in _dedupe(aliases) if a != name]


def _assembled_aliases(records: dict, m: dict) -> list[str]:
    name, aliases = _merged_record(records, m)
    return _clean_aliases(name, m["keep"], aliases)


def apply_decisions(decisions: dict, merges: dict) -> dict:
    out = copy.deepcopy(decisions)
    records = {d["canonical"]: d for d in out["decisions"]}
    gone: set[str] = set()
    for m in merges.get("merge", []):
        kept = records[m["keep"]]
        kept["name"], kept["aliases"] = _merged_record(records, m)
        ids = {src["id"] for src in kept["sources"]}
        for key in m["fold"]:
            for src in records[key]["sources"]:
                if src["id"] not in ids:
                    kept["sources"].append(copy.deepcopy(src))
                    ids.add(src["id"])
            gone.add(key)
    for s in merges.get("split", []):
        for src in records[s["concept"]]["sources"]:
            target = records[s["sources"][src["slug"]]]
            if all(t["id"] != src["id"] for t in target["sources"]):
                target["sources"].append(copy.deepcopy(src))
        gone.add(s["concept"])
    out["decisions"] = sorted((d for d in out["decisions"] if d["canonical"] not in gone),
                              key=lambda d: d["canonical"])
    return out


def apply_topics(topics: dict, merges: dict) -> dict:
    out = copy.deepcopy(topics)
    rename = {key: m["keep"] for m in merges.get("merge", []) for key in m["fold"]}
    removed = {s["concept"] for s in merges.get("split", [])}

    def remap(keys: list[str]) -> list[str]:
        return _dedupe([rename.get(k, k) for k in keys if k not in removed])

    placed: set[str] = set()
    for t in out["topics"]:
        t["concepts"] = remap(t.get("concepts", []))
        t["examples"] = [k for k in remap(t.get("examples", [])) if k not in t["concepts"]]
        placed.update(t["concepts"], t["examples"])
        for p in t.get("positions", []):
            p["concepts"] = remap(p.get("concepts", []))
            placed.update(p["concepts"])
    unplaced, seen = [], set()
    for u in out.get("unplaced", []):
        key = rename.get(u["concept"], u["concept"])
        if key in removed or key in placed or key in seen:
            continue
        seen.add(key)
        unplaced.append({**u, "concept": key})
    out["unplaced"] = unplaced

    synonyms = out.setdefault("synonyms", {})
    for m in merges.get("merge", []):
        for key in m["fold"]:
            synonyms.pop(key, None)
        synonyms[m["keep"]] = m["synonyms"]
    for key in removed:
        synonyms.pop(key, None)

    closed = [set(g.get("concepts", [])) for g in merges.get("keep_apart", [])]
    groups = []
    for g in out.get("merge_candidates", []):
        members = set(remap(g.get("concepts", [])))
        if len(members) < 2 or any(set(g.get("concepts", [])) <= c for c in closed):
            continue
        groups.append({**g, "concepts": remap(g.get("concepts", []))})
    out["merge_candidates"] = groups
    return out


def _write(path: Path, doc: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["check", "apply"])
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--folder", type=Path, help="staging folder (default _planning/staging/{corpus}/concepts)")
    parser.add_argument("--file", default="concept-merges.json", help="the merge review's decisions, in the folder")
    args = parser.parse_args(argv)
    folder = args.folder or staging_dir(args.corpus, "concepts")
    paths = {name: folder / name for name in ("decisions.json", "topics.json", args.file)}
    for path in paths.values():
        if not path.is_file():
            print(f"missing {path}")
            return 1
    decisions, topics, merges = (json.load(open(p, encoding="utf-8")) for p in paths.values())

    problems = validate(decisions, topics, merges)
    counts = (f"{len(merges.get('merge', []))} merges folding "
              f"{sum(len(m.get('fold', [])) for m in merges.get('merge', []))} concepts, "
              f"{len(merges.get('keep_apart', []))} kept apart, {len(merges.get('split', []))} splits")
    if problems:
        print(f"{counts}\nFAIL: {len(problems)} problems")
        for p in problems[:40]:
            print(f"  {p}")
        return 1
    if args.command == "check":
        print(f"{counts}\nPASS")
        return 0

    new_decisions, new_topics = apply_decisions(decisions, merges), apply_topics(topics, merges)
    _write(folder / "decisions.before-merges.json", decisions)
    _write(folder / "topics.before-merges.json", topics)
    _write(paths["decisions.json"], new_decisions)
    _write(paths["topics.json"], new_topics)
    print(f"{counts}\napplied: {len(decisions['decisions'])} -> {len(new_decisions['decisions'])} concepts; "
          f"{len(topics.get('merge_candidates', []))} -> {len(new_topics['merge_candidates'])} merge candidates open. "
          "Now --assemble, --emit-topic-payload and check_topics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
