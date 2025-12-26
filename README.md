# Floksbox Website

Полнофункциональное веб-приложение для FloksBox с бэкендом на Django и фронтендом на Nuxt.js.

## 🚀 Быстрый запуск

### Linux / macOS
```bash
./start.sh
```

### Windows
```cmd
start.bat
```

## 🔧 Что включено

- **Backend**: Django REST API на порту 8000
- **Frontend**: Nuxt.js приложение на порту 3000
- **База данных**: SQLite (готова к использованию)
- **Автоматические миграции**: Выполняются при каждом запуске
- **Зависимости**: Автоматическая установка для Python и Node.js

## 📋 Требования

### Общие требования
- Python 3.8+
- Node.js 16+
- npm или yarn

### Для разработки
- Git
- Виртуальное окружение Python (рекомендуется)

## 🌐 Доступные URL после запуска

- **Основное приложение**: http://localhost:3000
- **API Backend**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin
- **API Endpoints**: http://localhost:8000/api/

## 📦 Зависимости

### Backend (Python)
- Django
- Django REST Framework
- Другие зависимости в `backend/requirements.txt`

### Frontend (Node.js)
- Nuxt.js 4.0
- Vue.js 3.5
- SASS
- simple-parallax-js
- Другие зависимости в `frontend/package.json`

## 🐳 Docker (альтернативный запуск)

### Локальная разработка
```bash
docker-compose up --build
```

### Production развертывание
См. подробную инструкцию в [DEPLOY.md](./DEPLOY.md)

**Быстрый старт для production:**
```bash
# 1. Создайте .env файл из примера
cp .env.example .env

# 2. Отредактируйте .env (обязательно измените секретные ключи!)

# 3. Запустите
docker-compose up -d --build
```

## 🛠️ Ручная настройка

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📁 Структура проекта

```
floksbox/
├── start.sh          # Запуск для Linux/macOS
├── start.bat          # Запуск для Windows
├── docker-compose.yml # Docker конфигурация
├── backend/           # Django backend
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
└── frontend/          # Nuxt.js frontend
    ├── package.json
    ├── nuxt.config.ts
    └── ...
```
