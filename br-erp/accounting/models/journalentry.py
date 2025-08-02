"""
Journal Entry model for Accounting system.
"""
from django.db import models
from .journal import Journal
from .chartofaccount import ChartOfAccount

class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='entries')
    entry_date = models.DateField()
    description = models.TextField()
    debit_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='debit_entries')
    credit_account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='credit_entries')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Journal Entry'
        verbose_name_plural = 'Journal Entries'

    def __str__(self):
        return f"{self.journal.journal_name} - {self.entry_date}"
