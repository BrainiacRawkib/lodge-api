from django.urls import path
from . import views

urlpatterns = [
    # Block urls
    path('blocks/', views.BlockAPI.as_view()),
    path('create-block/', views.BlockAPI.as_view()),
    path('delete-block/', views.BlockAPI.as_view()),

    # Room urls
    path('rooms/', views.RoomAPI.as_view()),
    path('create-room/', views.RoomAPI.as_view()),
    path('delete-room/<str:code>/', views.RoomAPI.as_view()),
]
