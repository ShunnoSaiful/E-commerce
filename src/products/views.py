from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from carts.models import Cart
from .models import Product, Category



def home_view(request):
    products_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        "product" : products_list,
        "category" : category_list,
    }
    return render(request, "products/index.html", context)

def product_list_view(request,slug=None):
    category = get_object_or_404(Category, slug=slug)
    products_list = Product.objects.all()
    context = {
        "product" : products_list,
        "category" : category,
    }
    return render(request, "products/category.html", context)

def product_detail_view(request,slug=None):
    product = get_object_or_404(Product, slug=slug)
    image_list = product.images.all()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(cart_obj)
    context = {
        "product" : product,
        "image_list" : image_list,
        "cart" : cart_obj,
    }
    return render(request, "products/single-product.html", context)
