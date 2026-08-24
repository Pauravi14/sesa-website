"""Build raster logo mark from PDF (favicon etc.) — emblem band only."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF_RENDER = ROOT / "assets" / "logo-from-pdf.png"
SRC = ROOT / "assets" / "logo-sesa-source.png"
OUT = ROOT / "assets" / "logo-mark.png"


def is_copper(r: int, g: int, b: int) -> bool:
    if r < 75 or g < 50:
        return False
    if r < b + 15:
        return False
    return r + g >= 155


def copper_mask(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if is_copper(r, g, b):
                px[x, y] = (min(255, r), min(255, g), min(255, b), 255)
            else:
                px[x, y] = (0, 0, 0, 0)
    return im


def emblem_bounds(im: Image.Image) -> tuple[int, int, int, int]:
    w, h = im.size
    y0 = int(h * 0.21)
    y1 = int(h * 0.40)
    px = im.load()
    xs, ys = [], []
    for y in range(y0, y1):
        for x in range(w):
            if px[x, y][3] > 40:
                xs.append(x)
                ys.append(y)
    if not xs:
        return (0, y0, w, y1)
    pad = int(max(max(xs) - min(xs), max(ys) - min(ys)) * 0.12)
    return (
        max(0, min(xs) - pad),
        max(0, min(ys) - pad),
        min(w, max(xs) + pad),
        min(h, max(ys) + pad),
    )


def pad_square(im: Image.Image, size: int = 512) -> Image.Image:
    w, h = im.size
    scale = (size * 0.78) / max(w, h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.paste(im, ((size - nw) // 2, (size - nh) // 2), im)
    return canvas


def main():
    src_path = PDF_RENDER if PDF_RENDER.exists() else SRC
    im = Image.open(src_path)
    masked = copper_mask(im)
    box = emblem_bounds(masked)
    mark = pad_square(masked.crop(box), 512)
    mark.save(OUT, optimize=True)
    print("saved", OUT, mark.size, "crop", box)


if __name__ == "__main__":
    main()
