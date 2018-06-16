from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import View

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        page_range = context['paginator'].page_range
        first = max(page_obj.number-2, 1)
        last = min(page_obj.number+2, page_range[-1])
        context['paginator'] = page_range[first:last+1]
        return context


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
