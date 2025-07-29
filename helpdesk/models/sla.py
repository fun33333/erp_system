"""
SLA model for Helpdesk system.
"""
from django.db import models

class SLA(models.Model):
    sla_name = models.CharField(max_length=100)
    priority_level = models.CharField(max_length=10)
    response_time_minutes = models.PositiveIntegerField()
    resolution_time_minutes = models.PositiveIntegerField()
    apply_to_group = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'SLA'
        verbose_name_plural = 'SLAs'

    def __str__(self):
        return self.sla_name
