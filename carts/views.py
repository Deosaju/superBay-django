# carts/views.py

from django.shortcuts import render, redirect
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    try:
        cart_item = CartItem.objects.get(user=user, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(user=user, product=product)

    return redirect('cart')

# carts/views.py

@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    return render(request, 'cart.html', {'cart_items': cart_items})


# carts/views.py

@login_required
def increment_quantity(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


# carts/views.py

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')
