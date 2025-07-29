from django.db import models
from inventory_management.models.product import Product

class ProductVariant(models.Model):
    """Product Variant for product attributes."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attribute_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} - {self.attribute_name}: {self.value}" 