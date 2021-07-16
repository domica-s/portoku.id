from django.urls import path

from . import views

urlpatterns = [
    path('markets/', views.index, name='markets'),
    path('markets/crypto/<slug:coin_slug>', views.crypto_details, name='crypto-details')
]