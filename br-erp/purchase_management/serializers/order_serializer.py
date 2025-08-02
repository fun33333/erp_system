from rest_framework import serializers
from purchase_management.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""
    class Meta:
        model = Order
        fields = '__all__' 