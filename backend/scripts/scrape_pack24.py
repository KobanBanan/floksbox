"""Scrape and curate four-flap boxes from pack24.ru."""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

BASE = "https://pack24.ru"
LIST_URL = f"{BASE}/kartonnye-korobki/chetyrehklapannye-koroba"
UA = {"User-Agent": "Mozilla/5.0 (compatible; FloksboxImport/1.0)"}
PRODUCT_URL_RE = re.compile(
    r"https://pack24\.ru/kartonnye-korobki/chetyrehklapannye-koroba/gofrokorob-[^\"'#?\s]+"
)
SIZE_RE = re.compile(r"(\d+)\*(\d+)\*(\d+)")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def collect_product_urls() -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for page in range(1, 6):
        list_url = LIST_URL if page == 1 else f"{LIST_URL}?PAGEN_1={page}"
        try:
            html = fetch(list_url)
        except Exception:
            break
        found = 0
        for m in PRODUCT_URL_RE.finditer(html):
            u = m.group(0).split("#")[0]
            if u not in seen:
                seen.add(u)
                urls.append(u)
                found += 1
        print(f"page {page}: +{found} (total {len(urls)})")
        if found == 0:
            break
        time.sleep(0.3)
    return urls


def parse_ld_product(html: str) -> dict | None:
    for m in re.finditer(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.S
    ):
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "Product":
            return data
    return None


def parse_dimensions(ld: dict) -> tuple[float, float, float] | None:
    for field in (ld.get("size"), ld.get("name"), ld.get("description")):
        if not field:
            continue
        m = SIZE_RE.search(str(field))
        if m:
            d, w, h = (int(x) / 10 for x in m.groups())
            return round(d, 2), round(w, 2), round(h, 2)
    return None


def normalize_url(path: str) -> str:
    if path.startswith("http"):
        return path.split("||")[0].split("|")[0]
    if path.startswith("//"):
        return "https:" + path
    if path.startswith("/"):
        return BASE + path
    return BASE + "/" + path.lstrip("/")


GENERIC_IMAGE_MARKERS = (
    "4h_klapannye-korobki",
    "dlinnaya-korobka",
    "korobka-300-200",
    "200-200-200-ko",
)


JUNK_URL_MARKERS = (
    "gofrokarton-t-",
    "/catalog/karton/gofrokarton",
    "air_bubble",
    "puzyr",
    "puzyrkovaya",
    "||",
)


def is_unfold_url(url: str | None) -> bool:
    if not url:
        return False
    u = url.lower()
    return "/size/4x-kl" in u or bool(re.search(r"4x-kl-\d+x\d+x\d+", u))


def is_junk_url(url: str | None) -> bool:
    if not url:
        return True
    u = url.lower()
    return any(m in u for m in JUNK_URL_MARKERS)


def is_product_photo_url(url: str | None) -> bool:
    if not url or is_unfold_url(url) or is_junk_url(url):
        return False
    return not any(m in url.lower() for m in GENERIC_IMAGE_MARKERS)


def size_matches_filename(url: str, depth: float, width: float, height: float) -> bool:
    d_mm, w_mm, h_mm = (
        int(round(depth * 10)),
        int(round(width * 10)),
        int(round(height * 10)),
    )
    u = url.lower()
    parts = (
        f"{d_mm}-{w_mm}-{h_mm}",
        f"{d_mm}*{w_mm}*{h_mm}",
        f"{int(depth)}-{int(width)}-{int(height)}",
        f"{d_mm}x{w_mm}x{h_mm}",
    )
    return any(p in u for p in parts)


def image_exists(url: str) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers=UA)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception:
        return False


def _dedupe(urls: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def pick_gallery_photo(html: str) -> str | None:
    for pattern in (
        r'product-detail[\s\S]{0,14000}?src="(https://pack24\.ru/storage/thumbs/[^"]+\.webp)"',
        r'product-images[\s\S]{0,14000}?src="(https://pack24\.ru/storage/thumbs/[^"]+\.webp)"',
        r'class="[^"]*swiper[^"]*"[\s\S]{0,8000}?src="(https://pack24\.ru/storage/thumbs/[^"]+\.webp)"',
    ):
        m = re.search(pattern, html, re.I)
        if m:
            return normalize_url(m.group(1))
    return None


def pick_images(
    html: str, depth: float, width: float, height: float, ld: dict
) -> tuple[str | None, str | None]:
    """Фото товара (главное) и развертка 4x-kl (доп.)."""
    d_mm, w_mm, h_mm = (
        int(round(depth * 10)),
        int(round(width * 10)),
        int(round(height * 10)),
    )
    photos: list[str] = []
    unfolds: list[str] = []

    ld_images = ld.get("image")
    if isinstance(ld_images, str):
        ld_images = [ld_images]
    elif not isinstance(ld_images, list):
        ld_images = []
    for raw in ld_images:
        u = normalize_url(str(raw))
        if is_unfold_url(u):
            unfolds.append(u)
        elif not is_junk_url(u):
            photos.append(u)

    gallery = pick_gallery_photo(html)
    if gallery:
        photos.append(gallery)

    for m in re.finditer(
        r'(?:src|data-src|href|content)="([^"]*kartonnye-korobki[^"]+\.(?:jpg|jpeg|png|webp))"',
        html,
        re.I,
    ):
        u = normalize_url(m.group(1))
        if is_unfold_url(u):
            unfolds.append(u)
        elif not is_junk_url(u):
            photos.append(u)

    for m in re.finditer(
        r"/assets/images/catalog/kartonnye-korobki/size/4x-kl[^\"'\s>]+\.(?:jpg|jpeg|png|webp)",
        html,
        re.I,
    ):
        unfolds.append(normalize_url(m.group(0)))

    unfold_built = normalize_url(
        f"/assets/images/catalog/kartonnye-korobki/size/4x-kl-{d_mm}x{w_mm}x{h_mm}.jpg"
    )
    if image_exists(unfold_built):
        unfolds.append(unfold_built)

    photos = _dedupe(photos)
    unfolds = _dedupe(unfolds)

    def photo_rank(u: str) -> tuple:
        return (
            not size_matches_filename(u, depth, width, height),
            "/storage/thumbs/" in u.lower(),
            "korobka-" in u.lower() and not size_matches_filename(u, depth, width, height),
            not is_product_photo_url(u),
            u,
        )

    photo: str | None = None
    for u in sorted(photos, key=photo_rank):
        if is_unfold_url(u):
            continue
        photo = u
        break
    if not photo and photos:
        photo = photos[0]

    unfold: str | None = None
    for u in unfolds:
        if size_matches_filename(u, depth, width, height):
            unfold = u
            break
    if not unfold and unfolds:
        unfold = unfolds[0]

    if photo and is_unfold_url(photo):
        photo = None
    return photo, unfold


def shape_type(depth: float, width: float, height: float) -> str:
    """Д×Ш×В: высота — третье измерение (вертикаль коробки)."""
    base = max(depth, width)
    small = min(depth, width)
    if height >= base * 1.35 and height >= small * 1.5:
        return "tall"
    if height <= base * 0.45:
        return "flat"
    if (
        abs(depth - width) / max(depth, width, 0.1) < 0.18
        and abs(depth - height) / max(depth, height, 0.1) < 0.22
        and abs(width - height) / max(width, height, 0.1) < 0.22
    ):
        return "square"
    return "standard"


def size_signature(depth: float, width: float, height: float) -> str:
    """Exact size in mm (Д×Ш×В)."""
    return f"{int(round(depth * 10))}x{int(round(width * 10))}x{int(round(height * 10))}"


def scrape_product(url: str) -> dict | None:
    html = fetch(url)
    ld = parse_ld_product(html)
    if not ld:
        return None

    dims = parse_dimensions(ld)
    if not dims:
        return None
    depth, width, height = dims

    image_url, unfold_image_url = pick_images(html, depth, width, height, ld)
    if not image_url:
        return None

    return {
        "source_url": url,
        "name": f"Гофрокороб {depth:.0f}×{width:.0f}×{height:.0f} см",
        "description": (
            f"Четырехклапанный гофрокороб {depth}×{width}×{height} см (Д×Ш×В). "
            f"Материал: {ld.get('material') or 'гофрокартон'}. "
            "Универсальная транспортная упаковка."
        ),
        "depth": depth,
        "width": width,
        "height": height,
        "price": None,
        "image_url": image_url,
        "unfold_image_url": unfold_image_url,
        "material": ld.get("material"),
        "sku": ld.get("sku"),
        "shape": shape_type(depth, width, height),
        "size_sig": size_signature(depth, width, height),
    }


def item_rank(item: dict) -> tuple:
    img = item.get("image_url") or ""
    specific = is_product_photo_url(img) and size_matches_filename(
        img, item["depth"], item["width"], item["height"]
    )
    generic = not specific
    return (generic, generic and img in {"", None}, -specific, item["source_url"])


def curate_products(items: list[dict], max_per_size: int = 2) -> list[dict]:
    """Не больше max_per_size на один размер; уникальные картинки; разнообразие форм."""
    by_size: dict[str, list[dict]] = {}
    for item in items:
        by_size.setdefault(item["size_sig"], []).append(item)

    selected: list[dict] = []

    def can_take(item: dict, picked_for_size: int) -> bool:
        if picked_for_size >= max_per_size:
            return False
        if not item.get("image_url"):
            return False
        return True

    for sig in sorted(by_size.keys()):
        group = sorted(by_size[sig], key=item_rank)
        picked = 0
        for item in group:
            if not can_take(item, picked):
                continue
            selected.append(item)
            picked += 1

    caps = {"flat": 14, "tall": 14, "square": 12, "standard": 10}
    by_shape: dict[str, list[dict]] = {k: [] for k in caps}
    for item in items:
        by_shape[item["shape"]].append(item)

    final_keys = {(i["size_sig"], i["source_url"]) for i in selected}

    for shape in ("flat", "tall", "square", "standard"):
        have = sum(1 for i in selected if i["shape"] == shape)
        target = caps[shape]
        if have >= target:
            continue
        pool = sorted(by_shape[shape], key=item_rank)
        for item in pool:
            if have >= target:
                break
            key = (item["size_sig"], item["source_url"])
            if key in final_keys:
                continue
            count_sig = sum(1 for i in selected if i["size_sig"] == item["size_sig"])
            if count_sig >= max_per_size:
                continue
            if not can_take(item, count_sig):
                continue
            selected.append(item)
            final_keys.add(key)
            have += 1

    trimmed: list[dict] = []
    shape_count: dict[str, int] = {k: 0 for k in caps}
    for item in sorted(selected, key=item_rank):
        shape = item["shape"]
        if shape_count[shape] >= caps[shape]:
            continue
        trimmed.append(item)
        shape_count[shape] += 1

    trimmed.sort(key=lambda x: (x["shape"], x["depth"], x["width"], x["height"]))
    return trimmed


def scrape_all() -> list[dict]:
    urls = collect_product_urls()
    print(f"scraping {len(urls)} urls...")
    items: list[dict] = []
    for i, url in enumerate(urls):
        try:
            item = scrape_product(url)
            if item:
                items.append(item)
        except Exception as e:
            print(f"  fail {url}: {e}")
        if (i + 1) % 15 == 0:
            print(f"  progress {i + 1}/{len(urls)}")
        time.sleep(0.3)

    print(f"scraped {len(items)}")
    unique_imgs = len({i.get("image_url") for i in items if i.get("image_url")})
    print(f"unique image urls: {unique_imgs}")
    shapes = {}
    for i in items:
        shapes[i["shape"]] = shapes.get(i["shape"], 0) + 1
    print("all shapes:", shapes)

    curated = curate_products(items, max_per_size=2)
    print(f"curated {len(curated)}")
    unique_imgs2 = len({i.get("image_url") for i in curated if i.get("image_url")})
    print(f"curated unique images: {unique_imgs2}")
    shapes2 = {}
    for i in curated:
        shapes2[i["shape"]] = shapes2.get(i["shape"], 0) + 1
    print("curated shapes:", shapes2)
    return curated


if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "pack24_four_flap.json"
    data = scrape_all()
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"saved -> {out}")
