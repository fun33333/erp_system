from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.product import Product
from inventory_management.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for Product CRUD operations."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'uom', 'tracking', 'is_active']
    search_fields = ['name', 'barcode', 'sku']
    ordering_fields = ['name', 'price', 'sku']
    ordering = ['name'] 