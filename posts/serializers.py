from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'author',
            'category',
            'tags',
            'created_at',
            'updated_at',
            'status',
            'featured_image',
        )
        extra_kwargs = {
            'slug': {'read_only': True}
        }