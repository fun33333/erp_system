from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled'),
    ]
    customer = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    total = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer}" 