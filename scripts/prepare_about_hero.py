"""Crop a portrait hero image used only on the Über uns page."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

from prepare_service_thumbs import crop_cover, unified_grade

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "about"
SRC = ROOT / "assets" / "source" / "oldtimer-source.jpg"
OUT_FILE = OUT / "about-hero.jpg"
SIZE = (960, 1200)
FOCAL = (0.68, 0.38)


def about_hero_grade(img: Image.Image) -> Image.Image:
    img = unified_grade(img)
    img = ImageEnhance.Color(img).enhance(0.72)
    img = ImageEnhance.Brightness(img).enhance(0.58)
    img = ImageEnhance.Contrast(img).enhance(1.1)
    warmth = Image.new("RGB", img.size, (174, 102, 60))
    return Image.blend(img, warmth, 0.12)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with Image.open(SRC) as raw:
        img = ImageOps.exif_transpose(raw).convert("RGB")
        cropped = crop_cover(img, SIZE, FOCAL)
        polished = about_hero_grade(cropped)
        polished.save(OUT_FILE, "JPEG", quality=90, optimize=True)
        print("wrote", OUT_FILE.relative_to(ROOT))


if __name__ == "__main__":
    main()
