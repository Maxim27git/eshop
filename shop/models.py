
from django.db import models
class ProductManager(models.Manager):
    def in_stock(self):
        return self.get_queryset().filter(stock__gt=0)

    def get_sorted_by_price_desc(self):
        """Возвращает товары, отсортированные по цене от большего к меньшему."""
        return self.order_by("-price")

    def get_sorted_by_price_asc(self):
        """Возвращает товары, отсортированные по цене от меньшего к большему."""
        return self.order_by("price")
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    attributes = models.ManyToManyField('Attribute')
    objects = ProductManager()




class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)




class Attribute(models.Model):
    name = models.CharField(max_length=255)

#1111

