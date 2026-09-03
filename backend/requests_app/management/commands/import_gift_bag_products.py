import json
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from requests_app.models import Category, Product

CATEGORY_NAME = "Подарочные пакеты"
DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "gift_bags"
JSON_PATH = Path(__file__).resolve().parents[3] / "scripts" / "bison_gift_bags.json"

DEFAULT_DIMENSIONS = {
    "gift_bag_01.png": (27, 15, 31),
    "gift_bag_02.png": (24, 9, 28),
    "gift_bag_03.png": (32, 24, 12),
    "gift_bag_04.png": (20, 15, 25),
    "gift_bag_05.png": (30, 12, 35),
    "gift_bag_06.png": (37, 32, 20),
    "gift_bag_07.png": (23, 35, 10),
    "gift_bag_08.png": (23, 35, 10),
}


class Command(BaseCommand):
    help = "Import gift bag products scraped from bison-media.ru"

    def add_arguments(self, parser):
        parser.add_argument(
            "--json",
            type=str,
            default=str(JSON_PATH),
            help="Path to bison_gift_bags.json",
        )

    def handle(self, *args, **options):
        json_path = Path(options["json"])
        if not json_path.is_file():
            self.stderr.write(f"JSON not found: {json_path}")
            self.stderr.write("Run: python scripts/scrape_bison_gift_bags.py")
            return

        if not DATA_DIR.is_dir():
            self.stderr.write(f"Images directory not found: {DATA_DIR}")
            return

        items = json.loads(json_path.read_text(encoding="utf-8"))
        category, _ = Category.objects.get_or_create(
            name=CATEGORY_NAME,
            defaults={
                "description": "Подарочные пакеты из крафта и ламинированной бумаги с печатью логотипа.",
                "is_active": True,
            },
        )
        category.description = "Подарочные пакеты из крафта и ламинированной бумаги с печатью логотипа."
        category.is_active = True
        category.save()

        deleted_count, _ = Product.objects.filter(category=category).delete()
        self.stdout.write(f"Deleted {deleted_count} old products in category")

        created = 0
        for item in sorted(items, key=lambda row: row["sort"], reverse=True):
            image_name = item["image_file"]
            image_path = DATA_DIR / image_name
            if not image_path.is_file():
                self.stderr.write(f"Missing image: {image_path}")
                continue

            dims = item.get("dimensions")
            if dims:
                depth, width, height = dims["depth"], dims["width"], dims["height"]
            else:
                depth, width, height = DEFAULT_DIMENSIONS.get(image_name, (30, 20, 30))

            product = Product(
                name=item["floks_name"],
                description=item["floks_description"],
                category=category,
                depth=depth,
                width=width,
                height=height,
                is_active=True,
            )
            product.save()

            with image_path.open("rb") as image_file:
                product.image.save(image_name, File(image_file), save=True)

            created += 1
            self.stdout.write(f"Created: {product.name} (id={product.id})")

        self.stdout.write(self.style.SUCCESS(f"Done: created={created}, category={category.name}"))
