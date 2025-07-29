"""
Serializer for Payroll model.
"""
from rest_framework import serializers
from ..models.payroll import Payroll

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'
