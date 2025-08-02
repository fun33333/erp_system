from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.batchtransfer import BatchTransfer
from inventory_management.serializers.batchtransfer_serializer import BatchTransferSerializer

class BatchTransferViewSet(viewsets.ModelViewSet):
    """API endpoint for BatchTransfer CRUD operations."""
    queryset = BatchTransfer.objects.all()
    serializer_class = BatchTransferSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['source_location', 'dest_location', 'transfer_date', 'status']
    search_fields = ['batch_reference']
    ordering_fields = ['transfer_date', 'status']
    ordering = ['-transfer_date'] 