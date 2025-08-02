"""
Budget Management model for Accounting system.
"""
from django.db import models

class Budget(models.Model):
    fiscal_year = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    allocated_budget = models.DecimalField(max_digits=12, decimal_places=2)
    used_budget = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_budget = models.DecimalField(max_digits=12, decimal_places=2)
    remarks = models.TextField()

    class Meta:
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'

    def __str__(self):
        return f"{self.department} - {self.fiscal_year}"
