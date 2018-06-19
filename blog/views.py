from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Count

from .models import Post, Category, Tag


class IndexView(ListView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.annotate(count=Count('post'))
        context['tags'] = Tag.objects.annotate(count=Count('post'))
        blog_dates = Post.objects.dates('created_time', 'month', order='DESC')
        blog_dates_dict = {}
        for blog_date in blog_dates:
            blog_count = Post.objects.filter(created_time__year=blog_date.year,
                                             created_time__month=blog_date.month).count()
            blog_dates_dict[blog_date] = blog_count
        context['dates'] = blog_dates_dict
        return context


class BlogListView(IndexView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 分页功能
        # Returns a 4-tuple containing (paginator, page, object_list, is_paginated).
        queryset = self.get_queryset()
        page_context = self.paginate_queryset(queryset, self.paginate_by)
        paginator = page_context[0]
        page = page_context[1]
        left = max(page.number-2, 2)
        right = min(page.number+2, paginator.num_pages-1)
        page_nums = list(paginator.page_range)[left-1:right]
        if left > 2:
            page_nums.insert(0, '...')
        if right < paginator.num_pages - 1:
            page_nums.append('...')
        page_nums.insert(0, 1)
        if paginator.num_pages != 1:
            page_nums.append(paginator.num_pages)
        context['page_nums'] = page_nums
        return context


class CategoryView(BlogListView):
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(category=self.category)


class TagView(BlogListView):
    
    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        return Post.objects.filter(tags=self.tag)


class ArchiveView(BlogListView):
    
    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Post.objects.filter(created_time__year=year, created_time__month=month)


class BlogDetailView(IndexView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
