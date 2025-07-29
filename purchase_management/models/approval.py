from django.db import models
from django.contrib.auth import get_user_model
from purchase_management.models.requisition import Requisition

User = get_user_model()

class Approval(models.Model):
    """Approval for Requisition."""
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='approvals')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approvals')
    status = models.CharField(max_length=20)
    approved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approval for {self.requisition} by {self.approved_by}" 