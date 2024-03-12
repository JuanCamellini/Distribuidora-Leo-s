from .cart import Cart

#create context processors so our cart can work in all pages
def cart(request):
    return {'cart': Cart(request)}