from django.db import models
from markets.models import Stock, Coin
from django.contrib.auth.models import AbstractUser

#from .forms import NewUserForm
 
# Create your models here.
class UserProfile(AbstractUser):
    user_stock = models.ManyToManyField(Stock, blank=True, )
    user_coin = models.ManyToManyField(Coin, blank=True, )
