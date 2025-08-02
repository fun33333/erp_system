"""
Leave model for HRMS.
"""
from django.db import models
from .employee import Employee

class Leave(models.Model):
    LEAVE_TYPES = [
        ('Annual', 'Annual'),
        ('Sick', 'Sick'),
        ('Unpaid', 'Unpaid'),
        ('Other', 'Other'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Leave'
        verbose_name_plural = 'Leaves'

    def __str__(self):
        return f"{self.employee.full_name} - {self.leave_type}"
