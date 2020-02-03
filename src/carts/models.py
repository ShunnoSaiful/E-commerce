from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, m2m_changed

from products.models import Product
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session["cart_id"] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user 
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    product_name     = models.ManyToManyField(Product, related_name='cart_product_name')
    total_price      = models.DecimalField(default=00.00, max_digits=19, decimal_places=2)

    objects = CartManager()
    def __str__(self):
        return str(self.id)



def cart_pre_save_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action =='post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.product_price
        instance.total = total
        instance.save()


m2m_changed.connect(cart_pre_save_receiver, sender=Cart.products.through)