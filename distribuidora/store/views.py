from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q 

def home(request):
    return render(request, 'store/index.html', {})

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

def categoria_resumen(request):
    categories = Category.objects.all()
    products = Product.objects.all
    return render(request, 'store/product.html', {'categories': categories, 'products':products})

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
    return render(request, 'store/product-single.html', {'product':product})

def about(request):
    return render(request, 'store/about.html', {})

def contact(request):
    return render(request, 'store/contact.html', {})

def cart(request):
    return render(request, 'store/cart.html', {})

def base(request):
    return render(request, 'store/base.html', {})