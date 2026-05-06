#!/usr/bin/env python3
"""Crop each screenshot to the cream-colored card and re-encode with NO metadata.

For each input PNG:
  1. Find pixels close to the paper colour #F1E9D2 (RGB ≈ 241,233,210).
  2. Compute the bounding box of that region; expand by a small margin.
  3. Crop, then re-save as a fresh PNG with no EXIF / XMP / iTXt / tEXt chunks.
"""
import io
import sys
from pathlib import Path
from PIL import Image, PngImagePlugin

PAPER = (241, 233, 210)
TOL = 18  # max channel distance to count as paper


def is_paper(px):
    return all(abs(px[i] - PAPER[i]) <= TOL for i in range(3))


def find_paper_bbox(img):
    """Return (left, top, right, bottom) of the cream region, with margin."""
    px = img.load()
    w, h = img.size
    # Sample-scan to find rows/cols with paper pixels
    # Use a 4-pixel stride for speed; cards are large, no need for full resolution
    STRIDE = 4
    # Determine which rows contain paper
    paper_rows = [False] * h
    paper_cols = [False] * w
    for y in range(0, h, STRIDE):
        for x in range(0, w, STRIDE):
            p = px[x, y]
            if isinstance(p, int):
                continue
            if is_paper(p[:3]):
                paper_rows[y] = True
                paper_cols[x] = True
    if not any(paper_rows) or not any(paper_cols):
        return None
    top = next(i for i, v in enumerate(paper_rows) if v)
    bottom = h - 1 - next(i for i, v in enumerate(reversed(paper_rows)) if v)
    left = next(i for i, v in enumerate(paper_cols) if v)
    right = w - 1 - next(i for i, v in enumerate(reversed(paper_cols)) if v)
    # Tight margin so we keep a small dark frame around the card
    margin = 14
    left = max(0, left - margin)
    top = max(0, top - margin)
    right = min(w - 1, right + margin)
    bottom = min(h - 1, bottom + margin)
    return left, top, right + 1, bottom + 1


def strip_save(img, out_path):
    """Save img as PNG with no metadata."""
    # Build a clean image (drops palette/transparency baggage too) and write
    # via a brand-new bytes stream so PIL doesn't carry over input chunks.
    clean = Image.new("RGB", img.size, (0, 0, 0))
    clean.paste(img.convert("RGB"))
    info = PngImagePlugin.PngInfo()  # empty: no tEXt / iTXt
    buf = io.BytesIO()
    clean.save(buf, format="PNG", pnginfo=info, optimize=True, compress_level=6)
    out_path.write_bytes(buf.getvalue())


def main(srcs, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    for src in srcs:
        img = Image.open(src)
        bbox = find_paper_bbox(img)
        if bbox is None:
            print(f"!! no paper region in {src.name}, skipping")
            continue
        cropped = img.crop(bbox)
        out = out_dir / src.name.replace(" ", "_")
        strip_save(cropped, out)
        print(f"   {src.name}  ->  {out.name}  ({cropped.size[0]}×{cropped.size[1]})")


if __name__ == "__main__":
    out_dir = Path(sys.argv[1])
    srcs = [Path(p) for p in sys.argv[2:]]
    main(srcs, out_dir)
