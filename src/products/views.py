from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from carts.models import Cart
from .models import Product, Category, SubCategory



def product_list_view(request):
    products_list = Product.objects.all()
    new_arrival = Product.objects.all()
    category_list = Category.objects.all()
    subcategory_list = SubCategory.objects.all()
    context = {
        "product" : products_list,
        "new_arrival" : new_arrival,
        "category" : category_list,
        "subcategory" : subcategory_list,
    }
    return render(request, "products/index.html", context)

def product_detail_view(request,slug=None):
    products_list = get_object_or_404(Product, slug=slug)
    image_list = products_list.images.all()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(cart_obj)
    context = {
        "product" : products_list,
        "image_list" : image_list,
        "cart" : cart_obj,
    }
    return render(request, "products/single-product.html", context)
