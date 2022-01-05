from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Category, Brand, Product

# Create your views here.

def main_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()

    context = {
        "categories":categories,
        "brands":brands,
        "products":products,
    }
    return render(request, 'index.html', context=context)
