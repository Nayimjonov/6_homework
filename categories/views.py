from django.contrib.admin.templatetags.admin_list import pagination
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Category, Tag
from .serializers import CategorySerializer
from .paginations import CategoryPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    # @action(['GET'])
    # def
