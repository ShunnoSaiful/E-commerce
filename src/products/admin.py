from django.contrib import admin
from .models import SubCategory, Category, Product, ProductImage


# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]

admin.site.register(Product, ProductAdmin)