"""
ViewSet for SLA model.
"""
from rest_framework import viewsets
from ..models.sla import SLA
from ..serializers.sla_serializer import SLASerializer
from ..permissions import IsHelpdeskManager

class SLAViewSet(viewsets.ModelViewSet):
    queryset = SLA.objects.all()
    serializer_class = SLASerializer
    permission_classes = [IsHelpdeskManager]
