"""
ViewSet for Payroll model.
"""
from rest_framework import viewsets
from ..models.payroll import Payroll
from ..serializers.payroll_serializer import PayrollSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
