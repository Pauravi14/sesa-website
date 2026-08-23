"""Create transparent header mark (SA monogram only) from logo source."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "logo-sesa-source.png"
FULL = ROOT / "assets" / "logo-sesa.png"
MARK = ROOT / "assets" / "logo-mark.png"


def dist(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2))


def remove_background(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    w, h = im.size
    corners = [
        im.getpixel((5, 5)),
        im.getpixel((w - 6, 5)),
        im.getpixel((5, h - 6)),
        im.getpixel((w - 6, h - 6)),
    ]
    bg = tuple(int(sum(c[i] for c in corners) / 4) for i in range(3))
    px = im.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if dist((r, g, b), bg) < 3200 or (r < 50 and g < 50 and b < 55):
                px[x, y] = (0, 0, 0, 0)
    return im


def crop_emblem(im: Image.Image) -> Image.Image:
    w, h = im.size
    top = int(h * 0.02)
    bottom = int(h * 0.42)
    return im.crop((int(w * 0.08), top, int(w * 0.92), bottom))


def main():
    src = Image.open(SRC if SRC.exists() else FULL)
    clean = remove_background(src)
    clean.save(FULL, optimize=True)
    mark = crop_emblem(clean)
    mark.save(MARK, optimize=True)
    print("saved", FULL, mark.size)


if __name__ == "__main__":
    main()
