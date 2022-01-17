from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomAPI.as_view()),
    path('create-room/', views.RoomAPI.as_view()),
]
