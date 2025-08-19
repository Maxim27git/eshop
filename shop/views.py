from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
class AllProductsView(ListView):
    """Класс-представление для отображения списка продуктов."""
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        """Добавляет в контекст текущее время."""
        context = super().get_context_data(**kwargs)
        context["current_time"] = datetime.now()  # Передача текущей даты и времени
        return context

def all_products(request):
    """Возвращает HTML-страницу со списком продуктов и текущим временем."""
    products = Product.objects.all()
    current_time = datetime.now()  # Получение текущей даты и времени
    return render(request, "products.html", {
        "products": products,
        "current_time": current_time,  # Передача текущего времени в контекст
    })

# Create your views here.



