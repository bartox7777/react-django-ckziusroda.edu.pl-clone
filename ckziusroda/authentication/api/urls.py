from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/login/', views.LoginAPI.as_view()),
    path('auth/user/', views.UserAPI.as_view())
]