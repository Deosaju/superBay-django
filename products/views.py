from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from accounts.models import SellerProfile  

@login_required
def my_products(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'my_products.html', {'products': products})

@login_required
def product_create_view(request):
    try:
        seller_profile = request.user.sellerprofile
    except SellerProfile.DoesNotExist:
        return redirect('become_seller')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.seller = request.user
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

@login_required
def product_edit_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id, seller=request.user)

    if request.method == 'POST':
        # Get the form data from the POST request and update the product
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']

        # Save the updated product to the database
        product.save()

        # Redirect to the product detail page after editing
        return redirect('product_detail', product_id=product.id)

    return render(request, 'product_edit.html', {'product': product})


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    seller = product.seller 
    return render(request, 'product_detail.html', {'product': product, 'seller': seller})