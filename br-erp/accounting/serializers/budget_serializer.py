"""
Serializer for Budget model.
"""
from rest_framework import serializers
from ..models.budget import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
