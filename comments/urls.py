from django.urls import path
from .views import CommentList, CommentDetail

urlpatterns = [
    path('<int:id>/', CommentDetail.as_view(), name='comment-detail'),
]