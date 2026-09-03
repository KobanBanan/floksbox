from rest_framework import serializers
from .models import Category, Product, UserRequest


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'description', 'is_active', 
            'created_at', 'updated_at', 'products_count'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'products_count']
    
    def get_products_count(self, obj):
        """Возвращает количество активных товаров в категории"""
        return obj.products.filter(is_active=True).count()


class CategoryListSerializer(serializers.ModelSerializer):
    """Упрощенный сериализатор для списка категорий"""
    
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товаров"""
    
    category_name = serializers.CharField(source='category.name', read_only=True)
    dimensions = serializers.CharField(read_only=True)
    volume = serializers.FloatField(read_only=True)
    image_url = serializers.SerializerMethodField()
    image_unfold_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'image', 'image_url', 'image_unfold_url', 'price',
            'height', 'width', 'depth', 'dimensions', 'volume',
            'category', 'category_name', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 'dimensions', 'volume',
            'image_url', 'image_unfold_url',
        ]
    
    def get_image_url(self, obj):
        """Возвращает относительный URL изображения (от /media), чтобы хост подставлял ngrok"""
        if obj.image:
            return obj.image.url
        return None

    def get_image_unfold_url(self, obj):
        if obj.image_unfold:
            return obj.image_unfold.url
        return None
    
    def validate_image(self, value):
        """Дополнительная валидация изображения"""
        if value:
            # Проверяем размер файла
            if value.size > 5 * 1024 * 1024:  # 5MB
                raise serializers.ValidationError("Размер изображения не должен превышать 5MB")
            
            # Проверяем формат файла
            allowed_formats = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
            if hasattr(value, 'content_type') and value.content_type not in allowed_formats:
                raise serializers.ValidationError("Поддерживаются только форматы: JPG, PNG, WebP")
        
        return value


class ProductListSerializer(serializers.ModelSerializer):
    """Упрощенный сериализатор для списка товаров"""
    
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField()
    dimensions = serializers.CharField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'image_url', 'price', 'dimensions',
            'category', 'category_name', 'is_active'
        ]
    
    def get_image_url(self, obj):
        """Возвращает относительный URL изображения (от /media), чтобы хост подставлял ngrok"""
        if obj.image:
            return obj.image.url
        return None


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления товаров"""
    
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'image', 'price',
            'height', 'width', 'depth', 'category', 'is_active'
        ]
    
    def validate_price(self, value):
        """Валидация цены"""
        if value is not None and value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля")
        return value
    
    def validate(self, data):
        """Общая валидация данных"""
        # Проверяем, что все размеры указаны
        required_dimensions = ['height', 'width', 'depth']
        for dimension in required_dimensions:
            if data.get(dimension) is None:
                raise serializers.ValidationError(f"Поле '{dimension}' обязательно для заполнения")
            if data.get(dimension) <= 0:
                raise serializers.ValidationError(f"Значение '{dimension}' должно быть больше нуля")
        
        return data


class CrmOrderListSerializer(serializers.ModelSerializer):
    status_label = serializers.CharField(read_only=True)

    class Meta:
        model = UserRequest
        fields = [
            'id', 'name', 'phone', 'email', 'message', 'source',
            'status', 'status_label', 'created_at', 'updated_at',
        ]


class CrmOrderDetailSerializer(serializers.ModelSerializer):
    status_label = serializers.CharField(read_only=True)

    class Meta:
        model = UserRequest
        fields = [
            'id', 'name', 'phone', 'email', 'message', 'source',
            'status', 'status_label', 'manager_notes',
            'created_at', 'updated_at', 'is_processed',
        ]


class CrmOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['status', 'manager_notes']

    def validate_status(self, value):
        valid = {choice[0] for choice in UserRequest.Status.choices}
        if value not in valid:
            raise serializers.ValidationError('Некорректный статус')
        return value