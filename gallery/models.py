from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_pic')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    promo = models.BooleanField(default=False)
    promo_price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

