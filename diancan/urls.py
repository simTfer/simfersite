from django.urls import path
from .views import DishListView


app_name = 'diancan'
urlpatterns = [
    path('', DishListView.as_view(), name='dish_list'),
]