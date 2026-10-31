#!/usr/bin/env python3
"""Find where a piece of text sits in the demo corpus's converted sources.

Used for both arms: a Gemini citation's highlighted passage (its opening words,
as captured), and every quotation in either arm's answer. Text and sources are
normalised the same way (lowercase; line-break hyphens joined; curly quotes,
dashes and ellipses folded; everything but letters and digits treated as a
space), then searched as a plain substring.

    python3 locate.py "text to find"                 # every source
    python3 locate.py --slug caib-report-vol1 "..."  # one source
    python3 locate.py --json FILE                    # FILE: [{"id":..., "text":..., "slug": optional}]

Prints slug:line for each hit (line = 1-based line of the match's first
character, as grep -n counts), or MISSING.
"""
import argparse, bisect, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONVERTED = HERE.parents[3] / "corpus.commons/demo/sources/converted"


def norm_with_map(raw):
    """Return the normalised text and, per normalised char, its 1-based source line."""
    out, lines = [], []
    line = 1
    i, n = 0, len(raw)
    prev_space = True
    while i < n:
        c = raw[i]
        if c == "-" and re.match(r"-[ \t]*\n[ \t]*", raw[i:i + 8]):  # hyphen at a line break: join
            m = re.match(r"-[ \t]*\n[ \t]*", raw[i:])
            line += 1
            i += m.end()
            continue
        if c == "\n":
            line += 1
        ch = c.lower()
        if ch.isalnum():
            out.append(ch)
            lines.append(line)
            prev_space = False
        elif not prev_space:
            out.append(" ")
            lines.append(line)
            prev_space = True
        i += 1
    return "".join(out), lines


def norm(text):
    return norm_with_map(text)[0].strip()


_CACHE = {}


def source(slug):
    if slug not in _CACHE:
        _CACHE[slug] = norm_with_map((CONVERTED / f"{slug}.md").read_text())
    return _CACHE[slug]


def slugs():
    return sorted(p.stem for p in CONVERTED.glob("*.md") if p.name != "IMAGES-README.md")


def find(text, slug=None):
    q = norm(text)
    if not q:
        return []
    hits = []
    for s in [slug] if slug else slugs():
        body, lines = source(s)
        start = 0
        while True:
            k = body.find(q, start)
            if k < 0:
                break
            hits.append((s, lines[k]))
            start = k + 1
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text", nargs="?")
    ap.add_argument("--slug")
    ap.add_argument("--json")
    a = ap.parse_args()
    items = json.loads(Path(a.json).read_text()) if a.json else [{"id": "-", "text": a.text, "slug": a.slug}]
    for it in items:
        hits = find(it["text"], it.get("slug") or a.slug)
        where = ", ".join(f"{s}:{l}" for s, l in hits[:5]) + (f" (+{len(hits) - 5})" if len(hits) > 5 else "")
        print(f"{it['id']}\t{where or 'MISSING'}")


if __name__ == "__main__":
    main()
