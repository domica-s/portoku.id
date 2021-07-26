from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200, default="COINxNAME")
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    description = models.TextField()

class Stock(models.Model):
    name = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200, default="STOCKxNAME")
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    description = models.TextField()

