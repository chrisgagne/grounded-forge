#!/usr/bin/env python3
"""Summarise how each grounded-forge run reached (or missed) its target.

    python3 gf_route.py RUNS_DIR

Reads RUNS_DIR/{qid}-{run}.out/tools.json and reports per run: the topic IDs it
fetched rows for from concept-index.json, whether any of them is one the target
concept is filed under, whether it read the target's light or deep reference,
and whether it searched the converted sources or the references by text before
its first read of the target's reference (a word-search route, not the index),
and the patterns of any concept-index lookups by name rather than topic ID: the
words the run itself chose to look the concept up by.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def topic_ids(pat):
    """Topic IDs a grep pattern fetches, expanding character classes ("t00[789]" -> t007, t008, t009)."""
    ids = set(re.findall(r"t\d{3}(?![\d\[])", pat))
    for head, cls in re.findall(r"(t\d\d)\[(\d+)\]", pat):
        ids |= {head + c for c in cls}
    return ids


def main():
    runs = Path(sys.argv[1])
    targets = {t["id"]: t for t in json.loads((HERE / "targets.json").read_text())}
    print("run\ttopics fetched\ttarget topic hit\ttarget ref read\ttext search before target ref\ttool calls\tindex lookups by name")
    for d in sorted(runs.glob("K*.out")):
        qid = d.name.split("-")[0]
        t = targets[qid[:3]]
        want = {x.split()[0] for x in t["topics"]}
        tools = json.loads((d / "tools.json").read_text())
        topics, ref_at, search_before, lookups = set(), None, False, []
        for i, c in enumerate(tools):
            inp = c.get("input") or {}
            path = str(inp.get("path") or inp.get("file_path") or "")
            pat = str(inp.get("pattern") or "")
            if c["tool"] == "Grep" and path.endswith("concept-index.json"):
                topics |= topic_ids(pat)
                if not re.fullmatch(r"[\\\"|t\d.\[\]]+", pat) and "schema_version" not in pat:
                    lookups.append(pat)
            if c["tool"] == "Read" and f"references/{t['slug']}" in path and ref_at is None:
                ref_at = i
            if ref_at is None and c["tool"] == "Grep" and not path.endswith(".json") and \
                    ("sources/converted" in path or path.endswith("references") or path.endswith("/references/") or path == ""):
                search_before = True
        hit = bool(topics & want)
        print(f"{d.name[:-4]}\t{','.join(sorted(topics)) or '-'}\t{'yes' if hit else 'no'}\t"
              f"{'yes' if ref_at is not None else 'no'}\t{'yes' if search_before else 'no'}\t{len(tools)}\t{' / '.join(lookups) or '-'}")


if __name__ == "__main__":
    main()
