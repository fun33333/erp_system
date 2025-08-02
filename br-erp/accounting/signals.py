"""
Signals for Accounting system: auto journal entry creation.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.payment import Payment
from .models.asset import Asset
from .models.invoice import Invoice
from .models.journalentry import JournalEntry
from .models.journal import Journal

@receiver(post_save, sender=Payment)
@receiver(post_save, sender=Asset)
@receiver(post_save, sender=Invoice)
def create_journal_entry(sender, instance, created, **kwargs):
    if created:
        # Stub: implement logic to create JournalEntry automatically
        pass
