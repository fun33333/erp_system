from rest_framework import serializers
from inventory_management.models.stockreplenishment import StockReplenishment

class StockReplenishmentSerializer(serializers.ModelSerializer):
    """Serializer for StockReplenishment model."""
    class Meta:
        model = StockReplenishment
        fields = '__all__' 