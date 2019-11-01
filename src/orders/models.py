from django.db import models
from carts.models import Cart
from products.models import Product
# Create your models here.
class BillingAddress(models.Model):
    street     = models.CharField(max_length=30)
    city       = models.CharField(max_length=30)
    post_code  = models.CharField(max_length=30)
    country    = models.CharField(max_length=30)

    def __str__(self):
        return str(self.city)


class ShippingAddress(models.Model):
    street     = models.CharField(max_length=30)
    city       = models.CharField(max_length=30)
    post_code  = models.CharField(max_length=30)
    country    = models.CharField(max_length=30)

    def __str__(self):
        return str(self.city)



class Order(models.Model):
    order_number     = models.IntegerField()
    customer_name    = models.CharField(max_length=50)
    buying_product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_conatct = models.CharField(max_length=15)
    customer_email   = models.EmailField()
    billing_address  = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_number)
