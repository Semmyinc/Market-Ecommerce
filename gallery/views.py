from django.shortcuts import render, redirect,get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm, CategoryForm
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'title':'Home', 'products':products}
    return render(request, 'gallery/index.html', context)

def about(request):
    context = {'title':'About Us'}
    return render(request, 'gallery/about.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    related_product = Product.objects.filter(category=product.category).exclude(id=pk)
    context = {'title':'Product Detail', 'product':product, 'related_product':related_product}
    return render(request, 'gallery/product.html', context)

def category_summary(request):
    categories = Category.objects.all()
    
    context = {'title':'Product Category', 'categories':categories}
    return render(request, 'gallery/category_summary.html', context)

def category(request, word):
    word = word.replace('_', ' ')
    try:
        category = Category.objects.get(name=word)
        products = Product.objects.filter(category=category)
        context = {'title':'Product Category', 'category':category, 'products':products}
        return render(request, 'gallery/category.html', context)
    except:
        messages.info(request, f'That Category doesn\'t exist')
        return redirect('/')

def add_category(request):
    ac_form = CategoryForm()
    if request.method == 'POST':
        ac_form = CategoryForm(request.POST)
        if ac_form.is_valid():
            ac_form.save()
            messages.success(request, f'New category added successfully')
            return redirect('category_summary')
        else:
            messages.info(request, f'There was an error adding the new category. Please try again')
            return render(request, 'gallery/add_category.html', {'form':ac_form})
    else:
        return render(request, 'gallery/add_category.html', {'form':ac_form})
      
    #  context = {}
    #  return render(request, 'gallery/add_category.html', context)

def edit_category(request, word):
    ec_form = CategoryForm()
    if request.method == 'POST':
        # category = Category.objects.get(id=word)
        category = get_object_or_404(Category, id=word)
        ec_form = CategoryForm(request.POST or None, instance=category)
        if ec_form.is_valid():
            ec_form.save()
            messages.success(request, f'Product Category edited updated successfully')
            return redirect('category_summary')
        else:
            messages.alert(request, f'There was an error updating the Product Category. Please try again')
            return render(request, 'gallery/edit_category.html', {'form':ec_form})
    else:
        # category = Category.objects.get(id=word)
        category = get_object_or_404(Category, id=word)
        ec_form = CategoryForm(request.POST or None, instance=category)
        return render(request, 'gallery/edit_category.html', {'form':ec_form})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        search = Product.objects.filter(Q(name__icontains=search)|
                                        Q(description__icontains=search)|
                                        Q(price__icontains=search)|
                                        Q(promo_price__icontains=search)
                                        )
        if not search:
            messages.info(request, f'Sorry, no result for that search') 
        #    context = {'title':'Search', 'searched':searched}
            return render(request, 'gallery/search.html', {})
        else:
            return render(request, 'gallery/search.html', {'search':search})
    else:
        return render(request, 'gallery/search.html', {})
    
    
    # context = {'title':'Search Bar', 'search':search}
    # return render(request, 'navbar.html', context)

def upload_product(request):
    up_form = ProductForm()
    
    if request.user.is_authenticated:
        if request.method == "POST":
            up_form = ProductForm(request.POST or None, request.FILES or None)
            if up_form.is_valid():
            
                # up_form.save
                # product_user_id = request.user.id
                # up_form = up_form['product_user_id']
                up_form.save()
                messages.success(request, f'Product Uploaded Successfully. Weldone!')
                return redirect('/')
            else:
                messages.error(request, f'There is an error with  uploading the product. Please try again')
                return render(request, 'gallery/upload_product.html', {'form':up_form})
        else:
            # messages.error(request, f'There was an error with uploading your product. Please try again')
            # return redirect('upload_product')
            return render(request, 'gallery/upload_product.html', {'form':up_form})
    else:
        messages.error(request, f'You must be logged in to view that page')
        # context = {'title':'Upload Product', 'up_form':up_form}
        return redirect('login')
    
def edit_product(request, pk):

    ep_form = ProductForm()
    # product = get_object_or_404(Product, id=pk)
    if request.user.is_authenticated and request.user.is_superuser:
        # product = get_object_or_404(Product, id=pk)
        if request.method == "POST":
            product = get_object_or_404(Product, id=pk)
            ep_form = ProductForm(request.POST or None, request.FILES or None, instance=product)
            if ep_form.is_valid():
            
                # up_form.save
                # product_user_id = request.user.id
                # up_form = up_form['product_user_id']
                ep_form.save()
                messages.success(request, f'Product Edited Successfully. Weldone!')
                return redirect('home')
            else:
                messages.error(request, f'There is an error with  editing this product. Please try again')
                return render(request, 'gallery/edit_product.html', {'form':ep_form})
        else:
            product = get_object_or_404(Product, id=pk)
            ep_form = ProductForm(instance=product)
            # messages.error(request, f'There was an error with uploading your product. Please try again')
            # return redirect('upload_product')
            return render(request, 'gallery/edit_product.html', {'form':ep_form})
    else:
        messages.error(request, f'You must log in as a staff to view this page')
        # context = {'title':'Upload Product', 'up_form':up_form}
        return redirect('login')
    