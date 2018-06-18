from django.urls import path
from .views import BlogListView, BlogDetailView, CategoryView


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('category/<category>/', CategoryView.as_view(), name='blog_category'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
