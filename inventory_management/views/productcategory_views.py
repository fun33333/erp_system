from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.productcategory import ProductCategory
from inventory_management.serializers.productcategory_serializer import ProductCategorySerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for ProductCategory CRUD operations."""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['parent_category']
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name'] 