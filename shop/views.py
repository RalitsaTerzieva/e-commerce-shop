from django.shortcuts import render
from .models import Order, Products
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
    
def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total = request.POST.get('total', '')
        
        order = Order(items=items,name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()
    return render(request, 'shop/checkout.html')