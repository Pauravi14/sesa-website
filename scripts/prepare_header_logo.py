"""Header monogram from transparent monogram — bright copper, no dark shadows on navy."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "transparent monogram.png"
OUT = ROOT / "assets" / "logo-monogram.png"

COPPER = (201, 137, 88)
COPPER_LIGHT = (245, 215, 180)
COPPER_MID = (220, 165, 115)
MIN_LUM = 95


def is_copper_pixel(r: int, g: int, b: int) -> bool:
    if max(r, g, b) < MIN_LUM:
        return False
    if r < 70 or g < 45:
        return False
    if r < b + 10:
        return False
    return r + g >= 140


def copper_tint(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 25:
                px[x, y] = (0, 0, 0, 0)
                continue
            lum = max(r, g, b)
            if not is_copper_pixel(r, g, b):
                px[x, y] = (0, 0, 0, 0)
                continue
            t = min(1.0, (lum - MIN_LUM) / 155.0)
            out = tuple(
                int(COPPER[i] + t * (COPPER_LIGHT[i] - COPPER[i]))
                for i in range(3)
            )
            px[x, y] = (*out, min(255, a))
    return im


def crop_content(im: Image.Image, pad: float = 0.06) -> Image.Image:
    alpha = im.split()[-1]
    box = alpha.getbbox()
    if not box:
        return im
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    pad_x = int(w * pad)
    pad_y = int(h * pad)
    return im.crop(
        (
            max(0, x0 - pad_x),
            max(0, y0 - pad_y),
            min(im.width, x1 + pad_x),
            min(im.height, y1 + pad_y),
        )
    )


def resize_height(im: Image.Image, height: int) -> Image.Image:
    w, h = im.size
    scale = height / h
    return im.resize((max(1, int(w * scale)), height), Image.Resampling.LANCZOS)


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"missing source: {SRC}")
    raw = Image.open(SRC)
    cleaned = copper_tint(raw)
    cropped = crop_content(cleaned)
    out = resize_height(cropped, 280)
    out.save(OUT, optimize=True)
    print("saved", OUT, out.size)


if __name__ == "__main__":
    main()
