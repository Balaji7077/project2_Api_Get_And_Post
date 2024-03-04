from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    product_category_id=models.IntegerField(primary_key=True)
    product_category_name=models.CharField(max_length=100)
    

    def __str__(self):
        return self.product_category_name

class Product(models.Model):
    product_category_id=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name