"""
Credit/Debit Note model for Accounting system.
"""
from django.db import models
from .invoice import Invoice

class CreditDebitNote(models.Model):
    NOTE_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    note_number = models.CharField(max_length=30, unique=True)
    related_invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='notes')
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    reason = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_issued = models.DateField()

    class Meta:
        verbose_name = 'Credit/Debit Note'
        verbose_name_plural = 'Credit/Debit Notes'

    def __str__(self):
        return self.note_number
