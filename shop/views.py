from django.shortcuts import render
from .models import Products
from django.views.generic.list import ListView


class ProductsListView(ListView):
    model = Products
    template_name = 'shop/index.html'
    paginate_by = 4
    
    def get_queryset(self):
        queryset = super().get_queryset()
        item_name = self.request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            queryset = queryset.filter(title__icontains=item_name)
            
        return queryset