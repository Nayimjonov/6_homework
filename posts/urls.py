
from django.urls import path
from .views import PostList, PostDetail, UserPostList, PostLikeView
from comments.views import CommentList

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('<slug:slug>/like/', PostLikeView.as_view(), name='post-like'),
    path('<slug:slug>/comments/', CommentList.as_view(), name='post-comments'),
    path('user/<str:username>/', UserPostList.as_view(), name='user-posts'),
]