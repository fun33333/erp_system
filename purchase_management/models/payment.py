from django.db import models
from purchase_management.models.bill import Bill

class Payment(models.Model):
    """Vendor Payment."""
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    reference_no = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.id} for Bill {self.bill}" 