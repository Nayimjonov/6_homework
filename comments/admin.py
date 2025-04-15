from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content')
    search_fields = ('content', 'author__username', 'post')
    list_filter = ('post',)

