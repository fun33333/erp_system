from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.warehouse import Warehouse
from inventory_management.serializers.warehouse_serializer import WarehouseSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    """API endpoint for Warehouse CRUD operations."""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'manager']
    search_fields = ['name', 'location']
    ordering_fields = ['name', 'location']
    ordering = ['name'] 