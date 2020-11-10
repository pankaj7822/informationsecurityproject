from django.urls import path, re_path, include
from .views import ListNotificationsView,NotificationCreateView

urlpatterns = [
    path('',ListNotificationsView.as_view()),
    # path('create/',NotificationCreateView.as_view())
]
