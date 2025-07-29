from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.gatepass import GatePass
from inventory_management.serializers.gatepass_serializer import GatePassSerializer

class GatePassViewSet(viewsets.ModelViewSet):
    """API endpoint for GatePass CRUD operations."""
    queryset = GatePass.objects.all()
    serializer_class = GatePassSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['purpose', 'product', 'issued_to', 'issue_date', 'return_date', 'status']
    search_fields = ['gate_pass_number', 'product__name', 'issued_to']
    ordering_fields = ['issue_date', 'return_date', 'status']
    ordering = ['-issue_date'] 