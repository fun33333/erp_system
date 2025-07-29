from rest_framework import serializers
from inventory_management.models.warehouse import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    """Serializer for Warehouse model."""
    class Meta:
        model = Warehouse
        fields = '__all__' 