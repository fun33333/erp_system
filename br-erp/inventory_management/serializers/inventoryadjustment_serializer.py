from rest_framework import serializers
from inventory_management.models.inventoryadjustment import InventoryAdjustment

class InventoryAdjustmentSerializer(serializers.ModelSerializer):
    """Serializer for InventoryAdjustment model."""
    class Meta:
        model = InventoryAdjustment
        fields = '__all__' 