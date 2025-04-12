from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from posts.serializers import PostSerializer
from rest_framework.exceptions import PermissionDenied
from posts.models import Post
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, AnonymousUser):
            raise PermissionDenied("Sizni autentifikatsiyalash talab qilinadi.")

        return Post.objects.filter(author=user)