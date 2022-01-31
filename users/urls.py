from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views

urlpatterns = [
    path('api/users/', views.UserAPI.as_view()),
    path('api/users/auth/', views.LoginAPI.as_view()),
    path('api/get-auth-token/', rest_views.obtain_auth_token),
]
