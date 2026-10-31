#!/usr/bin/env python3
"""Map each Gemini citation chunk to a corpus slug and a line in the converted text.

    python3 locate_chunks.py demo CAPTURE.json ...
    python3 locate_chunks.py aarbuddy CAPTURE.json ...

demo: the notebook file name less its extension is the slug (SSDL's five briefs
map to one slug). aarbuddy: October's upload manifest maps file names to slugs,
and GF_CONVERTED must point at that corpus's sources/converted.

Writes CAPTURE.located.json ({marker: {source, slug, line, last_line}}) and
CAPTURE.annotated.md (the answer with [n] rewritten as [n:slug]). Prints per
answer: markers, distinct sources, and how many chunks were located.
"""
import csv, json, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KM = HERE.parent / "2026-11-keyword-match"
sys.path.insert(0, str(KM))
from locate_citations import SLUG as SSDL, locate_chunk  # noqa: E402

GF = HERE.parents[3]
MAIN = GF.parents[2] if (GF.parents[2] / "corpus.local/aarbuddy").exists() else GF
MANIFEST = Path(os.environ.get("GF_MANIFEST", MAIN / "corpus.local/aarbuddy/projects/gemini-notebook-arm/upload-manifest.csv"))


def slug_map(corpus):
    if corpus == "demo":
        return lambda name: SSDL.get(re.sub(r"\.(pdf|md|epub)$", "", name.strip()), re.sub(r"\.(pdf|md|epub)$", "", name.strip()))
    rows = {r["upload_name"].strip(): r["slug"].strip() for r in csv.DictReader(MANIFEST.open())}
    return lambda name: rows.get(name.strip(), "?" + name.strip())


def main():
    corpus, files = sys.argv[1], sys.argv[2:]
    to_slug = slug_map(corpus)
    for f in map(Path, files):
        if f.name.endswith((".located.json", ".report.json")):
            continue
        cap = json.loads(f.read_text())
        located, unknown = {}, 0
        for n, c in cap["legend"].items():
            slug = to_slug(c["source"]) if c["source"].strip() else ""
            first = last = None
            if slug and not slug.startswith("?") and c["chunk"]:
                try:
                    first, last = locate_chunk(c["chunk"], slug)
                except FileNotFoundError:
                    unknown += 1
            located[n] = {"source": c["source"], "slug": slug, "line": first, "last_line": last}
        f.with_suffix(".located.json").write_text(json.dumps(located, indent=1))
        text = re.sub(r"\[(\d+)\]", lambda m: f"[{m.group(1)}:{located.get(m.group(1), {}).get('slug', '?')}]", cap["text"])
        f.with_suffix(".annotated.md").write_text(f"# {cap['id']}\n\n{cap['question']}\n\n{text}\n")
        n_loc = sum(v["line"] is not None for v in located.values())
        print(f"{cap['id']}: {len(located)} markers, {len({v['slug'] for v in located.values()})} sources, "
              f"{n_loc} located, {sum(v['slug'].startswith('?') for v in located.values())} unmapped, {unknown} no converted text")


if __name__ == "__main__":
    main()
