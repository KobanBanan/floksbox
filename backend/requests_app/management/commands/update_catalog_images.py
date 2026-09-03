from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from requests_app.models import Category, Product

GIFT_BAG_CATEGORY = "Подарочные пакеты"
FOUR_FLAP_CATEGORY = "Четырехклапанные коробки"
FLEXO_CATEGORY = "Гофроупаковка с флексопечатью"
LAMINATED_CATEGORY = "Кашированные гофроупаковка"

DATA = Path(__file__).resolve().parents[3] / "data"

GIFT_BAG_NAMES = [
    "Крафт-пакет с бумажными шнурами",
    "Ламинированный пакет с бумажными шнурами",
    "Пакет на лентах",
    "Крафт-мешок на затяжке",
    "Ламинированный пакет с полноцветной печатью",
    "Крафт-пакет с тиснением",
    "Крафт-пакет с крафтовыми ручками",
    "Белый пакет с крафтовыми ручками",
]

QUADPACK_NAMES = [
    "Бурые четырехклапанные короба",
    "Четырехклапанные короба из гофрокартона с ручками",
    "Белые короба из гофрокартона",
    "Четырехклапанные короба из гофрокартона с вентиляционными отверстиями",
    "Четырехклапанные короба из гофрокартона-тубусы",
    "Четырехклапанные короба с нанесением флексопечати",
    "Четырехклапанные короба с нанесением офсетной печати",
]

QUADPACK_OFFSET_PRODUCT = {
    "name": "Четырехклапанные короба с нанесением офсетной печати",
    "description": (
        "Четырехклапанные короба с нанесением офсетной печати — решение для упаковки, "
        "где важны высокое качество отпечатка, насыщенные цвета и детальная графика. "
        "Офсетная печать позволяет воспроизводить сложные иллюстрации, градиенты и мелкие "
        "элементы фирменного стиля на поверхности гофрокартона.\n"
        "Такие короба подходят для премиальной и подарочной упаковки, retail-продукции, "
        "промо-наборов и товаров, где упаковка является частью бренда."
    ),
    "image": "quadpack_07.png",
}

LAMINATED_PRODUCT = {
    "name": "Кашированная гофроупаковка с офсетной печатью",
    "description": (
        "Кашированная гофроупаковка с нанесением офсетной печати. Премиальный внешний вид "
        "сочетается с прочностью гофрокартона — подходит для брендированной упаковки "
        "премиальных товаров, подарков и retail."
    ),
    "image": "laminated_01.png",
}

OFFSET_PRINTING_PRODUCT = {
    "name": "Нанесение Офсетной печати",
    "image": "quadpack_07.png",
    "image_unfold": "offset_unfold.png",
}

FLEXO_PRODUCT = {
    "name": "Гофрокороб с флексопечатью",
    "description": (
        "Четырехклапанный гофрокороб с нанесением флексопечати. Подходит для брендирования "
        "упаковки логотипом, иллюстрациями и маркировкой. Флексография обеспечивает чёткий "
        "отпечаток на гофрокартоне и экономична в больших тиражах.\n"
        "Используется в розничной торговле, пищевой отрасли, e-commerce и для подарочной упаковки."
    ),
    "image": "flexo_01.png",
}


def set_product_image(product: Product, image_path: Path, field: str = "image") -> None:
    with image_path.open("rb") as fh:
        getattr(product, field).save(image_path.name, File(fh), save=True)


class Command(BaseCommand):
    help = "Update catalog images from data/gift_bags, data/quadpack, data/flexo"

    def handle(self, *args, **options):
        self._update_gift_bags()
        self._update_quadpack()
        self._update_laminated_product()
        self._update_offset_printing_product()
        self._update_flexo_product()
        self._set_brown_box_unfold()
        self._set_quadpack_offset_unfold()
        self.stdout.write(self.style.SUCCESS("Catalog images updated"))

    def _update_gift_bags(self):
        category = Category.objects.filter(name=GIFT_BAG_CATEGORY).first()
        if not category:
            self.stderr.write(f"Category not found: {GIFT_BAG_CATEGORY}")
            return
        for index, name in enumerate(GIFT_BAG_NAMES, start=1):
            product = Product.objects.filter(category=category, name=name).first()
            image_path = DATA / "gift_bags" / f"gift_bag_{index:02d}.png"
            if not product:
                self.stderr.write(f"Gift bag product not found: {name}")
                continue
            if not image_path.is_file():
                self.stderr.write(f"Missing image: {image_path}")
                continue
            set_product_image(product, image_path)
            self.stdout.write(f"Updated gift bag: {name}")

    def _update_quadpack(self):
        category = Category.objects.filter(name=FOUR_FLAP_CATEGORY).first()
        if not category:
            self.stderr.write(f"Category not found: {FOUR_FLAP_CATEGORY}")
            return
        for index, name in enumerate(QUADPACK_NAMES, start=1):
            product = Product.objects.filter(category=category, name=name).first()
            image_path = DATA / "quadpack" / f"quadpack_{index:02d}.png"
            if not product and name == QUADPACK_OFFSET_PRODUCT["name"]:
                product = Product(
                    name=QUADPACK_OFFSET_PRODUCT["name"],
                    description=QUADPACK_OFFSET_PRODUCT["description"],
                    category=category,
                    height=30,
                    width=20,
                    depth=15,
                    is_active=True,
                )
                product.save()
            if not product:
                self.stderr.write(f"Quadpack product not found: {name}")
                continue
            if not image_path.is_file():
                self.stderr.write(f"Missing image: {image_path}")
                continue
            set_product_image(product, image_path)
            self.stdout.write(f"Updated quadpack: {name}")

    def _update_laminated_product(self):
        category = Category.objects.filter(name=LAMINATED_CATEGORY).first()
        if not category:
            self.stderr.write(f"Category not found: {LAMINATED_CATEGORY}")
            return

        image_path = DATA / "laminated" / LAMINATED_PRODUCT["image"]
        if not image_path.is_file():
            self.stderr.write(f"Missing laminated image: {image_path}")
            return

        product = Product.objects.filter(category=category, name=LAMINATED_PRODUCT["name"]).first()
        if not product:
            product = Product(
                name=LAMINATED_PRODUCT["name"],
                description=LAMINATED_PRODUCT["description"],
                category=category,
                height=30,
                width=20,
                depth=15,
                is_active=True,
            )
            product.save()

        set_product_image(product, image_path)
        self.stdout.write(f"Laminated product ready: {product.name} (id={product.id})")

    def _update_offset_printing_product(self):
        category = Category.objects.filter(name=FLEXO_CATEGORY).first()
        if not category:
            self.stderr.write(f"Category not found: {FLEXO_CATEGORY}")
            return

        main_path = DATA / "quadpack" / OFFSET_PRINTING_PRODUCT["image"]
        unfold_path = DATA / "flexo" / OFFSET_PRINTING_PRODUCT["image_unfold"]
        if not main_path.is_file():
            self.stderr.write(f"Missing offset main image: {main_path}")
            return
        if not unfold_path.is_file():
            self.stderr.write(f"Missing offset unfold image: {unfold_path}")
            return

        product = Product.objects.filter(category=category, name=OFFSET_PRINTING_PRODUCT["name"]).first()
        if not product:
            self.stderr.write(f"Offset printing product not found: {OFFSET_PRINTING_PRODUCT['name']}")
            return

        set_product_image(product, main_path)
        set_product_image(product, unfold_path, field="image_unfold")
        self.stdout.write(f"Offset printing product updated: {product.name} (id={product.id})")

    def _update_flexo_product(self):
        category, _ = Category.objects.get_or_create(
            name=FLEXO_CATEGORY,
            defaults={
                "description": "Гофроупаковка с качественной флексопечатью для больших тиражей.",
                "is_active": True,
            },
        )
        category.is_active = True
        category.save()

        image_path = DATA / "flexo" / FLEXO_PRODUCT["image"]
        if not image_path.is_file():
            self.stderr.write(f"Missing flexo image: {image_path}")
            return

        product = Product.objects.filter(category=category, name=FLEXO_PRODUCT["name"]).first()
        if not product:
            product = Product(
                name=FLEXO_PRODUCT["name"],
                description=FLEXO_PRODUCT["description"],
                category=category,
                height=30,
                width=20,
                depth=15,
                is_active=True,
            )
            product.save()

        set_product_image(product, image_path)
        self.stdout.write(f"Flexo product ready: {product.name} (id={product.id})")

    def _set_brown_box_unfold(self):
        category = Category.objects.filter(name=FOUR_FLAP_CATEGORY).first()
        if not category:
            return
        product = Product.objects.filter(category=category, name="Бурые четырехклапанные короба").first()
        image_path = DATA / "quadpack" / "pr2_unfold.png"
        if not product:
            self.stderr.write("Brown box product not found")
            return
        if not image_path.is_file():
            self.stderr.write(f"Missing unfold image: {image_path}")
            return
        set_product_image(product, image_path, field="image_unfold")
        self.stdout.write("Set carousel image for brown four-flap box")

    def _set_quadpack_offset_unfold(self):
        category = Category.objects.filter(name=FOUR_FLAP_CATEGORY).first()
        if not category:
            return
        product = Product.objects.filter(
            category=category,
            name=QUADPACK_OFFSET_PRODUCT["name"],
        ).first()
        image_path = DATA / "flexo" / "offset_unfold.png"
        if not product:
            self.stderr.write("Quadpack offset product not found")
            return
        if not image_path.is_file():
            self.stderr.write(f"Missing offset unfold image: {image_path}")
            return
        set_product_image(product, image_path, field="image_unfold")
        self.stdout.write("Set carousel image for quadpack offset box")
