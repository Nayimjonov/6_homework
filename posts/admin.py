from django.contrib import admin
from .models import Post, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'status',
    )
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('status', 'category', 'tags')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'value',)
    search_fields = ('author__username', 'post')
    list_filter = ('value', 'post')
