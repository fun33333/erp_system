"""
Appraisal model for HRMS.
"""
from django.db import models
from .employee import Employee

class Appraisal(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='appraisals')
    date = models.DateField()
    remarks = models.TextField()
    previous_salary = models.DecimalField(max_digits=12, decimal_places=2)
    new_salary = models.DecimalField(max_digits=12, decimal_places=2)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Appraisal'
        verbose_name_plural = 'Appraisals'

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"
