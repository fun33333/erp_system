"""
Serializer for Contract model.
"""
from rest_framework import serializers
from ..models.contract import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
