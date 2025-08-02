from django.db import models
from inventory_management.models.productcategory import ProductCategory
from inventory_management.models.unitofmeasure import UnitOfMeasure

class Product(models.Model):
    """Product for inventory management."""
    TRACKING_CHOICES = [
        ('none', 'None'),
        ('lot', 'Lot'),
        ('serial', 'Serial'),
    ]
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='products')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    tracking = models.CharField(max_length=10, choices=TRACKING_CHOICES, default='none')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 