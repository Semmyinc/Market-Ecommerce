from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from gallery.models import Product
from django.dispatch import receiver
import datetime

fields = ('shipping_fullname', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country')
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_fullname = models.CharField(max_length=255)
    shipping_email= models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255)
    shipping_zipcode = models.CharField(max_length=255)
    shipping_country = models.CharField(max_length=255)

    def __str__(self):
        return f'Shipping Address-{str(self.id)}'
    
    class Meta:
        verbose_name_plural = 'Shipping Address'

    def create_shipping(sender, instance, created, **kwargs):
        if created:
            user_shipping = ShippingAddress(user=instance)
            user_shipping.save()

    post_save.connect(create_shipping, sender=User)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    shipping_address = models.TextField()
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
# auto add shipping date
@receiver(pre_save, sender=Order)
def set_shipped_date_on_update(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now() 
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped = now

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)

    def __str__(self):
        return f'Order Item - {str(self.id)}'