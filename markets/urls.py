from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='markets'),
    path('crypto/<slug:coin_slug>', views.crypto_details, name='crypto-details'),
    path('stocks/<slug:stock_slug>', views.stock_details, name='stock-details')
]