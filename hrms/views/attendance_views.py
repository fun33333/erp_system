"""
ViewSet for Attendance model.
"""
from rest_framework import viewsets
from ..models.attendance import Attendance
from ..serializers.attendance_serializer import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
