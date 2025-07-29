from django.db import models
from django.utils import timezone

class Ledger(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"Ledger Entry {self.id} - {self.date.date()}" 