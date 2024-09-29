from django.contrib import admin
from .models import Product, BlogPost, Version
from .forms import ProductForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'description', 'price', 'image')
    search_fields = ('name', 'description')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'is_published', 'view_count')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_published', 'created_at')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['product', 'version_number', 'version_name', 'is_current']