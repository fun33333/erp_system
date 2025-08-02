from rest_framework import serializers
from inventory_management.models.productvariant import ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    """Serializer for ProductVariant model."""
    class Meta:
        model = ProductVariant
        fields = '__all__' 