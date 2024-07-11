from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegForm, UserUpdateForm, ProfileForm, UserInfoForm
from payment.forms import ShippingForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from payment.models import ShippingAddress
# Create your views here.

def register(request):
     reg_form = UserRegForm()
     if request.method == 'POST':
         reg_form = UserRegForm(request.POST)
         if reg_form.is_valid():
             reg_form.save()
             username = reg_form.cleaned_data.get('username')
             messages.success(request, f'Congrats {username}! Registration successful. Please proceed to fill the profile form')
             return redirect('profile')
         
     context = {'title':'User Registration', 'reg_form':reg_form}
     return render(request, 'users/register.html', context)

def login_page(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
        login(request, user)
        messages.success(request, f'Welcome {request.user}! You have been successfully logged in')
        return redirect('home')
       else:
            messages.info(request, f'Incorrect Username or Password')
            return redirect('login')
    else:
        context = {'title':'User login'}
        return render(request, 'users/login.html', context)

def logout_page(request):
    logout(request)
    messages.success(request, f'You have been logged out. Thanks for stopping by')
    return redirect('/')
    
@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'weldone {request.user}! Your Profile has just been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {'title':'User Profile', 'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'users/profile.html', context)

def userinfo(request):
    if request.user.is_authenticated:
        # get current user 
        current_user = Profile.objects.get(user=request.user)
        shipping_user = ShippingAddress.objects.get(user=request.user)
        b_form = UserInfoForm()
        s_form = ShippingForm()
        if request.method == 'POST':
            # current_user = Profile.objects.get(user=request.user)
            # shipping_user = ShippingAddress.objects.get(user=request.user)
            b_form = UserInfoForm(request.POST or None, instance=current_user)
            s_form = ShippingForm(request.POST or None, instance=shipping_user)
            if b_form.is_valid() and s_form.is_valid():
                b_form.save()
                s_form.save()
                messages.success(request, f'Information updated successfully')
                return redirect('userinfo')
            else:
                messages.warning(request, f'There was an error submitting the form. Please try again')
                context = {'title':'User Information', 'b_form':b_form, 's_form':s_form}
                return render(request, 'users/userinfo.html', context)
        else:
            # current_user = Profile.objects.get(user=request.user)
            # shipping_user = ShippingAddress.objects.get(user=request.user)
            b_form = UserInfoForm(instance=current_user)
            s_form = ShippingForm(instance=shipping_user)
            context = {'title':'User Information', 'b_form':b_form, 's_form':s_form}
            return render(request, 'users/userinfo.html', context)
    else:
        messages.alert(request, f'Oops! You must be logged in to access that page.')
        return redirect('login')
        # context = {'title':'User Information', 'b_form':b_form, 's_form':s_form}
        