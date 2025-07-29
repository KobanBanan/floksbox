from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
import os


def validate_image_size(image):
    """Валидатор размера изображения (макс 5MB)"""
    max_size = 5 * 1024 * 1024  # 5MB
    if image.size > max_size:
        raise ValidationError('Размер изображения не должен превышать 5MB')


def validate_word_count(value):
    """Валидатор количества слов (макс 200 слов)"""
    word_count = len(value.split())
    if word_count > 200:
        raise ValidationError(f'Описание должно содержать не более 200 слов. Текущее количество: {word_count}')


def product_image_path(instance, filename):
    """Функция для определения пути сохранения изображений товаров"""
    ext = filename.split('.')[-1]
    filename = f'product_{instance.id or "new"}_{timezone.now().strftime("%Y%m%d_%H%M%S")}.{ext}'
    return os.path.join('products', filename)


class Category(models.Model):
    """Модель категории товаров"""
    
    name = models.CharField(
        max_length=100, 
        unique=True,
        verbose_name='Название категории',
        help_text='Уникальное название категории'
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name='Описание категории',
        help_text='Дополнительная информация о категории'
    )
    created_at = models.DateTimeField(
        default=timezone.now, 
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна',
        help_text='Отображается ли категория на сайте'
    )
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    
    name = models.CharField(
        max_length=200,
        verbose_name='Название товара',
        help_text='Название товара для отображения на сайте'
    )
    description = models.TextField(
        validators=[validate_word_count],
        verbose_name='Описание',
        help_text='Подробное описание товара (до 200 слов)'
    )
    image = models.ImageField(
        upload_to=product_image_path,
        validators=[
            validate_image_size,
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])
        ],
        verbose_name='Изображение',
        help_text='Изображение товара (JPG, PNG, WebP, до 5MB)'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        blank=True,
        null=True,
        verbose_name='Цена за штуку',
        help_text='Цена в рублях (опционально)'
    )
    
    # Размеры товара
    height = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.1), MaxValueValidator(9999.99)],
        verbose_name='Высота (см)',
        help_text='Высота товара в сантиметрах'
    )
    width = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.1), MaxValueValidator(9999.99)],
        verbose_name='Ширина (см)',
        help_text='Ширина товара в сантиметрах'
    )
    depth = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.1), MaxValueValidator(9999.99)],
        verbose_name='Глубина (см)',
        help_text='Глубина товара в сантиметрах'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name='Категория',
        help_text='Категория товара'
    )
    
    # Метаданные
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображается ли товар на сайте'
    )
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category', 'is_active']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f'{self.name} ({self.category.name if self.category else "Без категории"})'
    
    @property
    def dimensions(self):
        """Возвращает размеры товара в виде строки"""
        if self.height and self.width and self.depth:
            return f'{self.height} × {self.width} × {self.depth} см'
        return 'Размеры не указаны'
    
    @property
    def volume(self):
        """Вычисляет объем товара в кубических сантиметрах"""
        if self.height and self.width and self.depth:
            return float(self.height * self.width * self.depth)
        return 0.0


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
