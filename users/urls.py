from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='user_create'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('users/<str:username>/posts/', views.UserPostsView.as_view(), name='user_posts'),

]