# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('<int:product_id>/edit/', views.product_edit_view, name='product_edit'),
    path('my_products/', views.my_products, name='my_products'),
    path('create/', views.product_create_view, name='product_create'), 
]
