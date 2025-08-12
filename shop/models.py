
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    attributes = models.ManyToManyField('Attribute')




class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)




class Attribute(models.Model):
    name = models.CharField(max_length=255)

#1111

