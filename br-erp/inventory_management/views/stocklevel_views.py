from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.stocklevel import StockLevel
from inventory_management.serializers.stocklevel_serializer import StockLevelSerializer

class StockLevelViewSet(viewsets.ModelViewSet):
    """API endpoint for StockLevel CRUD operations."""
    queryset = StockLevel.objects.all()
    serializer_class = StockLevelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'location']
    search_fields = ['product__name', 'location__name']
    ordering_fields = ['min_qty', 'max_qty']
    ordering = ['product'] 