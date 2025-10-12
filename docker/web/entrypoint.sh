#!/usr/bin/env bash
set -e

# Ждём базу
python - <<'PYCODE'
import os, time, psycopg2
host=os.getenv('POSTGRES_HOST','db'); port=int(os.getenv('POSTGRES_PORT','5432'))
user=os.getenv('POSTGRES_USER'); pwd=os.getenv('POSTGRES_PASSWORD'); db=os.getenv('POSTGRES_DB')
for i in range(60):
    try:
        psycopg2.connect(host=host, port=port, user=user, password=pwd, dbname=db).close()
        break
    except Exception as e:
        time.sleep(1)
else:
    raise SystemExit("Postgres is not ready")
PYCODE

# Миграции + статика
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Запускаем gunicorn
exec gunicorn test_indepo.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 60
