from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.location import Location
from inventory_management.serializers.location_serializer import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """API endpoint for Location CRUD operations."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'warehouse', 'parent_location']
    search_fields = ['name']
    ordering_fields = ['name', 'type']
    ordering = ['name'] 