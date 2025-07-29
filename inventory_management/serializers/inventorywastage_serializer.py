from rest_framework import serializers
from inventory_management.models.inventorywastage import InventoryWastage

class InventoryWastageSerializer(serializers.ModelSerializer):
    """Serializer for InventoryWastage model."""
    class Meta:
        model = InventoryWastage
        fields = '__all__' 