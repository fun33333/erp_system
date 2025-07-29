"""
Allowance model for HRMS.
"""
from django.db import models
from .employee import Employee

class Allowance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='allowances')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_given = models.DateField()

    class Meta:
        verbose_name = 'Allowance'
        verbose_name_plural = 'Allowances'

    def __str__(self):
        return f"{self.employee.full_name} - {self.title}"
