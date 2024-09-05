from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Главная страница со списком товаров
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Страница с деталями товара
]
