from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# POST /api/auth/register/
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# GET /api/users/
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# GET /api/users/me/
class MyProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

# PUT /api/users/me/
class UpdateMyProfileView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

# GET /api/users/<username>/
class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.select_related('user')

    def get_object(self):
        username = self.kwargs['username']
        return UserProfile.objects.get(user__username=username)
