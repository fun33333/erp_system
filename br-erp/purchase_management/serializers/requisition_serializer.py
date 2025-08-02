from rest_framework import serializers
from purchase_management.models.requisition import Requisition

class RequisitionSerializer(serializers.ModelSerializer):
    """Serializer for Requisition model."""
    class Meta:
        model = Requisition
        fields = '__all__' 