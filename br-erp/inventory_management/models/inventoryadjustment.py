from django.db import models
from inventory_management.models.location import Location
from django.contrib.auth import get_user_model

User = get_user_model()

class InventoryAdjustment(models.Model):
    """Inventory Adjustment for correcting stock levels."""
    reference = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='adjustments')
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=30)
    adjusted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='inventory_adjustments')
    adjusted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference 