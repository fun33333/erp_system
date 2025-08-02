"""
Serializer for Asset model.
"""
from rest_framework import serializers
from ..models.asset import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
