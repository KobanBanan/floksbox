"""Scrape curated gift bag products from bison-media.ru."""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

BASE = "https://bison-media.ru"
UA = {"User-Agent": "Mozilla/5.0 (compatible; FloksboxImport/1.0)"}
OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "gift_bags"
JSON_OUT = Path(__file__).resolve().parent / "bison_gift_bags.json"

PRODUCTS = [
    {
        "sort": 1,
        "slug": "paket-bumazhnyi-kraft-m-neokrashennyi-gi-1155-00",
        "floks_name": "Крафт-пакет с бумажными шнурами",
        "floks_description": (
            "Классический подарочный пакет из крафт-бумаги с двумя витыми бумажными ручками. "
            "Натуральный оттенок, плотность от 120 г/м², усиленное дно. Подходит для эко-брендов, "
            "кафе, магазинов и корпоративных подарков.\n"
            "Нанесение: шелкография, трафаретная печать, шелкотрансфер, тиснение.\n"
            "Размер M — универсальный для одежды, косметики и наборов среднего объёма."
        ),
        "image_file": "gift_bag_01.png",
    },
    {
        "sort": 2,
        "slug": "paket-bumazhnyi-lami-s-belyi-gi-18433-60",
        "floks_name": "Ламинированный пакет с бумажными шнурами",
        "floks_description": (
            "Пакет из мелованной бумаги с матовой ламинацией и бумажными ручками. "
            "Ровная белая или цветная поверхность, плотность до 200 г/м². Аккуратный вид "
            "для бутиков и премиальной розницы.\n"
            "Нанесение: шелкография, шелкотрансфер, тиснение.\n"
            "Размер S — для небольших подарков, косметики и сувениров."
        ),
        "image_file": "gift_bag_02.png",
    },
    {
        "sort": 3,
        "slug": "paket-bumazhnyi-manilla-m-chernyi-gi-16948-30",
        "floks_name": "Пакет на лентах",
        "floks_description": (
            "Подарочный пакет из плотной дизайнерской бумаги с ручками-лентами из полиэстера. "
            "Премиальный вид, высокая грузоподъёмность — до 3 кг. Подходит для брендированных "
            "подарков, VIP-клиентов и корпоративных наборов.\n"
            "Нанесение: шелкография, тиснение.\n"
            "Размер M."
        ),
        "image_file": "gift_bag_03.png",
    },
    {
        "sort": 4,
        "slug": "meshochek-podarochnyi-kolorit-s-polnotsvetnoi-pechatyu-razmer-m-ar-300224-l-2030",
        "floks_name": "Крафт-мешок на затяжке",
        "floks_description": (
            "Подарочный мешочек с затяжкой-кулиской. Компактная упаковка для украшений, "
            "сладостей, мелких сувениров и промо-наборов. Доступен в крафтовом исполнении "
            "под заказ.\n"
            "Нанесение: DTF, УФ-печать, полноцвет — логотип и графика в любых цветах.\n"
            "Размер M."
        ),
        "image_file": "gift_bag_04.png",
    },
    {
        "sort": 5,
        "slug": "paket-bumazhnyi-lami-tote-m-belyi-gi-18438-60",
        "floks_name": "Ламинированный пакет с полноцветной печатью",
        "floks_description": (
            "Пакет из ламинированной бумаги с ровной поверхностью для сложной печати. "
            "Две бумажные ручки, усиленное дно. Оптимален для яркого брендинга: фотографии, "
            "градиенты, многоцветные логотипы.\n"
            "Нанесение: DTF, УФ-печать, полноцвет, шелкотрансфер.\n"
            "Размер M."
        ),
        "image_file": "gift_bag_05.png",
    },
    {
        "sort": 6,
        "slug": "paket-bumazhnyi-kraft-l-neokrashennyi-gi-1156-00",
        "floks_name": "Крафт-пакет с тиснением",
        "floks_description": (
            "Крупный крафт-пакет с бумажными шнурами для объёмных подарков. Повышенная плотность "
            "бумаги, усиленное дно. Акцент на премиальную отделку: тиснение логотипа, шелкография.\n"
            "Размер L — для одежды, наборов и крупных подарков."
        ),
        "image_file": "gift_bag_06.png",
    },
    {
        "sort": 7,
        "slug": "paket-bumazhnyi-plat-m-kraft-gi-20966-00",
        "floks_name": "Крафт-пакет с крафтовыми ручками",
        "floks_description": (
            "Подарочный пакет из крафт-бумаги с плоскими ручками из крафта. Плотная бумага, "
            "усиленное дно, классический натуральный оттенок. Ручки из той же крафт-бумаги "
            "надежно крепятся к корпусу и выдерживают повседневную нагрузку.\n"
            "Нанесение: шелкография, трафаретная печать, тиснение, шелкотрансфер.\n"
            "Размер M — универсальный для подарков среднего объёма."
        ),
        "image_file": "gift_bag_07.png",
    },
    {
        "sort": 8,
        "slug": "paket-bumazhnyi-kraft-m-belyi-gi-1155-60",
        "floks_name": "Белый пакет с крафтовыми ручками",
        "floks_description": (
            "Светлый подарочный пакет с контрастными плоскими ручками из крафт-бумаги. "
            "Сочетание белого корпуса и натуральных крафтовых ручек выглядит аккуратно "
            "и подходит для бутиков, косметики и брендированных наборов.\n"
            "Нанесение: шелкография, DTF, полноцвет, шелкотрансфер.\n"
            "Размер M."
        ),
        "image_file": "gift_bag_08.png",
    },
]

DIM_RE = re.compile(r"(\d+)\s*[xх×]\s*(\d+)\s*[xх×]\s*(\d+)", re.I)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_ld_product(html: str) -> dict | None:
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "Product":
            return data
    return None


PRODUCT_IMG_RE = re.compile(
    r'/(product\d+x\d+[^/]*)/i/(product|photo)/([^"\s]+\.(?:jpg|jpeg|png|webp))',
    re.I,
)


def parse_product_image(html: str) -> str | None:
    m = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html, re.I)
    if m:
        return normalize_image_url(m.group(1))

    best = None
    best_size = 0
    for m in PRODUCT_IMG_RE.finditer(html):
        folder, subfolder, filename = m.group(1), m.group(2), m.group(3)
        size_m = re.search(r"product(\d+)x(\d+)", folder, re.I)
        size = int(size_m.group(1)) if size_m else 0
        if size > 1024:
            continue
        if size >= best_size:
            best_size = size
            best = f"{BASE}/{folder}/i/{subfolder}/{filename}"
    return best


def parse_gabarites(html: str) -> str | None:
    m = re.search(r"Габариты:\s*</[^>]+>\s*([^<\n]+)", html, re.I)
    if m:
        return m.group(1).strip()
    m = DIM_RE.search(html)
    if m:
        return f"{m.group(1)}x{m.group(2)}x{m.group(3)} см"
    return None


def normalize_image_url(url: str) -> str:
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return BASE + url
    return url


def download_image(url: str, dest: Path) -> None:
    candidates = [url]
    if "product1024x1024" in url:
        candidates.append(url.replace("product1024x1024", "product700x700"))
    if "product700x700" not in url:
        m = re.search(r"product\d+x\d+", url)
        if m:
            candidates.append(url.replace(m.group(0), "product700x700"))

    last_error: Exception | None = None
    for candidate in candidates:
        try:
            req = urllib.request.Request(normalize_image_url(candidate), headers=UA)
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            return
        except Exception as exc:
            last_error = exc
    raise last_error or RuntimeError(f"Could not download {url}")


def scrape_item(item: dict) -> dict:
    url = f"{BASE}/product/{item['slug']}/"
    html = fetch(url)
    ld = parse_ld_product(html) or {}
    image = parse_product_image(html)
    if not image:
        raise RuntimeError(f"No image for {url}")

    gabarites = parse_gabarites(html)
    dims = None
    if gabarites:
        m = DIM_RE.search(gabarites.replace("*", "x"))
        if m:
            dims = {
                "depth": float(m.group(1)),
                "width": float(m.group(2)),
                "height": float(m.group(3)),
            }

    return {
        **item,
        "source_url": url,
        "source_name": ld.get("name", ""),
        "image_url": normalize_image_url(str(image)),
        "dimensions_text": gabarites,
        "dimensions": dims,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for item in PRODUCTS:
        print(f"Scraping {item['slug']}...")
        try:
            row = scrape_item(item)
            img_path = OUT_DIR / item["image_file"]
            download_image(row["image_url"], img_path)
            row["local_image"] = str(img_path)
            results.append(row)
            print(f"  OK: {row['image_url'][:80]}...")
        except Exception as exc:
            print(f"  FAIL: {exc}")
        time.sleep(0.4)

    JSON_OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(results)} products to {JSON_OUT}")


if __name__ == "__main__":
    main()
