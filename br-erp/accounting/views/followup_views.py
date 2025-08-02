"""
ViewSet for FollowUp model.
"""
from rest_framework import viewsets, filters
from ..models.followup import FollowUp
from ..serializers.followup_serializer import FollowUpSerializer

class FollowUpViewSet(viewsets.ModelViewSet):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'notes']
    ordering_fields = ['followup_date', 'status']
