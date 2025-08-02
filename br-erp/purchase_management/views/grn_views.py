from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.grn import GRN
from purchase_management.serializers.grn_serializer import GRNSerializer

class GRNViewSet(viewsets.ModelViewSet):
    """API endpoint for GRN CRUD operations."""
    queryset = GRN.objects.all()
    serializer_class = GRNSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['order', 'received_by', 'received_on']
    search_fields = ['order__vendor__name', 'notes']
    ordering_fields = ['received_on', 'quantity_received']
    ordering = ['-received_on'] 