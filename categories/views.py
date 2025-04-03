from rest_framework import viewsets
from .models import Category, Tag
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    
