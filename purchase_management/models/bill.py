from django.db import models
from purchase_management.models.order import Order

class Bill(models.Model):
    """Vendor Bill."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='bills')
    bill_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill {self.id} for Order {self.order}" 