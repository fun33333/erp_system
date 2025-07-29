"""
Cheque Printing model for Accounting system.
"""
from django.db import models
from .payment import Payment

class Cheque(models.Model):
    cheque_number = models.CharField(max_length=30, unique=True)
    payee_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    linked_payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='cheques')
    printed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques'

    def __str__(self):
        return self.cheque_number
