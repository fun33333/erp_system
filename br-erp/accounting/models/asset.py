"""
Asset Management model for Accounting system.
"""
from django.db import models
from .chartofaccount import ChartOfAccount

class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_date = models.DateField()
    depreciation_method = models.CharField(max_length=50)
    lifespan_years = models.PositiveIntegerField()
    residual_value = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2)
    account = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE, related_name='assets')

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'

    def __str__(self):
        return self.asset_name
