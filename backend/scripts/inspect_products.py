import json
import os
import sqlite3
from collections import Counter

docs = r"C:\Users\lizal\Documents"
root = None
for d in os.listdir(docs):
    p = os.path.join(docs, d, "floksbox-main")
    if os.path.isdir(p):
        root = p
        break

db = os.path.join(root, "backend", "db.sqlite3")
con = sqlite3.connect(db)
cur = con.cursor()
cur.execute(
    """
    SELECT p.name, p.height, p.width, p.depth, p.image
    FROM requests_app_product p
    JOIN requests_app_category c ON p.category_id = c.id
    WHERE p.is_active = 1 AND c.name LIKE '%клапан%'
    ORDER BY p.depth, p.width, p.height
    """
)
rows = cur.fetchall()
print("active products", len(rows))
images = Counter()
for name, h, w, d, img in rows:
    images[img or "none"] += 1
print("unique images", len(images))
print("top repeated images:")
for img, cnt in images.most_common(8):
    print(cnt, (img or "")[-60:])

# aspect ratio buckets
def bucket(h, w, d):
    dims = sorted([float(h), float(w), float(d)], reverse=True)
    a, b, c = dims[0], dims[1], dims[2]
    ratio = a / max(c, 0.1)
    if ratio >= 2.2:
        return "tall"
    if abs(a - b) / max(a, 0.1) < 0.2:
        return "square"
    if abs(b - c) / max(b, 0.1) < 0.25:
        return "flat"
    return "standard"

bc = Counter()
for name, h, w, d, img in rows:
    bc[bucket(h, w, d)] += 1
print("shape buckets", dict(bc))

# size signature duplicates
sig = Counter()
for name, h, w, d, img in rows:
    sig[f"{d}x{w}x{h}"] += 1
print("duplicate size sigs", sum(1 for s, c in sig.items() if c > 1))

con.close()
