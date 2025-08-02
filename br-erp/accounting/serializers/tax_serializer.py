"""
Serializer for Tax model.
"""
from rest_framework import serializers
from ..models.tax import Tax

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
