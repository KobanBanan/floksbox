#!/bin/bash
set -e
echo "===PS==="
docker ps --filter name=floksbox --format "table {{.Names}}\t{{.Status}}"
echo "===VOL==="
ls -lah /var/lib/docker/volumes/floksbox_backend_db_data/_data/
echo "===MD5==="
md5sum /tmp/db.sqlite3 /var/lib/docker/volumes/floksbox_backend_db_data/_data/db.sqlite3 || true
echo "===GIT==="
cd /root/floksbox
git log -1 --oneline
echo "===SETTINGS==="
grep -n SQLITE backend/floksbox_backend/settings.py || true
grep DJANGO_SQLITE .env || true
echo "===SQL_COUNT==="
docker exec floksbox-backend python - <<'PY'
import sqlite3, os
path=os.environ.get('DJANGO_SQLITE_NAME','/data/db.sqlite3')
c=sqlite3.connect(path)
print('DB', path)
print('PRODUCTS', c.execute('SELECT count(*) FROM requests_app_product').fetchone()[0])
print('TABLES', [t[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()])
PY
echo "===DJANGO_COUNT==="
docker exec floksbox-backend python manage.py shell -c "from requests_app.models import Product; print('PRODUCTS=' + str(Product.objects.count()))"
echo "===MEDIA==="
find /root/floksbox/backend/media -type f 2>/dev/null | wc -l
docker exec floksbox-backend sh -c 'find /app/media -type f 2>/dev/null | wc -l'
echo "===LOGS==="
docker logs --tail 20 floksbox-backend
echo "===CURL_LOCAL==="
curl -sS -o /tmp/api_products.json -w "HTTP=%{http_code}\n" http://127.0.0.1:8000/api/products/ || true
python3 - <<'PY'
import json,os
p='/tmp/api_products.json'
if os.path.exists(p) and os.path.getsize(p)>0:
    raw=open(p).read()[:300]
    print('BODY_HEAD', raw)
    try:
        data=json.loads(open(p).read())
        if isinstance(data, dict) and 'count' in data:
            print('API_COUNT=', data['count'])
        elif isinstance(data, list):
            print('API_COUNT=', len(data))
        elif isinstance(data, dict) and 'results' in data:
            print('API_COUNT=', data.get('count', len(data['results'])))
        else:
            print('API_TYPE', type(data))
    except Exception as e:
        print('API_PARSE_ERR', e)
else:
    print('API_EMPTY')
PY
echo "===CURL_SITE==="
curl -sS -o /dev/null -w "SITE_HTTP=%{http_code}\n" https://floksbox.ru/ || true
curl -sS -o /tmp/api_site.json -w "SITE_API_HTTP=%{http_code}\n" https://floksbox.ru/api/products/ || true
python3 - <<'PY'
import json,os
p='/tmp/api_site.json'
if os.path.exists(p) and os.path.getsize(p)>0:
    try:
        data=json.load(open(p))
        if isinstance(data, dict) and 'count' in data:
            print('SITE_API_COUNT=', data['count'])
        elif isinstance(data, list):
            print('SITE_API_COUNT=', len(data))
        elif isinstance(data, dict) and 'results' in data:
            print('SITE_API_COUNT=', data.get('count', len(data['results'])))
    except Exception as e:
        print('SITE_API_ERR', e, open(p).read()[:200])
PY
echo DONE
