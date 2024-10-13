from django.urls import path
from .views import main_page, price_page, cart_page, Menu

urlpatterns = [
    path('', main_page, name='index'),
    path('shop/', price_page, name='shop'),
    path('cart/', cart_page, name='cart'),
    path('menu/', Menu.as_view(), name='menu')
]
