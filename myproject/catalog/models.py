from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False, help_text="Indicates if this is the current version of the product.")

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
