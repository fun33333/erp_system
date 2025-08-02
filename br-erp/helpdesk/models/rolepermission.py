"""
RolePermission model for Helpdesk system.
"""
from django.db import models

class RolePermission(models.Model):
    ROLE_CHOICES = [
        ('Agent', 'Agent'),
        ('Lead', 'Lead'),
        ('Manager', 'Manager'),
    ]
    role_name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    can_view_all = models.BooleanField(default=False)
    can_assign = models.BooleanField(default=False)
    can_edit_ticket = models.BooleanField(default=False)
    can_view_reports = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Role Permission'
        verbose_name_plural = 'Role Permissions'

    def __str__(self):
        return self.role_name
