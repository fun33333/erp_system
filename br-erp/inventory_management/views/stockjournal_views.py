from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from inventory_management.models.stockjournal import StockJournal
from inventory_management.serializers.stockjournal_serializer import StockJournalSerializer

class StockJournalViewSet(viewsets.ModelViewSet):
    """API endpoint for StockJournal CRUD operations."""
    queryset = StockJournal.objects.all()
    serializer_class = StockJournalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'source_location', 'destination_location']
    search_fields = ['name']
    ordering_fields = ['name', 'type']
    ordering = ['name'] 