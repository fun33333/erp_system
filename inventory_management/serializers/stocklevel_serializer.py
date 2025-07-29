from rest_framework import serializers
from inventory_management.models.stocklevel import StockLevel

class StockLevelSerializer(serializers.ModelSerializer):
    """Serializer for StockLevel model."""
    class Meta:
        model = StockLevel
        fields = '__all__' 