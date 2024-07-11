from django.shortcuts import render, get_object_or_404
from .cart import Cart
from gallery.models import Product
from django.http import JsonResponse
from decimal import Decimal
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    context = {'title':'Cart Summary Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals}
    return render(request, 'cart/cart_summary.html', context)

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # lookup product in the db
        product = get_object_or_404(Product, id=product_id)
        
        # save to our session
        cart.add(product=product, quantity=product_qty)

        # get cart qty
        cart_quantity = cart.__len__()
        # return response
        # response =  JsonResponse({'Product Name: ': product.name})
        response =  JsonResponse({'qty': cart_quantity})
        return response
    # context = {}
    # return render(request, 'cart/cart_add.html', context)

def cart_update(request):
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({'qty':product_qty})
        return response
        # return redirect('cart_summary')
    # context = {}
    # return render(request, 'cart/cart_update.html', context)

def cart_delete(request):
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        # get stuff
        # product_id = int(request.POST.get('product_id'))
        product_id = request.POST.get('product_id')
        # product_qty = int(request.POST.get('product_qty'))
        
        cart.delete(product=product_id)
        
        response = JsonResponse({'product':product_id})
        return response
    # context = {}
    # return render(request, 'cart/cart_delete.html', context)