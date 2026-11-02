#!/bin/bash
set -e
echo "=== MEDIA BEFORE ==="
find /root/floksbox/backend/media -type f 2>/dev/null | wc -l || true
if [ -f /tmp/media-sync.tar.gz ]; then
  echo "=== EXTRACT MEDIA ==="
  mkdir -p /root/floksbox/backend/media
  tar -xzf /tmp/media-sync.tar.gz -C /root/floksbox/backend/
fi
echo "=== MEDIA AFTER ==="
find /root/floksbox/backend/media -type f 2>/dev/null | wc -l
echo "=== CONTAINERS ==="
docker ps --filter name=floksbox --format "table {{.Names}}\t{{.Status}}"
echo "=== DB MD5 ==="
md5sum /tmp/db.sqlite3 /var/lib/docker/volumes/floksbox_backend_db_data/_data/db.sqlite3 || true
echo "=== SQL COUNT ==="
docker exec floksbox-backend python -c "import sqlite3; c=sqlite3.connect('/data/db.sqlite3'); print('PRODUCTS', c.execute('select count(*) from requests_app_product').fetchone()[0])"
echo "=== DJANGO COUNT ==="
docker exec floksbox-backend python manage.py shell -c "from requests_app.models import Product; print('PRODUCTS=' + str(Product.objects.count()))"
echo "=== API LOCAL ==="
curl -sS -o /tmp/p.json -w "API_HTTP=%{http_code}\n" --max-time 90 http://127.0.0.1:8000/api/products/ || echo API_CURL_FAIL
python3 -c "import json; d=json.load(open('/tmp/p.json')); print('API_COUNT', len(d) if isinstance(d,list) else d.get('count'))" || true
echo "=== LOGS ==="
docker logs --tail 30 floksbox-backend
echo "=== SITE ==="
curl -sS -o /dev/null -w "SITE=%{http_code}\n" --max-time 20 https://floksbox.ru/ || true
curl -sS -o /tmp/cats.json -w "CATS=%{http_code}\n" --max-time 20 https://floksbox.ru/api/categories/ || true
python3 -c "import json; print('CAT_COUNT', len(json.load(open('/tmp/cats.json'))))" || true
echo DONE
