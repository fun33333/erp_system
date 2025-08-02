from django.db import models
from django.contrib.auth import get_user_model
from purchase_management.models.product import Product

User = get_user_model()

class Requisition(models.Model):
    """Purchase Requisition."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requisitions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='requisitions')
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} x {self.quantity} by {self.requested_by}" 