from django.db import models

class Product(models.Model):
    """Product Master."""
    name = models.CharField(max_length=100)
    sku_code = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 