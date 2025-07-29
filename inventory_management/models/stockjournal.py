from django.db import models
from inventory_management.models.location import Location

class StockJournal(models.Model):
    """Stock Journal for inventory movements."""
    JOURNAL_TYPE = [
        ('receipt', 'Receipt'),
        ('delivery', 'Delivery'),
        ('internal', 'Internal'),
        ('return', 'Return'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOURNAL_TYPE)
    source_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='source_journals')
    destination_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination_journals')

    def __str__(self):
        return self.name 