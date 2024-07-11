from gallery.models import Product
from users.models import Profile
from decimal import Decimal

class Cart():
    def __init__(self, request):
        # get session
        self.session = request.session
        # get request
        self.request = request
        # get the current session key if it exists
        cart = self.session.get('session_key')
        # if user is new, no session key yet. so create one
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        # lets ensure the session is available on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get product ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup products in db
        products = Product.objects.filter(id__in=product_ids)

        # return those lookup products
        return products 

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # get cart
        ourcart = self.cart
        # update cart dictionary
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)

        # get cart
        ourcart = self.cart
        # delete from cart dictionary
        if product_id in ourcart:
           del ourcart[product_id]
        # else:
        #     pass

        self.session.modified = True

    def cart_total(self):
        # get product id 
        product_ids = self.cart.keys()
        # lookup those keys in our product database table
        products = Product.objects.filter(id__in=product_ids)
        # get quantities 
        quantities = self.cart
        # start counting at 0
        total = 0
        for key, value in quantities.items():
            # convert key string into int so we can do math 
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.promo:
                        total = total + (product.promo_price * value)
                    else:
                        total = total + (product.price * value)
        return total
