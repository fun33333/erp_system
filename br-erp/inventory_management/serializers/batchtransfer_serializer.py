from rest_framework import serializers
from inventory_management.models.batchtransfer import BatchTransfer

class BatchTransferSerializer(serializers.ModelSerializer):
    """Serializer for BatchTransfer model."""
    class Meta:
        model = BatchTransfer
        fields = '__all__' 