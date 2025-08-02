"""
Serializer for Automation model.
"""
from rest_framework import serializers
from ..models.automation import Automation

class AutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automation
        fields = '__all__'
