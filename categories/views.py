from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer
from .paginations import CategoryPagination, TagPagination
from posts.models import Post



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    # @action(detail=True, methods=['get'], url_path='posts')
    # def category_posts(self, request, slug=None):
    #     category = self.get_object()
    #     posts = Post.objects.filter(category=category, status='published').order_by('-created_at')
    #     paginator = PostPagination()
    #     result_page = paginator.paginate_queryset(posts, request)
    #     serializer = PostSerializer(result_page, many=True, context={'request': request})
    #     return paginator.get_paginated_response(serializer.data)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
