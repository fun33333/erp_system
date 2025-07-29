"""
ViewSet for Automation model.
"""
from rest_framework import viewsets, filters
from ..models.automation import Automation
from ..serializers.automation_serializer import AutomationSerializer
from ..permissions import IsHelpdeskAgent, IsTeamLead, IsHelpdeskManager

class AutomationViewSet(viewsets.ModelViewSet):
    queryset = Automation.objects.all()
    serializer_class = AutomationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['automation_name', 'trigger_event', 'action_type', 'action_target']
    ordering_fields = ['automation_name', 'trigger_event']
    permission_classes = [IsHelpdeskManager|IsTeamLead]
