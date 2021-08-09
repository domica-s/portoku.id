from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200, default="COINxNAME")
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    description = models.TextField()

# class Stock(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     fullname = models.CharField(max_length=200, default="STOCKxNAME")
#     slug = models.SlugField(unique=True)
#     price = models.FloatField()
#     description = models.TextField()

class Stock(models.Model):
    name = models.CharField(max_length=200, unique=True)
    fullname = models.CharField(max_length=200, default="STOCKxNAME", null=True)
    slug = models.SlugField(unique=True) # will be the same as name
    sector = models.CharField(max_length=200, null=True)
    industry = models.CharField(max_length=200, null=True)
    numOfShares = models.IntegerField(null=True)
    # below are dynamic datas
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    change24h = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    marketCap = models.FloatField(null=True)
    # update periodically, test this first
    price = models.FloatField(null=True)

