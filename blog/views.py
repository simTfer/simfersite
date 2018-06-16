from django.views.generic import TemplateView, ListView, DetailView

from .models import Post, Category, Tag


class IndexView(ListView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context


class BlogListView(IndexView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 10


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
