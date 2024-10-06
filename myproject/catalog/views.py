from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import F
from .models import Product, BlogPost, Version
from .forms import ProductForm, VersionForm
from django.utils.text import slugify

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        product.current_version = Version.objects.filter(product=product, is_current=True).first()  # Находим текущую версию
        context['product'] = product
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.current_version = Version.objects.filter(product=product, is_current=True).first()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

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
        BlogPost.objects.filter(pk=obj.pk).update(view_count=F('view_count') + 1)
        return obj

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_post_detail', args=[self.object.slug])

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog_post_detail', args=[self.object.slug])

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog_post_list')

class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])  # Получаем продукт
        form.instance.product = product  # Связываем версию с продуктом
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])  # Передаем продукт в шаблон
        return context

class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.object.product.pk])
