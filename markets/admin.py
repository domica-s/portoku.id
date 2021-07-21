from django.contrib import admin

from .models import Coin, Stock

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    list_filter = ('name',)

class StocksAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    list_filter = ('name',)

admin.site.register(Coin, CoinAdmin)
admin.site.register(Stock, StocksAdmin)
