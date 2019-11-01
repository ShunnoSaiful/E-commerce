from django.contrib import admin
from .models import Order, BillingAddress, ShippingAddress


# Register your models here.



admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
