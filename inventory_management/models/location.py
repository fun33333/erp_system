from django.db import models
from inventory_management.models.warehouse import Warehouse

class Location(models.Model):
    """Location inside or related to a warehouse."""
    LOCATION_TYPE = [
        ('internal', 'Internal'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
        ('scrap', 'Scrap'),
        ('transit', 'Transit'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=LOCATION_TYPE)
    parent_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.name 