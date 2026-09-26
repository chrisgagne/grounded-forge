#!/usr/bin/env python3
"""Extract images from PDF and EPUB sources alongside their converted markdown.

Operates per-corpus. Given a source binary at
corpus.commons/{corpus}/sources/original/{slug}.{pdf,epub}, the script:

1. Derives the corpus root from the source path.
2. Resolves the converted-md slug (typically the original stem,
   sometimes prefixed; matches the existing {prefix}-{slug}.md naming).
3. Writes images to
   corpus.commons/{corpus}/sources/converted/{md-slug}-images/.
4. Merges its results into the corpus-wide extraction manifest at
   corpus.commons/{corpus}/sources/converted/extraction-manifest.json.

The manifest is corpus-shared but the extractor runs per source, and during a
parallel ingestion batch four or five of them run at once. So the write is a
merge, not an overwrite: entries for the sources handled by *this* invocation
are replaced, every sibling entry is carried through, and the whole
read-modify-write happens under an exclusive lock on the converted/ directory
and lands via os.replace. Without that, the last extractor to finish published
a manifest holding only its own images and silently dropped its siblings'.

Classification (SUBSTANTIVE vs DECORATIVE) happens during ingestion
review; classified entries land in
corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml.

Usage:
    python3 scripts/extract-images.py corpus.commons/demo/sources/original/openstax-organizational-behavior.pdf

Dependencies:
    pip install PyMuPDF ebooklib
"""

import contextlib
import errno
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
import time
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

try:
    import ebooklib
    from ebooklib import epub
except ImportError:
    ebooklib = None

# Resolved so the manifest's relative paths survive a symlinked checkout.
REPO_ROOT = Path(__file__).resolve().parent.parent

MIN_WIDTH = 100
MIN_HEIGHT = 100
MIN_BYTES = 5000

MANIFEST_NAME = "extraction-manifest.json"
LOCK_TIMEOUT_S = 120
LOCK_POLL_S = 0.05


@contextlib.contextmanager
def converted_dir_lock(converted_dir):
    """Hold an exclusive advisory lock for one corpus's converted/ directory.

    The lock is taken on the directory itself rather than on a sidecar file:
    the manifest is published by os.replace, which swaps the inode, so a lock
    held on the manifest would not exclude anything. The directory's inode is
    stable, and locking it leaves no artefact behind in the corpus.

    Advisory locks only bind processes that ask for them, which is fine — the
    extractor is the only writer.
    """
    fd = os.open(str(converted_dir), os.O_RDONLY)
    deadline = time.monotonic() + LOCK_TIMEOUT_S
    try:
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError as e:
                if e.errno not in (errno.EACCES, errno.EAGAIN):
                    raise
                if time.monotonic() >= deadline:
                    raise SystemExit(
                        f"Timed out after {LOCK_TIMEOUT_S}s waiting for the manifest lock on "
                        f"{converted_dir}. Another extractor may be stuck; check for a hung run."
                    )
                time.sleep(LOCK_POLL_S)
        try:
            yield
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
    finally:
        os.close(fd)


def load_manifest(manifest_path):
    """Read the manifest, tolerating absence. A malformed file is reported and
    treated as empty — it is a regenerable working artefact, but the operator
    needs to know the history went missing rather than find out downstream.
    """
    if not manifest_path.exists():
        return []
    try:
        with open(manifest_path) as f:
            existing = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  WARNING: {manifest_path} unreadable ({e}); rebuilding from this run only")
        return []
    if not isinstance(existing, list):
        print(f"  WARNING: {manifest_path} is not a JSON list; rebuilding from this run only")
        return []
    return [e for e in existing if isinstance(e, dict)]


def manifest_sort_key(entry):
    return (
        str(entry.get("source_file") or ""),
        entry.get("page") if isinstance(entry.get("page"), int) else -1,
        str(entry.get("file") or ""),
    )


def merge_manifest(converted_dir, handled_sources, entries):
    """Fold this run's entries into the corpus manifest and return the total.

    Held under the directory lock so five concurrent extractors serialise
    rather than overwrite. Entries for `handled_sources` are dropped before the
    new ones go in, so re-running one source refreshes its own images without
    duplicating them or disturbing anyone else's.
    """
    manifest_path = converted_dir / MANIFEST_NAME
    handled = {str(Path(s).resolve().relative_to(REPO_ROOT)) for s in handled_sources}

    with converted_dir_lock(converted_dir):
        merged = [e for e in load_manifest(manifest_path) if e.get("source_file") not in handled]
        merged.extend(entries)
        merged.sort(key=manifest_sort_key)

        fd, tmp_name = tempfile.mkstemp(dir=str(converted_dir), prefix=".manifest-", suffix=".json")
        try:
            with os.fdopen(fd, "w") as f:
                json.dump(merged, f, indent=2)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_name, manifest_path)
        except BaseException:
            with contextlib.suppress(OSError):
                os.unlink(tmp_name)
            raise

    return len(merged)


def slugify(name):
    """Convert a source filename to a directory slug."""
    stem = Path(name).stem
    stem = re.sub(r"[-_]\d{4}$", "", stem)
    stem = re.sub(r"[-_](epub|pdf|mobi|azw3)$", "", stem, flags=re.IGNORECASE)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()
    return slug[:60]


# A source can be handed to the extractor from either staging directory.
# `ingesting-resources` runs extraction while the input is still in ingest/ —
# it has to, because the next step removes the input — and re-extraction later
# runs against the promoted copy in original/.
SOURCE_DIRS = ("original", "ingest")


def resolve_converted_dir(source_path):
    """Walk up from a source path under {corpus}/sources/{original,ingest}/
    to find the sibling converted/ dir.
    """
    p = source_path.resolve()
    for parent in p.parents:
        sibling = parent.parent / "converted"
        if parent.name in SOURCE_DIRS and sibling.is_dir():
            return sibling
    raise SystemExit(
        f"Could not resolve converted/ dir from {source_path}. "
        "Source must live under {corpus}/sources/original/ or {corpus}/sources/ingest/, "
        "alongside a sibling converted/ directory."
    )


def resolve_md_slug(source_path, converted_dir):
    """Return the converted markdown's stem (e.g. openstax-organizational-behavior)
    if a matching .md exists in converted_dir; otherwise fall back to the
    source's own slug.
    """
    src_slug = slugify(source_path.name)
    for candidate in converted_dir.glob("*.md"):
        if candidate.stem.endswith(src_slug) or candidate.stem == src_slug:
            return candidate.stem
    return src_slug


def extract_pdf_images(pdf_path, output_dir):
    if fitz is None:
        print(f"  SKIP (no PyMuPDF): {pdf_path}")
        return None

    manifest = []
    seen = set()

    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        print(f"  ERROR opening {pdf_path}: {e}")
        return None

    for page_num in range(len(doc)):
        page = doc[page_num]
        for img_idx, img_info in enumerate(page.get_images(full=True)):
            xref = img_info[0]
            try:
                base = doc.extract_image(xref)
            except Exception:
                continue
            if base is None:
                continue

            data = base["image"]
            w = base.get("width", 0)
            h = base.get("height", 0)
            ext = base.get("ext", "png")

            if w < MIN_WIDTH or h < MIN_HEIGHT:
                continue
            if len(data) < MIN_BYTES:
                continue

            h_id = hashlib.md5(data).hexdigest()[:12]
            if h_id in seen:
                continue
            seen.add(h_id)

            filename = f"p{page_num + 1:04d}-{img_idx + 1}.{ext}"
            out_path = output_dir / filename
            out_path.write_bytes(data)

            manifest.append({
                "file": str(out_path.relative_to(REPO_ROOT)),
                "source_file": str(pdf_path.relative_to(REPO_ROOT)),
                "page": page_num + 1,
                "width": w,
                "height": h,
                "size_bytes": len(data),
                "hash": h_id,
            })

    doc.close()
    return manifest


def extract_epub_images(epub_path, output_dir):
    if ebooklib is None:
        print(f"  SKIP (no ebooklib): {epub_path}")
        return None

    manifest = []
    seen = set()

    try:
        book = epub.read_epub(str(epub_path), options={"ignore_ncx": True})
    except Exception as e:
        print(f"  ERROR reading {epub_path}: {e}")
        return None

    img_idx = 0
    for item in book.get_items():
        if item.get_type() != ebooklib.ITEM_IMAGE:
            continue
        data = item.get_content()
        if len(data) < MIN_BYTES:
            continue

        h_id = hashlib.md5(data).hexdigest()[:12]
        if h_id in seen:
            continue
        seen.add(h_id)

        item_name = item.get_name()
        ext = Path(item_name).suffix.lstrip(".") or "png"
        if ext not in ("png", "jpg", "jpeg", "gif", "svg", "webp"):
            ext = "png"

        img_idx += 1
        filename = f"img-{img_idx:04d}.{ext}"
        out_path = output_dir / filename
        out_path.write_bytes(data)

        w, h = 0, 0
        if fitz and ext in ("png", "jpg", "jpeg"):
            try:
                pix = fitz.Pixmap(data)
                w, h = pix.width, pix.height
                pix = None
                if w < MIN_WIDTH or h < MIN_HEIGHT:
                    out_path.unlink()
                    continue
            except Exception:
                pass

        manifest.append({
            "file": str(out_path.relative_to(REPO_ROOT)),
            "source_file": str(epub_path.relative_to(REPO_ROOT)),
            "page": None,
            "item_name": item_name,
            "width": w,
            "height": h,
            "size_bytes": len(data),
            "hash": h_id,
        })

    return manifest


def process_file(source_path):
    source_path = Path(source_path).resolve()
    converted_dir = resolve_converted_dir(source_path)
    md_slug = resolve_md_slug(source_path, converted_dir)
    output_dir = converted_dir / f"{md_slug}-images"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n  {source_path.name} -> {output_dir.relative_to(REPO_ROOT)}/")

    suffix = source_path.suffix.lower()
    if suffix == ".pdf":
        manifest = extract_pdf_images(source_path, output_dir)
    elif suffix == ".epub":
        manifest = extract_epub_images(source_path, output_dir)
    else:
        return []

    if manifest is None:
        # The source was never inspected — a missing dependency or an
        # unreadable file. That is not the same as "inspected, found nothing",
        # and the caller must not let it clear this source's manifest entries.
        print(f"    -> not inspected; leaving any existing entries alone")
        return None

    if manifest:
        print(f"    -> {len(manifest)} images extracted")
    else:
        try:
            output_dir.rmdir()
        except OSError:
            pass
        print(f"    -> 0 images (skipped)")
    return manifest


def collect_sources():
    """Find every PDF/EPUB under any corpus tier's sources/original/ dir."""
    sources = []
    for tier in ("corpus.commons", "corpus.local"):
        root_dir = REPO_ROOT / tier
        if not root_dir.exists():
            continue
        for original in root_dir.glob("*/sources/original"):
            for root, _, files in os.walk(original):
                for f in files:
                    p = Path(root) / f
                    if p.suffix.lower() in (".pdf", ".epub"):
                        sources.append(p)
    return sorted(sources)


def main():
    if len(sys.argv) > 1:
        targets = [Path(arg) for arg in sys.argv[1:]]
    else:
        targets = collect_sources()

    if not targets:
        print(
            "No PDF/EPUB sources found under any corpus.commons/*/sources/original/."
        )
        sys.exit(0)

    print(f"\n{'=' * 60}")
    print(f"Extracting images from {len(targets)} source(s)")
    print(f"{'=' * 60}")

    # Sources are grouped by converted/ dir so one lock covers one corpus, and
    # the source list is kept alongside the entries: a source that yielded no
    # images still has to clear any stale entries it left behind.
    runs = {}
    for source in targets:
        if not source.exists():
            print(f"  ERROR: {source} not found")
            continue
        converted_dir = resolve_converted_dir(source)
        run = runs.setdefault(converted_dir, {"sources": [], "entries": [], "skipped": []})
        entries = process_file(source)
        if entries is None:
            # Un-inspected. Keep it out of handled_sources so merge_manifest
            # carries its existing entries through untouched.
            run["skipped"].append(source)
            continue
        run["sources"].append(source)
        run["entries"].extend(entries)

    total = 0
    skipped_any = False
    for converted_dir, run in runs.items():
        if run["skipped"]:
            skipped_any = True
            names = ", ".join(s.name for s in run["skipped"])
            print(f"\n  NOT INSPECTED ({len(run['skipped'])}): {names}")
        if not run["sources"]:
            continue
        merged = merge_manifest(converted_dir, run["sources"], run["entries"])
        total += len(run["entries"])
        manifest_path = converted_dir / MANIFEST_NAME
        print(
            f"\nManifest: {manifest_path.relative_to(REPO_ROOT)} "
            f"({len(run['entries'])} images this run, {merged} in the corpus)"
        )

    print(f"\n{'=' * 60}")
    print(f"DONE: {total} total image(s) extracted")
    print(f"{'=' * 60}")
    if skipped_any:
        print("\nSome sources were not inspected. Install the missing extractor")
        print("  pip install PyMuPDF ebooklib")
        print("and re-run; their existing manifest entries were left intact.")
    print("\nNext: classify each extracted image as SUBSTANTIVE or")
    print("DECORATIVE. Append SUBSTANTIVE entries to")
    print("corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml.")
    print("Delete DECORATIVE files.")


if __name__ == "__main__":
    main()
