from rest_framework import serializers
from inventory_management.models.lotserial import LotSerial

class LotSerialSerializer(serializers.ModelSerializer):
    """Serializer for LotSerial model."""
    class Meta:
        model = LotSerial
        fields = '__all__' 