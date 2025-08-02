"""
Bank Statement model for Accounting system.
"""
from django.db import models
from .chartofaccount import ChartOfAccount

class BankStatement(models.Model):
    bank_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='statements')
    statement_date = models.DateField()
    starting_balance = models.DecimalField(max_digits=12, decimal_places=2)
    ending_balance = models.DecimalField(max_digits=12, decimal_places=2)
    transactions_json = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Bank Statement'
        verbose_name_plural = 'Bank Statements'

    def __str__(self):
        return f"{self.bank_account.account_name} - {self.statement_date}"
