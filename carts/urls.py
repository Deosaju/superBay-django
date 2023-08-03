# carts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='cart'),
    # Other URL patterns for cart actions (add, remove, etc.) if applicable
]
