from django.urls import path
from UrbanDjango.task3 import views

urlpatterns = [
    path('', views.index, name='platform'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
]

