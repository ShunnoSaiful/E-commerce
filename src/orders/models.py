from django.db import models
from carts.models import Cart
from products.models import Product
from django.db.models.signals import pre_save, post_save
from .utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
    )





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
    order_id      = models.CharField(max_length=120, blank=True, null=True)
    cart              = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    #billing_address  = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    #shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    order_status      = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total    = models.DecimalField(default=5.99, max_digits=10, decimal_places=2)
    total             = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order_id)

    def update_total(self):
        cart_total = self.cart.total_price
        shipping_total = self.shipping_total
        new_total = cart_total + shipping_total
        self.total = new_total
        self.save()

        return new_total


def pre_save_order_id_create(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    print(instance.order_id)

pre_save.connect(pre_save_order_id_create, sender=Order)


def post_save_cart_total(sender,created, instance, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total_price
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, created, instance, *args, **kwargs):
    if created:
        instance.update_total()



post_save.connect(post_save_order, sender=Order)