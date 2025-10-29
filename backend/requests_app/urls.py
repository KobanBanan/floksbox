from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

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
    
    # API маршруты для товаров и категорий
    path('api/', include(router.urls)),
]
