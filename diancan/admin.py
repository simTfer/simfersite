from django.contrib import admin
from .models import Consumer, Menu, Dish, Favorite


@admin.register(Consumer, Menu, Dish, Favorite)
class BlogAdmin(admin.ModelAdmin):
    pass
