from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.pricelist import PriceList
from purchase_management.serializers.pricelist_serializer import PriceListSerializer

class PriceListViewSet(viewsets.ModelViewSet):
    """API endpoint for PriceList CRUD operations."""
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['vendor', 'product', 'valid_from', 'valid_to']
    search_fields = ['vendor__name', 'product__name']
    ordering_fields = ['price', 'valid_from', 'valid_to']
    ordering = ['valid_from'] 