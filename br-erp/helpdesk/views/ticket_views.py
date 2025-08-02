"""
ViewSet for Ticket model.
"""
from rest_framework import viewsets, filters
from ..models.ticket import Ticket
from ..serializers.ticket_serializer import TicketSerializer
from ..permissions import IsHelpdeskAgent, IsTeamLead, IsReadOnlyUser

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['subject', 'customer_email', 'ticket_number']
    ordering_fields = ['created_at', 'priority', 'status']
    permission_classes = [IsHelpdeskAgent|IsTeamLead|IsReadOnlyUser]
