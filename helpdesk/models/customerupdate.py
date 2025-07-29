"""
CustomerUpdate model for Helpdesk system.
"""
from django.db import models

class CustomerUpdate(models.Model):
    UPDATE_TYPES = [
        ('Ticket Open', 'Ticket Open'),
        ('Reply', 'Reply'),
        ('Closed', 'Closed'),
    ]
    update_type = models.CharField(max_length=20, choices=UPDATE_TYPES)
    message_template = models.TextField()
    send_email = models.BooleanField(default=True)
    send_sms = models.BooleanField(default=False)
    delay_seconds = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Customer Update'
        verbose_name_plural = 'Customer Updates'

    def __str__(self):
        return f"{self.update_type} update"
