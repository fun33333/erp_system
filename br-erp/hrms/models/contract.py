"""
Contract model for HRMS.
"""
from django.db import models
from .employee import Employee

class Contract(models.Model):
    CONTRACT_TYPES = [
        ('Permanent', 'Permanent'),
        ('Temporary', 'Temporary'),
        ('Internship', 'Internship'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='contracts')
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2)
    probation_period = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return f"{self.employee.full_name} - {self.contract_type}"
