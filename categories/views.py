from django.utils.text import slugify
from rest_framework import viewsets
from .models import Category, Tag
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'