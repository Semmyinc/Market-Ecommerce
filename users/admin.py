from django.contrib import admin
from .models import Profile
from payment.models import ShippingAddress
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress


class UserAdmin(admin.ModelAdmin):
    model = User 
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline, ShippingAddressInline]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
