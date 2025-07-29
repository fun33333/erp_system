from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.approval import Approval
from purchase_management.serializers.approval_serializer import ApprovalSerializer

class ApprovalViewSet(viewsets.ModelViewSet):
    """API endpoint for Approval CRUD operations."""
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'approved_by', 'approved_on']
    search_fields = ['requisition__product__name', 'approved_by__username']
    ordering_fields = ['approved_on', 'status']
    ordering = ['-approved_on'] 