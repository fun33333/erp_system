"""
Follow-up model for Accounting system.
"""
from django.db import models
from .invoice import Invoice

class FollowUp(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    ]
    followup_date = models.DateField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='followups')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField()

    class Meta:
        verbose_name = 'Follow Up'
        verbose_name_plural = 'Follow Ups'

    def __str__(self):
        return f"Follow-up for {self.invoice.invoice_number}"
