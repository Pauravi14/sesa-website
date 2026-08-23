"""Extract crisp SA monogram with transparent background for header."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "logo-sesa-source.png"
FULL = ROOT / "assets" / "logo-sesa.png"
MARK = ROOT / "assets" / "logo-mark.png"


def is_foreground(r: int, g: int, b: int) -> bool:
    """Keep rose-gold / copper logo pixels; drop dark grey background."""
    if r < 55 and g < 55 and b < 60:
        return False
    # metallic copper / rose gold
    if r >= 90 and r >= b + 15 and g >= 50:
        return True
    # bright metal highlights
    if r >= 150 and g >= 110 and b >= 70:
        return True
    return False


def remove_background(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if is_foreground(r, g, b):
                px[x, y] = (r, g, b, 255)
            else:
                px[x, y] = (0, 0, 0, 0)
    return im


def trim_alpha(im: Image.Image, pad: int = 8) -> Image.Image:
    alpha = im.split()[3]
    bbox = alpha.getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(im.width, x1 + pad)
    y1 = min(im.height, y1 + pad)
    return im.crop((x0, y0, x1, y1))


def crop_emblem(im: Image.Image) -> Image.Image:
    """Isolate circular SA mark above the SESA wordmark."""
    w, h = im.size
    px = im.load()
    top_limit = int(h * 0.52)
    xs, ys = [], []
    for y in range(top_limit):
        for x in range(w):
            if px[x, y][3] > 20:
                xs.append(x)
                ys.append(y)
    if not xs:
        return trim_alpha(im.crop((0, 0, w, int(h * 0.45))))
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    pad = int(max(x1 - x0, y1 - y0) * 0.06)
    return trim_alpha(
        im.crop(
            (
                max(0, x0 - pad),
                max(0, y0 - pad),
                min(w, x1 + pad),
                min(h, y1 + pad),
            )
        ),
        pad=4,
    )


def resize_mark(im: Image.Image, size: int = 240) -> Image.Image:
    w, h = im.size
    scale = size / max(w, h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    return im.resize((new_w, new_h), Image.Resampling.LANCZOS)


def main():
    src = Image.open(SRC)
    clean = remove_background(src)
    clean.save(FULL, optimize=True)
    mark = crop_emblem(clean)
    mark = resize_mark(mark, 240)
    mark.save(MARK, optimize=True)
    alpha = mark.split()[3]
    print("saved mark", mark.size, "bbox", alpha.getbbox())


if __name__ == "__main__":
    main()
