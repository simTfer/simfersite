from django.views.generic import ListView, DetailView
# from django.views.generic.list import MultipleObjectMixin
# from django.views.generic.base import View

from .models import Post, Category, Tag


class IndexView(ListView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class BlogListView(IndexView):
    queryset = Post.objects.all()
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
