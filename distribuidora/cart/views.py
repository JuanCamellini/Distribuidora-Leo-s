from django.shortcuts import get_object_or_404, render, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products
    quantity = cart.get_quantities
    totals = cart.get_total()
    return render(request, 'cart/cart.html', {'cart_products': cart_products, 'quantity': quantity, 'totals': totals})

def cart_add(request):
    #get the cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':

        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        #lookup product in db
        product = get_object_or_404(Product, id=product_id)

        #save the session
        cart.add(product=product, quantity = product_quantity)

        #quantity
        cart_quantity = cart.__len__()

        response = JsonResponse({'quantity': cart_quantity})
        return response
        #return redirect('cart')
def cart_update(request):
    """Update a single item"""
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity = product_quantity)
        print(product_quantity)
        response = JsonResponse({'quantity': product_quantity, 'product_id': product_id})
        messages.warning(request, "Producto Actualizado")
        return response
        #return render(request, 'cart/cart_update.html', {'success':'Producto Actualizado!'})
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #delete function
        cart.delete(product=product_id)

        response = JsonResponse({'product_id': product_id})
        return response
    return render(request, 'cart/cart_delete.html')

def checkout(request):
    cart = Cart(request)
    totals = cart.get_total()
    return render(request, 'cart/checkout.html', {'totals': totals})