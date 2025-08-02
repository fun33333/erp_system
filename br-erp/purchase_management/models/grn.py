from django.db import models
from purchase_management.models.order import Order
from django.contrib.auth import get_user_model

User = get_user_model()

class GRN(models.Model):
    """Goods Receipt Note."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='grns')
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grns')
    received_on = models.DateField()
    quantity_received = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"GRN {self.id} for Order {self.order}"

class ReceivedItem(models.Model):
    grn = models.ForeignKey(GRN, on_delete=models.CASCADE, related_name='received_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_received = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} x {self.quantity_received}" 