"""
Serializer for Cheque model.
"""
from rest_framework import serializers
from ..models.cheque import Cheque

class ChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheque
        fields = '__all__'
