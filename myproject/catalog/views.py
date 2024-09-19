from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, BlogPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'object_list'


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_post_list.html'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog_post_list')
