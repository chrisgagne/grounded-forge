#!/usr/bin/env python3
"""Locate every Gemini citation chunk in the converted sources and mark it against the target section.

    python3 locate_citations.py CAPTURE.json [CAPTURE.json ...]

A capture is one Gemini answer as saved from the notebook page: the answer text
with [n] markers, and per marker the source file name and the full text of the
chunk its citation panel shows. Each chunk is located in the converted text of
the source it names (the notebook holds the original PDFs; the converted
Markdown is the same text, deterministically extracted): word windows from the
chunk's start, then from anywhere in it, are searched with locate.py until one is
found, from both ends of the chunk, since a chunk can run across a section
boundary. The chunk is IN when its span overlaps the target section, else OUT
(target source, other section), ALT (an alt source for the concept), OTHER
(another source), UNLOCATED, or EMPTY (the panel showed nothing when captured).

Writes CAPTURE.located.json beside each capture and prints a summary line per
answer: the answer with each [n] replaced by [n:VERDICT] goes to CAPTURE.annotated.md.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from locate import find, norm  # noqa: E402

# notebook file name -> converted slug, where they differ
SLUG = {
    "ssdl-accumulations": "ssdl-systems-thinking-foundations",
    "ssdl-characteristics-of-complex-problems": "ssdl-systems-thinking-foundations",
    "ssdl-mental-models": "ssdl-systems-thinking-foundations",
    "ssdl-system-archetypes": "ssdl-systems-thinking-foundations",
    "ssdl-understanding-systems-from-a-feedback-perspective": "ssdl-systems-thinking-foundations",
}


def slug_of(source):
    stem = re.sub(r"\.(pdf|md|epub)$", "", source.strip())
    return SLUG.get(stem, stem)


def _windows(words, size, from_end=False):
    starts = list(range(0, max(1, len(words) - size + 1), max(1, size // 2)))
    return reversed(starts[-40:]) if from_end else iter(starts[:40])


def locate_chunk(chunk, slug):
    """Return (first line, last line) of the chunk in the converted source, or (None, None).

    A chunk can run across a section boundary, so both ends are located: word
    windows from its start give the first line, windows from its end the last."""
    words = norm(chunk).split()
    ends = []
    for from_end in (False, True):
        found = None
        for size in (12, 8):
            for s in _windows(words, size, from_end):
                hits = find(" ".join(words[s:s + size]), slug)
                if len(hits) == 1 or (hits and size == 8):
                    found = hits[0][1]
                    break
            if found is not None:
                break
        ends.append(found)
    first, last = ends
    if first is None:
        first = last
    if last is None or (first is not None and last < first):
        last = first
    return first, last


def main():
    targets = {t["id"]: t for t in json.loads((HERE / "targets.json").read_text())}
    for f in map(Path, sys.argv[1:]):
        cap = json.loads(f.read_text())
        t = targets[cap["id"][:3]]
        sec = t["section"]
        located = {}
        for n, c in cap["legend"].items():
            slug = slug_of(c["source"])
            first, last = locate_chunk(c["chunk"], slug) if c["chunk"] else (None, None)
            if not c["source"].strip():
                verdict = "EMPTY"  # the citation panel didn't load in time; counted against Gemini
            elif slug == t["slug"]:
                verdict = "UNLOCATED" if first is None else ("IN" if first <= sec["end"] and last >= sec["start"] else "OUT")
            elif slug in t["alt_sources"]:
                verdict = "ALT"
            else:
                verdict = "OTHER"
            located[n] = {"source": slug, "line": first, "last_line": last, "verdict": verdict}
        f.with_suffix(".located.json").write_text(json.dumps(located, indent=1))
        text = re.sub(r"\[(\d+)\]", lambda m: f"[{m.group(1)}:{located.get(m.group(1), {}).get('verdict', '?')}:"
                      f"{located.get(m.group(1), {}).get('source', '?')}]", cap["text"])
        f.with_suffix(".annotated.md").write_text(f"# {cap['id']}\n\n{cap['question']}\n\n{text}\n")
        tally = {}
        for v in located.values():
            tally[v["verdict"]] = tally.get(v["verdict"], 0) + 1
        print(f"{cap['id']}: {len(located)} citations {tally}")


if __name__ == "__main__":
    main()
