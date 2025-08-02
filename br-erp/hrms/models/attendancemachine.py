"""
Attendance Machine Integration model for HRMS.
"""
from django.db import models

class AttendanceMachine(models.Model):
    machine_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    connected_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Attendance Machine'
        verbose_name_plural = 'Attendance Machines'

    def __str__(self):
        return f"{self.machine_id} - {self.location}"
