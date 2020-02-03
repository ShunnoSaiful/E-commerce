from django.db import models

# Create your models here.

class ShippingAddress(models.Model):
    street   = models.CharField(max_length=100)
    city     = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.city)



class BiliingAddress(models.Model):
    street   = models.CharField(max_length=100)
    city     = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.city)



class Customer(models.Model):
    first_name       = models.CharField(max_length=100)
    last_name        = models.CharField(max_length=100)
    username         = models.CharField(max_length=100)
    email            = models.EmailField()
    phone_number     = models.IntegerField()
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    billing_address  = models.ForeignKey(BiliingAddress, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.username)

