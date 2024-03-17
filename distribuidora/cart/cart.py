from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session
        # get the current session key if it exists
        cart = self.session.get('session_key')
        # if the user is new, there isnt session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        # make sure cart is available on all pages
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id) 
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else: 
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)
        self.session.modified = True

    def get_total(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)
        
        total = 0
        for product_id, product_quantity in self.cart.items():
            key = int(product_id)
            for product in products:
                if product.id == key:
                    total += product.price * product_quantity
        return total

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #use ids to look up products in database
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quantities(self):
        return self.cart
    
    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)
        
        ourcart = self.cart
        ourcart[product_id] = product_quantity
        
        self.session.modified = True

        t = self.cart
        return t

    def delete(self, product):
        product_id = str(product)
        #delete from dictionaryu
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
        