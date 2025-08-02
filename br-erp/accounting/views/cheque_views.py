"""
ViewSet for Cheque model.
"""
from rest_framework import viewsets, filters
from ..models.cheque import Cheque
from ..serializers.cheque_serializer import ChequeSerializer

class ChequeViewSet(viewsets.ModelViewSet):
    queryset = Cheque.objects.all()
    serializer_class = ChequeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['cheque_number', 'payee_name']
    ordering_fields = ['date', 'amount']
