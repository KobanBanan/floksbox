import json
import re
import urllib.request
from decimal import Decimal
from io import BytesIO
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from requests_app.models import Category, Product

CATEGORY_NAME = "Четырехклапанные коробки"
DEFAULT_JSON = (
    Path(__file__).resolve().parents[3] / "scripts" / "pack24_four_flap.json"
)


def build_description(item: dict) -> str:
    d, w, h = item["depth"], item["width"], item["height"]
    material = item.get("material") or "гофрокартон"
    text = (
        f"Четырехклапанный гофрокороб {d}×{w}×{h} см (Д×Ш×В). "
        f"Материал: {material}. "
        "Универсальная транспортная и складская упаковка: четыре верхних и четыре нижних "
        "клапана фиксируются лентой, скобами или клеем. "
        "Подходит для пищевой, промышленной, фармацевтической и торговой отраслей."
    )
    words = text.split()
    return " ".join(words[:200])


def download_image(url: str) -> ContentFile | None:
    if not url:
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        ext = "jpg"
        m = re.search(r"\.(jpe?g|png|webp)", url, re.I)
        if m:
            ext = m.group(1).lower().replace("jpeg", "jpg")
        return ContentFile(data, name=f"import.{ext}")
    except Exception:
        return None


class Command(BaseCommand):
    help = "Import four-flap box products from pack24 JSON scrape"

    def add_arguments(self, parser):
        parser.add_argument(
            "--json",
            type=str,
            default=str(DEFAULT_JSON),
            help="Path to pack24_four_flap.json",
        )
        parser.add_argument(
            "--replace",
            action="store_true",
            help="Deactivate existing products in category before import",
        )

    def handle(self, *args, **options):
        json_path = Path(options["json"])
        if not json_path.is_file():
            self.stderr.write(f"File not found: {json_path}")
            return

        items = json.loads(json_path.read_text(encoding="utf-8"))
        category, _ = Category.objects.get_or_create(
            name=CATEGORY_NAME,
            defaults={
                "description": "Четырехклапанные гофрокороба стандартных и индивидуальных размеров.",
                "is_active": True,
            },
        )
        category.is_active = True
        category.save()

        if options["replace"]:
            updated = Product.objects.filter(category=category).update(is_active=False)
            self.stdout.write(f"Deactivated {updated} old products in category")

        created = 0
        updated_count = 0
        skipped = 0

        for item in items:
            name = f"Гофрокороб {item['depth']:.0f}×{item['width']:.0f}×{item['height']:.0f} см"
            description = build_description(item)
            price = item.get("price")
            price_val = Decimal(str(price)) if price else None

            product = Product.objects.filter(
                category=category,
                height=item["height"],
                width=item["width"],
                depth=item["depth"],
            ).first()

            img_url = item.get("image_url")

            is_new = product is None
            if is_new:
                product = Product(category=category)

            product.name = name
            product.description = description
            product.height = item["height"]
            product.width = item["width"]
            product.depth = item["depth"]
            product.price = price_val
            product.is_active = True
            product.category = category
            product.save()

            if is_new or options["replace"]:
                image_file = download_image(img_url)
                if image_file:
                    product.image.save(image_file.name, image_file, save=True)

                unfold_url = item.get("unfold_image_url")
                unfold_file = download_image(unfold_url)
                if unfold_file:
                    product.image_unfold.save(unfold_file.name, unfold_file, save=True)
                elif product.image_unfold:
                    product.image_unfold.delete(save=False)

            if is_new:
                created += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done: created={created}, updated={updated_count}, skipped={skipped}, "
                f"category={category.name}"
            )
        )
