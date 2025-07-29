"""
Signals for Inventory Management
Handles auto journal creation, valuation, and replenishment triggers.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.stockmovement import StockMovement
from .models.stockjournal import StockJournal
from .models.stockvaluation import StockValuation
from .models.stockreplenishment import StockReplenishment

# Example: Auto-create journal entry on StockMovement completion
@receiver(post_save, sender=StockMovement)
def create_journal_entry(sender, instance, created, **kwargs):
    if created and instance.status == 'completed':
        StockJournal.objects.create(
            name=f"Journal for {instance.reference_no}",
            type=instance.movement_type,
            source_location=instance.from_location,
            destination_location=instance.to_location
        )

# Example: Auto-calculate valuation (FIFO/Weighted Avg)
@receiver(post_save, sender=StockMovement)
def auto_calculate_valuation(sender, instance, created, **kwargs):
    if created and instance.status == 'completed':
        # Call FIFO or Weighted Avg logic from utils
        pass

# Example: Auto-trigger replenishment
@receiver(post_save, sender=StockMovement)
def auto_trigger_replenishment(sender, instance, created, **kwargs):
    if created and instance.status == 'completed':
        # Check stock level and trigger replenishment if needed
        pass
