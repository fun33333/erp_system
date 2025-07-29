from rest_framework import serializers
from purchase_management.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment model."""
    class Meta:
        model = Payment
        fields = '__all__' 