from django.db import models
from inventory_management.models.product import Product

class StockValuation(models.Model):
    """Stock Valuation for inventory costing."""
    METHOD_CHOICES = [
        ('fifo', 'FIFO'),
        ('average', 'Average'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='valuations')
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2)
    total_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.product} - {self.method}" 