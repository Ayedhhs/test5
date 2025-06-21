from django.shortcuts import render
from .models import Product

# عرض قائمة المنتجات
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
