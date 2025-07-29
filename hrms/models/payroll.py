"""
Payroll Management model for HRMS.
"""
from django.db import models
from .employee import Employee

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')
    month = models.DateField()
    gross_salary = models.DecimalField(max_digits=12, decimal_places=2)
    deductions = models.DecimalField(max_digits=12, decimal_places=2)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'

    def __str__(self):
        return f"{self.employee.full_name} - {self.month.strftime('%Y-%m')}"
