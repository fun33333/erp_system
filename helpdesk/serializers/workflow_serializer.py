"""
Serializer for Workflow model.
"""
from rest_framework import serializers
from ..models.workflow import Workflow

class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'
