from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.stockvaluation import StockValuation
from inventory_management.serializers.stockvaluation_serializer import StockValuationSerializer

class StockValuationViewSet(viewsets.ModelViewSet):
    """API endpoint for StockValuation CRUD operations."""
    queryset = StockValuation.objects.all()
    serializer_class = StockValuationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'method', 'date']
    search_fields = ['product__name']
    ordering_fields = ['date', 'unit_cost', 'total_value']
    ordering = ['-date'] 