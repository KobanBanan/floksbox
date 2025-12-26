# 🚀 Быстрое решение проблем со сборкой

## Если сайт не собирается на VPS:

### Шаг 1: Проверьте что все файлы подтянулись
```bash
cd /opt/floksbox  # или где у вас проект
git pull origin strawberries
git status
```

### Шаг 2: Создайте .env файл (если его нет)
```bash
cp env.example .env
nano .env
```

**Обязательно заполните:**
- `DJANGO_SECRET_KEY` - сгенерируйте новый
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=ваш-домен.com,ваш-ip`
- `NUXT_PUBLIC_API_BASE=http://backend:8000`
- `BACKEND_URL=http://backend:8000`

### Шаг 3: Полная пересборка
```bash
# Остановите все
docker compose down

# Пересоберите без кэша
docker compose build --no-cache

# Запустите
docker compose up -d

# Смотрите логи
docker compose logs -f
```

### Шаг 4: Если ошибка при сборке frontend

Проверьте что в `frontend/Dockerfile` все правильно:
- `package.json` должен быть скопирован
- `npm ci` должен выполниться
- `npm run build` должен выполниться

### Шаг 5: Если ошибка при сборке backend

Проверьте что:
- `requirements.txt` в корне проекта
- `backend/Dockerfile` правильно копирует файлы
- `docker-entrypoint.sh` имеет права на выполнение

### Шаг 6: Проверка работы

```bash
# Статус контейнеров
docker compose ps

# Логи backend
docker compose logs backend

# Логи frontend  
docker compose logs frontend

# Проверка что порты открыты
curl http://localhost:3000
curl http://localhost:8000/api/
```

## Частые ошибки:

### "Cannot find module" в frontend
```bash
cd frontend
rm -rf node_modules .output
npm install
npm run build
```

### "requirements.txt not found" в backend
```bash
# Убедитесь что requirements.txt в корне проекта
ls -la requirements.txt
```

### "Permission denied" для docker-entrypoint.sh
```bash
chmod +x backend/docker-entrypoint.sh
```

### Контейнеры падают сразу после запуска
```bash
# Смотрите логи
docker compose logs backend
docker compose logs frontend

# Проверьте .env файл
cat .env
```

## Если ничего не помогает:

1. **Полная очистка и пересборка:**
```bash
docker compose down -v
docker system prune -f
docker compose build --no-cache
docker compose up -d
```

2. **Проверьте конфигурацию:**
```bash
docker compose config
```

3. **Сохраните логи:**
```bash
docker compose logs > errors.log 2>&1
cat errors.log
```

## 📝 Пришлите мне:
- Вывод `docker compose logs backend`
- Вывод `docker compose logs frontend`  
- Вывод `docker compose ps`
- Содержимое `.env` (без секретных ключей!)

