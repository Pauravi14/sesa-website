"""Crop full-bleed hero slideshow images (16:9 widescreen)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps

from prepare_service_thumbs import crop_cover, unified_grade

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "hero"

SPECS = [
    ("hero-inspection.png", "slide-1.jpg", (0.45, 0.38)),
    ("damage-detail.png", "slide-2.jpg", (0.52, 0.42)),
    ("source/wohnmobile-source.jpg", "slide-3.jpg", (0.5, 0.45)),
    ("source/oldtimer-source.jpg", "slide-4.jpg", (0.5, 0.4)),
    ("workshop-tools.png", "slide-5.jpg", (0.48, 0.55)),
]

SIZE = (1920, 1080)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, out_name, focal in SPECS:
        src = ROOT / "assets" / src_name
        if not src.exists():
            raise FileNotFoundError(f"Missing source image: {src}")
        out = OUT / out_name
        with Image.open(src) as raw:
            img = ImageOps.exif_transpose(raw).convert("RGB")
            cropped = crop_cover(img, SIZE, focal)
            polished = unified_grade(cropped)
            polished.save(out, "JPEG", quality=90, optimize=True)
            print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
