from rest_framework import serializers
from inventory_management.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    class Meta:
        model = Product
        fields = '__all__' 