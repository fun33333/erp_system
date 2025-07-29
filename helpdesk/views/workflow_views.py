"""
ViewSet for Workflow model.
"""
from rest_framework import viewsets
from ..models.workflow import Workflow
from ..serializers.workflow_serializer import WorkflowSerializer
from ..permissions import IsHelpdeskManager

class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
    permission_classes = [IsHelpdeskManager]
