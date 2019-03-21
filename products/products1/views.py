from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views import View
from django.db.models import Q


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'products-form.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST or None, instance = product)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'products-form.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = Product.objects.get(id = id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'prod-delete-confirm.html', {'product': product})



class SearchView(View):

    template_name = 'search.html'
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        founded_articles = Product.objects.filter(Q(description__icontains=query) | Q(description__icontains=query))
        context = {
            'founded_articles': founded_articles
        }
        return render(self.request, self.template_name, context)


# Create your views here.