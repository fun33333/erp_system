"""
ViewSet for JournalEntry model.
"""
from rest_framework import viewsets, filters
from ..models.journalentry import JournalEntry
from ..serializers.journalentry_serializer import JournalEntrySerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'reference']
    ordering_fields = ['entry_date', 'amount']
