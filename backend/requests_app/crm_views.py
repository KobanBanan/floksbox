from django.contrib.auth import authenticate
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import UserRequest
from .serializers import CrmOrderDetailSerializer, CrmOrderListSerializer, CrmOrderUpdateSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def crm_login(request):
    username = (request.data.get('username') or '').strip()
    password = request.data.get('password') or ''

    if not username or not password:
        return Response(
            {'success': False, 'error': 'Укажите логин и пароль'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = authenticate(request, username=username, password=password)
    if user is None or not user.is_staff:
        return Response(
            {'success': False, 'error': 'Неверный логин или пароль'},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'success': True,
        'token': token.key,
        'user': {
            'id': user.id,
            'username': user.username,
            'name': user.get_full_name() or user.username,
        },
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crm_logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({'success': True})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crm_me(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'name': user.get_full_name() or user.username,
        'is_staff': user.is_staff,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crm_orders(request):
    status_filter = (request.query_params.get('status') or '').strip()
    search = (request.query_params.get('search') or '').strip()

    queryset = UserRequest.objects.all()
    if status_filter:
        queryset = queryset.filter(status=status_filter)
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(phone__icontains=search)
            | Q(email__icontains=search)
            | Q(message__icontains=search)
        )

    stats = {
        row['status']: row['count']
        for row in UserRequest.objects.values('status').annotate(count=Count('id'))
    }
    for value, _ in UserRequest.Status.choices:
        stats.setdefault(value, 0)

    serializer = CrmOrderListSerializer(queryset[:200], many=True)
    return Response({
        'results': serializer.data,
        'stats': stats,
        'total': queryset.count(),
    })


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def crm_order_detail(request, order_id):
    try:
        order = UserRequest.objects.get(pk=order_id)
    except UserRequest.DoesNotExist:
        return Response({'error': 'Заявка не найдена'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(CrmOrderDetailSerializer(order).data)

    serializer = CrmOrderUpdateSerializer(order, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(CrmOrderDetailSerializer(order).data)
