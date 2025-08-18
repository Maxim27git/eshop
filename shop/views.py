from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
def  all_products(request):
    products=Product.objects.all()
    body=''' <!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Список продуктов</title>
    </head>
    <body>
    <h1> Список продуктов</h1>
    <ul>
    '''
    if products.exists():
        for product in products:
            body += f'<li>{product.title} - {product.price}-{product.stock}-{product.attributes}</li>'

    else:
        body+= '<li>Продукты отсутствуют</li>'


    body += '''
    </ul>
    </body>
</html>'''
    return HttpResponse(body)
# Create your views here.



