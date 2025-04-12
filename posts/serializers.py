from rest_framework import serializers
from .models import Post


class PostAuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class PostCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)


class PostTagsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

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
            'slug': {'read_only': True},
            'author': {'read_only': True},
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = PostAuthorSerializer(instance.author).data
        rep['category'] = PostCategorySerializer(instance.category).data
        rep['tags'] = PostTagsSerializer(instance.tags.all(), many=True).data
        return rep