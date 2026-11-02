#!/bin/bash
set -e
TS=$(date +%Y%m%d_%H%M%S)
VOL=/var/lib/docker/volumes/floksbox_backend_db_data/_data
echo "=== BACKUP ==="
if [ -f "$VOL/db.sqlite3" ]; then
  cp -a "$VOL/db.sqlite3" "$VOL/backup_${TS}.sqlite3"
  ls -la "$VOL/backup_${TS}.sqlite3"
fi
ls -la /tmp/db.sqlite3
echo "=== STOP + DOCKER CP ==="
docker stop floksbox-backend || true
docker cp /tmp/db.sqlite3 floksbox-backend:/data/db.sqlite3
ls -la "$VOL/db.sqlite3" 2>/dev/null || true
md5sum /tmp/db.sqlite3 "$VOL/db.sqlite3"
echo "=== GIT PULL ==="
cd /root/floksbox
git fetch origin
git pull origin main
echo "=== SETTINGS CHECK ==="
grep -n SQLITE backend/floksbox_backend/settings.py || true
grep DJANGO_SQLITE .env || true
echo "=== REBUILD ==="
docker compose build backend
docker compose up -d backend
sleep 8
docker ps --filter name=floksbox --format "table {{.Names}}\t{{.Status}}"
echo "=== COUNT ==="
docker exec floksbox-backend python manage.py shell -c "from catalog.models import Product; print('PRODUCTS=' + str(Product.objects.count()))"
echo DONE

