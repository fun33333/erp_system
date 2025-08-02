from django.db import models
from inventory_management.models.product import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class GatePass(models.Model):
    """Gate Pass for product issue/return."""
    PURPOSE_CHOICES = [
        ('issue', 'Issue'),
        ('return', 'Return'),
    ]
    gate_pass_number = models.CharField(max_length=100, unique=True)
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gatepasses')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    issued_to = models.CharField(max_length=100)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.gate_pass_number 