from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Category, Brand, Product
from django.shortcuts import get_list_or_404
from django.db.models import Q

# Create your views here.

def main_view(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    search_product = request.GET.get('search')
    if search_product:
        products = Product.objects.filter(Q(name__icontains=search_product))
    else:
        products = get_list_or_404(Product, status = True)

    context = {
        "categories":categories,
        "brands":brands,
        "products":products,
    }
    return render(request, 'index.html', context=context)
