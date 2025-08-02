"""
ViewSet for CreditDebitNote model.
"""
from rest_framework import viewsets, filters
from ..models.creditdebitnote import CreditDebitNote
from ..serializers.creditdebitnote_serializer import CreditDebitNoteSerializer

class CreditDebitNoteViewSet(viewsets.ModelViewSet):
    queryset = CreditDebitNote.objects.all()
    serializer_class = CreditDebitNoteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['note_number', 'note_type', 'reason']
    ordering_fields = ['note_number', 'date_issued']
