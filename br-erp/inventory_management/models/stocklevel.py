from django.db import models
from inventory_management.models.product import Product
from inventory_management.models.location import Location

class StockLevel(models.Model):
    """Stock Level for min/max inventory at a location."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_levels')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stock_levels')
    min_qty = models.DecimalField(max_digits=12, decimal_places=2)
    max_qty = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product} @ {self.location}" 