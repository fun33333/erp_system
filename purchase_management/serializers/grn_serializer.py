from rest_framework import serializers
from purchase_management.models.grn import GRN

class GRNSerializer(serializers.ModelSerializer):
    """Serializer for GRN model."""
    class Meta:
        model = GRN
        fields = '__all__' 