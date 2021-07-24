from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('markets', views.market_view, name='markets'),
    path('crypto/<slug:coin_slug>', views.crypto_details, name='crypto-details'),
    path('stock/<slug:stock_slug>', views.stock_details, name='stock-details'),
    path('getUpdatedStockPrice', views.getUpdatedStockPrice, name='getUpdatedStockPrice')
]