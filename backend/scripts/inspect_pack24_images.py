"""Inspect image candidates on pack24 product pages."""
import json
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
BASE = "https://pack24.ru"

SAMPLES = [
    "gofrokorob-650350100-mm",
    "gofrokorob-600400200-mm",
    "gofrokorob-580-480120-mm",
    "gofrokorob-420210180-mm",
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def main() -> None:
    for slug in SAMPLES:
        url = f"{BASE}/kartonnye-korobki/chetyrehklapannye-koroba/{slug}"
        html = fetch(url)
        print("\n===", slug, "===")
        for tag in ("og:image", "itemprop=\"image\"", "product", "gallery", "swiper"):
            if tag in html.lower():
                pass
        for pat in [
            r'property="og:image"\s+content="([^"]+)"',
            r'itemprop="image"[^>]+content="([^"]+)"',
            r'data-zoom-image="([^"]+)"',
            r'class="[^"]*product[^"]*"[^>]*>[\s\S]{0,500}?src="([^"]+)"',
        ]:
            m = re.search(pat, html, re.I)
            if m:
                print(" ", pat[:40], "->", m.group(1)[-80:])

        for m in re.finditer(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S
        ):
            try:
                data = json.loads(m.group(1))
            except json.JSONDecodeError:
                continue
            if isinstance(data, dict) and data.get("@type") == "Product":
                print("  ld image:", data.get("image"))
                imgs = data.get("image")
                if isinstance(imgs, list):
                    print("  ld images:", imgs)
                break


if __name__ == "__main__":
    main()
