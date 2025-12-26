# 🚀 План развертывания FloksBox на VPS

## 📋 Подготовка к деплою

### 1. Подготовка Git репозитория

```bash
# Проверка статуса
git status

# Добавление всех файлов (кроме игнорируемых)
git add .

# Коммит
git commit -m "Prepare for production deployment"

# Создание репозитория на GitHub/GitLab (если еще нет)
# Затем:
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. Проверка перед коммитом

✅ Убедитесь, что в `.gitignore` исключены:
- `backend/venv/`
- `backend/db.sqlite3`
- `backend/__pycache__/`
- `frontend/node_modules/`
- `.env` файлы
- `*.log` файлы

✅ Проверьте, что `.env.example` содержит все необходимые переменные

✅ Убедитесь, что `docker-compose.yml` настроен правильно

## 🐳 Развертывание на VPS с Docker

### Требования на сервере:
- Docker и Docker Compose установлены
- Git установлен
- Порты 80, 443, 3000, 8000 открыты (или настроен reverse proxy)

### Шаги развертывания:

#### 1. Подключение к серверу
```bash
ssh user@your-vps-ip
```

#### 2. Клонирование репозитория
```bash
cd /opt  # или другая директория
git clone <your-repo-url> floksbox
cd floksbox
```

#### 3. Настройка переменных окружения
```bash
# Создайте .env файл из примера
cp .env.example .env

# Отредактируйте .env файл
nano .env
```

**Важно заполнить:**
- `DJANGO_SECRET_KEY` - сгенерируйте новый секретный ключ
- `DJANGO_DEBUG=False` - для production
- `DJANGO_ALLOWED_HOSTS` - ваш домен/IP
- `DJANGO_CSRF_TRUSTED_ORIGINS` - ваш домен с https

#### 4. Генерация секретного ключа Django
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 5. Сборка и запуск контейнеров
```bash
# Сборка образов
docker-compose build

# Запуск в фоновом режиме
docker-compose up -d

# Просмотр логов
docker-compose logs -f
```

#### 6. Проверка работы
```bash
# Проверка статуса контейнеров
docker-compose ps

# Проверка логов
docker-compose logs backend
docker-compose logs frontend
```

### 7. Настройка Nginx (Reverse Proxy) - Рекомендуется

Создайте конфигурацию Nginx:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    # Редирект на HTTPS (если есть SSL)
    # return 301 https://$server_name$request_uri;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /media/ {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
    }

    location /static/ {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
    }
}
```

### 8. Настройка SSL (Let's Encrypt)

```bash
# Установка Certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# Получение сертификата
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Автоматическое обновление
sudo certbot renew --dry-run
```

## 🔄 Обновление приложения

```bash
# На сервере
cd /opt/floksbox

# Получение обновлений
git pull origin main

# Пересборка и перезапуск
docker-compose down
docker-compose build
docker-compose up -d

# Проверка логов
docker-compose logs -f
```

## 📊 Мониторинг и обслуживание

### Просмотр логов
```bash
# Все сервисы
docker-compose logs -f

# Только backend
docker-compose logs -f backend

# Только frontend
docker-compose logs -f frontend
```

### Остановка/Запуск
```bash
# Остановка
docker-compose down

# Запуск
docker-compose up -d

# Перезапуск
docker-compose restart
```

### Резервное копирование базы данных
```bash
# Создание бэкапа
docker-compose exec backend cp /data/db.sqlite3 /data/backup_$(date +%Y%m%d_%H%M%S).sqlite3

# Восстановление
docker-compose exec backend cp /data/backup_YYYYMMDD_HHMMSS.sqlite3 /data/db.sqlite3
```

## 🛠️ Устранение неполадок

### Проблема: Контейнеры не запускаются
```bash
# Проверка логов
docker-compose logs

# Проверка конфигурации
docker-compose config
```

### Проблема: База данных не работает
```bash
# Проверка миграций
docker-compose exec backend python manage.py showmigrations

# Применение миграций вручную
docker-compose exec backend python manage.py migrate
```

### Проблема: Статические файлы не загружаются
```bash
# Сбор статических файлов
docker-compose exec backend python manage.py collectstatic --noinput
```

## 📝 Чеклист перед деплоем

- [ ] Все секретные ключи изменены
- [ ] DEBUG=False в production
- [ ] ALLOWED_HOSTS настроен правильно
- [ ] CSRF_TRUSTED_ORIGINS настроен правильно
- [ ] .env файл не попал в Git
- [ ] База данных инициализирована
- [ ] Статические файлы собраны
- [ ] Порты открыты в firewall
- [ ] Nginx настроен (если используется)
- [ ] SSL сертификат установлен (если используется)
- [ ] Резервное копирование настроено

## 🔐 Безопасность

1. **Никогда не коммитьте `.env` файл**
2. **Используйте сильные секретные ключи**
3. **Настройте firewall (ufw/iptables)**
4. **Регулярно обновляйте зависимости**
5. **Используйте HTTPS в production**
6. **Ограничьте доступ к админке Django**

## 📞 Поддержка

При возникновении проблем проверьте:
1. Логи контейнеров: `docker-compose logs`
2. Статус контейнеров: `docker-compose ps`
3. Сеть Docker: `docker network ls`
4. Использование ресурсов: `docker stats`

