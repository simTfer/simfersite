from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category, Tag)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
