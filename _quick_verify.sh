#!/bin/bash
set -e
echo "=== containers ==="
docker ps --format '{{.Names}} {{.Status}}' | grep floks || true
echo "=== db ==="
docker exec floksbox-backend ls -la /data/db.sqlite3
docker exec floksbox-backend md5sum /data/db.sqlite3
echo "=== settings env ==="
docker exec floksbox-backend printenv DJANGO_SQLITE_NAME || true
echo "=== product count via manage.py ==="
docker exec floksbox-backend python manage.py shell -c "from products.models import Product; print(Product.objects.count())" 2>/dev/null || \
docker exec floksbox-backend python -c "import os,django;os.environ.setdefault('DJANGO_SETTINGS_MODULE','floksbox_backend.settings');django.setup();from products.models import Product;print(Product.objects.count())"
echo "=== api ==="
curl -sS -o /tmp/p.json -w 'api_http %{http_code}\n' --max-time 20 https://floksbox.ru/api/products/ || true
python3 -c "import json;d=json.load(open('/tmp/p.json'));print('count', d.get('count', len(d) if isinstance(d,list) else 'n/a'))" 2>/dev/null || head -c 200 /tmp/p.json
echo "=== site ==="
curl -sS -o /dev/null -w 'site %{http_code}\n' --max-time 15 https://floksbox.ru/ || echo 'site timeout/fail'
echo "=== media files ==="
docker exec floksbox-backend find /app/media -type f 2>/dev/null | wc -l || true
echo "=== backups ==="
ls -lt /root/floksbox/backup*.sqlite3 2>/dev/null | head -3 || true
ls -lt /tmp/backup*.sqlite3 2>/dev/null | head -3 || true
find /var/lib/docker/volumes -name '*backup*.sqlite3' 2>/dev/null | head -5 || true
echo "=== git ==="
cd /root/floksbox && git log -1 --oneline && grep -n SQLITE_DB_NAME backend/floksbox_backend/settings.py | head -5
