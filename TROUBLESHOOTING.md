# 🔧 Устранение проблем со сборкой

## Частые проблемы и решения

### 1. Проблема: "Сайт не собирается"

#### Проверка локальной сборки frontend:
```bash
cd frontend
npm install
npm run build
```

Если сборка успешна локально, проблема может быть в:
- Отсутствии `.env` файла на сервере
- Неправильных переменных окружения
- Проблемах с Docker на сервере

#### Проверка на сервере (VPS):

```bash
# 1. Проверьте что файлы подтянулись
git status
git pull origin strawberries

# 2. Проверьте наличие .env файла
ls -la .env

# 3. Если .env нет, создайте из примера
cp env.example .env
nano .env  # Заполните переменные

# 4. Проверьте Docker
docker --version
docker compose version

# 5. Попробуйте собрать
docker compose build --no-cache

# 6. Проверьте логи при сборке
docker compose build 2>&1 | tee build.log
```

### 2. Проблема: "Ошибки при сборке Docker"

#### Ошибка: "Cannot find module"
```bash
# Убедитесь что все зависимости установлены
cd frontend
rm -rf node_modules package-lock.json
npm install
```

#### Ошибка: "requirements.txt not found"
```bash
# Проверьте что requirements.txt в корне проекта
ls -la requirements.txt

# Если нет, создайте из backend зависимостей
cd backend
pip freeze > ../requirements.txt
```

### 3. Проблема: "Контейнеры не запускаются"

```bash
# Проверьте логи
docker compose logs backend
docker compose logs frontend

# Проверьте статус
docker compose ps

# Перезапустите
docker compose down
docker compose up -d
```

### 4. Проблема: "API не отвечает"

```bash
# Проверьте что backend запущен
docker compose exec backend python manage.py check

# Проверьте миграции
docker compose exec backend python manage.py showmigrations

# Примените миграции
docker compose exec backend python manage.py migrate

# Соберите статику
docker compose exec backend python manage.py collectstatic --noinput
```

### 5. Проблема: "Frontend не подключается к Backend"

Проверьте `.env` файл:
```bash
# Должно быть:
NUXT_PUBLIC_API_BASE=http://backend:8000
BACKEND_URL=http://backend:8000
```

В production с Nginx:
```bash
NUXT_PUBLIC_API_BASE=https://your-domain.com
BACKEND_URL=http://backend:8000
```

### 6. Проблема: "Пустая папка server/api"

Это нормально! Мы удалили API endpoint для stories, теперь используется статический массив. Папка может быть пустой.

### 7. Полная пересборка с нуля

```bash
# Остановите все
docker compose down -v

# Удалите образы
docker compose rm -f
docker rmi floksbox-backend floksbox-frontend 2>/dev/null || true

# Очистите кэш
docker system prune -f

# Пересоберите
docker compose build --no-cache

# Запустите
docker compose up -d

# Проверьте логи
docker compose logs -f
```

### 8. Проверка что все файлы на месте

```bash
# Проверьте структуру
ls -la
ls -la frontend/
ls -la backend/
ls -la frontend/server/api/  # Может быть пустой - это нормально

# Проверьте что stories файлы есть
ls -la frontend/stories/
ls -la frontend/public/stories/
```

### 9. Проблема с правами доступа (Linux)

```bash
# Дайте права на выполнение скриптов
chmod +x backend/docker-entrypoint.sh
chmod +x start.sh

# Проверьте права на файлы
ls -la backend/docker-entrypoint.sh
```

### 10. Диагностика проблем

Создайте файл `check.sh`:
```bash
#!/bin/bash
echo "=== Проверка Git ==="
git status
echo ""
echo "=== Проверка файлов ==="
ls -la .env 2>/dev/null || echo ".env файл отсутствует!"
ls -la requirements.txt
ls -la docker-compose.yml
echo ""
echo "=== Проверка Docker ==="
docker --version
docker compose version
echo ""
echo "=== Проверка контейнеров ==="
docker compose ps
echo ""
echo "=== Последние логи ==="
docker compose logs --tail=20
```

Запустите: `bash check.sh`

## 📞 Если ничего не помогает

1. **Проверьте логи полностью:**
   ```bash
   docker compose logs > all_logs.txt
   cat all_logs.txt
   ```

2. **Проверьте конфигурацию:**
   ```bash
   docker compose config
   ```

3. **Проверьте сеть Docker:**
   ```bash
   docker network ls
   docker network inspect floksbox-net
   ```

4. **Проверьте volumes:**
   ```bash
   docker volume ls
   docker volume inspect floksbox_backend_db_data
   ```

## ✅ Чеклист перед обращением за помощью

- [ ] `.env` файл создан и заполнен
- [ ] Все файлы подтянуты из Git (`git pull`)
- [ ] Docker установлен и работает
- [ ] Порты 3000 и 8000 свободны
- [ ] Логи проверены на ошибки
- [ ] Конфигурация проверена (`docker compose config`)

