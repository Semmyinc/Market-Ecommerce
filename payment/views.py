from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from django.contrib.auth.models import User
from .forms import ShippingForm, PaymentForm
from django.contrib import messages
from .models import ShippingAddress, Order, OrderItem
from users.models import Profile
# Create your views here.

def payment_success(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total
    form = ShippingForm()
    if request.method == 'POST':
        shipping_user = get_object_or_404(ShippingAddress, user__id=request.user.id)
        # shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Shipping Details Added')
            return redirect('payment_success')
        else:
            messages.error(request, f'Oops! There was an error submitting the form. Please try again.')
            return render(request, 'payment/payment_success.html', {})
    else:
        shipping_user = get_object_or_404(ShippingAddress, user__id=request.user.id)
        # shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = ShippingForm(instance=shipping_user)

    context = {'title':'Payment Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'form':form}
    return render(request, 'payment/payment_success.html', context)

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total
    form = ShippingForm()
    # checkout as a logged in user 
    if request.user.is_authenticated:
        shipping_user = get_object_or_404(ShippingAddress, user__id=request.user.id)
        # if request.method == 'POST':
        form = ShippingForm(request.POST or None, instance=shipping_user)
        context = {'title':'Payment Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'form':form}
        return render(request, 'payment/checkout.html', context)
            # if form.is_valid():
            #     form.save()
            #     messages.success(request, f'shipping details registered')
    else:
        # checkout as a guest
        form = ShippingForm(request.POST or None)
        context = {'title':'Payment Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'form':form}
        return render(request, 'payment/checkout.html', context)
    

def billing_info(request):
    if request.POST:   
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total

        # create a session with shipping info 
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
        # check to see if user is logged in 
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            context = {'title':'Payment Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_details':request.POST, 'billing_form':billing_form}
            return render(request, 'payment/billing_info.html', context)
        else:
            # not logged in 
            
            billing_form = PaymentForm()
            context = {'title':'Payment Page', 'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_details':request.POST, 'billing_form':billing_form}
            return render(request, 'payment/billing_info.html', context)
    else:
        messages.info(request, f'Oops! Access Denied.')
        return redirect('home')
    
def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total

        # get the billing info from last page 
        payment_form = PaymentForm(request.POST or None)
        # get shipping session data 
        my_shipping = request.session.get('my_shipping')
        
        # gather order info 
        fullname = my_shipping['shipping_fullname']
        email = my_shipping['shipping_email']
        
        # get shipping address from the info stored in session 
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_paid = totals()

        # create an order 
        if request.user.is_authenticated:
            # logged in user 
            user = request.user
            create_order = Order(user=user, fullname=fullname, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            
            create_order.save()

            # add order item 
            # get the order id 
            order_id = create_order.pk
            # get product id
            for product in cart_products():
                product_id = product.id

                # get product price 
                if product.promo:
                    price = product.promo_price
                else:
                    price = product.price
                # get quantity 
                for key, value in quantities().items():
                    if int(key) == product.id:
                        # create orderitem 
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        create_order_item.save()
            
            # delete our cart
            for key in list(request.session.keys()):
                if key == 'session_key':
                    # delete the key
                    del request.session[key]
            
            # # delete cart from database (old_cart field)
            # current_user = Profile.objects.filter(user__id=request.user.id)
            # # delete shopping cart in db (old_cart field) 
            # current_user.update(old_cart='')


            messages.success(request, f'You just placed an Order')
            return redirect('home')

        else:
            # not logged in 
            # create order 
            create_order = Order(fullname=fullname, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            # add order item 
            # get the order id 
            order_id = create_order.pk
            # get product id
            for product in cart_products():
                product_id = product.id

                # get product price 
                if product.promo:
                    price = product.promo_price
                else:
                    price = product.price
                # get quantity 
                for key, value in quantities().items():
                    if int(key) == product.id:
                        # create orderitem 
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        create_order_item.save()


            # delete our cart
            for key in list(request.session.keys()):
                if key == 'session_key':
                    # delete the key
                    del request.session[key]
                    # print(my_shipping)
            messages.success(request, f'You just placed an order')
            return redirect('home')
                    # context = {'title':'Payment Page'}
                    # return render(request, 'payment/process_order.html', context)
    else:
        messages.info(request, f'Oops! Access Denied.')
        return redirect('home')
        # context = {'title':'Payment Page'}
        # return render(request, 'payment/process_order.html', context)   
def specific_order(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        # specific_order = Order.objects.get(id=pk)
        specific_order = get_object_or_404(Order, id=pk)
        specific_order_items = OrderItem.objects.filter(order__id=specific_order.id)

        if request.POST:
            status = request.POST['shipping_status']
            # check if true or false 
            if status == 'true':
                order = Order.objects.filter(id=pk)
                # update the status 
                order.update(shipped=True)
                messages.success(request, 'Shipping status updated')
                return redirect('all_order')
            else:
                order = Order.objects.filter(id=pk)
                # update the status 
                order.update(shipped=False)
                messages.success(request, 'Shipping status updated')
                return redirect('all_order')

        context = {'title':'Shipped Orders', 'specific_order':specific_order, 'specific_order_items':specific_order_items}
        return render(request, 'payment/specific_order.html', context)
    else:
        messages.info(request, f'Access Denied')
        return redirect('home')

def all_order(request):
    if request.user.is_authenticated and request.user.is_superuser:
        all_orders = Order.objects.all
        context = {'title':'Shipped Orders', 'all_orders':all_orders}
        return render(request, 'payment/all_order.html', context)
    else:
        messages.info(request, f'Access Denied')
        return redirect('home')
    

def shipped_order(request):
    if request.user.is_authenticated and request.user.is_superuser:
        shipped_orders = Order.objects.filter(shipped=True)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            # grab the order 
            order = Order.objects.filter(id=num)
            # update order 
            order.update(shipped=False)
            messages.success(request, f'Shipping status updated')
            return redirect('all_order') 
        context = {'title':'Shipped Orders', 'shipped_orders':shipped_orders}
        return render(request, 'payment/shipped_order.html', context)
    else:
        messages.info(request, f'Access Denied')
        return redirect('home') 
    
       

def unshipped_order(request):
    if request.user.is_authenticated and request.user.is_superuser:
        unshipped_orders = Order.objects.filter(shipped=False)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            # grab the order 
            order = Order.objects.filter(id=num)
            # update order 
            order.update(shipped=True)
            messages.success(request, f'Shipping status updated')
            return redirect('all_order')
        context = {'title':'Unshipped Orders', 'unshipped_orders':unshipped_orders}
        return render(request, 'payment/unshipped_order.html', context)
    else:
        messages.info(request, f'Access Denied')
        return redirect('home')
      