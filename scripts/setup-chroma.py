#!/usr/bin/env python3
"""Embed a corpus into a persisted Chroma collection.

Implements the v0.2 semantic-search retrieval backend committed to in
`.claude/skills/matching-references/SKILL.md`. The persisted DB lives *inside*
each corpus root at `{corpus_root}/chroma/`, alongside the corpus's
references, distillations, and lenses. Chroma is corpus-bound data, not
substrate; it travels with the corpus and is regenerated on clone (the DB
is gitignored at every corpus root). This script rebuilds it from the
current state of the corpus's `references/` and `distillations/` directories.

Multi-corpus support: pass `--corpus path/to/corpus` to target any corpus root.
The default is `corpus.commons/demo` for convenience; operators with multiple
corpora (e.g. `corpus.commons/your-corpus`, `corpus.local/your-corpus`) should
pass `--corpus` explicitly. The chroma directory resolves per-corpus:

    python3 scripts/setup-chroma.py                                  # → corpus.commons/demo/chroma/
    python3 scripts/setup-chroma.py --corpus corpus.local/your-corpus # → corpus.local/your-corpus/chroma/

The collection name is also corpus-bound, derived from the corpus slug,
so two corpora's collections cannot collide if a fork ever loads both
clients in one Chroma process.

Contract (from matching-references SKILL.md, v0.2 commitment):
- Semantic search returns *pointers* to candidate references (filenames,
  authors, similarity scores), never document bodies. Bodies stay in the
  file system, where they were projected once at ingestion.
- Semantic search sits *beneath* the curated indexes in the retrieval
  hierarchy, not above them. The curated index entries are the operator's
  pre-thought-of routing; semantic search is the safety net for genuinely
  novel queries.

Embedding model: chromadb's default (`DefaultEmbeddingFunction`), which
runs `all-MiniLM-L6-v2` through ONNX runtime. No PyTorch, no
sentence-transformers dependency, ~80MB ONNX weights downloaded to a
per-machine cache on first call. A fork that wants larger or
domain-tuned embeddings can swap `_make_embedding_function` below.

Granularity:
- Light refs: one embedding per file (the routing target).
- Distillations: one embedding per file (the routing target).
- Deep refs: one embedding per `##` section (so semantic search can land at
  the relevant part of a long deep ref, not just the file).

Idempotence: the script records a content checksum of every embedded
document at `{corpus_root}/chroma/.manifest.json`; reruns that find the
manifest matching the current corpus exit early as a no-op. Use `--rebuild`
to force a clean rebuild after editing references or distillations.
Chroma's HNSW segment is stored in a UUID-named subdirectory; rebuilds
produce a fresh UUID but functionally identical retrieval.

Optional reranking (`--rerank`): a cross-encoder reranks Chroma's top-k
by `(query, candidate)` pair scoring. Improves ordering on synthesis
queries where multiple candidates are close in vector space. Costs
sentence-transformers (~hundreds of MB with PyTorch) and one extra
model load per session. Considered but not evaluated against the corpus
yet; the flag exists so a fork can try it and report back whether the
quality bump justifies the install size.

Usage:
    python3 scripts/setup-chroma.py            # build (or no-op if up-to-date)
    python3 scripts/setup-chroma.py --rebuild  # force clean rebuild
    python3 scripts/setup-chroma.py --check    # run 3 canned queries, print top hits
    python3 scripts/setup-chroma.py --check --rerank  # ...with cross-encoder rerank
    python3 scripts/setup-chroma.py --stats    # print collection statistics

Dependencies:
    pip install chromadb              # required
    pip install sentence-transformers # optional, only for --rerank
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CORPUS_ROOT_DEFAULT = REPO_ROOT / "corpus.commons" / "demo"

# All four are resolved at runtime from the --corpus flag in main().
# Defaults below target the demo corpus so a bare `python3 setup-chroma.py`
# works on a fresh clone.
CORPUS_ROOT = CORPUS_ROOT_DEFAULT
CHROMA_DIR = CORPUS_ROOT / "chroma"
MANIFEST_PATH = CHROMA_DIR / ".manifest.json"
COLLECTION_NAME = f"{CORPUS_ROOT.name}-corpus"
REFERENCES_DIR = CORPUS_ROOT / "references"
DISTILLATIONS_DIR = CORPUS_ROOT / "distillations"


def _import_chromadb():
    try:
        import chromadb
        from chromadb.config import Settings
        from chromadb.utils import embedding_functions
    except ImportError:
        sys.stderr.write(
            "Missing dependency: chromadb. Install with:\n"
            "    pip install chromadb\n"
        )
        sys.exit(2)
    return chromadb, Settings, embedding_functions


def _make_embedding_function():
    """Return the default embedding function (ONNX, no PyTorch).

    Swap here to use a different model. For OpenAI / Voyage / custom
    embeddings, instantiate a different `embedding_functions.*` class
    and rebuild the collection (`--rebuild`); embedding spaces are
    not interchangeable.
    """
    _, _, embedding_functions = _import_chromadb()
    return embedding_functions.DefaultEmbeddingFunction()


# ---------------------------------------------------------------------------
# Corpus discovery
# ---------------------------------------------------------------------------


def _slug_from_path(path: Path) -> str:
    """Derive the source slug from a reference or distillation path."""
    name = path.stem
    name = re.sub(r"-deep$", "", name)
    for task_dir in DISTILLATIONS_DIR.iterdir() if DISTILLATIONS_DIR.exists() else []:
        if path.is_relative_to(task_dir):
            task = task_dir.name
            name = re.sub(rf"-{re.escape(task)}$", "", name)
    return name


def _parse_frontmatter_block(text: str) -> dict[str, str]:
    """Pull `**Source:**`, `**Scope:**`, etc. out of the head of a deep ref."""
    out: dict[str, str] = {}
    pattern = re.compile(r"^\*\*([A-Za-z][A-Za-z ]*):\*\*\s*(.+)$", re.MULTILINE)
    head = text[:5000]
    for m in pattern.finditer(head):
        key = m.group(1).strip().lower()
        out[key] = m.group(2).strip()
    return out


def _split_deep_ref_by_sections(text: str) -> list[tuple[str, str]]:
    """Split a deep ref into (section_anchor, section_text) chunks.

    Sections are delimited by `## ` headings. The frontmatter block (before
    the first `## `) is emitted as the synthetic section `_frontmatter`.
    """
    lines = text.split("\n")
    sections: list[tuple[str, list[str]]] = [("_frontmatter", [])]
    for line in lines:
        if line.startswith("## "):
            anchor = line[3:].strip()
            sections.append((anchor, []))
        else:
            sections[-1][1].append(line)
    return [(anchor, "\n".join(buf).strip()) for anchor, buf in sections if "\n".join(buf).strip()]


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------


def _build_documents() -> list[dict]:
    """Walk the corpus and assemble the list of documents to embed.

    Each document is a dict with keys: `id`, `text`, `metadata`. The id is
    stable across runs so re-embeds with the same corpus produce the same
    collection.
    """
    docs: list[dict] = []

    # Light refs: one per file.
    for path in sorted(REFERENCES_DIR.glob("*.md")):
        if path.name in ("README.md", "REFERENCE-INDEX.md"):
            continue
        if path.name.endswith("-deep.md"):
            continue
        text = path.read_text(encoding="utf-8")
        slug = _slug_from_path(path)
        rel = path.relative_to(REPO_ROOT).as_posix()
        docs.append(
            {
                "id": f"light:{slug}",
                "text": text,
                "metadata": {
                    "kind": "light",
                    "slug": slug,
                    "path": rel,
                },
            }
        )

    # Deep refs: one chunk per `## ` section.
    for path in sorted(REFERENCES_DIR.glob("*-deep.md")):
        text = path.read_text(encoding="utf-8")
        slug = _slug_from_path(path)
        rel = path.relative_to(REPO_ROOT).as_posix()
        frontmatter = _parse_frontmatter_block(text)
        for anchor, body in _split_deep_ref_by_sections(text):
            docs.append(
                {
                    "id": f"deep:{slug}:{_anchor_id(anchor)}",
                    "text": body,
                    "metadata": {
                        "kind": "deep",
                        "slug": slug,
                        "path": rel,
                        "section": anchor,
                        "scope": frontmatter.get("scope", "unknown"),
                    },
                }
            )

    # Distillations: one per file. Carries the task axis in metadata.
    if DISTILLATIONS_DIR.exists():
        for task_dir in sorted(DISTILLATIONS_DIR.iterdir()):
            if not task_dir.is_dir():
                continue
            task = task_dir.name
            for path in sorted(task_dir.glob("*.md")):
                if path.name == "README.md":
                    continue
                text = path.read_text(encoding="utf-8")
                slug = _slug_from_path(path)
                rel = path.relative_to(REPO_ROOT).as_posix()
                docs.append(
                    {
                        "id": f"distillation:{task}:{slug}",
                        "text": text,
                        "metadata": {
                            "kind": "distillation",
                            "slug": slug,
                            "task": task,
                            "path": rel,
                        },
                    }
                )

    return docs


def _anchor_id(anchor: str) -> str:
    """Stable, filesystem-safe id from a section anchor."""
    s = anchor.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "section"


# ---------------------------------------------------------------------------
# Manifest / idempotence
# ---------------------------------------------------------------------------


def _corpus_checksum(docs: list[dict]) -> str:
    """A checksum of every doc's id + text + sorted metadata items."""
    h = hashlib.sha256()
    for d in docs:
        h.update(d["id"].encode("utf-8"))
        h.update(b"\0")
        h.update(d["text"].encode("utf-8"))
        h.update(b"\0")
        meta_items = sorted(d["metadata"].items())
        h.update(repr(meta_items).encode("utf-8"))
        h.update(b"\x01")
    return h.hexdigest()


def _read_manifest() -> dict | None:
    if not MANIFEST_PATH.exists():
        return None
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _write_manifest(checksum: str, doc_count: int) -> None:
    payload = {
        "collection": COLLECTION_NAME,
        "checksum": checksum,
        "document_count": doc_count,
        "embedding_model": "all-MiniLM-L6-v2",
    }
    MANIFEST_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Build / check / stats
# ---------------------------------------------------------------------------


def _client():
    chromadb, Settings, _ = _import_chromadb()
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(
        path=str(CHROMA_DIR),
        settings=Settings(anonymized_telemetry=False),
    )


def _get_collection(client, embed_fn, *, create_if_missing: bool):
    try:
        return client.get_collection(name=COLLECTION_NAME, embedding_function=embed_fn)
    except Exception:
        if not create_if_missing:
            raise
        return client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=embed_fn,
            metadata={"hnsw:space": "cosine"},
        )


def build(*, rebuild: bool) -> int:
    docs = _build_documents()
    if not docs:
        sys.stderr.write("No documents found. Has the corpus been ingested?\n")
        return 1

    checksum = _corpus_checksum(docs)
    manifest = _read_manifest()

    if not rebuild and manifest and manifest.get("checksum") == checksum:
        print(
            f"chroma/ is up-to-date ({manifest.get('document_count')} docs, "
            f"checksum {checksum[:12]}). Skipping rebuild. Use --rebuild to force."
        )
        return 0

    if rebuild and CHROMA_DIR.exists():
        for child in CHROMA_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()

    embed_fn = _make_embedding_function()
    client = _client()

    try:
        client.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass

    collection = _get_collection(client, embed_fn, create_if_missing=True)

    batch_size = 64
    for i in range(0, len(docs), batch_size):
        batch = docs[i : i + batch_size]
        collection.add(
            ids=[d["id"] for d in batch],
            documents=[d["text"] for d in batch],
            metadatas=[d["metadata"] for d in batch],
        )

    _write_manifest(checksum, len(docs))

    by_kind: dict[str, int] = {}
    for d in docs:
        by_kind[d["metadata"]["kind"]] = by_kind.get(d["metadata"]["kind"], 0) + 1
    kinds_str = ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items()))
    print(f"Embedded {len(docs)} documents ({kinds_str}) into collection '{COLLECTION_NAME}'.")
    print(f"Persisted to {CHROMA_DIR.relative_to(REPO_ROOT)}/ (checksum {checksum[:12]}).")
    return 0


def _try_load_reranker():
    """Try to instantiate a CrossEncoder reranker; return None on failure.

    The reranker is an optional quality lever: it scores `(query, candidate)`
    pairs more accurately than vector similarity alone, at the cost of one
    extra model and the sentence-transformers / PyTorch stack. This has
    been considered but not evaluated against the corpus yet; the flag
    exists so a fork can try it and report back whether the quality bump
    justifies the install size.
    """
    try:
        from sentence_transformers import CrossEncoder
    except ImportError:
        sys.stderr.write(
            "--rerank requires sentence-transformers. Install with:\n"
            "    pip install sentence-transformers\n"
        )
        return None
    return CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def check(*, rerank: bool = False) -> int:
    """Run a small fixed set of queries and print the top hits.

    Proves the retrieval loop end-to-end without invoking Claude Code. A
    reviewer who clones the repo, runs setup, and then runs --check sees
    the matrix architecture working: a natural-language query routes to
    pre-projected distillations of the corpus.
    """
    embed_fn = _make_embedding_function()
    client = _client()
    try:
        collection = _get_collection(client, embed_fn, create_if_missing=False)
    except Exception:
        sys.stderr.write(
            "Collection not found. Run `python3 scripts/setup-chroma.py` first.\n"
        )
        return 1

    reranker = _try_load_reranker() if rerank else None
    if rerank and reranker is None:
        return 1

    top_n_final = 5
    top_k_retrieve = 25 if rerank else top_n_final

    queries = [
        "How should I handle a stakeholder conflict where positions are entrenched?",
        "What does the corpus say about employee motivation?",
        "How do I make a decision when the evidence is ambiguous?",
    ]
    for q in queries:
        print(f"\n> {q}")
        result = collection.query(query_texts=[q], n_results=top_k_retrieve)
        ids = result.get("ids", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        docs = result.get("documents", [[]])[0]
        dists = result.get("distances", [[]])[0]

        if reranker is not None and docs:
            pairs = [(q, d) for d in docs]
            scores = reranker.predict(pairs)
            ordered = sorted(
                zip(scores, ids, metas, dists), key=lambda t: -t[0]
            )[:top_n_final]
            for rank, (score, doc_id, meta, dist) in enumerate(ordered, start=1):
                tag = meta.get("kind", "?")
                slug = meta.get("slug", "?")
                extra = ""
                if tag == "deep":
                    extra = f" §{meta.get('section', '?')}"
                elif tag == "distillation":
                    extra = f" [{meta.get('task', '?')}]"
                print(
                    f"  {rank}. [{tag}] {slug}{extra}  "
                    f"(rerank={score:.3f}, sim={1 - dist:.3f})  → {meta.get('path')}"
                )
        else:
            for rank, (doc_id, meta, dist) in enumerate(
                zip(ids[:top_n_final], metas[:top_n_final], dists[:top_n_final]),
                start=1,
            ):
                similarity = 1 - dist  # cosine distance → similarity
                tag = meta.get("kind", "?")
                slug = meta.get("slug", "?")
                extra = ""
                if tag == "deep":
                    extra = f" §{meta.get('section', '?')}"
                elif tag == "distillation":
                    extra = f" [{meta.get('task', '?')}]"
                print(
                    f"  {rank}. [{tag}] {slug}{extra}  (sim={similarity:.3f})  → {meta.get('path')}"
                )
    return 0


def stats() -> int:
    embed_fn = _make_embedding_function()
    client = _client()
    try:
        collection = _get_collection(client, embed_fn, create_if_missing=False)
    except Exception:
        sys.stderr.write("Collection not found.\n")
        return 1
    count = collection.count()
    manifest = _read_manifest() or {}
    print(f"Collection: {COLLECTION_NAME}")
    print(f"Document count: {count}")
    print(f"Embedding model: {manifest.get('embedding_model', 'unknown')}")
    print(f"Checksum: {manifest.get('checksum', 'unknown')}")
    print(f"Persisted to: {CHROMA_DIR.relative_to(REPO_ROOT)}/")
    return 0


def main() -> int:
    global REFERENCES_DIR, DISTILLATIONS_DIR
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rebuild", action="store_true", help="force clean rebuild")
    parser.add_argument("--check", action="store_true", help="run canned queries, print top hits")
    parser.add_argument("--stats", action="store_true", help="print collection statistics")
    parser.add_argument(
        "--corpus",
        default=str(CORPUS_ROOT_DEFAULT),
        help=f"corpus root to embed (default: {CORPUS_ROOT_DEFAULT.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--rerank",
        action="store_true",
        help="rerank --check results with a cross-encoder (needs sentence-transformers)",
    )
    args = parser.parse_args()

    global CHROMA_DIR, MANIFEST_PATH, COLLECTION_NAME, CORPUS_ROOT
    corpus_root = Path(args.corpus)
    if not corpus_root.is_absolute():
        corpus_root = REPO_ROOT / corpus_root
    CORPUS_ROOT = corpus_root
    CHROMA_DIR = corpus_root / "chroma"
    MANIFEST_PATH = CHROMA_DIR / ".manifest.json"
    COLLECTION_NAME = f"{corpus_root.name}-corpus"
    REFERENCES_DIR = corpus_root / "references"
    DISTILLATIONS_DIR = corpus_root / "distillations"

    os.chdir(REPO_ROOT)

    if args.check:
        return check(rerank=args.rerank)
    if args.stats:
        return stats()
    return build(rebuild=args.rebuild)


if __name__ == "__main__":
    sys.exit(main())
