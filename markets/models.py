from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.slug}'

