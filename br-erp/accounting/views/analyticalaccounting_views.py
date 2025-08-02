"""
ViewSet for AnalyticalAccounting model.
"""
from rest_framework import viewsets, filters
from ..models.analyticalaccounting import AnalyticalAccounting
from ..serializers.analyticalaccounting_serializer import AnalyticalAccountingSerializer

class AnalyticalAccountingViewSet(viewsets.ModelViewSet):
    queryset = AnalyticalAccounting.objects.all()
    serializer_class = AnalyticalAccountingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['cost_center_name', 'department']
    ordering_fields = ['cost_center_name', 'budget_allocated', 'used_amount']
