from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import UserRequest
from .services import NotificationService
import logging

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
