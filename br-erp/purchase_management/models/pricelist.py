from django.db import models
from purchase_management.models.vendor import Vendor
from purchase_management.models.product import Product

class PriceList(models.Model):
    """Vendor/Product Price List."""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='pricelists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pricelists')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()

    def __str__(self):
        return f"{self.vendor} - {self.product}" 