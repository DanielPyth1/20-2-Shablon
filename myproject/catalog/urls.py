from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('product_list')),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('version/<int:pk>/edit/', views.VersionUpdateView.as_view(), name='version_edit'),
    path('product/<int:pk>/version/add/', views.VersionCreateView.as_view(), name='version_add'),
    path('blog/new/', views.BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/<slug:slug>/update/', views.BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='blog_post_delete'),
]