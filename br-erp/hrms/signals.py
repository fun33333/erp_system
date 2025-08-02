"""
Signals for HRMS payroll recalculation.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.contract import Contract
from .models.leave import Leave
from .models.loan import Loan
from .models.tax import Tax
from .models.payroll import Payroll

@receiver(post_save, sender=Contract)
@receiver(post_save, sender=Leave)
@receiver(post_save, sender=Loan)
@receiver(post_save, sender=Tax)
def recalculate_payroll(sender, instance, created, **kwargs):
    # Find related payroll and recalculate
    # (Stub: implement actual logic)
    pass
