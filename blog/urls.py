from django.urls import path
from .views import AboutView, BlogListView, BlogDetailView, CategoryView, TagView, ArchiveView


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('about/', AboutView.as_view(), name='blog_about'),
    path('category/<category>/', CategoryView.as_view(), name='blog_category'),
    path('tag/<tag>/', TagView.as_view(), name='blog_tag'),
    path('archive/<int:year>/<int:month>/', ArchiveView.as_view(), name='blog_archive'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
