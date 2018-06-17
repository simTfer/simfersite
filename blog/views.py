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
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator, page, object_list, is_paginated  = self.paginate_queryset(self.queryset, self.paginate_by)
        left = max(page.number-2, 2)
        right = min(page.number+2, paginator.num_pages-1)
        page_nums = list(paginator.page_range)[left-1:right]
        if left > 2:
            page_nums.insert(0, '...')
        if right < paginator.num_pages - 1:
            page_nums.append('...')
        page_nums.insert(0, 1)
        page_nums.append(paginator.num_pages)
        context['page_nums'] = page_nums
        return context


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
