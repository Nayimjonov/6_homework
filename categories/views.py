from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer
from .paginations import CategoryPagination, TagPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    # @action(['GET'])
    # def

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
