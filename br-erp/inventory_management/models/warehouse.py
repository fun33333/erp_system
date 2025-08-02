from django.db import models
from hr_management.models.employee import Employee

class Warehouse(models.Model):
    """Warehouse entity for inventory management."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='warehouses')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 