from rest_framework import serializers
from inventory_management.models.stockvaluation import StockValuation

class StockValuationSerializer(serializers.ModelSerializer):
    """Serializer for StockValuation model."""
    class Meta:
        model = StockValuation
        fields = '__all__' 