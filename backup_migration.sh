#!/usr/bin/env bash
set -e

# === Настройки ===
PROJECT_NAME="indepo-site"
PROJECT_PATH="/home/popcorn/test-docker-project//indepo-site"
TMP_DIR="/tmp/${PROJECT_NAME}-migration"
BACKUP_DIR="${TMP_DIR}/backups"
ARTIFACTS_DIR="${TMP_DIR}/artifacts"

# === Проверки ===
echo "➡️ Проверка проекта..."
cd "$PROJECT_PATH" || { echo "❌ Не найден проект в ${PROJECT_PATH}"; exit 1; }

mkdir -p "$BACKUP_DIR" "$ARTIFACTS_DIR"

echo "➡️ Создаём дамп базы..."
docker compose exec -T db bash -c "pg_dump -U \$POSTGRES_USER \$POSTGRES_DB" > \
  "${BACKUP_DIR}/db_backup_$(date +%F_%H-%M).sql"
echo "✅ База сохранена: ${BACKUP_DIR}"

echo "➡️ Копируем файлы проекта..."
cp -a docker-compose.yml requirements.txt .env "$ARTIFACTS_DIR"/ 2>/dev/null || true
cp -a docker nginx "$ARTIFACTS_DIR"/ 2>/dev/null || true
cp -a vol "$ARTIFACTS_DIR"/ 2>/dev/null || true

if [ -d data/postgres ]; then
  echo "➡️ Найдена bind-база — копируем каталог..."
  mkdir -p "$ARTIFACTS_DIR/data"
  cp -a data/postgres "$ARTIFACTS_DIR/data/"
fi

echo "➡️ Проверяем сертификаты..."
if [ -d nginx/certs ]; then
  cp -a nginx/certs "$ARTIFACTS_DIR/"
elif [ -d /etc/nginx/certs ]; then
  mkdir -p "$ARTIFACTS_DIR/nginx-certs"
  sudo cp -a /etc/nginx/certs "$ARTIFACTS_DIR/nginx-certs"
fi

echo "➡️ Сохраняем Docker-образы (если нужно)..."
docker save indepo-site-web > "${ARTIFACTS_DIR}/indepo_web.tar"
docker save nginx:1.25-alpine > "${ARTIFACTS_DIR}/nginx.tar"
docker save postgres:15 > "${ARTIFACTS_DIR}/postgres.tar"

echo "➡️ Упаковываем всё в архив..."
cd /tmp
tar czf ${PROJECT_NAME}-migration-$(date +%F_%H-%M).tar.gz ${PROJECT_NAME}-migration
echo "✅ Готово: /tmp/${PROJECT_NAME}-migration-*.tar.gz"

#echo "➡️ Перенеси архив на новый хост:"
#echo "scp /tmp/${PROJECT_NAME}-migration-*.tar.gz user@NEW_HOST:/tmp/"
