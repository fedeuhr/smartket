from itertools import product
from django.db import models
from django.conf import settings
import os
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
from PIL import Image

from smarket.models import Product, PurchaseProduct

User = settings.AUTH_USER_MODEL

def user_directory_path_profile(instance, filename):
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

class User(AbstractUser):
    stripe_costumer_id = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to=user_directory_path_profile, default='user/default_user.jpg')
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="library")
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.email

def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        library = UserLibrary.objects.create(user=instance)

        purchase_products = PurchaseProduct.objects.filter(email=instance.email)

        for purchased_product in purchase_products:
            library.products.add(purchased_product.product)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(post_save_user_receiver, sender=User)
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
