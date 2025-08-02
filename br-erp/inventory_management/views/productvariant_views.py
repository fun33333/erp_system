from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.productvariant import ProductVariant
from inventory_management.serializers.productvariant_serializer import ProductVariantSerializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    """API endpoint for ProductVariant CRUD operations."""
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product', 'attribute_name']
    search_fields = ['attribute_name', 'value']
    ordering_fields = ['attribute_name', 'value']
    ordering = ['attribute_name'] 