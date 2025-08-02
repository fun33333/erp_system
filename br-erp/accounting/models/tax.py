"""
Tax model for Accounting system.
"""
from django.db import models

class Tax(models.Model):
    TAX_TYPES = [
        ('Sales Tax', 'Sales Tax'),
        ('VAT', 'VAT'),
        ('GST', 'GST'),
    ]
    tax_name = models.CharField(max_length=100)
    tax_type = models.CharField(max_length=20, choices=TAX_TYPES)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    account = models.ForeignKey('ChartOfAccount', on_delete=models.CASCADE, related_name='taxes')
    is_active = models.BooleanField(default=True)
    apply_on = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return self.tax_name
