from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from inventory.models import Inventory
from django.db.models.signals import pre_save, post_save

class Invoice(models.Model):
	invoice_to 		= models.TextField()
	invoice_note 	= models.TextField(null=True, blank=True)
	invoice_date 	= models.DateTimeField()
	discount     	= models.PositiveIntegerField(default=0)
	total_invoice_price = models.PositiveIntegerField(default=0)
	created_by   	= models.ForeignKey(User,on_delete=models.CASCADE)


	def __str__(self):
		return self.invoice_to



class InvoiceProduct(models.Model):
	invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
	total_price = models.PositiveIntegerField(default=0)
	price       = models.PositiveIntegerField(default=0)
	quantity	= models.PositiveIntegerField(default=1)
	product 	= models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.product)
