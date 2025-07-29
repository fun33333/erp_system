"""
Automation model for Helpdesk system.
"""
from django.db import models

class Automation(models.Model):
    TRIGGER_EVENTS = [
        ('New Ticket', 'New Ticket'),
        ('Status Change', 'Status Change'),
        ('SLA Breach', 'SLA Breach'),
    ]
    ACTION_TYPES = [
        ('Assign', 'Assign'),
        ('Email', 'Email'),
        ('Escalate', 'Escalate'),
    ]
    automation_name = models.CharField(max_length=100)
    trigger_event = models.CharField(max_length=20, choices=TRIGGER_EVENTS)
    condition = models.TextField(help_text='JSON or string condition')
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    action_target = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Automation'
        verbose_name_plural = 'Automations'

    def __str__(self):
        return self.automation_name
