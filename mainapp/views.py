from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Category, Brand, Product
from django.shortcuts import get_list_or_404

# Create your views here.

def main_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = get_list_or_404(Product, status = True)

    context = {
        "categories":categories,
        "brands":brands,
        "products":products,
    }
    return render(request, 'index.html', context=context)