"""
Serializer for CustomerUpdate model.
"""
from rest_framework import serializers
from ..models.customerupdate import CustomerUpdate

class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUpdate
        fields = '__all__'
