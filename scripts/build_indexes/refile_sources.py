"""Re-file sources from their deep references: carry out the re-filing agent's changes on decisions.json and topics.json.

The cross-link pass credits a source on the rows its extracted candidates
matched, and the topic linker files each row under the topics its name
suggests. A source that treats an idea in one section, in its own words, ends
up credited only on rows about something else, so a question about that idea
never reaches it. The `ingest-refiler` agent reads a batch of sources' deep
references against the assembled index and writes `refile/refile-{batch}.json`
in the staging folder:

    {"batch": "b01", "sources": [{"slug": "", "id": "",
      "credits":  [{"row": "<display name>", "context": "", "evidence": ""}],
      "removals": [{"row": "<display name>", "evidence": ""}],
      "filings":  [{"row": "<display name>", "add_topics": ["t044", "t236.1"],
                    "remove_topics": [], "evidence": ""}],
      "new_rows": [{"name": "", "kind": "concept", "synonyms": [], "topics": ["t044"],
                    "context": "", "evidence": ""}],
      "duplicates": [{"rows": ["<display name>", "<display name>"], "note": ""}],
      "notes": ""}]}

Rows are named by display name, which is unique in decisions.json. A topic is
named by its ID; ``t236.1`` is the first side of debate t236. ``context`` is
optional: a few words on how this source treats the idea, shown beside its ID
in the row.

This script makes the changes, so no agent edits either large file:

- removal: the source leaves the row; a row left with no source goes from
  both files.
- filing: the row leaves each ``remove_topics`` topic, then joins each
  ``add_topics`` topic, keeping at most three subject topics (debate sides
  don't count). An addition past three is skipped and logged. ``replace`` (an
  older field) names one topic to drop only when the row is full.
- credit: the source joins an existing row, with its context.
- duplicates: rows the agent saw naming one idea twice join the merge
  candidates, for the concept linker's merge review to decide.
- new row: a new concept credited to the source and filed under its topics,
  examples under a topic's examples. New rows from different files with the
  same name, ignoring case, punctuation and parentheticals, become one row.

Changes apply file by file and, within a source, in that order. A change that
no longer fits when its turn comes (a credit already present, a removal
already made, a full row) is skipped and logged, not an error. ``check``
reports what can't apply at all (a row or topic that doesn't exist, a source
the slug table doesn't know) and ``apply`` refuses until it's clean.

    python3 -m scripts.build_indexes.refile_sources batches --corpus aarbuddy [--texts map.json]
    python3 -m scripts.build_indexes.refile_sources check --corpus aarbuddy [--files a.json b.json]
    python3 -m scripts.build_indexes.refile_sources apply --corpus aarbuddy --label w1

``batches`` writes ``refile/refile-batches.json``: every source with a deep
reference, grouped so each batch's deep references come to about
``--per-batch-kb`` kilobytes, with each source's converted text path
(``sources/converted/{slug}.md``, else the ``--texts`` map of slug to path
from the corpus root, else null). ``apply`` keeps the previous states as
``decisions.before-{label}.json`` and ``topics.before-{label}.json`` and logs
every change's outcome to ``refile/applied-{label}.json``. Then run
``--assemble``, ``--emit-topic-payload`` and ``check_topics``.
"""

from __future__ import annotations

import argparse
import copy
import glob
import json
import re
import sys
from pathlib import Path

from .common import corpus_root, deep_ref_path, load_slug_table, slug_to_id, staging_dir

MAX_SUBJECT_TOPICS = 3
MAX_CONTEXT = 200


def _norm_name(name: str) -> str:
    name = re.sub(r"\([^)]*\)", " ", name).casefold()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", name).split())


def _slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.casefold()).strip("-") or "concept"


def _parse_topic(ref: str) -> tuple[str, int | None]:
    base, _, side = ref.partition(".")
    return base, (int(side) if side.isdigit() else None) if side else None


class Filing:
    """topics.json placements, looked up by concept and changed in place."""

    def __init__(self, topics: dict):
        self.doc = topics
        self.by_id = {t["id"]: t for t in topics["topics"]}

    def subject_topics(self, key: str) -> list[str]:
        return [t["id"] for t in self.doc["topics"]
                if key in t.get("concepts", []) or key in t.get("examples", [])]

    def is_example(self, key: str) -> bool:
        in_examples = any(key in t.get("examples", []) for t in self.doc["topics"])
        elsewhere = any(key in t.get("concepts", []) or any(key in p.get("concepts", []) for p in t.get("positions", []))
                        for t in self.doc["topics"])
        return in_examples and not elsewhere

    def has(self, key: str, ref: str) -> bool:
        base, side = _parse_topic(ref)
        t = self.by_id[base]
        if side is None:
            return key in t.get("concepts", []) or key in t.get("examples", [])
        return key in t["positions"][side - 1].get("concepts", [])

    def add(self, key: str, ref: str, example: bool) -> None:
        base, side = _parse_topic(ref)
        t = self.by_id[base]
        if side is None:
            t.setdefault("examples" if example else "concepts", []).append(key)
        else:
            t["positions"][side - 1].setdefault("concepts", []).append(key)
        self.doc["unplaced"] = [u for u in self.doc.get("unplaced", []) if u["concept"] != key]

    def remove(self, key: str, ref: str) -> bool:
        base, side = _parse_topic(ref)
        t = self.by_id[base]
        lists = [t.setdefault("concepts", []), t.setdefault("examples", [])] if side is None \
            else [t["positions"][side - 1].setdefault("concepts", [])]
        hit = False
        for lst in lists:
            while key in lst:
                lst.remove(key)
                hit = True
        return hit

    def drop_concept(self, key: str) -> None:
        for t in self.doc["topics"]:
            for field in ("concepts", "examples"):
                if key in t.get(field, []):
                    t[field] = [k for k in t[field] if k != key]
            for p in t.get("positions", []):
                if key in p.get("concepts", []):
                    p["concepts"] = [k for k in p["concepts"] if k != key]
        self.doc["unplaced"] = [u for u in self.doc.get("unplaced", []) if u["concept"] != key]
        self.doc.get("synonyms", {}).pop(key, None)
        groups = []
        for g in self.doc.get("merge_candidates", []):
            members = [k for k in g.get("concepts", []) if k != key]
            if len(members) >= 2:
                groups.append({**g, "concepts": members})
        self.doc["merge_candidates"] = groups


def _topic_problems(refs: list, by_id: dict, where: str) -> list[str]:
    problems = []
    for ref in refs:
        base, side = _parse_topic(str(ref))
        t = by_id.get(base)
        if t is None:
            problems.append(f"{where}: no topic {ref}")
        elif side is not None and not (t.get("kind") == "debate" and 1 <= side <= len(t.get("positions", []))):
            problems.append(f"{where}: {ref} is not a side of a debate topic")
    return problems


def validate(decisions: dict, topics: dict, proposals: list[dict], slug_ids: dict[str, str]) -> list[str]:
    """Every change that can't apply at all. Empty means the files apply."""
    names = {}
    problems: list[str] = []
    for d in decisions["decisions"]:
        if d["name"] in names:
            problems.append(f"decisions.json: display name '{d['name']}' is not unique")
        names[d["name"]] = d["canonical"]
    by_id = {t["id"]: t for t in topics["topics"]}
    for doc in proposals:
        label = doc.get("batch", "?")
        for s in doc.get("sources", []):
            slug, sid = s.get("slug", ""), s.get("id", "")
            where = f"{label}/{slug}"
            if slug_ids.get(slug) != sid:
                problems.append(f"{where}: slug and id '{sid}' don't match the slug table")
            for c in s.get("credits", []) + s.get("removals", []):
                if c.get("row") not in names:
                    problems.append(f"{where}: no row '{c.get('row')}'")
                if len(c.get("context", "")) > MAX_CONTEXT:
                    problems.append(f"{where}: context on '{c.get('row')}' is over {MAX_CONTEXT} characters")
            for f in s.get("filings", []):
                if f.get("row") not in names:
                    problems.append(f"{where}: no row '{f.get('row')}' to file")
                problems += _topic_problems(f.get("add_topics", []) + f.get("remove_topics", [])
                                            + ([f["replace"]] if f.get("replace") else []),
                                            by_id, f"{where} filing '{f.get('row')}'")
            for g in s.get("duplicates", []):
                rows = g.get("rows", [])
                if len(set(rows)) < 2:
                    problems.append(f"{where}: a duplicates group needs two rows: {rows}")
                for row in rows:
                    if row not in names:
                        problems.append(f"{where}: duplicates names no row '{row}'")
            for n in s.get("new_rows", []):
                nm = n.get("name", "").strip()
                if not nm:
                    problems.append(f"{where}: new row with no name")
                    continue
                if n.get("kind", "concept") not in ("concept", "example"):
                    problems.append(f"{where}: new row '{nm}' has kind '{n.get('kind')}'")
                if not n.get("topics"):
                    problems.append(f"{where}: new row '{nm}' has no topics")
                if len([t for t in n.get("topics", []) if "." not in str(t)]) > MAX_SUBJECT_TOPICS:
                    problems.append(f"{where}: new row '{nm}' has more than {MAX_SUBJECT_TOPICS} subject topics")
                if len(n.get("context", "")) > MAX_CONTEXT:
                    problems.append(f"{where}: context on new row '{nm}' is over {MAX_CONTEXT} characters")
                problems += _topic_problems(n.get("topics", []), by_id, f"{where} new row '{nm}'")
    return problems


def apply(decisions: dict, topics: dict, proposals: list[dict]) -> tuple[dict, dict, list[dict]]:
    decisions, topics = copy.deepcopy(decisions), copy.deepcopy(topics)
    records = {d["canonical"]: d for d in decisions["decisions"]}
    by_name = {d["name"]: d["canonical"] for d in decisions["decisions"]}
    by_norm = {_norm_name(d["name"]): d["canonical"] for d in decisions["decisions"]}
    filing = Filing(topics)
    log: list[dict] = []
    created: list[str] = []

    def note(src: dict, change: str, row: str, outcome: str) -> None:
        log.append({"slug": src["slug"], "change": change, "row": row, "outcome": outcome})

    def credit(key: str, src: dict, context: str) -> bool:
        rec = records[key]
        if any(x["id"] == src["id"] for x in rec["sources"]):
            return False
        entry = {"slug": src["slug"], "id": src["id"]}
        if context:
            entry["context"] = context
        rec["sources"].append(entry)
        return True

    def file_under(key: str, refs: list, src: dict, row: str, replace: str = "") -> None:
        example = filing.is_example(key)
        for ref in refs:
            if filing.has(key, ref):
                note(src, "filing", row, f"already under {ref}")
                continue
            if "." not in ref and len(filing.subject_topics(key)) >= MAX_SUBJECT_TOPICS:
                if replace and filing.remove(key, replace):
                    note(src, "filing", row, f"replaced {replace}")
                    replace = ""
                else:
                    note(src, "filing", row, f"skipped {ref}: already under {MAX_SUBJECT_TOPICS} subject topics")
                    continue
            filing.add(key, ref, example)
            note(src, "filing", row, f"added {ref}")

    for doc in proposals:
        for s in doc.get("sources", []):
            src = {"slug": s["slug"], "id": s["id"]}
            for r in s.get("removals", []):
                key = by_name.get(r["row"])
                rec = records.get(key) if key else None
                if rec is None or not any(x["id"] == src["id"] for x in rec["sources"]):
                    note(src, "removal", r["row"], "skipped: not credited")
                    continue
                rec["sources"] = [x for x in rec["sources"] if x["id"] != src["id"]]
                if rec["sources"]:
                    note(src, "removal", r["row"], "removed")
                else:
                    filing.drop_concept(key)
                    del records[key]
                    by_name.pop(rec["name"], None)
                    by_norm.pop(_norm_name(rec["name"]), None)
                    note(src, "removal", r["row"], "removed; row had no other source and is gone")
            for f in s.get("filings", []):
                key = by_name.get(f["row"])
                if key is None:
                    note(src, "filing", f["row"], "skipped: row is gone")
                    continue
                for ref in f.get("remove_topics", []):
                    note(src, "filing", f["row"], f"removed {ref}" if filing.remove(key, ref) else f"not under {ref}")
                file_under(key, f.get("add_topics", []), src, f["row"], f.get("replace", ""))
            for c in s.get("credits", []):
                key = by_name.get(c["row"])
                if key is None:
                    note(src, "credit", c["row"], "skipped: row is gone")
                    continue
                note(src, "credit", c["row"], "added" if credit(key, src, c.get("context", "")) else "skipped: already credited")
            for n in s.get("new_rows", []):
                name = n["name"].strip()
                key = by_name.get(name) or by_norm.get(_norm_name(name))
                if key:
                    added = credit(key, src, n.get("context", ""))
                    note(src, "new row", name, f"merged into '{records[key]['name']}'" + ("" if added else " (already credited)"))
                    file_under(key, n.get("topics", []), src, records[key]["name"])
                    continue
                key, k = _slugify(name), 2
                while key in records:
                    key, k = f"{_slugify(name)}-{k}", k + 1
                synonyms = [x for x in dict.fromkeys(n.get("synonyms", [])) if x and x != name]
                entry = {"slug": src["slug"], "id": src["id"]}
                if n.get("context"):
                    entry["context"] = n["context"]
                records[key] = {"canonical": key, "name": name, "aliases": synonyms, "sources": [entry]}
                by_name[name], by_norm[_norm_name(name)] = key, key
                topics.setdefault("synonyms", {})[key] = synonyms
                example = n.get("kind") == "example"
                for ref in n.get("topics", []):
                    filing.add(key, ref, example and "." not in ref)
                note(src, "new row", name, f"created as {key}")
                created.append(key)
            for g in s.get("duplicates", []):
                keys = list(dict.fromkeys(by_name[r] for r in g.get("rows", []) if r in by_name))
                if len(keys) < 2:
                    note(src, "duplicates", " | ".join(g.get("rows", [])), "skipped: a row is gone")
                    continue
                groups = topics.setdefault("merge_candidates", [])
                if any(set(keys) <= set(x.get("concepts", [])) for x in groups):
                    note(src, "duplicates", " | ".join(g["rows"]), "already flagged")
                    continue
                groups.append({"concepts": keys, "note": g.get("note") or "flagged by the re-filing pass"})
                note(src, "duplicates", " | ".join(g["rows"]), "flagged")
    _flag_overlaps(created, records, topics)
    decisions["decisions"] = sorted(records.values(), key=lambda d: d["canonical"])
    return decisions, topics, log


def _flag_overlaps(created: list[str], records: dict, topics: dict) -> None:
    """Flag new rows whose names contain one another for the merge review.

    Batches run in parallel, so two agents can name one idea differently
    ("Flynn Effect", "IQ Malleability (Flynn Effect)"). The flag only queues
    the pair for the concept linker's merge review, which decides.
    """
    full = {k: _norm_name(records[k]["name"].replace("(", " ").replace(")", " ")) for k in created if k in records}
    base = {k: _norm_name(records[k]["name"]) for k in full}
    groups = topics.setdefault("merge_candidates", [])
    seen = {frozenset(g.get("concepts", [])) for g in groups}
    keys = sorted(full)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if not base[a] or not base[b]:
                continue
            if f" {base[a]} " in f" {full[b]} " or f" {base[b]} " in f" {full[a]} ":
                pair = frozenset((a, b))
                if pair not in seen:
                    seen.add(pair)
                    groups.append({"concepts": [a, b], "note": "new rows from the re-filing pass with overlapping names"})


def make_batches(corpus: str, per_batch_kb: int, texts: dict, only: set[str] | None) -> dict:
    slug_ids = slug_to_id(load_slug_table(corpus))
    root = corpus_root(corpus)
    items = []
    for slug, sid in sorted(slug_ids.items()):
        if only is not None and slug not in only:
            continue
        deep = deep_ref_path(corpus, slug)
        if not deep.is_file():
            continue
        conv = root / "sources" / "converted" / f"{slug}.md"
        text = f"sources/converted/{slug}.md" if conv.is_file() else texts.get(slug)
        if text and not (root / text).is_file():
            text = None
        items.append({"slug": slug, "id": sid, "deep_kb": round(deep.stat().st_size / 1024), "text": text})
    total = sum(i["deep_kb"] for i in items)
    n = max(1, -(-total // per_batch_kb))
    bins = [[0, []] for _ in range(n)]
    for item in sorted(items, key=lambda i: -i["deep_kb"]):
        b = min(bins, key=lambda x: x[0])
        b[0] += item["deep_kb"]
        b[1].append(item)
    width = len(str(n))
    return {"corpus": corpus, "per_batch_kb": per_batch_kb,
            "batches": {f"b{i + 1:0{width}d}": sorted(b[1], key=lambda x: x["slug"]) for i, b in enumerate(bins)}}


def _write(path: Path, doc: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["batches", "check", "apply"])
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--folder", type=Path, help="staging folder (default _planning/staging/{corpus}/concepts)")
    parser.add_argument("--files", nargs="*", help="proposal files (default refile/refile-b*.json in the folder)")
    parser.add_argument("--label", default="refile", help="names the backups and the log")
    parser.add_argument("--per-batch-kb", type=int, default=340)
    parser.add_argument("--texts", type=Path, help="JSON map of slug to converted-text path from the corpus root")
    parser.add_argument("--sources", help="comma-separated slugs to batch (default: every source with a deep ref)")
    args = parser.parse_args(argv)
    folder = args.folder or staging_dir(args.corpus, "concepts")
    refile = folder / "refile"

    if args.command == "batches":
        texts = json.load(open(args.texts, encoding="utf-8")) if args.texts else {}
        only = set(args.sources.split(",")) if args.sources else None
        doc = make_batches(args.corpus, args.per_batch_kb, texts, only)
        refile.mkdir(parents=True, exist_ok=True)
        _write(refile / "refile-batches.json", doc)
        sizes = [sum(i["deep_kb"] for i in b) for b in doc["batches"].values()]
        print(f"{sum(len(b) for b in doc['batches'].values())} sources in {len(sizes)} batches "
              f"({min(sizes)}-{max(sizes)} KB of deep refs each) -> {refile / 'refile-batches.json'}")
        return 0

    paths = {name: folder / name for name in ("decisions.json", "topics.json")}
    for path in paths.values():
        if not path.is_file():
            print(f"missing {path}")
            return 1
    files = [Path(f) for f in args.files] if args.files else sorted(Path(p) for p in glob.glob(str(refile / "refile-b*.json")))
    if not files:
        print(f"no proposal files in {refile}")
        return 1
    decisions, topics = (json.load(open(p, encoding="utf-8")) for p in paths.values())
    proposals = [json.load(open(f, encoding="utf-8")) for f in files]
    slug_ids = slug_to_id(load_slug_table(args.corpus))
    counts = {k: sum(len(s.get(k, [])) for d in proposals for s in d.get("sources", []))
              for k in ("credits", "removals", "filings", "new_rows", "duplicates")}
    summary = (f"{len(files)} files, {sum(len(d.get('sources', [])) for d in proposals)} sources: "
               + ", ".join(f"{v} {k.replace('_', ' ')}" for k, v in counts.items()))
    problems = validate(decisions, topics, proposals, slug_ids)
    if problems:
        print(f"{summary}\nFAIL: {len(problems)} problems")
        for p in problems[:40]:
            print(f"  {p}")
        return 1
    if args.command == "check":
        print(f"{summary}\nPASS")
        return 0

    new_decisions, new_topics, log = apply(decisions, topics, proposals)
    _write(folder / f"decisions.before-{args.label}.json", decisions)
    _write(folder / f"topics.before-{args.label}.json", topics)
    _write(paths["decisions.json"], new_decisions)
    _write(paths["topics.json"], new_topics)
    refile.mkdir(parents=True, exist_ok=True)
    _write(refile / f"applied-{args.label}.json", {"files": [str(f) for f in files], "changes": log})
    outcomes: dict[str, int] = {}
    for entry in log:
        k = f"{entry['change']}: {entry['outcome'].split(':')[0].split(' ')[0]}"
        outcomes[k] = outcomes.get(k, 0) + 1
    print(f"{summary}\napplied: {len(decisions['decisions'])} -> {len(new_decisions['decisions'])} concepts; "
          + ", ".join(f"{k} {v}" for k, v in sorted(outcomes.items()))
          + ". Now --assemble, --emit-topic-payload and check_topics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
