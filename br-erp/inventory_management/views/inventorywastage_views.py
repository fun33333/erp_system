from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.inventorywastage import InventoryWastage
from inventory_management.serializers.inventorywastage_serializer import InventoryWastageSerializer

class InventoryWastageViewSet(viewsets.ModelViewSet):
    """API endpoint for InventoryWastage CRUD operations."""
    queryset = InventoryWastage.objects.all()
    serializer_class = InventoryWastageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'location', 'approved_by', 'wastage_date']
    search_fields = ['product__name', 'reason']
    ordering_fields = ['wastage_date', 'quantity']
    ordering = ['-wastage_date'] 