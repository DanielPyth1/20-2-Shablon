from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'includes/product_detail.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'includes/product_list.html', context)