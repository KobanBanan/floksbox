from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import UserRequest
from .services import NotificationService
import logging

# Новые импорты для товаров и категорий
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Category, Product
from .serializers import (
    CategorySerializer, CategoryListSerializer,
    ProductSerializer, ProductListSerializer, ProductCreateUpdateSerializer
)

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def sent_request(request):
    """API endpoint для отправки заявки"""
    try:
        # Получаем данные из запроса
        data = request.data
        name = data.get('name', '').strip()
        phone = data.get('phone', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Валидация обязательных полей
        if not name:
            return Response({
                'success': False,
                'error': 'Поле "Имя" обязательно для заполнения'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not phone:
            return Response({
                'success': False,
                'error': 'Поле "Телефон" обязательно для заполнения'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Создаем заявку
        user_request = UserRequest.objects.create(
            name=name,
            phone=phone,
            email=email if email else None,
            message=message if message else None
        )

        # Отправляем уведомления
        notification_results = NotificationService.send_notifications(user_request)

        logger.info(f"Создана заявка {user_request.id} от {name}")

        return Response({
            'success': True,
            'message': 'Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.',
            'request_id': user_request.id,
            'notifications': notification_results
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Ошибка при создании заявки: {e}")
        return Response({
            'success': False,
            'error': 'Произошла ошибка при отправке заявки. Попробуйте позже.'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Проверка работоспособности API"""
    return Response({
        'status': 'ok',
        'message': 'FloksBox Backend API работает'
    })


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet для управления категориями"""
    
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']
    
    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от действия"""
        if self.action == 'list':
            return CategoryListSerializer
        return CategorySerializer
    
    def get_queryset(self):
        """Фильтрация queryset"""
        queryset = Category.objects.all()
        
        # Фильтр только активных категорий
        active_only = self.request.query_params.get('active_only', None)
        if active_only and active_only.lower() == 'true':
            queryset = queryset.filter(is_active=True)
        
        return queryset
    
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Получить все товары в категории"""
        category = self.get_object()
        products = category.products.filter(is_active=True)
        
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet для управления товарами"""
    
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от действия"""
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return ProductSerializer
    
    def get_queryset(self):
        """Фильтрация queryset с дополнительными параметрами"""
        queryset = Product.objects.select_related('category')
        
        # Фильтр только активных товаров
        active_only = self.request.query_params.get('active_only', None)
        if active_only and active_only.lower() == 'true':
            queryset = queryset.filter(is_active=True)
        
        # Фильтр по категории (по имени)
        category_name = self.request.query_params.get('category_name', None)
        if category_name:
            queryset = queryset.filter(category__name__icontains=category_name)
        
        # Фильтр по ценовому диапазону
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if min_price:
            try:
                min_price = float(min_price)
                queryset = queryset.filter(price__gte=min_price)
            except ValueError:
                pass
        
        if max_price:
            try:
                max_price = float(max_price)
                queryset = queryset.filter(price__lte=max_price)
            except ValueError:
                pass
        
        # Фильтр по размерам
        min_volume = self.request.query_params.get('min_volume', None)
        max_volume = self.request.query_params.get('max_volume', None)
        
        if min_volume:
            try:
                min_volume = float(min_volume)
                queryset = queryset.extra(
                    where=["height * width * depth >= %s"],
                    params=[min_volume]
                )
            except ValueError:
                pass
        
        if max_volume:
            try:
                max_volume = float(max_volume)
                queryset = queryset.extra(
                    where=["height * width * depth <= %s"],
                    params=[max_volume]
                )
            except ValueError:
                pass
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Получить рекомендуемые товары (последние 4 активных)"""
        products = self.get_queryset().filter(is_active=True)[:4]
        serializer = ProductListSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Получить товары, сгруппированные по категориям"""
        categories = Category.objects.filter(is_active=True).prefetch_related('products')
        result = []
        
        for category in categories:
            products = category.products.filter(is_active=True)
            if products.exists():
                result.append({
                    'category': CategoryListSerializer(category).data,
                    'products': ProductListSerializer(products, many=True, context={'request': request}).data
                })
        
        return Response(result)
    
    def perform_create(self, serializer):
        """Дополнительная логика при создании товара"""
        product = serializer.save()
        logger.info(f"Создан товар {product.id}: {product.name}")
    
    def perform_update(self, serializer):
        """Дополнительная логика при обновлении товара"""
        product = serializer.save()
        logger.info(f"Обновлен товар {product.id}: {product.name}")
    
    def perform_destroy(self, instance):
        """Дополнительная логика при удалении товара"""
        logger.info(f"Удален товар {instance.id}: {instance.name}")
        instance.delete()
