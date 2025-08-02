"""
ViewSet for ChartOfAccount model.
"""
from rest_framework import viewsets, filters
from ..models.chartofaccount import ChartOfAccount
from ..serializers.chartofaccount_serializer import ChartOfAccountSerializer

class ChartOfAccountViewSet(viewsets.ModelViewSet):
    queryset = ChartOfAccount.objects.all()
    serializer_class = ChartOfAccountSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['account_code', 'account_name', 'account_type']
    ordering_fields = ['account_code', 'account_name']
