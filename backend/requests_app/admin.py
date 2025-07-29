from django.contrib import admin
from .models import UserRequest, Category, Product


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    """Админка для заявок пользователей"""

    list_display = ('name', 'phone', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at',)
    list_per_page = 20

    fieldsets = (
        ('Информация о заявке', {
            'fields': ('name', 'phone', 'email', 'message')
        }),
        ('Системная информация', {
            'fields': ('created_at', 'is_processed'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')

    actions = ['mark_as_processed', 'mark_as_unprocessed']

    def mark_as_processed(self, request, queryset):
        updated = queryset.update(is_processed=True)
        self.message_user(request, f'{updated} заявок отмечено как обработанные.')

    mark_as_processed.short_description = 'Отметить как обработанные'

    def mark_as_unprocessed(self, request, queryset):
        updated = queryset.update(is_processed=False)
        self.message_user(request, f'{updated} заявок отмечено как необработанные.')

    mark_as_unprocessed.short_description = 'Отметить как необработанные'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий товаров"""
    
    list_display = ('name', 'is_active', 'products_count', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'products_count')
    list_per_page = 20
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'is_active')
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at', 'products_count'),
            'classes': ('collapse',)
        }),
    )
    
    def products_count(self, obj):
        """Количество товаров в категории"""
        return obj.products.count()
    
    products_count.short_description = 'Количество товаров'
    
    actions = ['activate_categories', 'deactivate_categories']
    
    def activate_categories(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} категорий активировано.')
    
    activate_categories.short_description = 'Активировать категории'
    
    def deactivate_categories(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} категорий деактивировано.')
    
    deactivate_categories.short_description = 'Деактивировать категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для товаров"""
    
    list_display = ('name', 'category', 'price', 'dimensions', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'dimensions', 'volume')
    list_per_page = 20
    
    def get_fieldsets(self, request, obj=None):
        """Возвращает разные fieldsets для создания и редактирования"""
        if obj:  # Редактирование существующего товара
            return (
                ('Основная информация', {
                    'fields': ('name', 'description', 'category', 'is_active')
                }),
                ('Изображение и цена', {
                    'fields': ('image', 'price')
                }),
                ('Размеры', {
                    'fields': ('height', 'width', 'depth', 'dimensions', 'volume'),
                    'description': 'Размеры указываются в сантиметрах'
                }),
                ('Системная информация', {
                    'fields': ('created_at', 'updated_at'),
                    'classes': ('collapse',)
                }),
            )
        else:  # Создание нового товара
            return (
                ('Основная информация', {
                    'fields': ('name', 'description', 'category', 'is_active')
                }),
                ('Изображение и цена', {
                    'fields': ('image', 'price')
                }),
                ('Размеры', {
                    'fields': ('height', 'width', 'depth'),
                    'description': 'Размеры указываются в сантиметрах'
                }),
            )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')
    
    actions = ['activate_products', 'deactivate_products', 'copy_products']
    
    def activate_products(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} товаров активировано.')
    
    activate_products.short_description = 'Активировать товары'
    
    def deactivate_products(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} товаров деактивировано.')
    
    deactivate_products.short_description = 'Деактивировать товары'
