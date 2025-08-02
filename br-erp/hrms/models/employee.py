"""
Employee Master model for HRMS.
"""
from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    cnic = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    join_date = models.DateField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name
