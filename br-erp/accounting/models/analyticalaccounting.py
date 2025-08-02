"""
Analytical Accounting model for Accounting system.
"""
from django.db import models
from .chartofaccount import ChartOfAccount

class AnalyticalAccounting(models.Model):
    cost_center_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    assigned_accounts = models.ManyToManyField(ChartOfAccount, related_name='cost_centers')
    budget_allocated = models.DecimalField(max_digits=12, decimal_places=2)
    used_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Analytical Accounting'
        verbose_name_plural = 'Analytical Accounting'

    def __str__(self):
        return self.cost_center_name
