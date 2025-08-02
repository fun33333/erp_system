"""
ViewSet for Tax model.
"""
from rest_framework import viewsets
from ..models.tax import Tax
from ..serializers.tax_serializer import TaxSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
