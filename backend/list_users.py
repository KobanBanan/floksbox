#!/usr/bin/env python
"""
Скрипт для просмотра существующих пользователей Django
"""
import os
import django
from django.contrib.auth import get_user_model

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'floksbox_backend.settings')
django.setup()

User = get_user_model()

print("👥 Список пользователей в системе:")
print("=" * 50)

users = User.objects.all()
if users:
    for user in users:
        status = "👑 Суперпользователь" if user.is_superuser else "👤 Обычный пользователь"
        print(f"📝 Имя: {user.username}")
        print(f"📧 Email: {user.email or 'Не указан'}")
        print(f"🔑 Статус: {status}")
        print(f"✅ Активен: {'Да' if user.is_active else 'Нет'}")
        print(f"📅 Дата создания: {user.date_joined.strftime('%d.%m.%Y %H:%M')}")
        print("-" * 30)
else:
    print("❌ Пользователи не найдены")

print(f"\n📊 Всего пользователей: {users.count()}")
superusers = users.filter(is_superuser=True)
print(f"👑 Суперпользователей: {superusers.count()}")
