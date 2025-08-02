"""
Serializer for Loan model.
"""
from rest_framework import serializers
from ..models.loan import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
