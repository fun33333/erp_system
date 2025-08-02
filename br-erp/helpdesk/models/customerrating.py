"""
CustomerRating model for Helpdesk system.
"""
from django.db import models
from .ticket import Ticket

class CustomerRating(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    feedback_comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Customer Rating'
        verbose_name_plural = 'Customer Ratings'

    def __str__(self):
        return f"Rating {self.rating} for Ticket {self.ticket_id}"
