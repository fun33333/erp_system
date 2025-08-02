"""
Serializer for CreditDebitNote model.
"""
from rest_framework import serializers
from ..models.creditdebitnote import CreditDebitNote

class CreditDebitNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditDebitNote
        fields = '__all__'
