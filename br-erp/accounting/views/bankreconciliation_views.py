"""
ViewSet for BankReconciliation model.
"""
from rest_framework import viewsets, filters
from ..models.bankreconciliation import BankReconciliation
from ..serializers.bankreconciliation_serializer import BankReconciliationSerializer

class BankReconciliationViewSet(viewsets.ModelViewSet):
    queryset = BankReconciliation.objects.all()
    serializer_class = BankReconciliationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status']
    ordering_fields = ['status', 'difference']
