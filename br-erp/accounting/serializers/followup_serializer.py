"""
Serializer for FollowUp model.
"""
from rest_framework import serializers
from ..models.followup import FollowUp

class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'
