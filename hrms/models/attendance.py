"""
Attendance (Clock In/Out) model for HRMS.
"""
from django.db import models
from .employee import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    clock_in = models.TimeField()
    clock_out = models.TimeField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"
