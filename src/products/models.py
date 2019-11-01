from django.db import models

# Create your models here.




class Category(models.Model):
    category_name = models.CharField(max_length=30)
    

    def __str__(self):
        return str(self.category_name)



class SubCategory(models.Model):
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=30)
    

    def __str__(self):
        return str(self.sub_category)



class Product(models.Model):
    product_name        = models.CharField(max_length=100)
    product_image       = models.ImageField(upload_to='product_image/')
    # product_category    = models.ForeignKey(Category, on_delete=models.CASCADE)
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


