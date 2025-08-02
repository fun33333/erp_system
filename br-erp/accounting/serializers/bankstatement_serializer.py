"""
Serializer for BankStatement model.
"""
from rest_framework import serializers
from ..models.bankstatement import BankStatement

class BankStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatement
        fields = '__all__'
