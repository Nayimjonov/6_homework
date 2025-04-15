from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me/', views.MeView.as_view(), name='me'),
    path('users/<str:username>/', views.PublicUserProfileView.as_view(), name='user_profile'),
    path('users/<str:username>/comments/', views.UserCommentsView.as_view(), name='user_comments'),
]
