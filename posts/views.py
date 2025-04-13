from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostLikeSerializer
from .paginations import PostPagination
from comments.models import PostLike


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], url_path='like')
    def like(self, request, slug=None):
        post = self.get_object()
        serializer = PostLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        like_obj, created = PostLike.objects.get_or_create(
            post=post,
            author=request.user,
            defaults={'value': serializer.validated_data['value']}
        )
        if not created:
            like_obj.value = serializer.validated_data['value']
            like_obj.save()
        return Response({
            'value': like_obj.value
        }, status=status.HTTP_200_OK)

    # @action(detail=True, methods=['post'], url_path='comment')
    # def comment(self, request, slug=None):
    #     post = self.get_object()
    #     serializer = CommentSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(post=post, author=request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # @action(detail=True, methods=['get'], url_path='comments')
    # def get_comments(self, request, slug=None):
    #     post = self.get_object()
    #     comments = post.comments.all()
    #     serializer = CommentSerializer(comments, many=True)
    #     return Response(serializer.data)