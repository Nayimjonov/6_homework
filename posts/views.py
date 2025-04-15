from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer, PostLikeSerializer
from .paginations import PostPagination
from users.permissions import IsAuthorOrReadOnly, IsPostAuthorOrAdminOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.objects.filter(status='published')


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthorOrAdminOrReadOnly]
    lookup_field = 'slug'


class PostLikeView(generics.GenericAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request, 'post': post}
        )
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        return Response({
            'value': like.value
        }, status=status.HTTP_200_OK)


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        if self.request.user.is_authenticated:
            return Post.objects.filter(author=user)
        else:
            return Post.objects.filter(
                author=user,
                status='published'
            )