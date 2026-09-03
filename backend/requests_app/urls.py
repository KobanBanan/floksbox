from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import crm_views

# Создаем роутер для ViewSets
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products', views.ProductViewSet, basename='product')

urlpatterns = [
    # Root URL - redirects to health check for basic API status
    path('', views.health_check, name='root'),
    
    # Существующие URL
    path('sent_request/', views.sent_request, name='sent_request'),
    path('api/sent_request/', views.sent_request, name='sent_request_api'),
    path('health/', views.health_check, name='health_check'),

    # CRM API
    path('api/crm/login/', crm_views.crm_login, name='crm_login'),
    path('api/crm/logout/', crm_views.crm_logout, name='crm_logout'),
    path('api/crm/me/', crm_views.crm_me, name='crm_me'),
    path('api/crm/orders/', crm_views.crm_orders, name='crm_orders'),
    path('api/crm/orders/<int:order_id>/', crm_views.crm_order_detail, name='crm_order_detail'),
    
    # API маршруты для товаров и категорий
    path('api/', include(router.urls)),
]
