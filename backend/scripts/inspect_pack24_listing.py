import re
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
url = "https://pack24.ru/kartonnye-korobki/chetyrehklapannye-koroba"
html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8", "replace")

# split by product links
parts = re.split(
    r"(https://pack24\.ru/kartonnye-korobki/chetyrehklapannye-koroba/gofrokorob-[^\"'#?\s]+)",
    html,
)
pairs = []
for i in range(1, len(parts), 2):
    link = parts[i].split("#")[0]
    chunk = parts[i + 1] if i + 1 < len(parts) else ""
    size_img = re.search(
        r"(/assets/images/catalog/kartonnye-korobki/size/[^\"']+\.(?:jpg|jpeg|png|webp))",
        chunk,
        re.I,
    )
    thumb = re.search(r"(/storage/thumbs/[^\"']+\.webp)", chunk, re.I)
    pairs.append((link, size_img.group(1) if size_img else None, thumb.group(1) if thumb else None))

print("cards", len(pairs))
with_size = sum(1 for _, s, _ in pairs if s)
with_thumb = sum(1 for _, _, t in pairs if t)
print("with size img", with_size, "with thumb", with_thumb)
for link, s, t in pairs[:6]:
    print(link.split("/")[-1][:40], "size=", (s or "")[-40:], "thumb=", (t or "")[-30:])
