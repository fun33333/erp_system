from django.db import models
from inventory_management.models.product import Product
from inventory_management.models.location import Location
from inventory_management.models.stockjournal import StockJournal

class StockMovement(models.Model):
    """Stock Movement for tracking inventory movements."""
    MOVEMENT_TYPE = [
        ('in', 'In'),
        ('out', 'Out'),
        ('internal', 'Internal'),
        ('return', 'Return'),
    ]
    reference_no = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stock_out')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stock_in')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPE)
    movement_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    journal = models.ForeignKey(StockJournal, on_delete=models.SET_NULL, null=True, related_name='movements')

    def __str__(self):
        return f"{self.reference_no} - {self.product}" 