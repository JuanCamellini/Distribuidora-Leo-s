from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q 
from django.views.generic import ListView
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products':products, 'title':'Home'})

def catalogo(request):
    products = Product.objects.all
    return render(request, 'store/product.html', {'products':products})

def category(request, foo):
    #replace hyphens with spaces
    foo = foo.replace('-', ' ')
    #grab the category from the url
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products':products, 'category':category})
    except:
        messages.success(request, "La categoria no existe")
        return redirect('home')

class CategoriaResumen(ListView):
    model = Category
    template_name = 'store/product.html'
    paginate_by = 12
    context_object_name = 'categories'
    is_paginated = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context
def categoria_resumen(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    p = Paginator(products, 12)
    page = request.GET.get('page')
    paginator = p.get_page(page)
    return render(request, 'store/product.html', {'categories': categories, 'products':products, 'paginator':paginator})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched) | Q(description__contains=searched))
        if products.count() == 0:
            messages.success(request, "No hay resultados")
            return render(request, 'store/search.html', {'error':"No hay resultados"})
        return render(request, 'store/search.html', {'searched':searched, 'products':products})
    else:
        return render(request, 'store/search.html', {})

def productSingle(request, pk):
    product = Product.objects.get(id=pk)
    category = product.category
    related = Product.objects.filter(category=category).exclude(id=pk)[:3]
    return render(request, 'store/product-single.html', {'product':product, 'related':related})

def about(request):
    return render(request, 'store/about.html', {})

def contact(request):
    return render(request, 'store/contact.html', {})

def cart(request):
    return render(request, 'store/cart.html', {})

def base(request):
    return render(request, 'store/base.html', {})