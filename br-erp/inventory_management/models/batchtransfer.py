from django.db import models
from inventory_management.models.location import Location

class BatchTransfer(models.Model):
    """Batch Transfer for moving stock in bulk."""
    batch_reference = models.CharField(max_length=100)
    source_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='batch_source')
    dest_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='batch_dest')
    transfer_date = models.DateField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.batch_reference 