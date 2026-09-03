import json
import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
BASE = "https://pack24.ru"

samples = [
    "gofrokorob-80-80-80-mm",
    "gofrokorob-100100200-mm",
    "gofrokorob-150-150-150-mm",
    "gofrokorob-650-350-100-mm",
    "gofrokorob-115115300-mm",
]

def extract(html, d, w, h):
    candidates = []
    for m in re.finditer(
        r'(?:src|data-src|href|content)="([^"]*/(?:size/4x-kl[^"]+|storage/thumbs/[^"]+))"',
        html,
        re.I,
    ):
        u = m.group(1)
        if u.startswith("//"):
            u = "https:" + u
        elif u.startswith("/"):
            u = BASE + u
        elif u.startswith("assets/"):
            u = BASE + "/" + u
        candidates.append(u)
    # built path
    for fmt in [
        f"/assets/images/catalog/kartonnye-korobki/size/4x-kl-{int(d*10)}x{int(w*10)}x{int(h*10)}.jpg",
        f"/assets/images/catalog/kartonnye-korobki/size/4x-kl-{int(d)}x{int(w)}x{int(h)}.jpg",
    ]:
        candidates.insert(0, BASE + fmt)
    # dedupe
    seen = set()
    out = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out[:5]

for slug in samples:
    url = f"{BASE}/kartonnye-korobki/chetyrehklapannye-koroba/{slug}"
    html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8", "replace")
    ld = None
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(m.group(1))
            if isinstance(data, dict) and data.get("@type") == "Product":
                ld = data
        except json.JSONDecodeError:
            pass
    if not ld:
        print(slug, "no ld")
        continue
    sm = re.search(r"(\d+)\*(\d+)\*(\d+)", str(ld.get("size") or ld.get("name")))
    d, w, h = [int(x) / 10 for x in sm.groups()]
    imgs = extract(html, d, w, h)
    print(slug, f"{d}x{w}x{h}", "ld", ld.get("image", "")[-50:])
    for im in imgs[:3]:
        print("  ", im[-70:])
