from django.shortcuts import render
from pandas.core.resample import f

from .models import Coin
from .models import Stock

from markets import models

from django.http import JsonResponse
# Create your views here.

def index(request):
    coins = Coin.objects.all()
    stocks = Stock.objects.all()
    return render(request, 'markets/index.html', {
        'coins': coins,
        'stocks': stocks,
    })

def market_view(request):
    coins = Coin.objects.all()
    stocks = Stock.objects.all()
    return render(request, 'markets/market.html',{
        'coins': coins, 
        'stocks': stocks,
    })

def crypto_view(request):
    coins = Coin.objects.all()
    return render(request, 'markets/crypto.html', {
        'coins' : coins
    })

def stock_view(request):
    stocks = Stock.objects.all()
    return render(request, 'markets/stock.html', {
        'stocks' : stocks,
    })

def crypto_details(request, coin_slug):
    selected_crypto = Coin.objects.get(slug=coin_slug)
    return render(request, 'markets/crypto-details.html', {
        'coins' : selected_crypto,
    })

def stock_details(request, stock_slug):
    selected_stock = Stock.objects.get(slug=stock_slug)
    # ticker = selected_stock.name + ".JK"
    return render(request, 'markets/stock-details.html',
        {
            'stocks' : selected_stock,
        }
    )

def getUpdatedStockPrice(request):
    if request.method == 'POST':
        name = request.POST['slug']
        selected_stock = Stock.objects.get(slug=name.upper())
        
        return JsonResponse({"price": selected_stock.price})
