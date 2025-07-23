from django.contrib import admin
from .models import UserRequest


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