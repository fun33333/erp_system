from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.inventoryadjustment import InventoryAdjustment
from inventory_management.serializers.inventoryadjustment_serializer import InventoryAdjustmentSerializer

class InventoryAdjustmentViewSet(viewsets.ModelViewSet):
    """API endpoint for InventoryAdjustment CRUD operations."""
    queryset = InventoryAdjustment.objects.all()
    serializer_class = InventoryAdjustmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location', 'status', 'adjusted_by', 'adjusted_on']
    search_fields = ['reference', 'reason']
    ordering_fields = ['adjusted_on', 'status']
    ordering = ['-adjusted_on'] 