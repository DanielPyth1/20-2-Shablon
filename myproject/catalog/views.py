from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, BlogPost
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify


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

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog_post_detail', args=[self.object.id])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog_post_list')
