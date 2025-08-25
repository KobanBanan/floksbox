#!/usr/bin/env python
"""
Скрипт для создания суперпользователя Django
"""
import os
import django
from django.contrib.auth import get_user_model

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'floksbox_backend.settings')
django.setup()

User = get_user_model()

# Данные суперпользователя
username = 'admin'
email = 'admin@floksbox.com'
password = 'admin123'  # Измените на более безопасный пароль

# Проверяем, существует ли уже пользователь
if not User.objects.filter(username=username).exists():
    # Создаем суперпользователя
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f'✅ Суперпользователь "{username}" успешно создан!')
    print(f'📧 Email: {email}')
    print(f'🔑 Пароль: {password}')
    print(f'🌐 Админка доступна по адресу: http://localhost:8000/admin')
else:
    print(f'⚠️  Пользователь "{username}" уже существует!')
