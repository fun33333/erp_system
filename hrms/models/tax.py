"""
Tax model for HRMS.
"""
from django.db import models
from .employee import Employee

class Tax(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='taxes')
    month = models.DateField()
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return f"{self.employee.full_name} - {self.month.strftime('%Y-%m')}"
