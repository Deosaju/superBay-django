# categories/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    # Additional fields for the category
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
