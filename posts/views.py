from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostLikeSerializer
from .paginations import PostPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], url_path='like', permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self, request, slug=None):
        post = self.get_object()
        serializer = PostLikeSerializer(
            data=request.data,
            context={'request': request, 'post': post}
        )
        serializer.is_valid(raise_exception=True)
        like = serializer.save()
        return Response({
            'value': like.value
        }, status=status.HTTP_200_OK)
