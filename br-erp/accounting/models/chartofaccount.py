"""
Chart of Account model for Accounting system.
"""
from django.db import models

class ChartOfAccount(models.Model):
    ACCOUNT_TYPES = [
        ('Asset', 'Asset'),
        ('Liability', 'Liability'),
        ('Income', 'Income'),
        ('Expense', 'Expense'),
        ('Equity', 'Equity'),
    ]
    account_code = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    parent_account = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='child_accounts')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Chart Of Account'
        verbose_name_plural = 'Chart Of Accounts'

    def __str__(self):
        return f"{self.account_code} - {self.account_name}"
