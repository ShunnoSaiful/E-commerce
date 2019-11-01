from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
	name 		   = models.CharField(max_length=100)
	description	   = models.TextField(max_length=100)
	vendor		   = models.CharField(max_length=100)  
	create_date    = models.DateTimeField(auto_now = True,auto_now_add = False)
	update 		   = models.DateTimeField(auto_now = False,auto_now_add = True)

	def __str__(self):
		return self.name

