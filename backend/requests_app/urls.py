from django.urls import path
from . import views

urlpatterns = [
    path('sent_request/', views.sent_request, name='sent_request'),
    path('health/', views.health_check, name='health_check'),
]
