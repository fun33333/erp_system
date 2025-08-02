from django.db import models

class UnitOfMeasure(models.Model):
    """Unit of Measure for products."""
    UOM_TYPE = [
        ('ref', 'Reference'),
        ('bigger', 'Bigger'),
        ('smaller', 'Smaller'),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=UOM_TYPE)
    conversion_factor = models.DecimalField(max_digits=10, decimal_places=4, default=1)

    def __str__(self):
        return self.name 