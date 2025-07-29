"""
Serializer for Allowance model.
"""
from rest_framework import serializers
from ..models.allowance import Allowance

class AllowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allowance
        fields = '__all__'
