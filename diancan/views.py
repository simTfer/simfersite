from django.shortcuts import render
from django.views.generic import ListView

from .models import Dish, Menu


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'


class TodayDishView(ListView):
    def get_queryset(self):
        month = self.kwargs['month']
        day = self.kwargs['day']
        time_quantum = self.kwargs['quantum']
        return Menu.objects.filter(
            menu_date__month=month,
            menu_date__day=day,
            time_quantum=time_quantum)
