from django.shortcuts import render
from django.views.generic import ListView
from .models import Dish


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishs'
