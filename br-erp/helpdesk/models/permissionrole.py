"""
PermissionRole model for Helpdesk system.
"""
from django.db import models

class PermissionRole(models.Model):
    ROLE_CHOICES = [
        ('Agent', 'Agent'),
        ('Team Lead', 'Team Lead'),
        ('Manager', 'Manager'),
    ]
    role_name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    can_view_all = models.BooleanField(default=False)
    can_assign = models.BooleanField(default=False)
    can_change_status = models.BooleanField(default=False)
    can_edit_ticket = models.BooleanField(default=False)
    can_view_reports = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Permission Role'
        verbose_name_plural = 'Permission Roles'

    def __str__(self):
        return self.role_name
