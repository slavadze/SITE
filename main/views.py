from django.shortcuts import render
from .models import *


def indexPage(requests):
    return render(requests, 'index.html')


def catalogPage(requests):
    products = Product.objects.all()
    return render(requests, 'catalog.html', {'products': products})
