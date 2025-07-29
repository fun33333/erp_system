"""
Serializer for CustomerRating model.
"""
from rest_framework import serializers
from ..models.customerrating import CustomerRating

class CustomerRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRating
        fields = '__all__'
