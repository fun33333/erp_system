"""
Serializer for Attendance model.
"""
from rest_framework import serializers
from ..models.attendance import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
