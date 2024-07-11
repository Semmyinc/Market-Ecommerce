from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from payment.models import ShippingAddress

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


# @receiver(post_save, sender=User)
# def create_shippinginfo(sender, instance, created, **kwargs):
#     if created:
#         ShippingAddress.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_ShippingAddress(sender, instance, **kwargs):
#     instance.userinfo.save()






    # Alternative way in models
    # create a user Profile by default when user signs up
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         user_profile = Profile(user=instance)
    #         user_profile.save()

    # # automate the profile thing
    # post_save.connect(create_profile, sender=User)