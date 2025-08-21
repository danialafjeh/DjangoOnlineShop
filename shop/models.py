from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    data_modified = models.DateTimeField(User, auto_now = True)
    phone = models.CharField(max_length=25, blank = True)
    address1 = models.CharField(max_length=250, blank = True)
    address2 = models.CharField(max_length=250, blank = True)
    city = models.CharField(max_length=25, blank = True)
    state = models.CharField(max_length=25, blank = True)
    zipcode = models.CharField(max_length=25, blank = True)
    country = models.CharField(max_length=25, default='IRAN')
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    def __str__(self):
        return self.name

    
