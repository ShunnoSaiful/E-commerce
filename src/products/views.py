from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product, Category, SubCategory



def product_list_view(request):
    products_list = Product.objects.all()
    category_list = Category.objects.all()
    subcategory_list = SubCategory.objects.all()
    context = {
        "product" : products_list,
        "category" : products_list,
        "subcategory" : subcategory_list,
    }
    return render(request, "products/index.html", context)


