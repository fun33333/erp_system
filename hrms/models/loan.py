"""
Loan and Deductions model for HRMS.
"""
from django.db import models
from .employee import Employee

class Loan(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reason = models.TextField()
    start_date = models.DateField()
    monthly_installment = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_settled = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'

    def __str__(self):
        return f"{self.employee.full_name} - {self.amount}"
