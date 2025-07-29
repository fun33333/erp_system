"""
Journal model for Accounting system.
"""
from django.db import models
from .chartofaccount import ChartOfAccount

class Journal(models.Model):
    JOURNAL_TYPES = [
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('bank', 'Bank'),
        ('cash', 'Cash'),
    ]
    journal_name = models.CharField(max_length=100)
    journal_type = models.CharField(max_length=20, choices=JOURNAL_TYPES)
    default_debit_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='debit_journals')
    default_credit_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='credit_journals')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return self.journal_name
