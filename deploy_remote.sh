#!/bin/bash
set -e
TS=$(date +%Y%m%d_%H%M%S)
VOL=/var/lib/docker/volumes/floksbox_backend_db_data/_data
echo "=== BACKUP ==="
cp -a "$VOL/db.sqlite3" "$VOL/backup_${TS}.sqlite3"
echo "BACKED_UP backup_${TS}.sqlite3"
ls -la /tmp/db.sqlite3 "$VOL/db.sqlite3"
echo "=== STOP + DOCKER CP ==="
docker stop floksbox-backend || true
docker cp /tmp/db.sqlite3 floksbox-backend:/data/db.sqlite3
ls -la "$VOL/db.sqlite3"
echo "=== GIT PULL ==="
cd /root/floksbox
git pull origin main
echo "=== REBUILD ==="
docker compose build backend
docker compose up -d backend
sleep 5
docker ps --filter name=floksbox --format "table {{.Names}}\t{{.Status}}"
echo "=== VERIFY SETTINGS ==="
grep -n SQLITE backend/floksbox_backend/settings.py
grep DJANGO_SQLITE .env || true
echo DONE
