# products/models.py

from django.contrib.auth.models import User
from django.db import models
from categories.models import Category

def product_image_upload_path(instance, filename):
    # Custom function to generate the upload path for product images
    return f'products/product_images/{instance.seller.username}/{filename}'

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Updated field for the product image with custom upload path
    image = models.ImageField(upload_to=product_image_upload_path, blank=True, null=True)

    # Additional fields for the product
    quantity_available = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
