from django.db import models
from inventory_management.models.product import Product
from inventory_management.models.location import Location

class StockReplenishment(models.Model):
    """Stock Replenishment for auto/manual restocking."""
    TYPE_CHOICES = [
        ('manual', 'Manual'),
        ('auto', 'Auto'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='replenishments')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='replenishments')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    trigger_level = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product} - {self.location}" 