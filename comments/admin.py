from django.contrib import admin
from .models import Comment, PostLike

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content')
    search_fields = ('content', 'author__username', 'post')
    list_filter = ('post',)

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'value',)
    search_fields = ('author__username', 'post')
    list_filter = ('value', 'post')
