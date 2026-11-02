#!/bin/bash
set -e
echo "=== DB COUNT ==="
docker exec floksbox-backend python -c "import sqlite3; c=sqlite3.connect('/data/db.sqlite3'); print('products', c.execute('select count(*) from requests_app_product').fetchone()[0]); print('categories', c.execute('select count(*) from requests_app_category').fetchone()[0])"
echo "=== API ==="
for url in \
  http://127.0.0.1:8000/api/products/ \
  http://127.0.0.1:8000/api/requests/products/ \
  http://127.0.0.1:8000/api/catalog/products/
do
  code=$(curl -sS -o /tmp/api_products.json -w '%{http_code}' "$url" || echo FAIL)
  echo "$url -> $code"
  if [ "$code" = "200" ]; then
    python3 - <<'PY'
import json
d=json.load(open('/tmp/api_products.json'))
if isinstance(d, list):
    print('api_count', len(d))
elif isinstance(d, dict):
    print('api_count', d.get('count', len(d.get('results', []))))
    print('keys', list(d.keys())[:10])
PY
    break
  fi
done
echo "=== MEDIA ==="
ls /var/www/floksbox-media/products 2>/dev/null | wc -l
docker exec floksbox-backend sh -c 'ls /app/media/products 2>/dev/null | wc -l; ls /data/media/products 2>/dev/null | wc -l; ls -la /app/media 2>/dev/null | head'
echo "=== CONTAINERS ==="
docker ps --filter name=floksbox --format "table {{.Names}}\t{{.Status}}"
echo "=== LOGS ==="
docker logs floksbox-backend --tail 15
echo "=== SITE ==="
curl -sS -o /dev/null -w 'local_root %{http_code}\n' http://127.0.0.1/ || true
curl -sS -o /dev/null -w 'https %{http_code}\n' https://floksbox.ru/ || true
echo DONE
