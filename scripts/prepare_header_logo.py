"""Header monogram mask — painted with CSS var(--copper) for exact brand color match."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "transparent monogram.png"
OUT_MASK = ROOT / "assets" / "logo-monogram-mask.png"

MIN_LUM = 40


def logo_alpha(raw: Image.Image) -> Image.Image:
    arr = np.array(raw.convert("RGBA"))
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    lum = np.maximum(np.maximum(r, g), b)
    in_logo = (a > 15) & (lum > MIN_LUM)
    strength = np.zeros_like(lum, dtype=np.float32)
    strength[in_logo] = np.clip((lum[in_logo] - MIN_LUM) / 190.0, 0.12, 1.0)
    strength[in_logo] *= a[in_logo] / 255.0
    alpha = (strength * 255).astype(np.uint8)
    out = np.zeros((arr.shape[0], arr.shape[1], 4), dtype=np.uint8)
    out[:, :, 0] = 255
    out[:, :, 1] = 255
    out[:, :, 2] = 255
    out[:, :, 3] = alpha
    return Image.fromarray(out)


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
    mask = logo_alpha(raw)
    mask = crop_content(mask)
    mask = resize_height(mask, 280)
    mask.save(OUT_MASK, optimize=True)
    print("saved", OUT_MASK, mask.size)


if __name__ == "__main__":
    main()
