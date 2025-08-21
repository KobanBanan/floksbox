#!/bin/bash

echo "🚀 Запуск FloksBox Full Stack Application..."
echo "================================================="

# Функция для проверки доступности порта
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null ; then
        echo "⚠️  Порт $1 уже занят. Завершаем процесс..."
        kill $(lsof -t -i:$1) 2>/dev/null || true
        sleep 2
    fi
}

# Функция для очистки процессов при завершении скрипта
cleanup() {
    echo "🛑 Завершение работы..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    exit 0
}

# Обработчик сигнала для корректного завершения
trap cleanup SIGINT SIGTERM

# Переходим в корневую директорию проекта
cd "$(dirname "$0")"

echo "📍 Рабочая директория: $(pwd)"
echo ""

# Проверяем и освобождаем порты
echo "🔍 Проверка портов..."
check_port 8000
check_port 3000
echo ""

# Активируем виртуальное окружение Python если существует
if [ -d "venv" ]; then
    echo "🐍 Активация виртуального окружения Python..."
    
    # Определяем операционную систему и активируем соответствующим образом
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
        # Windows (Git Bash, MSYS2, Cygwin)
        source venv/Scripts/activate
    elif [ -f "venv/Scripts/activate.bat" ]; then
        # Windows (если скрипт запускается через cmd)
        call venv/Scripts/activate.bat
    else
        # Unix/Linux/macOS
        source venv/bin/activate
    fi
    
    echo "✅ Виртуальное окружение активировано"
else
    echo "⚠️  Виртуальное окружение не найдено. Используем системный Python"
fi
echo ""

# Запуск бэкенда
echo "🔧 Запуск Backend (Django)..."
echo "================================"
cd backend

# Проверяем зависимости Python
if [ -f "requirements.txt" ]; then
    echo "📦 Установка/обновление зависимостей Python..."
    pip install -r requirements.txt
fi

# Выполняем миграции
echo "🗄️  Выполнение миграций Django..."
python manage.py makemigrations
python manage.py migrate

# Запускаем backend в фоне
echo "🌐 Запуск Django сервера на http://localhost:8000"
python manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!

# Переходим обратно в корень
cd ..
echo ""

# Запуск фронтенда
echo "⚛️  Запуск Frontend (Nuxt.js)..."
echo "================================="
cd frontend

# Проверяем Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js не установлен. Пожалуйста, установите Node.js"
    exit 1
fi

# Проверяем npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm не установлен. Пожалуйста, установите npm"
    exit 1
fi

# Устанавливаем зависимости
echo "📦 Установка/обновление зависимостей npm..."
npm install

# Запускаем frontend в фоне
echo "🎨 Запуск Nuxt.js сервера на http://localhost:3000"
npm run dev -- --host 0.0.0.0 --port 3000 &
FRONTEND_PID=$!

# Переходим обратно в корень
cd ..
echo ""

echo "🎉 Приложение успешно запущено!"
echo "================================="
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:8000"
echo "⚙️  Админка: http://localhost:8000/admin"
echo "📡 API:      http://localhost:8000/api/"
echo ""
echo "📋 Для остановки нажмите Ctrl+C"
echo ""

# Ожидаем завершения (бесконечный цикл до получения сигнала)
while true; do
    # Проверяем, работают ли процессы
    if ! kill -0 $BACKEND_PID 2>/dev/null; then
        echo "❌ Backend процесс завершился неожиданно"
        break
    fi
    if ! kill -0 $FRONTEND_PID 2>/dev/null; then
        echo "❌ Frontend процесс завершился неожиданно"
        break
    fi
    sleep 5
done

cleanup
