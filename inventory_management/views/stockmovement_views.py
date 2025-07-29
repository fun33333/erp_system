from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.stockmovement import StockMovement
from inventory_management.serializers.stockmovement_serializer import StockMovementSerializer

class StockMovementViewSet(viewsets.ModelViewSet):
    """API endpoint for StockMovement CRUD operations."""
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'from_location', 'to_location', 'movement_type', 'status', 'journal']
    search_fields = ['reference_no', 'product__name']
    ordering_fields = ['movement_date', 'quantity']
    ordering = ['-movement_date'] 