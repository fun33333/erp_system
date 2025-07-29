from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.requisition import Requisition
from purchase_management.serializers.requisition_serializer import RequisitionSerializer

class RequisitionViewSet(viewsets.ModelViewSet):
    """API endpoint for Requisition CRUD operations."""
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'requested_by', 'created_at']
    search_fields = ['product__name', 'requested_by__username']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at'] 