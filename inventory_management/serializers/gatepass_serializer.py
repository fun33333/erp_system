from rest_framework import serializers
from inventory_management.models.gatepass import GatePass

class GatePassSerializer(serializers.ModelSerializer):
    """Serializer for GatePass model."""
    class Meta:
        model = GatePass
        fields = '__all__' 