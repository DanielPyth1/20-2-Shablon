from django.urls import path
from .views import (ProductListView, ProductDetailView,
                    BlogPostListView, BlogPostDetailView,
                    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/new/', BlogPostCreateView.as_view(), name='blog_post_new'),
    path('blog/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
]
