"""Crop homepage service images to a consistent 16:9 frame with unified grading."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "service"

# All workshop / vehicle scenes for a cohesive look (no landscape road shot).
SPECS = [
    ("damage-detail.png", "service-unfall.jpg", (0.5, 0.45)),
    ("workshop-tools.png", "service-bewertung.jpg", (0.5, 0.5)),
    ("hero-inspection.png", "service-wohnmobile.jpg", (0.55, 0.38)),
    ("damage-detail.png", "service-oldtimer.jpg", (0.32, 0.42)),
]

SIZE = (1280, 720)


def crop_cover(img: Image.Image, size: tuple[int, int], focal: tuple[float, float]) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / img.width, target_h / img.height)
    resized = img.resize(
        (round(img.width * scale), round(img.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = int((resized.width - target_w) * focal[0])
    top = int((resized.height - target_h) * focal[1])
    left = max(0, min(left, resized.width - target_w))
    top = max(0, min(top, resized.height - target_h))
    return resized.crop((left, top, left + target_w, top + target_h))


def unified_grade(img: Image.Image) -> Image.Image:
    """Match contrast, warmth and saturation across all service/hero photos."""
    img = ImageEnhance.Contrast(img).enhance(1.12)
    img = ImageEnhance.Color(img).enhance(0.86)
    img = ImageEnhance.Brightness(img).enhance(0.97)
    warmth = Image.new("RGB", img.size, (201, 137, 88))
    img = Image.blend(img, warmth, 0.09)
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, out_name, focal in SPECS:
        src = ROOT / "assets" / src_name
        out = OUT / out_name
        with Image.open(src) as raw:
            img = ImageOps.exif_transpose(raw).convert("RGB")
            cropped = crop_cover(img, SIZE, focal)
            polished = unified_grade(cropped)
            polished.save(out, "JPEG", quality=90, optimize=True)
            print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
