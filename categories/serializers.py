from rest_framework import serializers
from .models import Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')
        extra_kwargs = {
            'slug': {'read_only': True}
        }

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
        extra_kwargs = {
            'slug': {'read_only': True}
        }
