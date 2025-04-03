from asyncio.events import on_fork
from asyncio.windows_events import CONNECT_PIPE_MAX_DELAY

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category, Tag


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    featured_image = models.ImageField(upload_to='post_images/')


