from django.db import models
from django.utils import timezone
from accounting.models.invoice import Invoice

class Payment(models.Model):
    PAYMENT_TYPE = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    ]
    PAYMENT_METHOD = [
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('CARD', 'Card'),
        ('CHEQUE', 'Cheque'),
    ]
    invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.SET_NULL, related_name='payments')
    type = models.CharField(max_length=3, choices=PAYMENT_TYPE)
    date = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Payment {self.id} - {self.amount}" 