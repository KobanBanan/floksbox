# 📋 План действий: Подготовка к Git и деплой на VPS

## ✅ Что уже готово

- ✅ Docker конфигурация (`docker-compose.yml`, `Dockerfile` для backend и frontend)
- ✅ `.gitignore` обновлен (исключает venv, node_modules, .env, db файлы)
- ✅ `env.example` создан с шаблоном переменных окружения
- ✅ `DEPLOY.md` - подробная инструкция по развертыванию
- ✅ `PRE_DEPLOY_CHECKLIST.md` - чеклист перед деплоем
- ✅ `README.md` обновлен с информацией о Docker

## 🎯 План действий (пошагово)

### Этап 1: Подготовка к Git (СЕЙЧАС)

#### 1.1 Проверка что не попадет в Git
```bash
# Проверьте статус
git status

# Убедитесь что эти файлы/папки НЕ будут закоммичены:
# - backend/venv/
# - backend/db.sqlite3
# - .env
# - frontend/node_modules/
# - *.log файлы
```

#### 1.2 Создание .env файла (если еще нет)
```bash
# Скопируйте пример
cp env.example .env

# Отредактируйте .env (НЕ коммитьте его!)
# Заполните реальные значения для локальной разработки
```

#### 1.3 Первый коммит
```bash
# Добавьте все файлы
git add .

# Проверьте что будет закоммичено
git status

# Создайте коммит
git commit -m "Initial commit: FloksBox project ready for deployment"

# Если репозиторий еще не создан на GitHub/GitLab:
# 1. Создайте репозиторий на GitHub/GitLab
# 2. Добавьте remote:
git remote add origin <your-repo-url>

# 3. Запушьте:
git push -u origin main
```

### Этап 2: Подготовка VPS сервера

#### 2.1 Установка Docker на сервере
```bash
# Подключитесь к серверу
ssh user@your-vps-ip

# Установите Docker (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker

# Проверьте установку
docker --version
docker-compose --version
```

#### 2.2 Настройка firewall (если нужно)
```bash
# Откройте необходимые порты
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw allow 3000/tcp  # Frontend (или используйте Nginx)
sudo ufw allow 8000/tcp  # Backend (или используйте Nginx)
sudo ufw enable
```

### Этап 3: Развертывание на VPS

#### 3.1 Клонирование репозитория
```bash
# На сервере
cd /opt  # или /var/www или другая директория
sudo git clone <your-repo-url> floksbox
cd floksbox
```

#### 3.2 Настройка переменных окружения
```bash
# Создайте .env из примера
cp env.example .env

# Отредактируйте .env
nano .env
```

**Обязательно измените:**
- `DJANGO_SECRET_KEY` - сгенерируйте новый:
  ```bash
  python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- `DJANGO_DEBUG=False` - для production
- `DJANGO_ALLOWED_HOSTS` - ваш домен/IP сервера
- `DJANGO_CSRF_TRUSTED_ORIGINS` - ваш домен с https

#### 3.3 Запуск приложения
```bash
# Сборка образов
docker-compose build

# Запуск в фоновом режиме
docker-compose up -d

# Проверка статуса
docker-compose ps

# Просмотр логов
docker-compose logs -f
```

#### 3.4 Проверка работы
```bash
# Проверьте что контейнеры запущены
docker-compose ps

# Проверьте логи на ошибки
docker-compose logs backend
docker-compose logs frontend

# Откройте в браузере:
# http://your-vps-ip:3000 (frontend)
# http://your-vps-ip:8000/api/ (backend API)
```

### Этап 4: Настройка Nginx (Рекомендуется)

#### 4.1 Установка Nginx
```bash
sudo apt-get install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

#### 4.2 Создание конфигурации
```bash
sudo nano /etc/nginx/sites-available/floksbox
```

Вставьте конфигурацию (см. DEPLOY.md, раздел "Настройка Nginx")

#### 4.3 Активация конфигурации
```bash
sudo ln -s /etc/nginx/sites-available/floksbox /etc/nginx/sites-enabled/
sudo nginx -t  # Проверка конфигурации
sudo systemctl reload nginx
```

### Этап 5: Настройка SSL (Let's Encrypt)

```bash
# Установка Certbot
sudo apt-get install -y certbot python3-certbot-nginx

# Получение сертификата
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Автоматическое обновление
sudo certbot renew --dry-run
```

### Этап 6: Настройка резервного копирования

```bash
# Создайте скрипт для бэкапа
nano /opt/floksbox/backup.sh
```

Содержимое скрипта:
```bash
#!/bin/bash
BACKUP_DIR="/opt/backups/floksbox"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

# Бэкап базы данных
docker-compose exec -T backend cp /data/db.sqlite3 /data/backup_$DATE.sqlite3

# Копирование бэкапа на хост
docker cp floksbox-backend:/data/backup_$DATE.sqlite3 $BACKUP_DIR/

echo "Backup created: $BACKUP_DIR/backup_$DATE.sqlite3"
```

```bash
chmod +x /opt/floksbox/backup.sh

# Добавьте в crontab для автоматического бэкапа
crontab -e
# Добавьте строку (каждый день в 3:00):
0 3 * * * /opt/floksbox/backup.sh
```

## 🔄 Обновление приложения (после деплоя)

```bash
# На сервере
cd /opt/floksbox

# Получение обновлений
git pull origin main

# Пересборка и перезапуск
docker-compose down
docker-compose build
docker-compose up -d

# Проверка
docker-compose logs -f
```

## 📞 Полезные команды

```bash
# Просмотр логов
docker-compose logs -f [service_name]

# Перезапуск сервиса
docker-compose restart [service_name]

# Остановка всех сервисов
docker-compose down

# Запуск всех сервисов
docker-compose up -d

# Просмотр использования ресурсов
docker stats

# Вход в контейнер
docker-compose exec backend bash
docker-compose exec frontend sh
```

## ⚠️ Важные замечания

1. **НИКОГДА не коммитьте `.env` файл** - он содержит секретные данные
2. **Всегда используйте `DEBUG=False` в production**
3. **Настройте резервное копирование базы данных**
4. **Используйте HTTPS в production** (Let's Encrypt бесплатный)
5. **Регулярно обновляйте зависимости** для безопасности

## 📚 Дополнительные ресурсы

- Подробная инструкция: `DEPLOY.md`
- Чеклист перед деплоем: `PRE_DEPLOY_CHECKLIST.md`
- Основной README: `README.md`

---

**Готово к деплою!** Следуйте плану пошагово, и все должно работать. 🚀

