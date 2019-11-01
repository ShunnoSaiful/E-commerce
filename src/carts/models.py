from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    product_name     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product_name')
    product_price    = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product_price')
    product_quantity = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product_quantity')
    total_price      = models.DecimalField(max_digits=19, decimal_places=2)


    def __str__(self):
        return str(self.product_name)

