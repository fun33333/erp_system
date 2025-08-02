"""
ViewSet for Tax model.
"""
from rest_framework import viewsets, filters
from ..models.tax import Tax
from ..serializers.tax_serializer import TaxSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['tax_name', 'tax_type']
    ordering_fields = ['rate', 'tax_name']
