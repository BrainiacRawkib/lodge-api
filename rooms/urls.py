from django.urls import path
from . import views

urlpatterns = [
    # Block urls
    path('blocks/', views.BlockAPI.as_view()),

    # Room urls
    path('rooms/', views.RoomAPI.as_view()),
]
