from django.db import models
from product.models import Product


# Create your models here.
class Inventory(models.Model):
	product 		= models.OneToOneField(Product)
	total_stock   	= models.PositiveIntegerField(default=100)
	stock   		= models.PositiveIntegerField(default=100)
	create_date     = models.DateTimeField(auto_now = True,auto_now_add = False)
	update 		    = models.DateTimeField(auto_now = False,auto_now_add = True)

	def __str__(self):
		return str(self.product)
