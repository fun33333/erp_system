"""
Serializer for AnalyticalAccounting model.
"""
from rest_framework import serializers
from ..models.analyticalaccounting import AnalyticalAccounting

class AnalyticalAccountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticalAccounting
        fields = '__all__'
