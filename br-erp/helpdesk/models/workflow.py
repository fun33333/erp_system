"""
Workflow model for Helpdesk system.
"""
from django.db import models

class Workflow(models.Model):
    workflow_name = models.CharField(max_length=100)
    trigger_status = models.CharField(max_length=20)
    next_status = models.CharField(max_length=20)
    allowed_roles = models.ManyToManyField('RolePermission', related_name='workflows')

    class Meta:
        verbose_name = 'Workflow'
        verbose_name_plural = 'Workflows'

    def __str__(self):
        return self.workflow_name
