
from django.db import models
class ProductManager(models.Manager):
    def in_stock(self):
        return self.get_queryset().filter(stock__gte=3)

    def get_sorted_by_price_desc(self):
        """Возвращает товары, отсортированные по цене от большего к меньшему."""
        return self.order_by("-price")

    def get_sorted_by_price_asc(self):
        """Возвращает товары, отсортированные по цене от меньшего к большему."""
        return self.order_by("price")
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название" )
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    stock = models.IntegerField(verbose_name="В наличие")
    attributes = models.ManyToManyField('Attribute')
    objects = ProductManager()

    def __str__(self):
        return self.title

class Meta:
        db_table = 'product'
        indexes = [models.Index(fields=["price"])]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    #image = models.ImageField(upload_to="products", verbose_name="Изображение")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)




class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


#1111

