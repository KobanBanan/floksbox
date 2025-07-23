from django.db import models
from django.utils import timezone


class UserRequest(models.Model):
    """Модель для заявок пользователей"""
    
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    message = models.TextField(blank=True, null=True, verbose_name='Сообщение')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.phone} ({self.created_at.strftime("%d.%m.%Y %H:%M")})' 