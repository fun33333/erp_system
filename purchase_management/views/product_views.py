from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from purchase_management.models.product import Product
from purchase_management.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for Product CRUD operations."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'unit']
    search_fields = ['name', 'sku_code', 'description']
    ordering_fields = ['name', 'sku_code']
    ordering = ['name'] 