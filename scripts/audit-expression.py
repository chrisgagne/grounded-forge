#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["chromadb", "numpy"]
# ///
"""Expression-distance audit: how close does a distillation sit to its source's wording?

Copyright protects expression, not ideas or methods. A distillation that restates a
source's method in its own words, organised around the task, sits far from the source's
expression; one that condenses the book in its own order, in close paraphrase, sits near
it. This audit measures that distance, so "safe to ship" for copyrighted scopes can be a
build check rather than a judgement made file by file.

It reports, per distillation, against its converted source text:

  verbatim      share of the distillation's 8-word runs found in the source, the longest
                verbatim run, and the text of every run of LONG_RUN words or more (lines
                carrying a [V] marker are left out: those quotes are deliberate and
                scope-gated elsewhere)
  quotes        passages of five or more words inside quotation marks, on lines without a [V]
                marker, that appear word for word in the source: unmarked verbatim text, which
                a copyrighted-scope distillation shouldn't carry (a quoted title, whether of a
                chapter, a section, the work or a work it cites, is a citation, not copying,
                and doesn't count)
  paraphrase    share of distillation sentences whose nearest source sentence is both
                semantically close and shares most of its content words
  order         Spearman correlation between the order of the distillation's sentences and
                the positions of their nearest source sentences: near 1 means the
                distillation walks the book in the book's order
  coverage      share of the source's chapters the distillation draws on, and its length as
                a share of the source's
  specifics     numbers and multi-word names the distillation shares with the source (the
                author's own case details, as opposed to the method)

The thresholds are provisional until calibrated against labelled examples, as Pass I is
against tests/audit-fixtures/. The audit measures distance; where the line sits is a
policy decision for the operator and their counsel.

Sources resolve from {corpus}/sources/converted/{slug}.md, else from the converted-text
link in {corpus}/sources/original/{slug}.source.md. A distillation with neither is
reported as unmapped, never matched by guesswork.

Embeddings use chromadb's default model (all-MiniLM-L6-v2), the one scripts/setup-chroma.py
uses. Source embeddings are cached under the output directory, keyed by the source text's
hash.

Usage:
    uv run scripts/audit-expression.py --corpus corpus.local/my-corpus --task aar
    uv run scripts/audit-expression.py --corpus corpus.commons/demo --task aar --slug lfuo-learning-review-guide-2024
Output: {corpus}/_audit/expression/{task}/ (SUMMARY.md, one JSON per distillation).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

N = 8                      # verbatim run length, in words
CLOSE_SIM = 0.70           # provisional: nearest-source similarity for a close paraphrase
CLOSE_CONTAIN = 0.50       # provisional: share of content words shared with that sentence
MAP_SIM = 0.60             # a sentence at or above this is "drawn from" its nearest source sentence
MIN_WORDS = 8              # shorter sentences are too generic to compare
LONG_RUN = 15              # verbatim runs this long are listed in full
MODEL = "all-MiniLM-L6-v2"

STOP = set("""about above after again against also among another because been before being
below between both could does doing down during each even every from further have having here
into itself just like made make many more most much must only other over same should since some
such than that their them then there these they this those through under until upon very were
what when where which while whom whose will with within without would your yours""".split())


def clean_md(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[\]\{[^}]*\}", " ", text)                 # pandoc anchors: []{#id}
    text = re.sub(r"\{[#.][^}]*\}", " ", text)                  # pandoc attributes: {#id .class}
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)           # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)        # links -> text
    text = re.sub(r"\[([^\]]*)\]", r"\1", text)                 # leftover brackets
    text = re.sub(r"[*_`]+", "", text)
    return text


def sentences(text: str, keep_marked: bool) -> list[tuple[str, int]]:
    """Sentences of at least MIN_WORDS words, each with its chapter index."""
    raw = text.splitlines()
    levels = [len(m.group(1)) for line in raw if (m := re.match(r"^(#{1,3}) ", line))]
    top = next((lvl for lvl in (1, 2, 3) if levels.count(lvl) >= 3), 1)
    out, chapter, para = [], 0, []

    def flush():
        joined = clean_md(" ".join(para))
        for s in re.split(r"(?<=[.!?])[\"”’)]?\s+(?=[A-Z\"“(])", joined):
            s = re.sub(r"\s+", " ", s).strip(" -|>")
            if len(s.split()) >= MIN_WORDS:
                out.append((s, chapter))
        para.clear()

    for line in raw:
        m = re.match(r"^(#{1,6}) ", line)
        if m:
            flush()
            if len(m.group(1)) == top:
                chapter += 1
            continue
        if not line.strip() or re.match(r"^\s*(?:-{3,}|={3,}|[\s:|-]*\|[\s:|-]*)$", line):
            flush()                                        # blank, rule or table separator
            continue
        if not keep_marked and ("[V]" in line or re.match(r"^\s*\**(?:Framework )?Source:", line)):
            flush()                                        # marked quotes and citation lines
            continue
        if re.match(r"^\s*(?:[-*+]\s|\d+[.)]\s|\|)", line):   # list items and table rows stand alone
            flush()
            para.append(re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line).replace("|", " "))
            flush()
        else:
            para.append(line)
    flush()
    return out


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?", clean_md(text).lower())


def content_words(s: str) -> set[str]:
    return {w for w in words(s) if len(w) >= 4 and w not in STOP and not w.isdigit()}


def verbatim(dist_text: str, src_text: str) -> tuple[float, int, list[str]]:
    dist = words("\n".join(l for l in dist_text.splitlines() if "[V]" not in l))
    src = words(src_text)
    src_grams = {tuple(src[i:i + N]) for i in range(len(src) - N + 1)}
    grams = [tuple(dist[i:i + N]) for i in range(len(dist) - N + 1)]
    hit = [g in src_grams for g in grams]
    runs, i = [], 0
    while i < len(hit):
        if hit[i]:
            j = i
            while j < len(hit) and hit[j]:
                j += 1
            runs.append((i, j - i + N - 1))
            i = j
        else:
            i += 1
    best = max((n for _, n in runs), default=0)
    long_runs = [" ".join(dist[s:s + n]) for s, n in runs if n >= LONG_RUN]
    return (sum(hit) / len(grams) if grams else 0.0), best, long_runs


def looks_like_title(text: str) -> bool:
    """Title Case: most words over three letters are capitalised, as titles are and prose isn't."""
    big = [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", text) if len(w) > 3]
    return len(big) >= 2 and sum(w[0].isupper() for w in big) / len(big) >= 0.75


def citation_sections(src_text: str) -> str:
    """The text of the source's reference, bibliography and notes sections, where cited titles live."""
    out, keep = [], False
    for line in src_text.splitlines():
        if line.startswith("#"):
            keep = bool(re.search(r"reference|bibliograph|notes|works cited|sources", line, re.I))
        elif keep:
            out.append(line)
    return "\n".join(out)


QUOTED = re.compile(r"[\"“]([^\"“”]{20,}?)[\"”]")


def unmarked_quotes(dist_text: str, src_text: str) -> list[str]:
    """Quoted passages on unmarked lines that appear word for word in the source.

    Matching ignores spacing, because conversions from PDF often split words across a line
    break ("increas ingly"), which an exact word match would miss."""
    src = "".join(words(src_text))
    titles = {"".join(words(l.lstrip("#"))) for l in src_text.splitlines() if l.startswith("#")}
    titles.add("".join(words(citation_sections(src_text))))
    titles |= {"".join(words(q)) for line in src_text.splitlines()      # per line: one stray quote mark
               for q in QUOTED.findall(clean_md(line)) if looks_like_title(q)}  # can't misalign the rest
    found = []
    for line in dist_text.splitlines():
        if "[V]" in line:
            continue
        for q in QUOTED.findall(clean_md(line)):
            for piece in re.split(r"\s*(?:…|\.\.\.)\s*", q):    # an ellipsis joins separate excerpts
                w = words(piece)
                if (len(w) >= 5 and "".join(w) in src and not looks_like_title(piece)
                        and not any("".join(w) in h for h in titles)):
                    found.append(piece.strip())
    return found


def spearman(a: list[int], b: list[int]) -> float | None:
    if len(a) < 8:
        return None
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    if ra.std() == 0 or rb.std() == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


SPECIFIC_NUM = re.compile(r"(?<!Ch )(?<!Ch\. )(?<!p\. )(?<!pp\. )(?<![\w.])\d[\d,.]*\d(?:\s?%| hours| years| days| percent)?")
SPECIFIC_NAME = re.compile(r"(?<=[a-z,;:] )([A-Z][a-z]+(?: (?:of |the |and )?[A-Z][a-z0-9]+)+)")


def specifics(dist_text: str, src_text: str) -> list[str]:
    body = clean_md(dist_text)
    cands = {m.group(0).strip() for m in SPECIFIC_NUM.finditer(body)}
    cands |= {m.group(1) for m in SPECIFIC_NAME.finditer(body)}
    src = clean_md(src_text)
    return sorted(c for c in cands if len(c) >= 3 and c in src)


class Embedder:
    def __init__(self, cache: Path):
        from chromadb.utils import embedding_functions
        self.fn = embedding_functions.DefaultEmbeddingFunction()
        self.cache = cache
        cache.mkdir(parents=True, exist_ok=True)

    def embed(self, texts: list[str]) -> np.ndarray:
        vecs = []
        for i in range(0, len(texts), 256):
            vecs.extend(self.fn(texts[i:i + 256]))
        m = np.asarray(vecs, dtype=np.float32)
        return m / np.maximum(np.linalg.norm(m, axis=1, keepdims=True), 1e-9)

    def embed_source(self, slug: str, text: str, sents: list[str]) -> np.ndarray:
        key = hashlib.sha256((MODEL + text).encode()).hexdigest()[:16]
        path = self.cache / f"{slug}-{key}.npy"
        if path.exists():
            return np.load(path)
        m = self.embed(sents)
        np.save(path, m)
        return m


def resolve_source(corpus: Path, slug: str) -> Path | None:
    direct = corpus / "sources" / "converted" / f"{slug}.md"
    if direct.is_file():
        return direct
    card = corpus / "sources" / "original" / f"{slug}.source.md"
    if card.is_file():
        m = re.search(r"\]\((\.\./converted/[^)]+\.md)\)", card.read_text())
        if m:
            path = (card.parent / m.group(1)).resolve()
            if path.is_file():
                return path
    return None


def scope_of(corpus: Path, slug: str) -> str:
    deep = corpus / "references" / f"{slug}-deep.md"
    if deep.is_file():
        m = re.search(r"\*\*Scope:\*\*\s*([a-z-]+)", deep.read_text()[:4000])
        if m:
            return m.group(1)
    return "unknown"


def audit(corpus: Path, task: str, slug: str, emb: Embedder) -> dict:
    dist_path = corpus / "distillations" / task / f"{slug}-{task}.md"
    row = {"slug": slug, "scope": scope_of(corpus, slug)}
    src_path = resolve_source(corpus, slug)
    if src_path is None:
        return row | {"status": "unmapped"}
    dist_text, src_text = dist_path.read_text(), src_path.read_text()
    d_sents = sentences(dist_text, keep_marked=False)
    s_sents = sentences(src_text, keep_marked=True)
    if not d_sents or not s_sents:
        return row | {"status": "empty", "source": src_path.name}

    vb_share, vb_run, vb_long = verbatim(dist_text, src_text)
    d_emb = emb.embed([s for s, _ in d_sents])
    s_emb = emb.embed_source(slug, src_text, [s for s, _ in s_sents])
    best_idx = np.empty(len(d_sents), dtype=int)
    best_sim = np.empty(len(d_sents), dtype=np.float32)
    for i in range(0, len(d_sents), 64):
        sims = d_emb[i:i + 64] @ s_emb.T
        best_idx[i:i + 64] = sims.argmax(axis=1)
        best_sim[i:i + 64] = sims.max(axis=1)

    pairs = []
    for k, (s, _) in enumerate(d_sents):
        src_s, chap = s_sents[best_idx[k]]
        cw = content_words(s)
        contain = len(cw & content_words(src_s)) / len(cw) if cw else 0.0
        pairs.append({"i": k, "sim": round(float(best_sim[k]), 3), "contain": round(contain, 2),
                      "src_pos": int(best_idx[k]), "chapter": chap,
                      "distillation": s, "source": src_s})
    close = [p for p in pairs if p["sim"] >= CLOSE_SIM and p["contain"] >= CLOSE_CONTAIN]
    mapped = [p for p in pairs if p["sim"] >= MAP_SIM]
    chapters = max(c for _, c in s_sents) or 1

    return row | {
        "status": "ok",
        "source": src_path.name,
        "words": {"distillation": len(words(dist_text)), "source": len(words(src_text))},
        "length_ratio": round(len(words(dist_text)) / max(len(words(src_text)), 1), 4),
        "verbatim": {"share": round(vb_share, 4), "longest_run": vb_run, "long_runs": vb_long},
        "paraphrase": {"close_share": round(len(close) / len(pairs), 3), "close": len(close),
                       "sentences": len(pairs),
                       "median_sim": round(float(np.median(best_sim)), 3)},
        "order": {"spearman": spearman([p["i"] for p in mapped], [p["src_pos"] for p in mapped]),
                  "mapped": len(mapped)},
        "coverage": {"chapters_drawn_on": len({p["chapter"] for p in mapped}), "chapters": chapters},
        "unmarked_quotes": unmarked_quotes(dist_text, src_text),
        "specifics": specifics(dist_text, src_text),
        "closest": sorted(pairs, key=lambda p: -p["sim"])[:25],
    }


def summary(rows: list[dict], task: str) -> str:
    ok = sorted((r for r in rows if r.get("status") == "ok"),
                key=lambda r: (-r["paraphrase"]["close_share"], -(r["order"]["spearman"] or 0)))
    lines = [f"# Expression-distance audit: {task}", "",
             f"Provisional thresholds: close paraphrase = similarity >= {CLOSE_SIM} and "
             f">= {CLOSE_CONTAIN:.0%} shared content words; drawn-on = similarity >= {MAP_SIM}. "
             "Uncalibrated: read the per-slug JSON before acting on a number.", "",
             "| slug | scope | unmarked quotes | runs of 15+ words | close paraphrase | median sim | order (rho) | chapters | verbatim | longest run | length | specifics |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in ok:
        rho = r["order"]["spearman"]
        lines.append(
            f"| {r['slug']} | {r['scope']} | {len(r['unmarked_quotes'])} | {len(r['verbatim']['long_runs'])} | {r['paraphrase']['close_share']:.0%} "
            f"({r['paraphrase']['close']}/{r['paraphrase']['sentences']}) | {r['paraphrase']['median_sim']:.2f} | "
            f"{'—' if rho is None else f'{rho:+.2f}'} | {r['coverage']['chapters_drawn_on']}/{r['coverage']['chapters']} | "
            f"{r['verbatim']['share']:.1%} | {r['verbatim']['longest_run']} | {r['length_ratio']:.1%} | {len(r['specifics'])} |")
    other = [r for r in rows if r.get("status") != "ok"]
    if other:
        lines += ["", f"Not audited ({len(other)}): " + ", ".join(f"{r['slug']} ({r['status']})" for r in other)]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--corpus", required=True, type=Path)
    ap.add_argument("--task", required=True)
    ap.add_argument("--slug", action="append", help="audit only these slugs (repeatable)")
    ap.add_argument("--out", type=Path, help="default: {corpus}/_audit/expression/{task}")
    args = ap.parse_args()

    dist_dir = args.corpus / "distillations" / args.task
    suffix = f"-{args.task}.md"
    slugs = args.slug or sorted(p.name[: -len(suffix)] for p in dist_dir.glob(f"*{suffix}"))
    out = args.out or args.corpus / "_audit" / "expression" / args.task
    out.mkdir(parents=True, exist_ok=True)
    emb = Embedder(out / ".cache")

    rows = []
    for n, slug in enumerate(slugs, 1):
        row = audit(args.corpus, args.task, slug, emb)
        (out / f"{slug}.json").write_text(json.dumps(row, indent=2, ensure_ascii=False))
        rows.append(row)
        brief = (f"close {row['paraphrase']['close_share']:.0%}, rho {row['order']['spearman']}"
                 if row.get("status") == "ok" else row["status"])
        print(f"[{n}/{len(slugs)}] {slug}: {brief}", file=sys.stderr, flush=True)
    if not args.slug:
        (out / "SUMMARY.md").write_text(summary(rows, args.task))
    print(summary(rows, args.task))


if __name__ == "__main__":
    main()
