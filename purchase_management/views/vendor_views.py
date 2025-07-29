from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.vendor import Vendor
from purchase_management.serializers.vendor_serializer import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    """API endpoint for Vendor CRUD operations."""
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['name']
    ordering = ['name'] 