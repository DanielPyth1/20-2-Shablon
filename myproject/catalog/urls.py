from django.shortcuts import redirect
from django.urls import path
from .views import (
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    VersionCreateView,
    VersionUpdateView,
    unpublish_product,
)

urlpatterns = [
    path('', lambda request: redirect('product_list')),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', unpublish_product, name='unpublish_product'),
    path('version/<int:pk>/edit/', VersionUpdateView.as_view(), name='version_edit'),
    path('product/<int:pk>/version/add/', VersionCreateView.as_view(), name='version_add'),
    path('blog/new/', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
]
