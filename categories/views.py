from rest_framework import generics, permissions
from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer
from posts.serializers import PostSerializer
from posts.models import Post
from .paginations import CategoryPagination, TagPagination

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class CategoryPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return Post.objects.filter(
            category__slug=category_slug,
            status='published'
        ).order_by('-created_at')


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class TagPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        return Post.objects.filter(
            tags__slug=tag_slug,
            status='published'
        ).order_by('-created_at')