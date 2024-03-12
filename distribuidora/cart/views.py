from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart/cart.html')

def cart_add(request):
    #get the cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #lookup product in db
        product = get_object_or_404(Product, id=product_id)
        #save the session
        cart.add(product=product)
        response = JsonResponse({'Product name: ': product.name})
        return response

def cart_update(request):
    return render(request, 'cart/cart_update.html')

def cart_delete(request):
    return render(request, 'cart/cart_delete.html')