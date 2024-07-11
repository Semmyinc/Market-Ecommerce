from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# create an OrderItem Inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# extend our Order Model 
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    readonly_fields = ['date_ordered']
    # fields = ['user', 'fullname', 'shipped']
    

# unregister the order Model 
admin.site.unregister(Order)
# re register our order and orderadmin
admin.site.register(Order, OrderAdmin)