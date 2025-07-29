from rest_framework import serializers
from purchase_management.models.approval import Approval

class ApprovalSerializer(serializers.ModelSerializer):
    """Serializer for Approval model."""
    class Meta:
        model = Approval
        fields = '__all__' 