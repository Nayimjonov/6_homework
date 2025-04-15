# from django.urls import path
# from .views import (
#     CategoryList, CategoryDetail, CategoryPosts,
#     TagList, TagDetail, TagPosts
# )
#
# urlpatterns = [
#     path('', CategoryList.as_view(), name='category-list'),
#     path('<str:slug>/', CategoryDetail.as_view(), name='category-detail'),
#     path('<str:slug>/posts/', CategoryPosts.as_view(), name='category-posts'),
#     path('tags/', TagList.as_view(), name='tag-list'),
#     path('tags/<str:slug>/', TagDetail.as_view(), name='tag-detail'),
#     path('tags/<str:slug>/posts/', TagPosts.as_view(), name='tag-posts'),
# ]