from django.shortcuts import render
from .models import *

from django.views.generic import ListView, DetailView # новое

# новое
class CatalogListView(ListView):
    model = Product
    template_name = 'catalog.html'

# новое
class CatalogDetailView(DetailView):  # новое
    model = Product
    template_name = 'product_detail.html'

# новое
class CartDetailView(DetailView):  # новое
    model = Product
    template_name = 'cart.html'

def indexPage(requests):
    return render(requests, 'index.html')


def catalogPage(requests):
    products = Product.objects.all()
    return render(requests, 'catalog.html', {'products': products})

def categoryPage(requests):
    categories = Category.objects.all()
    return render(requests, 'category.html', {'categories': categories})