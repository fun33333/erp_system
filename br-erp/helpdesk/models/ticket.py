"""
Ticket model for Helpdesk system.
"""
from django.db import models
from django.conf import settings
from django.utils import timezone

class Ticket(models.Model):
    TICKET_PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]
    TICKET_STATUS = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    CHANNEL_CHOICES = [
        ('Email', 'Email'),
        ('Web', 'Web'),
        ('Phone', 'Phone'),
        ('Chat', 'Chat'),
    ]
    ticket_number = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    customer_email = models.EmailField()
    priority = models.CharField(max_length=10, choices=TICKET_PRIORITY, db_index=True)
    status = models.CharField(max_length=20, choices=TICKET_STATUS, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tickets')
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        indexes = [
            models.Index(fields=['priority']),
            models.Index(fields=['status']),
            models.Index(fields=['assigned_to']),
        ]

    def __str__(self):
        return f"Ticket #{self.ticket_number}: {self.subject}"
