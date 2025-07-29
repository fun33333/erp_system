from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.lotserial import LotSerial
from inventory_management.serializers.lotserial_serializer import LotSerialSerializer

class LotSerialViewSet(viewsets.ModelViewSet):
    """API endpoint for LotSerial CRUD operations."""
    queryset = LotSerial.objects.all()
    serializer_class = LotSerialSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'type', 'status', 'mfg_date', 'exp_date']
    search_fields = ['lot_or_serial_no', 'product__name']
    ordering_fields = ['mfg_date', 'exp_date', 'status']
    ordering = ['-mfg_date'] 