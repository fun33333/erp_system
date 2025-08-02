"""
Serializer for AttendanceMachine model.
"""
from rest_framework import serializers
from ..models.attendancemachine import AttendanceMachine

class AttendanceMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceMachine
        fields = '__all__'
