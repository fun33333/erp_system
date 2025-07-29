"""
Serializer for SLA model.
"""
from rest_framework import serializers
from ..models.sla import SLA

class SLASerializer(serializers.ModelSerializer):
    class Meta:
        model = SLA
        fields = '__all__'
