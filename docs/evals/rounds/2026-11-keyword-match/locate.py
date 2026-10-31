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
import os
CONVERTED = Path(os.environ.get("GF_CONVERTED", HERE.parents[3] / "corpus.commons/demo/sources/converted"))  # another corpus: set GF_CONVERTED


def norm_with_map(raw, join=True):
    """Return the normalised text and, per normalised char, its 1-based source line.

    join=True joins a hyphen at a line break ("fric-\\ntion" -> "friction");
    join=False reads it as a space ("paper-\\nbased" -> "paper based"). find() tries both."""
    out, lines = [], []
    line = 1
    i, n = 0, len(raw)
    prev_space = True
    while i < n:
        c = raw[i]
        if join and c == "-" and re.match(r"-[ \t]*\n", raw[i:i + 8]):  # hyphen at a line break (blank lines too): join
            m = re.match(r"-[ \t]*\n[ \t\n]*", raw[i:])
            line += m.group().count("\n")
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


def source(slug, join=True):
    if (slug, join) not in _CACHE:
        _CACHE[(slug, join)] = norm_with_map((CONVERTED / f"{slug}.md").read_text(), join)
    return _CACHE[(slug, join)]


def slugs():
    return sorted(p.stem for p in CONVERTED.glob("*.md") if p.name != "IMAGES-README.md")


def find(text, slug=None):
    q = norm(text)
    if not q:
        return []
    hits = []
    for join in (True, False):
        for s in [slug] if slug else slugs():
            body, lines = source(s, join)
            start = 0
            while True:
                k = body.find(q, start)
                if k < 0:
                    break
                hits.append((s, lines[k]))
                start = k + 1
        if hits:
            break
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
