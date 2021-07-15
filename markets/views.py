from django.shortcuts import render

from .models import Coin
# Create your views here.

def index(request):
    coins = Coin.objects.all()
    num_coins = coins.count()
    return render(request, 'markets/index.html', {
        'coins': coins,
        'num_coins': num_coins
    })