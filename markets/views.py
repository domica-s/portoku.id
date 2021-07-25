from django.shortcuts import render
from pandas.core.resample import f

from .models import Coin
from .models import Stock
from .stocksAPI import getFullStockName, getStockGraph, getStockSpotPrice, getStockSummary

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
    stock_prices = {}
    for stock in stocks:
        ticker = stock.name + ".JK"
        stock_prices[stock.name] = getStockSpotPrice(ticker)
    print(stock_prices)
    return render(request, 'markets/stock.html', {
        'stocks' : stocks,
        'prices' : stock_prices,
    })

def crypto_details(request, coin_slug):
    selected_crypto = Coin.objects.get(slug=coin_slug)
    return render(request, 'markets/crypto-details.html', {
        'coins' : selected_crypto,
    })

def stock_details(request, stock_slug):
    selected_stock = Stock.objects.get(slug=stock_slug)
    ticker = selected_stock.name + ".JK"
    return render(request, 'markets/stock-details.html',
        {
            'name' : selected_stock.name,
            'fullname' : getFullStockName(ticker),
            'slug' : selected_stock.name,
            'price' : getStockSpotPrice(ticker),
            'data' : getStockGraph(ticker),
            'description' : getStockSummary(ticker)
        }
    )

def getUpdatedStockPrice(request):
    if request.method == 'POST':
        name = request.POST['slug']
        selected_stock = Stock.objects.get(slug=name.lower())
        ticker = selected_stock.name + ".JK"

        return JsonResponse({"price": getStockSpotPrice(ticker)})
