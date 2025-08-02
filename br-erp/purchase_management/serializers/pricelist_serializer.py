from rest_framework import serializers
from purchase_management.models.pricelist import PriceList

class PriceListSerializer(serializers.ModelSerializer):
    """Serializer for PriceList model."""
    class Meta:
        model = PriceList
        fields = '__all__' 