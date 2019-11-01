from django.contrib import admin
from .models import SubCategory, Category, Product


# Register your models here.



admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)