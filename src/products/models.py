from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.




class Category(models.Model):
    category = models.CharField(max_length=30)
    image    = models.ImageField(upload_to='category image/')
    slug     = models.SlugField(blank=True)


    def __str__(self):
        return str(self.category)

    def get_absolute_url(self):
        return reverse('products:product_list_view', kwargs={"slug":self.slug})





class Product(models.Model):
    product_name        = models.CharField(max_length=100)
    slug                = models.SlugField(blank=True, unique=True)
    product_image       = models.ImageField(upload_to='product image/')
    product_category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_color       = models.CharField(max_length=20)
    product_brand       = models.CharField(max_length=30)
    product_size        = models.CharField(max_length=10)
    product_description = models.TextField()
    product_price       = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock       = models.IntegerField()
    product_quantity    = models.IntegerField()
    product_review      = models.CharField(max_length=300)
    product_ratting     = models.DecimalField(max_digits=10, decimal_places=1,null=True,blank=True)

    def __str__(self):
        return str(self.product_name)
    def get_absolute_url(self):
        return reverse('products:detail', kwargs={"slug":self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return str(self.image)





def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


