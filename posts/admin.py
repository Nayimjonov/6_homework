from django.contrib import admin
from .models import Post


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