from django.views.generic import TemplateView, ListView, DetailView

from .models import Post 


class IndexView(TemplateView):
    template_name = 'blog/home.html'


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
