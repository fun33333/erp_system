"""
Bank Reconciliation model for Accounting system.
"""
from django.db import models
from .bankstatement import BankStatement
from .payment import Payment

class BankReconciliation(models.Model):
    statement = models.ForeignKey(BankStatement, on_delete=models.CASCADE, related_name='reconciliations')
    matched_payments = models.ManyToManyField(Payment, related_name='reconciliations')
    difference = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Bank Reconciliation'
        verbose_name_plural = 'Bank Reconciliations'

    def __str__(self):
        return f"Reconciliation for {self.statement}"
