from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.unitofmeasure import UnitOfMeasure
from inventory_management.serializers.unitofmeasure_serializer import UnitOfMeasureSerializer

class UnitOfMeasureViewSet(viewsets.ModelViewSet):
    """API endpoint for UnitOfMeasure CRUD operations."""
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['name']
    ordering_fields = ['name', 'type']
    ordering = ['name'] 