from django.shortcuts import render
from .models import Products
from django.views.generic.list import ListView

class ProductsListView(ListView):
    model = Products
    template_name = 'shop/index.html'
