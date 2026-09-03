import json
import re
import urllib.request

url = "https://pack24.ru/kartonnye-korobki/chetyrehklapannye-koroba"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

product_links = []
for m in re.finditer(
    r"https://pack24\.ru/kartonnye-korobki/chetyrehklapannye-koroba/gofrokorob-[^\"'#?\s]+",
    html,
):
    u = m.group(0).split("#")[0]
    if u not in product_links:
        product_links.append(u)

print("product urls", len(product_links))
print("first 5", product_links[:5])

# json-ld
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
    try:
        data = json.loads(m.group(1))
        if isinstance(data, dict) and data.get("@type") == "ItemList":
            print("ItemList", len(data.get("itemListElement", [])))
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("@type") in ("Product", "ItemList"):
                    print("found", item.get("@type"), str(item)[:200])
    except json.JSONDecodeError:
        pass

# sample product page
if product_links:
    u = product_links[0]
    h = urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60
    ).read().decode("utf-8", "replace")
    print("product page size", len(h))
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            data = json.loads(m.group(1))
            print("ld+json:", json.dumps(data, ensure_ascii=False)[:500])
        except json.JSONDecodeError:
            pass
    print("h1", re.search(r"<h1[^>]*>([^<]+)", h))
