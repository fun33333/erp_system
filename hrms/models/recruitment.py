"""
Recruitment model for HRMS.
"""
from django.db import models

class Recruitment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position_applied = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Recruitment'
        verbose_name_plural = 'Recruitments'

    def __str__(self):
        return f"{self.full_name} - {self.position_applied}"
