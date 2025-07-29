"""
ViewSet for AttendanceMachine model.
"""
from rest_framework import viewsets
from ..models.attendancemachine import AttendanceMachine
from ..serializers.attendancemachine_serializer import AttendanceMachineSerializer

class AttendanceMachineViewSet(viewsets.ModelViewSet):
    queryset = AttendanceMachine.objects.all()
    serializer_class = AttendanceMachineSerializer
