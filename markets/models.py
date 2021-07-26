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
    slug = models.SlugField(unique=True) # will be the same as name
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    numOfShares = models.IntegerField()
    # below are dynamic datas
    price = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    change24h = models.FloatField()
    volume = models.FloatField()

    def calculateMarketCap(self):
        return Stock.objects.filter(name=self).price * Stock.objects.filter(name=self).numOfShares 

    marketCap = property(calculateMarketCap)

