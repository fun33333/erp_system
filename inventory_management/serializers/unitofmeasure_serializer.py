from rest_framework import serializers
from inventory_management.models.unitofmeasure import UnitOfMeasure

class UnitOfMeasureSerializer(serializers.ModelSerializer):
    """Serializer for UnitOfMeasure model."""
    class Meta:
        model = UnitOfMeasure
        fields = '__all__' 