from rest_framework import serializers
from inventory_management.models.stockmovement import StockMovement

class StockMovementSerializer(serializers.ModelSerializer):
    """Serializer for StockMovement model."""
    class Meta:
        model = StockMovement
        fields = '__all__' 