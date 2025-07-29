"""
Serializer for BankReconciliation model.
"""
from rest_framework import serializers
from ..models.bankreconciliation import BankReconciliation

class BankReconciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankReconciliation
        fields = '__all__'
