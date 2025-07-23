#!/bin/bash

echo "🚀 Запуск FloksBox Backend..."

# Проверяем наличие виртуального окружения
if [ ! -d "venv" ]; then
    echo "📦 Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активируем виртуальное окружение
echo "🔧 Активация виртуального окружения..."
source venv/bin/activate

# Устанавливаем зависимости
echo "📋 Установка зависимостей..."
pip install -r requirements.txt

# Проверяем миграции
echo "🗄️ Проверка миграций..."
python manage.py makemigrations
python manage.py migrate

echo "✅ Backend готов к работе!"
echo "🌐 Запуск сервера на http://localhost:8000"
echo "⚙️ Админка доступна на http://localhost:8000/admin"
echo "📡 API endpoint: http://localhost:8000/api/sent_request/"
echo ""
echo "Для остановки сервера нажмите Ctrl+C"
echo ""

# Запускаем сервер
python manage.py runserver 0.0.0.0:8000 