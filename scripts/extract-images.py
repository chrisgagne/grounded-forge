#!/usr/bin/env python3
"""Extract images from PDF and EPUB sources alongside their converted markdown.

Operates per-corpus. Given a source binary at
corpus.commons/{corpus}/sources/original/{slug}.{pdf,epub}, the script:

1. Derives the corpus root from the source path.
2. Resolves the converted-md slug (typically the original stem,
   sometimes prefixed; matches the existing {prefix}-{slug}.md naming).
3. Writes images to
   corpus.commons/{corpus}/sources/converted/{md-slug}-images/.
4. Emits an extraction manifest at
   corpus.commons/{corpus}/sources/converted/extraction-manifest.json.

Classification (SUBSTANTIVE vs DECORATIVE) happens during ingestion
review; classified entries land in
corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml.

Usage:
    python3 scripts/extract-images.py corpus.commons/demo/sources/original/openstax-organizational-behavior.pdf

Dependencies:
    pip install PyMuPDF ebooklib
"""

import hashlib
import json
import os
import re
import sys
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

REPO_ROOT = Path(__file__).parent.parent

MIN_WIDTH = 100
MIN_HEIGHT = 100
MIN_BYTES = 5000


def slugify(name):
    """Convert a source filename to a directory slug."""
    stem = Path(name).stem
    stem = re.sub(r"[-_]\d{4}$", "", stem)
    stem = re.sub(r"[-_](epub|pdf|mobi|azw3)$", "", stem, flags=re.IGNORECASE)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()
    return slug[:60]


def resolve_converted_dir(source_path):
    """Walk up from a source path under corpus.commons/{corpus}/sources/original/
    to find the sibling converted/ dir.
    """
    p = source_path.resolve()
    for parent in p.parents:
        sibling = parent.parent / "converted"
        if parent.name == "original" and sibling.is_dir():
            return sibling
    raise SystemExit(
        f"Could not resolve converted/ dir from {source_path}. "
        "Source must live under corpus.commons/{corpus}/sources/original/."
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
        return []

    manifest = []
    seen = set()

    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        print(f"  ERROR opening {pdf_path}: {e}")
        return []

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
        return []

    manifest = []
    seen = set()

    try:
        book = epub.read_epub(str(epub_path), options={"ignore_ncx": True})
    except Exception as e:
        print(f"  ERROR reading {epub_path}: {e}")
        return []

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
    """Find every PDF/EPUB under any corpus.commons/*/sources/original/ dir."""
    sources = []
    commons = REPO_ROOT / "corpus.commons"
    if not commons.exists():
        return sources
    for original in commons.glob("*/sources/original"):
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

    manifest_by_dir = {}
    for source in targets:
        if not source.exists():
            print(f"  ERROR: {source} not found")
            continue
        converted_dir = resolve_converted_dir(source)
        manifest_by_dir.setdefault(converted_dir, []).extend(process_file(source))

    total = 0
    for converted_dir, manifest in manifest_by_dir.items():
        manifest_path = converted_dir / "extraction-manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)
        total += len(manifest)
        print(f"\nManifest: {manifest_path.relative_to(REPO_ROOT)} ({len(manifest)} images)")

    print(f"\n{'=' * 60}")
    print(f"DONE: {total} total image(s) extracted")
    print(f"{'=' * 60}")
    print("\nNext: classify each extracted image as SUBSTANTIVE or")
    print("DECORATIVE. Append SUBSTANTIVE entries to")
    print("corpus.commons/{corpus}/sources/converted/IMAGE-INDEX.yaml.")
    print("Delete DECORATIVE files.")


if __name__ == "__main__":
    main()
