from django.shortcuts import render

from .models import Coin
# Create your views here.

def index(request):
    coins = Coin.objects.all()
    return render(request, 'markets/index.html', {
        'coins': coins,
    })

def crypto_details(request, coin_slug):
    coins = Coin.objects.all()
    return render(request, 'markets/crypto-details.html', {
        'coins' : coins,
    })