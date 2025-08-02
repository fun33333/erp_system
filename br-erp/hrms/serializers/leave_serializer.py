"""
Serializer for Leave model.
"""
from rest_framework import serializers
from ..models.leave import Leave

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
