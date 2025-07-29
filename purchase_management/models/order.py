from django.db import models
from purchase_management.models.requisition import Requisition
from purchase_management.models.vendor import Vendor
from purchase_management.models.product import Product

class Order(models.Model):
    """Purchase Order."""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
    ]
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='orders')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"Order {self.id} for {self.vendor}"

class PurchaseOrderLine(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.product} x {self.quantity}" 