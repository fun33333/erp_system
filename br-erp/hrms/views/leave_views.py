"""
ViewSet for Leave model.
"""
from rest_framework import viewsets
from ..models.leave import Leave
from ..serializers.leave_serializer import LeaveSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
