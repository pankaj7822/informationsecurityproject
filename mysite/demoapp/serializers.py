from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=["id","text","link","date_added","ntype","description"]
        
        

class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=["id","text","link","date_added","ntype","description"]