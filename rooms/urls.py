from django.urls import path
from . import views

urlpatterns = [
    # Block urls
    path('api/blocks/', views.BlockAPI.as_view()),

    # Room urls
    path('api/rooms/', views.RoomAPI.as_view()),
]
