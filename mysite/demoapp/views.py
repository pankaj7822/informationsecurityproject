from django.shortcuts import render
from .models import Notification
from django.http import JsonResponse

from rest_framework import generics
from .serializers import NotificationSerializer, NotificationCreateSerializer

def notification(request):
    a=list(Notification.objects.all())
    print(a[0])
    return JsonResponse({'foo':'bar'})

    
class ListNotificationsView(generics.ListAPIView):
    queryset=Notification.objects.all()[0:1000]
    serializer_class=NotificationSerializer
    
class NotificationCreateView(generics.CreateAPIView):
    serializer_class=NotificationCreateSerializer
    
