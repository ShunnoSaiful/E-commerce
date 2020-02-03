from django.shortcuts import render
from django.db.models import Q

from products.models import Product, Category, SubCategory



def product_search_view(request):
    product_list = []
    new_arrival = Product.objects.all()
    category_list = Category.objects.all()
    subcategory_list = SubCategory.objects.all()


    query = request.GET.get("q")
    print(query)
    if query:
        product_list = Product.objects.filter(
                Q(product_name__icontains=query)|
                Q(product_brand__icontains=query)|
                Q(product_category__sub_category__icontains=query)|
                Q(product_category__category__category_name__icontains=query)|
                Q(product_name__icontains=query)
                ).distinct()
    print(product_list)
    
    context = {
        "product_list" : product_list,
        "new_arrival" : new_arrival,
        "category" : category_list,
        "subcategory" : subcategory_list,
    }
    return render(request, "search/search.html", context)
