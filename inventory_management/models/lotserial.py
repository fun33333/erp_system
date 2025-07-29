from django.db import models
from inventory_management.models.product import Product

class LotSerial(models.Model):
    """Lot or Serial number tracking for products."""
    TYPE_CHOICES = [
        ('lot', 'Lot'),
        ('serial', 'Serial'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('used', 'Used'),
        ('expired', 'Expired'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lotserials')
    lot_or_serial_no = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    mfg_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product} - {self.lot_or_serial_no}" 