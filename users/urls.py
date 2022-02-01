from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserAPI.as_view()),
    path('api/users/auth/', views.LoginAPI.as_view()),
    path('api/get-auth-token/', views.CustomAuthToken.as_view()),
]
