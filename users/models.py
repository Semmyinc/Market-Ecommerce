from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} Profile'
    
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
    
    post_save.connect(create_profile, sender=User)

    

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) 