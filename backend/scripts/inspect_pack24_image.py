import json
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
url = "https://pack24.ru/kartonnye-korobki/chetyrehklapannye-koroba/gofrokorob-100100200-mm"
req = urllib.request.Request(url, headers=UA)
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
    try:
        data = json.loads(m.group(1))
        if isinstance(data, dict) and data.get("@type") == "Product":
            print("Product image:", data.get("image"))
            print("name:", data.get("name"))
    except json.JSONDecodeError:
        pass

imgs = []
for m in re.finditer(r'(?:src|data-src|content)="([^"]+\.(?:jpg|jpeg|png|webp)[^"]*)"', html, re.I):
    u = m.group(1)
    if any(x in u.lower() for x in ("upload", "iblock", "storage", "catalog", "resize")):
        if u.startswith("//"):
            u = "https:" + u
        elif u.startswith("/"):
            u = "https://pack24.ru" + u
        imgs.append(u)

unique = []
for u in imgs:
    if u not in unique:
        unique.append(u)
print("catalog images", len(unique))
for u in unique[:12]:
    print(" ", u)
