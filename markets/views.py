from django.shortcuts import render

from .models import Coin
from .models import Stock
from .stocksAPI import getStockQuote
# Create your views here.

def index(request):
    coins = Coin.objects.all()
    stocks = Stock.objects.all()
    return render(request, 'markets/index.html', {
        'coins': coins,
        'stocks': stocks,
    })

def crypto_details(request, coin_slug):
    selected_crypto = Coin.objects.get(slug=coin_slug)
    return render(request, 'markets/crypto-details.html', {
        'coins' : selected_crypto,
    })

def stock_details(request, stock_slug):
    selected_stock = Stock.objects.get(slug=stock_slug)
    return render(request, 'markets/stock-details.html', {
        'stocks' : getStockQuote(selected_stock.name),
    })