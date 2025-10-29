#!/bin/sh
set -e

DEFAULT_DB="/app/db.sqlite3"
TARGET_DB="${DJANGO_SQLITE_NAME:-$DEFAULT_DB}"
TARGET_DIR="$(dirname "$TARGET_DB")"

# Ensure target directory exists (for named volumes)
mkdir -p "$TARGET_DIR"

# Seed the persistent volume with the bundled DB if it is missing
if [ ! -f "$TARGET_DB" ] && [ -f "$DEFAULT_DB" ] && [ "$TARGET_DB" != "$DEFAULT_DB" ]; then
    cp "$DEFAULT_DB" "$TARGET_DB"
    echo "Seeded SQLite database at $TARGET_DB"
fi

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn floksbox_backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
