from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from purchase_management.models.requisition import Requisition
from purchase_management.models.approval import Approval
from purchase_management.models.order import Order
from purchase_management.models.grn import GRN
from purchase_management.models.bill import Bill

User = get_user_model()

@receiver(post_save, sender=Requisition)
def auto_create_approval(sender, instance, created, **kwargs):
    """Auto-create Approval when a new Requisition is created."""
    if created:
        Approval.objects.create(requisition=instance, approved_by=instance.requested_by, status='pending')

@receiver(post_save, sender=Order)
def auto_generate_grn(sender, instance, **kwargs):
    """Auto-generate GRN when Order status is marked 'delivered'."""
    if instance.status == 'delivered' and not GRN.objects.filter(order=instance).exists():
        GRN.objects.create(order=instance, received_by=instance.vendor, received_on=instance.delivery_date, quantity_received=0)

@receiver(post_save, sender=GRN)
def auto_generate_bill(sender, instance, created, **kwargs):
    """Auto-generate Bill after GRN is saved."""
    if created:
        Bill.objects.create(order=instance.order, bill_date=instance.received_on, amount=0, due_date=instance.received_on, is_paid=False) 