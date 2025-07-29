from django.db import models
from inventory_management.models.product import Product
from inventory_management.models.location import Location
from django.contrib.auth import get_user_model

User = get_user_model()

class InventoryWastage(models.Model):
    """Inventory Wastage for lost/damaged stock."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wastages')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    reason = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='wastages')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_wastages')
    wastage_date = models.DateField()

    def __str__(self):
        return f"{self.product} - {self.quantity}" 