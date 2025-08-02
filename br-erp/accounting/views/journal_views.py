"""
ViewSet for Journal model.
"""
from rest_framework import viewsets, filters
from ..models.journal import Journal
from ..serializers.journal_serializer import JournalSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['journal_name', 'journal_type']
    ordering_fields = ['journal_name', 'journal_type']
