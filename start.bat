@echo off
chcp 65001 >nul
echo 🚀 Запуск FloksBox Full Stack Application...
echo =================================================

:: Переходим в директорию скрипта
cd /d "%~dp0"
echo 📍 Рабочая директория: %cd%
echo.

:: Функция для проверки и завершения процессов на портах
echo 🔍 Проверка портов...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    echo ⚠️  Завершаем процесс на порту 8000 (PID: %%a)
    taskkill /F /PID %%a >nul 2>&1
)
for /f "tokens=5" %%b in ('netstat -aon ^| find ":3000" ^| find "LISTENING"') do (
    echo ⚠️  Завершаем процесс на порту 3000 (PID: %%b)
    taskkill /F /PID %%b >nul 2>&1
)
timeout /t 2 /nobreak >nul
echo.

:: Активируем виртуальное окружение Python если существует
if exist "venv" (
    echo 🐍 Активация виртуального окружения Python...
    if exist "venv\Scripts\activate.bat" (
        call venv\Scripts\activate.bat
        echo ✅ Виртуальное окружение активировано
    ) else (
        echo ❌ Файл активации не найден в venv\Scripts\activate.bat
        goto :error
    )
) else (
    echo ⚠️  Виртуальное окружение не найдено. Используем системный Python
)
echo.

:: Запуск бэкенда
echo 🔧 Запуск Backend (Django)...
echo ================================
cd backend

:: Проверяем зависимости Python
if exist "requirements.txt" (
    echo 📦 Установка/обновление зависимостей Python...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Ошибка установки зависимостей Python
        goto :error
    )
)

:: Выполняем миграции
echo 🗄️  Выполнение миграций Django...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo ❌ Ошибка выполнения миграций
    goto :error
)

:: Запускаем backend в фоне
echo 🌐 Запуск Django сервера на http://localhost:8000
start /b cmd /c "python manage.py runserver 0.0.0.0:8000"

:: Переходим обратно в корень
cd ..
echo.

:: Запуск фронтенда
echo ⚛️  Запуск Frontend (Nuxt.js)...
echo =================================
cd frontend

:: Проверяем Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js не установлен. Пожалуйста, установите Node.js
    goto :error
)

:: Проверяем npm
npm --version >nul 2>&1
if errorlevel 1 (
    echo ❌ npm не установлен. Пожалуйста, установите npm
    goto :error
)

:: Устанавливаем зависимости
echo 📦 Установка/обновление зависимостей npm...
npm install
if errorlevel 1 (
    echo ❌ Ошибка установки зависимостей npm
    goto :error
)

:: Запускаем frontend в фоне
echo 🎨 Запуск Nuxt.js сервера на http://localhost:3000
start /b cmd /c "npm run dev -- --host 0.0.0.0 --port 3000"

:: Переходим обратно в корень
cd ..
echo.

echo 🎉 Приложение успешно запущено!
echo =================================
echo 🌐 Frontend: http://localhost:3000
echo 🔧 Backend:  http://localhost:8000
echo ⚙️  Админка: http://localhost:8000/admin
echo 📡 API:      http://localhost:8000/api/
echo.
echo 📋 Для остановки нажмите Ctrl+C или закройте это окно
echo.

:: Ожидание (пауза до нажатия клавиши)
pause
goto :end

:error
echo.
echo ❌ Произошла ошибка при запуске приложения!
echo Проверьте установку зависимостей и повторите попытку.
pause
exit /b 1

:end
exit /b 0
