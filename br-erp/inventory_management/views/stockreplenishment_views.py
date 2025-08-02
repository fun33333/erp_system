from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.stockreplenishment import StockReplenishment
from inventory_management.serializers.stockreplenishment_serializer import StockReplenishmentSerializer

class StockReplenishmentViewSet(viewsets.ModelViewSet):
    """API endpoint for StockReplenishment CRUD operations."""
    queryset = StockReplenishment.objects.all()
    serializer_class = StockReplenishmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'location', 'type']
    search_fields = ['product__name']
    ordering_fields = ['trigger_level', 'quantity']
    ordering = ['product'] 