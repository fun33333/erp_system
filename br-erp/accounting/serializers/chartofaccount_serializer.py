"""
Serializer for ChartOfAccount model.
"""
from rest_framework import serializers
from ..models.chartofaccount import ChartOfAccount

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = '__all__'
