from django.contrib import admin
from .models import InvoiceProduct,Invoice

# Register your models here.
admin.site.register(InvoiceProduct)
admin.site.register(Invoice)

